import sys
import re
#import profile
#from line_profiler import 
from string import ascii_lowercase

frequency = [19,7,1,2,4,10,2,2,5,6,1,1,3,2,6,6,2,1,5,5,7,2,1,2,1,2,1] 
frequency_dict = {k:v for k,v in zip(' '+ascii_lowercase, frequency)}

#map_finished = False


def usage():
    print("The default wordlist is english_words.txt, you could also specify dictionary by:")
    print("python3 " + __file__ + " [dictionary]\n")

#Not used in this version
def words_with_length_two(dict_list):
    return [word for word in dict_list if len(word) == 2]


#Not used in this version
# if all 106 keys are found
def is_fin(map):
    return len(map) == sum(frequency)

def decipher_from_map(decipher_map:dict, cipher:list):
    plain_list = [decipher_map[letter] if letter in decipher_map else '*' for letter in cipher]
    return ''.join(plain_list)
    

# find the longest already decrypted part
# see if it's a part of a word in dictionary
def ifvalid(full_deciphered_length, map, dict_list, cipher_list):
    partial_plaintext = decipher_from_map(map, cipher_list)[full_deciphered_length:]
    partial_list = re.split('\*+|\s', partial_plaintext)
    longest_plain = max(partial_list, key=len)
    for word in dict_list:
        if longest_plain in word:
            return True
    return False

#Not used in this version
# the only word with length 1 is "a"
# filter out map that wrongly interpret space
def filter_wrong_space(map, cipher_list, a_in_dict):
    partial_plaintext = decipher_from_map(map,cipher_list)
    plain_word_list = partial_plaintext.split(' ')
    shortest_word = min(plain_word_list, key=len)
    if a_in_dict:
        shortest = 1
    else:
        shortest = 0
    if len(shortest_word) <= shortest:
        return False
    return True

def build_map(plain:str, cipher:list, start_point:int, map=dict()):

    if start_point + len(plain) > len(cipher):
        plain = plain[:len(cipher)-start_point]
    decipher_map = dict(map)

    for i in range(start_point, start_point+len(plain)): #O(len(plain))
        if cipher[i] in decipher_map: 
            if decipher_map[cipher[i]] != plain[i - start_point]:
                return False
        decipher_map[cipher[i]] = plain[i - start_point]

    # do the second check, which needs to reverse the map
    inv_map = dict() 
    for k, v in decipher_map.items():
        inv_map[v] = inv_map.get(v, [])
        inv_map[v].append(k)
    for letter in inv_map:
        if frequency_dict[letter] < len(inv_map[letter]):
            return False

#    if is_fin(decipher_map):
#        global map_finished
#        map_finished = True

    return decipher_map

def brute(dict_list, cipher_list):
    stack = [('', dict())]
    while stack:
        base, step_map = stack.pop()

        if not filter_wrong_space(step_map, cipher_list, 'a' in dict_list):
            continue

        # this check itself also take a lot of time
        # after trading off, only do this check when candidates are short
        # so we can filter out lots of potential candidates by one check
        if 1 < len(base) and len(base) < 38:
            if not ifvalid(len(base) , step_map, dict_list, cipher_list):
                continue
    
        for word in dict_list:
            word = word.rstrip()
            cur = base + word + ' '

            map = build_map(word+' ', cipher_list, len(base), step_map)
            if map:
#                if map_finished:
#                    decrypt_by_map(map, cipher_list)
                if len(cur) >= len(cipher_list):
                    print('Plaintext:\n' + cur[:len(cipher_list)],'\n')
                    return True
                else:
                    stack.append((cur, map))
    print("No plaintext could be found\n")
    return False

def decrypt(dict_list, ciphers):
    for cipher_string in ciphers:
        cipher_list = cipher_string.split(',') 
        brute(dict_list, cipher_list)

def main():

    usage()
    if len(sys.argv) == 1:
        dictionary_filename = 'english_words.txt'
    elif len(sys.argv) == 2:
        dictionary_filename = sys.argv[1]
    else:
        sys.exit()

    print("please input ciphertext:\n")
    ciphers = [cipher.rstrip('\n') for cipher in sys.stdin]
    with open(dictionary_filename) as f:
        dict_list = [l.rstrip('\n') for l in f]
    decrypt(dict_list, ciphers)

if __name__ == "__main__":
    main()

import ipdb
import random
import sys
from string import ascii_lowercase

def generate(dictionary_filename:str , num_testcase:int , len_testcase:int):

    frequency = [19,7,1,2,4,10,2,2,5,6,1,1,3,2,6,6,2,1,5,5,7,2,1,2,1,2,1]
    frequency_dict = {k:v for k,v in zip(' '+ascii_lowercase, frequency)}

    # generate keymap
    # { ' ': [1,2,3,4,40,45 ...] ... }
    keymap = {}
    cipher_space = range(106)
    # item: (' ', 19)
    keymap = { item[0]:random.choices(cipher_space, k=item[1]) for item in frequency_dict.items() }

    # read plaintexts
    plaintext = []
    # read all testcases into plaintext
    with open(dictionary_filename, 'r') as f:
        plaintext = [ line.rstrip()[:len_testcase] for line in f ]
    # discard extra lines
    plaintext = random.choices(plaintext, k = num_testcase)


    # encrypt plaintexts
    return encrypt(plaintext, keymap)

def schedule1(letter:tuple):
    return keymap[letter[1]][letter[0]%len(keymap[letter[1]])]

def schedule_random():
    pass

def schedule(m, len_keyspace, schedule_random = False )
    if schedule_random:
        return random.randint(0, len_keyspace)
    return m % len_keyspace

def encrypt(plaintext, keymap, schedule_random = False):
    cipher_text = []
    for case in plaintext:
        cipher_text.append(encrypt_case(case, keymap, schedule))
    return cipher_text

def encrypt_case(case, keymap, schedule):
    encrypted_case = [ keymap[letter[1]][schedule(letter)] for letter in enumerate(case) ]
    return ','.join(str(cipher) for cipher in encrypted_case)
    


if __name__ == "__main__":

    if len(sys.argv) != 4: 
        print("usage: python3" + __name__ + "dictionary.txt [number of testcases] [lenth of test case]")
    
    print(generate(sys.argv[1] , int(sys.argv[2]), int(sys.argv[3])))

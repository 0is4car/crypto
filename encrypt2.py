import random
import sys
from string import ascii_lowercase

frequency = [19,7,1,2,4,10,2,2,5,6,1,1,3,2,6,6,2,1,5,5,7,2,1,2,1,2,1]
frequency_dict = {k:v for k,v in zip(' '+ascii_lowercase, frequency)}

def generate(dictionary_filename:str, num_testcase:int, len_testcase:int):

    keymap = generate_keymap()
    #print(keymap)

    # read all plaintext testcases and discard extra.
    res = []
    with open(dictionary_filename, 'r') as f:
        word_list = [ line.rstrip() for line in f ]
    for case in range(num_testcase):
        plaintext = ' '.join(random.choices(word_list, k=100))[:len_testcase]
        res.append((plaintext, encrypt(plaintext, keymap)))
    return res

def generate_keymap():
    keymap = dict()
    cipher_space = set(range(106))
    for item in frequency_dict.items():
        keymap[item[0]] = random.sample(list(cipher_space), k = item[1])
        cipher_space -= set(keymap[item[0]])
    return keymap

def schedule(letter):
    ''' 
    given a letter, return the order of the key to be used
    schdule_random is used for simulating a complex schdule. 
    '''
    order = random.randint(0, frequency_dict[letter]-1)
    return order

def encrypt(plaintext:str, keymap:dict):
    cipher = [ keymap[letter][schedule(letter)] for letter in plaintext]
    cipher_text = ','.join(str(cipher) for cipher in cipher)
    return cipher_text



if __name__ == "__main__":

    if len(sys.argv) != 4: 
        print("usage: python3 " + __file__ + " [dictionary] [number of testcases] [lenth of test case]")
        print("example: python3 " + __file__ + " test1.txt 3 100")
        sys.exit()
    
    testcases = generate(sys.argv[1] , int(sys.argv[2]), int(sys.argv[3]))
    with open('ciphertext.txt','w') as c, open('plaintext.txt','w') as p:
        for plain, cipher in testcases:
            c.write(cipher)
            c.write('\n')
            p.write(plain)
            p.write('\n')

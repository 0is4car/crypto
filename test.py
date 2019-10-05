import sys
from encrypt import generate
from decrypt import decrypt

if __name__ == "__main__":

    if len(sys.argv) != 4: 
        print("usage: python3 " + __file__ + " [dictionary] [number of testcases] [lenth of test case]")
        print("example: python3 " + __file__ + "test1.txt 3 100")
        sys.exit()
    
    plaintext, ciphertext = generate(sys.argv[1] , int(sys.argv[2]), int(sys.argv[3]))
    assert plaintext == decrypt(ciphertext)

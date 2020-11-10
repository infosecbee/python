import base64
import string

# I will be adding functions here that are related to encoding and decoding Base 64

# I used this for a CTF challenge
# There were over 10 base64 strings and only  one of them decoded to HEX value.
def testIfHex(fileName):
    
    with open(fileName) as file:
        line = file.readline().strip()
        while line:
            #print(line)
            #print('------ decoded ---------\n')
            result = base64.b64decode(line)
            ## print(base64.b64decode(line))
            ## print('\n----------------\n')
            resultStr = result.decode('utf-8')
            
            # I learnt about the all() function. very cool
            # https://www.programiz.com/python-programming/methods/built-in/all

            isHex = all(c in string.hexdigits for c in resultStr)

            if isHex == True:
                print(line)
            line = file.readline().strip()


testIfHex('base64.txt')     
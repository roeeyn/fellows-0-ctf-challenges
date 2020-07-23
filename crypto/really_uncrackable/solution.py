import sys
import base64
import string
from itertools import cycle


# Input: two base64 strings
# Output: str xored
def xor_two_strings(first_str, second_str):
    first_str = base64.b64decode(first_str).decode()
    second_str = base64.b64decode(second_str).decode()

    xored = ''.join(chr(ord(x) ^ ord(y)) for (x,y) in zip(first_str, cycle(second_st)))

    return base64.b64encode(xored.encode()).decode()


def bruteforce_key_char(plain_char, cipher_char):
    for key_char in string.printable:
        if chr(ord(key_char) ^ ord(plain_char)) == cipher_char:
            return key_char
    raise ValueError



def bruteforce_key(plaintext, ciphertext):
    ciphertext = base64.b64decode(ciphertext).decode()

    key = ''
    for (plain_char, cipher_char) in zip(plaintext, ciphertext):
        key += bruteforce_key_char(plain_char, cipher_char)

    return key


def test_key(plaintext, ciphertext, key):
    crafted_ciphertext = ''.join(chr(ord(x) ^ ord(y)) for (x,y) in zip(plaintext, cycle(key)))

    ciphertext = base64.b64decode(ciphertext).decode()

    assert ciphertext == crafted_ciphertext


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("usage: python3", sys.argv[0], "<CIPHERTEXT> <PLAINTEXT>")
        exit(1)

    ciphertext = sys.argv[1]
    plaintext = sys.argv[2]

    key = bruteforce_key(plaintext, ciphertext)
    test_key(plaintext, ciphertext, key)

    print("Ciphertext: ", ciphertext)
    print("Plaintext: ", plaintext)
    print("Key: ", key)

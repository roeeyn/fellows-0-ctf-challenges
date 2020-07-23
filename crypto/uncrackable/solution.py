import sys
import base64
from itertools import cycle

def the_most_uncrackable_crypto_ever_yeah_believe_me(data, key = 'awesomepassword', encode_output=False, decode_input=False):

    if decode_input:
        data = base64.b64decode(data).decode()

    super_duper_secure_ciphertext = ''.join(chr(ord(x) ^ ord(y)) for (x,y) in zip(data, cycle(key)))

    if encode_output:
        return base64.b64encode(super_duper_secure_ciphertext.encode())

    return super_duper_secure_ciphertext




if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("usage: python3", sys.argv[0], "<CIPHERTEXT>")
        exit(1)

    ciphertext = sys.argv[1]

    # Simply pass the ciphertext through the XOR again
    plaintext = the_most_uncrackable_crypto_ever_yeah_believe_me(ciphertext, decode_input=True)
    print("Ciphertext: ", ciphertext)
    print("Plaintext: ", plaintext)

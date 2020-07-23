import sys
import base64
from itertools import cycle

def read_key(filename):
    key = ''

    with open(filename) as fp:
        key = fp.read().strip()

    return key


def the_most_uncrackable_crypto_ever_now_with_bug_fixes(data, encode_output=False, decode_input=False):
    key = read_key("mykey.txt")
    print("Key:", key)

    if decode_input:
        data = base64.b64decode(data).decode()

    # important: cycle because key might be shorter than data
    super_duper_secure_ciphertext = ''.join(chr(ord(x) ^ ord(y)) for (x,y) in zip(data, cycle(key)))

    if encode_output:
        return base64.b64encode(super_duper_secure_ciphertext.encode()).decode()

    return super_duper_secure_ciphertext


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("usage: python3", sys.argv[0], "<CIPHERTEXT>")
        exit(1)

    ciphertext = sys.argv[1]

    plaintext = the_most_uncrackable_crypto_ever_now_with_bug_fixes(ciphertext, decode_input=True)
    print("Plaintext: ", plaintext)

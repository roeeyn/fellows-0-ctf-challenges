import sys

def decrypt(encrypted_string_data):
    decrypted_data = list(encrypted_string_data)

    # Have to go backwards on the loop
    for i in range(len(decrypted_data)-1, -1, -1):

        magic_index = i*2 % len(decrypted_data)
        saved = decrypted_data[i]
        decrypted_data[i] = decrypted_data[magic_index]
        decrypted_data[magic_index] = saved

    return "".join(decrypted_data)


if __name__ == "__main__":
    filename = sys.argv[1]
    with open(filename, "r") as fp:
        for line in fp:
            print(decrypt(line.strip()))

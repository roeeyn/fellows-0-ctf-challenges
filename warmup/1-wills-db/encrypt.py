def encrypt(string_data):
    encrypted_data = list(string_data)

    for i in range(len(encrypted_data)):

        magic_index = i*2 % len(encrypted_data)
        saved = encrypted_data[i]
        encrypted_data[i] = encrypted_data[magic_index]
        encrypted_data[magic_index] = saved

    return "".join(encrypted_data)


if __name__ == "__main__":
    input_data = input("Insert the data to be encrpyted: ")
    print(encrypt(input_data))

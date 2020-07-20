import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print('usage: python3', sys.argv[0], 'host port')
        exit(1)

    text = ""

    while not text.startswith("mlh"):
        text = requests.get('http://' + sys.argv[1] + ':' +\
                            sys.argv[2]).content.decode()
        print(text)

    print(text)

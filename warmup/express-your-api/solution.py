import requests


if __name__ == "__main__":
    text = ""

    while not text.startswith("mlh"):
        text = requests.get('http://localhost').content.decode()

    print(text)

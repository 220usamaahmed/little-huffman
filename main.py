from src.huffman import *


def main():
    with open('kenji.txt', 'r') as file:
        orig_text = file.read()

        tree, stream = encode(orig_text)
        decoded_text = decode(tree, stream)


if __name__ == "__main__":
    main()

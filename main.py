from src.huffman import *


def main():
    with open('kenji.txt', 'r') as file:
        original_text = file.read()

        tree, stream = encode(original_text)
        decoded_text = decode(tree, stream)

        print("-- ORIGINAL TEXT --\n", original_text)
        print("-- DECODED TEXT --\n", decoded_text)


if __name__ == "__main__":
    main()

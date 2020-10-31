def get_char_frequencies(text):
    char_frequencies = {}
    for char in text:
        if char in char_frequencies: char_frequencies[char] += 1
        else: char_frequencies[char] = 1
    
    return char_frequencies


def generate_huffman_tree(text):
    char_frequencies = sorted(get_char_frequencies(text).items(), key=lambda x: x[1], reverse=True)

    i = len(char_frequencies) - 1
    while len(char_frequencies) > 1:
        combined_freq = char_frequencies[i][-1] + char_frequencies[i - 1][-1]
        sub_tree = [((char_frequencies[i], char_frequencies[i - 1]), combined_freq)]
        
        j = i - 1
        while combined_freq > char_frequencies[j][-1] and j > -1: j -= 1
        
        char_frequencies = char_frequencies[:j + 1] + sub_tree + char_frequencies[j + 1:]
        del char_frequencies[-2:]
        
        i -= 1

    return char_frequencies[0]


def generate_lookup_table(huffman_tree):
    lookup_table = {}

    def treverse(node, sequence=[]):
        if isinstance(node[0], str):
            lookup_table[node[0]] = sequence
        else:
            treverse(node[0][0], sequence + [False])
            treverse(node[0][1], sequence + [True])

    treverse(huffman_tree)

    return lookup_table


def encode(text):
    tree = generate_huffman_tree(text)
    lookup_table = generate_lookup_table(tree)

    encoding = []
    for char in text: encoding += lookup_table[char]

    return tree, encoding


def decode(tree, stream):
    output = ""

    sub_tree = tree
    for bit in stream:
        sub_tree = sub_tree[0][int(bit)]
        if isinstance(sub_tree[0], str):
            output += sub_tree[0]
            sub_tree = tree

    return output

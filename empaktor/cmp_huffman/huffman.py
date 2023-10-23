'''
Gestion de l'encodage selon Huffman
'''

import heapq
from collections import Counter


class Node:
    def __init__(self, char, frequency):
        self.char = char
        self.frequency = frequency
        self.left_child = None
        self.right_child = None


    def __eq__(self, other):
        return self.frequency == other.frequency

    def __lt__(self, other):
        return self.frequency < other.frequency
    

def build_huffman_tree(frequency_table):
    heap = [Node(char, frequency) for char, frequency in
            frequency_table.items()]

    heapq.heapify(heap)
    

    while len(heap) > 1:
        left_child = heapq.heappop(heap)
        right_child = heapq.heappop(heap)

        parent = Node(None, left_child.frequency + right_child.frequency)
        if left_child.frequency == right_child.frequency:
            if left_child.char and right_child.char and left_child.char < right_child.char:
                parent.left_child = left_child
                parent.right_child = right_child
            else:
                parent.left_child = right_child
                parent.right_child = left_child
        else:
            parent.left_child = left_child
            parent.right_child = right_child
        heapq.heappush(heap, parent)

    return heap[0]


def build_frequency_table(data):
    '''
    Crée une table de fréquences des caractères contenus dans la séquence de
    données.
    Args:
        data: La séquence de données de laquelle nous établirons la table de
        fréquences.
    Return:
        Counter: table de fréquences des caractères provenant de la séquence de
        données.
    '''
    frequency_table = Counter(data)
    frequency_table = dict(sorted(frequency_table.items(),
                                  key=lambda item: item[1]))
    return frequency_table


def build_codes(node, prefix = '', code = {}):
    if node is None: return
    if node.char is not None:
        code[node.char] = prefix
    build_codes(node.left_child, prefix + '0', code)
    build_codes(node.right_child, prefix + '1', code)


def display_huffman_tree(node, indent="", last=True):
    if node is not None:
        print(indent, end="")
        if last:
            print("└── ", end="")
            indent += "    "
        else:
            print("├── ", end="")
            indent += "│   "

        if node.char is not None:
            print(f"{node.char} ({node.frequency})")
        else:
            print(node.frequency)

        display_huffman_tree(node.left_child, indent, False)
        display_huffman_tree(node.right_child, indent, True)


def compress_data(data: str) -> str:
    frequency_table = build_frequency_table(data)

    print(frequency_table)

    tree = build_huffman_tree(frequency_table)

    display_huffman_tree(tree)

    encoded_data = {}
    build_codes(tree, '', encoded_data)

    print(encoded_data)

    output = ''
    for char in data:
        output = output + encoded_data[char]

    return output

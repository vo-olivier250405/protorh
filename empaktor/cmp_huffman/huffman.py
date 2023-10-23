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
    '''
    Génère un arbre de huffman correspondant à la table de fréquences entrée en
    paramètre.
    Args:
        frequency_table(dict): Table de fréquences de caractères.
    Returns:
        Node: Noeud racine de l'arbre de Huffman.
    '''

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


def build_frequency_table(data: str) -> dict:
    '''
    Crée une table de fréquences des caractères contenus dans la séquence de
    données.
    Args:
        data (str): La séquence de données à partir de laquelle nous établissons
        la table de fréquences.
    Return:
        dict: Table de fréquences des caractères provenant de la séquence de
        données.
    '''

    # Compte les occurences de chaque caractère de la séquence
    frequency_table = Counter(data)
    # Tri la table de fréquences par ordre croissant de fréquences
    frequency_table = dict(sorted(frequency_table.items(),
                                  key=lambda item: item[1]))
    # Retourne la table de fréquences
    return frequency_table


def build_codes(node: Node, prefix: str = '', code = None):
    """
    Génère le code binaire correspondant à chacun des nœuds de l'arbre de
    Huffman et stocke ces codes dans un dictionnaire.
    Args:
        node (Node): Le noeud de l'arbre actuellement exploré.
        prefix (str): Le préfixe de code binaire actuel (vide par défaut).
        code (dict): Dictionnaire stockant les codes binaires générés.
    """

    # Si le noeud est vide, stop la récursion
    if node is None:
        return

    # Si le noeud contient un caractère, c'est une feuille de l'arbre
    if node.char is not None:
        # Attribution du prefix (code binaire actuel) au caractère
        # correspondant
        code[node.char] = prefix
    # Explore l'enfant gauche du noeud actuel
    build_codes(node.left_child, prefix + '0', code)
    # Explore l'enfant droit du noeud actuel
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
    '''
    Encode une séquence de données en utilisant l'algorithme de codage de
    Huffman.
    Args:
        data (str): Séquence de données à encoder.
    Return:
        str: Séquence de données encodée.
    '''

    # Construction de la table de fréquences des caractères présents dans la
    # séquence à encoder
    frequency_table = build_frequency_table(data)

    print(frequency_table)

    # Construction de l'arbre de Huffman à partir de la table de fréquences
    tree = build_huffman_tree(frequency_table)

    # Construction de la table de fréquences des caractères présents dans la
    # séquence à encoder
    encoded_data = {}
    build_codes(tree, '', encoded_data)

    # Initialise une chaîne de caractères vide pour stocker la séquence encodée
    output = ''
    for char in data:
        output = output + encoded_data[char]
    # Retourne la séquence encodée
    return output

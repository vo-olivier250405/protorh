'''
Gestion de l'encodage selon Huffman
'''

import heapq
from collections import Counter


class Node:
    """
    Noeuds d'arbre binaire
    """

    def __init__(self, char: str, frequency: dict):
        self.char = char
        self.frequency = frequency
        self.left_child = None
        self.right_child = None

    def __eq__(self, other):
        return self.frequency == other.frequency

    def __lt__(self, other):
        return self.frequency < other.frequency


def build_huffman_tree(frequency_table: dict) -> Node:
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


def build_codes(node: Node, prefix: str = '', code=None):
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
    """
    Affiche l'arbre binaire
    Args:
        - node (Node): Le noeud de l'arbre actuellement exploré.
        - last (bool): 
        - indent (str): Indente les nœuds pour plus de visibilité
    """
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


def compress_data(data: str) -> (str, Node):
    '''
    Encode une séquence de données en utilisant l'algorithme de codage de
    Huffman.
    Args:
        data (str): Séquence de données à encoder.
    Return:
        str: Séquence de données encodée
        dict: Dictionnaire associant chaque caractère à son code binaire
    '''

    # Construction de la table de fréquences des caractères présents dans la
    # séquence à encoder
    frequency_table = build_frequency_table(data)

    # Construction de l'arbre de Huffman à partir de la table de fréquences
    tree = build_huffman_tree(frequency_table)

    # Construction de la table de fréquences des caractères présents dans la
    # séquence à encoder
    codes = {}
    build_codes(tree, '', codes)

    # Initialise une chaîne de caractères vide pour stocker la séquence encodée
    output = ''
    for char in data:
        output = output + codes[char]
    # Retourne la séquence encodée
    return output, codes


def decompress_data(compressed_data: str, codes: dict):
    '''
    Décode une séquence de données selon le codage de Huffman.
    Args:
        compressed_data (str): Séquence de données encodée
        codes (dict): Dictionnaire associant chaque caractère à son code binaire
    Return:
        str: Séquence de données décodée
    '''

    decompressed_data = ''
    buffer: str = ''

    for char in compressed_data:
        buffer = buffer + char
        for code in codes.keys():
            if codes[code] == buffer:
                decoded_char = code
                decompressed_data = decompressed_data + decoded_char
                buffer = ''
    return decompressed_data


def decompress_data_old(compressed_data: str, root: dict) -> str:
    """
    Décode une séquence de données selon le codage de Huffman, et la racine de
    l'arbre.
    Args:
        compressed_data (str): Séquence de données encodée
        codes (dict): Dictionnaire associant chaque caractère à son
         code binaire
    Return:
        str: Séquence de données décodée
    """
    decompressed_data = ''
    current_node = root

    for bit in compressed_data:
        if bit == '0':
            current_node = current_node.left_child
        else:
            current_node = current_node.right_child

        if current_node.char is not None:
            decompressed_data = decompressed_data + current_node.char
            current_node = root

    return decompressed_data

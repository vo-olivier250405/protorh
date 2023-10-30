'''
Gestion de la transformation selon Burrows-Wheeler (BWT).
'''


def transform_bwt(data: str) -> (str, int):
    '''
    Applique la transformation Burrows-Wheeler (BWT) à une séquence de données.
    Args:
        data (str): La séquence de données à transformer.
    Returns:
        str: La séquence transformée.
        int: Clé permettant la restauration de la séquence de données.
    '''

    # Copie les données d'entrée pour prévenir de toutes modifications
    data_copy = data
    # Crée une liste contenant chacune des lettres de data_copy
    words = list(data_copy)
    # Crée une liste vide qui stockera toutes les rotations possibles
    bwt = []

    # Parcourt la liste de lettres de data_copy pour générer les rotations
    for _ in range(len(words)):
        # Génère une rotation en plaçant la dernière lettre en première
        # position
        rotation = data_copy[-1] + data_copy[:-1]
        # Ajoute la rotation à la liste de rotations
        bwt.append(rotation)
        # Attribue la valeur de la rotation à data_copy pour la prochaine
        # itération
        data_copy = rotation

    # Trie la liste bwt
    bwt = sorted(bwt)
    # print(bwt)
    # Initialise une chaîne de caractères vide pour stocker la séquence
    # transformée
    output = ''
    # Parcourt la liste bwt pour récupérer la dernière lettre de chaque
    # rotation
    for rotation in bwt:
        # Récupère la dernière lettre de la rotation à l'index i et l'ajoute à
        # la variable de sortie
        output = output + rotation[-1]
    # Retourne la séquence transformée ainsi que la clé
    return output, bwt.index(data)


def inverse_bwt(transformed_data: str, key: int) -> str:
    '''
    Restaure une séquence de données ayant subie une transformation
    Burrows-Wheeler (BWT).
    Args:
        transformed_data (str): La séquence de données à restaurer.
        key (int): Clé générée lors de la transformation et permettant la
        restauration de la séquence de données.
    Returns:
        str: La séquence restaurée.
    '''

    # Copie les données d'entrée pour prévenir de toutes modifications
    transformed_data_copy = transformed_data

    # Initialise une liste indexes_chars pour associer chaque caractère à son
    # indice
    indexes_chars = []
    for index, char in enumerate(transformed_data_copy):
        indexes_chars.append((index, char))

    # Trie la liste de tuples par ordre alphabétique et par index
    indexes_chars = sorted(indexes_chars, key=lambda pair: pair[1])

    # Initialise une liste index_permutation de la longueur de
    # transformed_data_copy
    index_permutation = [None for _ in range(len(transformed_data_copy))]

    # Remplit index_permutation avec les indices triés des caractères
    for i, pair in enumerate(indexes_chars):
        original_index, _ = pair
        index_permutation[original_index] = i

    # Initialise une liste temp qui contient la clé
    temp = [key]

    # Remplit la liste temp avec les index de permutation
    for i in range(1, len(transformed_data_copy)):
        temp.append(index_permutation[temp[i - 1]])

    # Initialise une chaîne de caractères vide pour stocker la séquence
    # restaurée
    output = ''
    # Remplit la séquence restaurée en suivant la clé temporaire
    for i in temp:
        output = output + transformed_data_copy[i]
    # Inverse la séquence restaurée pour la ramener à sa forme d'origine
    output = output[::-1]

    # Retourne la séquence d'origine
    return output

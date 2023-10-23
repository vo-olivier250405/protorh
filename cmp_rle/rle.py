"""
Ce module permet de coder et de décoder des chaines de caractères à 
l'aide de l'algorithme Run-Length Encoding
"""


def encode_rle(data) -> str:
    """
    Cette fonction prend une chaîne de caractères en entrée. Elle renvoie une
    autre chaine de caractère codée. Chaque nombre qui précède une lettre
    est le nombre d'occurences consécutives de cette lettre. Ainsi,
    2A correspond à AA.
    """
    temp: list = list(data.upper()).copy()
    res: str = ""
    index: int = 0

    while index < len(temp):
        count: int = 1

        # Boucle tant que la valeur est encore la même
        while temp[index] == temp[index + 1] and index + 1 < len(temp):
            count += 1
            index += 1

        # Si on change de lettre, on rajoute la lettre précédée de son nombre
        # d'occurence
        res += str(count) + temp[index]
        index += 1
    return res


def decode_rle(encoded_data) -> str:
    """
    """
    pass

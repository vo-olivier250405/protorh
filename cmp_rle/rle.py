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
    temp: list = list(data).copy()
    res: str = ""
    index: int = 0

    while index < len(temp):
        count: int = 1

        # Boucle tant que la valeur est encore la même
        while index + 1 < len(temp) and temp[index] == temp[index + 1]:
            count += 1
            index += 1

        # Si on change de lettre, on rajoute la lettre précédée de son nombre
        # d'occurence
        res += str(count) + temp[index]
        index += 1
    return res


def decode_rle(encoded_data) -> str:
    """
    Fonction qui prend en paramètre une chaine de caractères et renvoi la
    chaine décodée. Teste si la lettre un digit, et ajoute, si non
    la lettre un certain nombre de fois.
    """
    temp: str = "" + encoded_data
    num: str = ""
    res: str = ""
    for letter in temp:
        # Teste si la valeur est un chiffre
        if not letter.isdigit():
            # Si non, on ajoute num fois la lettre dans la variable résultat
            for _ in range(int(num)):
                res += letter
            # Remet la chaine de caractère à zéro.
            num = ""
        else:
            # Stocke les chiffres pour les convertir en nombre
            num += letter
    return res

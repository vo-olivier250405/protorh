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
        # On rajoute des délimiteurs afin de pouvoir distinguer
        #  le nombre d'occurence et les chiffres (considérés comme caractères)
        res += f"{str(count)}¬{temp[index]}╦"
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
    for i in range(len(temp) - 1):
        # Vérifie si le caractère suivant n'est pas un délimiteur
        # et ajoute les valeurs
        if temp[i].isdigit() and temp[i + 1] != "╦":
            num += temp[i]
        elif temp[i] == "¬":
            res += temp[i + 1] * int(num)
            num = ""
    return res

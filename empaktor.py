"""
Module qui va compresser les fichiers à l'aide d'une des 3 méthodes.
"""

from sys import argv
import tarfile
from base64 import b64encode
from cmp_rle.rle import encode_rle, decode_rle


def open_file(name: str) -> str:
    """
    Ouvre un fichier et lit les infos dedans. Puis le ferme.
    """
    file = open(name, "r")
    data = file.read()
    file.close()
    return data


def rewrite_file(txt: str, name: str) -> None:
    """
    Réécrit dans un fichier
    """
    file = open(name, "a")
    file.truncate(0)
    file.write(txt)
    # file.read()
    file.close()


def filter_txt(name: str) -> str:
    """
    Retire tout les délimiteurs
    """
    name = name.replace("/", "").replace("|", "")
    return name


def compress(name: str, file_add: str) -> None:
    """
    Fonction qui prend en paramètre le nom du fichier à compresser et
    en crée une archive
    """
    temp = tarfile.open(name, "w:gz")
    temp.add(file_add)
    temp.close()
    return None


def uncompress(name: str) -> None:
    """
    Fonction qui décomppresse l'archive
    """
    file = tarfile.open(name)
    file.extractall(f"./{name[:8]}")
    print("Décompréssé(s): ", file.getnames())
    file.close()


data = open_file(argv[1])
coded = encode_rle(data=data)
decoded = decode_rle(encoded_data=coded)

rewrite_file(filter_txt(coded), argv[1])

# Compresse
compress("test.tar.gz", "cmp_rle/test.txt")
# Décompresse
uncompress("test.tar.gz")
rewrite_file(decoded, "test.tar/cmp_rle/test.txt")

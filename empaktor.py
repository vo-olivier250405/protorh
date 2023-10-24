"""
Module qui va compresser les fichiers à l'aide d'une des 3 méthodes.
"""

from sys import argv
from os import listdir
import tarfile
from base64 import b64encode
from cmp_rle.rle import encode_rle, decode_rle

# data = open_file(argv[1])
# coded = encode_rle(data=data)
# decoded = decode_rle(encoded_data=coded)
#
# rewrite_file(filter_txt(coded), argv[1])
#
# # Compresse
# compress("test.tar.gz", "cmp_rle/test.txt")
# # Décompresse
# uncompress("test.tar.gz")
# rewrite_file(decoded, "test.tar/cmp_rle/test.txt")


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


def compress(name: str, file_add: list) -> None:
    """
    Fonction qui prend en paramètre le nom du fichier à compresser et
    en crée une archive
    """
    temp = tarfile.open(name, "w:gz")
    for files in file_add:
        print(f"\nCompression de: {files}...")
        coded = encode_rle(data=open_file(files))
        decoded = decode_rle(encoded_data=coded)
        rewrite_file(coded, files)
        temp.add(files)
        rewrite_file(decoded, files)
        # temp.add(rewrite_file(filter_txt(coded), files))
        print(f"Compression de: {files} dans {name}: [\x1b[32mOK\x1b[0m]")
    temp.close()
    return None


def uncompress(name: str) -> None:
    """
    Fonction qui décomppresse l'archive
    """
    print(f"\nDécompression de {name}...")
    file = tarfile.open(name)
    file.extractall(f"./{name[:7]}")
    print(f"Décompression de {name}: [\x1b[32mOK\x1b[0m]")
    print(f"Éléments décompréssé(s): {file.getnames()}")
    file.close()
    return f"./{name[:7]}"


def get_files(argvs: list) -> list:
    """
    Récupère les fichiers à compresser et les renvoie
    """
    file_add: list = []
    for i in range(3, len(argvs)):
        file_add.append(argvs[i])
    return file_add


def main() -> None:
    """
    Lance le main pour permettre de décomprésser ou compresser
    """
    if argv[2] == "--compression":
        compress(argv[1], get_files(argv))
    elif argv[2] == "--décompression":
        path = uncompress(argv[1])
        for file in listdir(path):
            data = open_file(f"{path}/{file}")
            decoded = decode_rle(encoded_data=data)
            rewrite_file(decoded, f"{path}/{file}")
    else:
        print(f"\x1b[31mErreur: \x1b[0mArgument {argv[2]} non valide.")
    return None


main()

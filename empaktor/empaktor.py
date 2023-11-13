"""
Module principal du programme empaktor, il est le gestionnaire de compression.
"""

from os import path as os_path, walk, remove
from sys import argv
from tarfile import open as tar_open
from json import dump, loads
from cmp_rle.rle import *
from cmp_burrows.burrows_wheeler import *
from cmp_huffman.huffman import compress_data, decompress_data

def read_file(path: str) -> str:
    """
    Ouvre un fichier puis retourne les données contenues à l'intérieur.
    Args:
        - path(str): Chemin du fichier à ouvrir
    Return:
        - str: Données contenues dans le fichier
    """

    with open(path, "r", encoding="utf-8") as file:
        data = file.read()
        file.close()
    return data


def overwrite_file(path: str, data: str):
    """
    Modifie un fichier en remplaçant les données contenues à l'intérieur.
    Args:
        - path(str): Fichier à modifier
        - data(str): Nouvelles données
    """

    with open(path, "a", encoding="utf-8") as file:
        file.truncate(0)
        file.write(data)
        file.close()


def method_manager() -> bool:
    if argv == ["empaktor.py"]:
        print("\n\x1b[31mErreur: \x1b[0mVous n'avez rien saisi.\n")
        return False

    if len(argv) < 4:
        print("\n\x1b[31mErreur: \x1b[0mCommande incorrecte.\n")
        return False

    # Vérifie si l'on souhaite compresser
    if argv[2] == "--compression":
        valid: bool = check_compression_args()
        if valid:
            compress_files(argv[1], get_files_from_args(), argv[3])
        return valid

    # Vérifie si l'on souhaite décompresser
    if argv[1] == "--extract":
        valid: bool = check_extraction_args()
        if valid:
            path = extract(argv[3])
            decode_file(path, argv[2])
        return valid

    # Vérifie les erreurs
    print(f"\n\x1b[31mErreur: \x1b[0mArgument {argv[2]} non valide.")
    print("Veuillez utiliser --compression ou --extract.")
    return False


def check_compression_args() -> bool:
    """
    Vérifie si les arguments liés à la compression sont valides ou non.
    Return:
        - bool: True si les arguments sont valides, False sinon
    """

    # Vérifie si le fichier existe
    for file in get_files_from_args():
        if not os_path.exists(file):
            print(f"\n\x1b[31mErreur: \x1b[0m{file} n'existe pas.")
            return False

    # Vérifie si le chemin cible est correct
    if not check_target_path(argv[1]):
        print(f"\n\x1b[31mErreur: \x1b[0m{argv[1]} n'est pas un chemin cible valide.")
        return False

    # Vérifie si le nombre d'arguments est correct
    if len(argv) == 3:
        print("\n\x1b[31mErreur: \x1b[0mCommande non valide.")
        return False
    
    # Vérifie si la méthode de compression souhaitée est valide
    if argv[3] not in ["rle", "huffman", "burrows_wheeler"]:
        print(f"\n\x1b[31mErreur: \x1b[0mArgument {argv[3]} non valide.")
        print(f"{argv[3]} n'est pas un algorithme proposé.")
        return False
    
    # Vérifie si il y a des fihciers à compresser
    if not get_files_from_args():
        print("\n\x1b[31mErreur: \x1b[0mLes fichiers n'existent pas.")
        return False
    return True


def check_extraction_args() -> bool:
    """
    Vérifie si les arguments liés à la décompression sont valides ou non.
    Return:
        - bool: True si les arguments sont valides, False sinon
    """

    # Vérifie si la méthode de décompression souhaitée est valide
    if argv[2] not in ["rle", "huffman", "burrows_wheeler"]:
        print(f"\n\x1b[31mErreur: \x1b[0mArgument {argv[2]} non valide.")
        print(f"{argv[2]} n'est pas un algorithme proposé.")
        return False

    # Vérifie si le fichier à décompresser existe
    if not os_path.exists(argv[3]):
        print(f"\n\x1b[31mErreur: \x1b[0m{argv[3]} n'existe pas.")
        return False

    # Vérifie si le nombre d'arguments est correct
    if len(argv) != 4:
        print("\n\x1b[31mErreur: \x1b[0mCe n'est pas la bonne commande.\n")
        return False
    return True


def get_files_from_args() -> list:
    """
    Récupère la liste de fichiers à compresser depuis les arguments du
    programme.
    Return:
        - list: Liste de fichiers à compresser
    """

    file_add: list = []
    for i in range(4, len(argv)):
        file_add.append(argv[i])
    return file_add


def check_target_path(path: str) -> int:
    """
    Vérifie si le chemin cible est correct.
    Args:
        - name(str): Chemin du fichier à vérifier
    Return:
        - bool: True si le nom est correct, False sinon
    """

    parts = path.split(".")
    if (len(parts) > 2 and parts[-1] == "gz" and parts[-2] == "tar"):
        return True
    return False


def compress_files(target: str, files: list, method: str):
    """
    Crée une archive contenant une liste de fichiers compressés selon la
    méthode choisie.
    Args:
        - target(str): Chemin de l'archive à créer
        - files(list): Liste de fichiers à compresser
        - method(str): Méthode de compression à utiliser
    """

    try:
        with tar_open(target, "w:gz") as tar:
            for file_or_dir in files:
                print()
                if os_path.isdir(file_or_dir):
                    for dir_path, dirnames, file_names in walk(file_or_dir):
                        for file in file_names:
                            print("isDir")
                            compress_file(os_path.join(dir_path, file), method, tar)

                else:
                    file = file_or_dir
                    compress_file(file, method, tar)

            tar.close()

    except Exception as exception:
        print(f"\n\x1b[31mErreur: \x1b[0mÉchec lors de la compression: {exception}")


def compress_file(file: str, method: str, tar):
    print(f"Compression de: {file}...")

    match method:
        case "rle":
            decoded_data = read_file(file)
            overwrite_file(file, encode_rle(decoded_data))
            tar.add(file, arcname=os_path.relpath(file))
            overwrite_file(file, decoded_data)

        case _:
            raise Exception("Méthode de compression non valide.")


def extract(path: str):
    """
    Décompresse une archive compressée avec empaktor.
    Args:
        - path(str): Chemin de l'archive à décompresser
    """

    print(f"\nDécompression de {path}...")

    try:
        with tar_open(path) as tar:
            tar.extractall(f"./{path[:-7]}")
            print(f"Décompression de {path}: [\x1b[32mOK\x1b[0m]")
            print(f"Éléments décompréssé(s): {tar.getnames()}")
            tar.close()
        return f"./{path[:-7]}"

    except Exception as exception:
        print(f"\n\x1b[31mErreur: \x1b[0mÉchec lors de la compression: {exception}")


def decode_file(path: str, method: str):
    """
    Décode les fichiers encodés après la décompressions selon la méthode
    choisie.
    Args:
        - path(str): Chemin du dossier à décompresser
        - method(str): Méthode de compression utilisée
    """
    methods = {"huffman": decompress_data, "burrows_wheeler": inverse_bwt}

    for dir_path, dirnames, file_names in walk(path):
        for file in file_names:
            file_path = os_path.join(dir_path, file)
            data = read_file(file_path)
            if method in ["huffman", "burrows_wheeler"] and file[-5:] != ".json":
                data = loads(read_file(dir_path + f"/.{file}.json"))
                decoded = methods[method](data["msg"], data["code"])
                remove(dir_path= + f"/.{file}.json")

            elif method == "rle":
                decoded = decode_rle(encoded_data=data)

            if file[-5:] != ".json":
                overwrite_file(file_path, decoded)


def main():
    if len(argv) != 1 and argv[1] == "--help":
        help_path = os_path.join(os_path.dirname(os_path.abspath(__file__)),
                                 "help.txt")
        print(read_file(help_path))
    elif not method_manager():
        print(
            "Entrez: \x1b[32mpython3 empaktor.py --help\x1b[0m pour de l'aide.")


main()
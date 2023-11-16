"""
Module principal du programme empaktor, il est le gestionnaire de compression.
"""

from json import dump, loads
from os import path as os_path, remove, makedirs, walk
from re import match as re_match
from shutil import rmtree
from sys import argv
from tarfile import open as tar_open

from cmp_burrows.burrows_wheeler import transform_bwt, inverse_bwt
from cmp_huffman.huffman import compress_data, decompress_data
from cmp_rle.rle import encode_rle, decode_rle


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


def method_manager() -> bool:
    """
    Lance une compression ou une extraction de fichiers
    """
    if argv == ["empaktor.py"]:
        print("\n\x1b[31mErreur: \x1b[0mVous n'avez rien saisi.\n")
        return False

    if len(argv) < 3:
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
            path = extract(argv[2])
            decode_files(path)
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
        print(
            f"\n\x1b[31mErreur: \x1b[0m{argv[1]} n'est pas un"
            " chemin cible valide.")
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
    python3 empaktor.py --extract rle.tar.gz

    Vérifie si les arguments liés à la décompression sont valides ou non.
    Return:
        - bool: True si les arguments sont valides, False sinon
    """

    # Vérifie si le fichier à décompresser existe
    if not os_path.exists(argv[2]):
        print(f"\n\x1b[31mErreur: \x1b[0m{argv[2]} n'existe pas.")
        return False

    # Vérifie si le nombre d'arguments est correct
    if len(argv) != 3:
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
    return len(parts) > 2 and parts[-2] == "tar" and parts[-1] == "gz"


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
                    for dir_path, _, file_names in walk(file_or_dir):
                        for file in file_names:
                            compress_file(os_path.join(
                                dir_path, file), method, tar)

                else:
                    compress_file(file_or_dir, method, tar)

    except Exception as error:
        print(
            f"\n\x1b[31mErreur: \x1b[0mÉchec lors de la compression: {error}")


def compress_file(file: str, method: str, tar):
    """
    Création de dossier temporaire
    Args:
        - file(str): Fichier à compresser
        - method(list): Méthode de compression à utiliser
        - tar(str): Archive dans laquelle on ajoute nos fichiers codés
    """
    print(f"Compression de: {file}...")

    temp_folder_path = os_path.join(
        os_path.dirname(os_path.abspath(__file__)), 'temp')
    makedirs(temp_folder_path, exist_ok=True)

    temp_file_path = os_path.join(temp_folder_path, os_path.basename(file))

    with open(temp_file_path, "w", encoding="utf-8") as temp_file:
        match method:
            case "rle": coded = encode_rle(read_file(file))
            case "burrows_wheeler": coded, key = transform_bwt(read_file(file))
            case "huffman": coded, key = compress_data(read_file(file))
            case _: raise Exception("Méthode de compression non valide.")

        temp_file.write(coded)
    tar.add(temp_file_path, arcname=os_path.relpath(file))

    if method in ["burrows_wheeler", "huffman"]:
        json_name = '.' + os_path.basename(file) + '.json'
        temp_file_path = os_path.join(temp_folder_path, json_name)
        with open(temp_file_path, "w", encoding="utf-8") as temp_file:
            dump({"code": key}, temp_file)
        json_file_path = os_path.relpath(
            os_path.join(os_path.dirname(file), json_name))
        tar.add(temp_file_path, arcname=json_file_path)

    rmtree(temp_folder_path)


def extract(path: str) -> str:
    """
    Décompresse une archive compressée avec empaktor.
    Args:
        - path(str): Chemin de l'archive à décompresser
    """

    with tar_open(path) as tar:
        path = os_path.basename(path)
        parts = path.split(".")
        parts = parts[:-2]
        path = ".".join(parts)
        path = f"./{path}/"
        tar.extractall(path)

    return path


def decode_files(path: str):
    """
    Args:
    Décode les fichiers d'un dossier en fonction de la méthode de compression
        - path(str): Chemin du dossier contenant les fichiers à décoder
    """
    for dir_path, _, file_names in walk(path):
        for file in file_names:
            if not re_match(r'^\..*\.json$', file):
                print(file)
                json_file_path = os_path.join(dir_path, '.' + file + '.json')
                if os_path.exists(json_file_path):
                    json_data = loads(read_file(json_file_path))
                    if 'code' in json_data:
                        if isinstance(json_data['code'], int):
                            file_path = os_path.join(dir_path, file)
                            coded = read_file(file_path)
                            overwrite_file(file_path, inverse_bwt(
                                coded, json_data['code']))
                            remove(json_file_path)
                        elif isinstance(json_data['code'], dict):
                            file_path = os_path.join(dir_path, file)
                            coded = read_file(file_path)
                            overwrite_file(file_path, decompress_data(
                                coded, json_data['code']))
                            remove(json_file_path)
                    else:
                        raise Exception("Fichier JSON invalide.")
                else:
                    file_path = os_path.join(dir_path, file)
                    coded = read_file(file_path)
                    overwrite_file(file_path, decode_rle(coded))


def main():
    """
    Lance la décompression, la compression ou affiche de l'aide en fonction des
    arguments
    """
    if len(argv) != 1 and argv[1] == "--help":
        help_path = os_path.join(os_path.dirname(os_path.abspath(__file__)),
                                 "help.txt")
        print(read_file(help_path))
    elif not method_manager():
        print(
            "Entrez: \x1b[32mpython3 empaktor.py --help\x1b[0m pour de l'aide."
        )


main()

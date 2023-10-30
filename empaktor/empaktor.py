"""
Module qui va compresser les fichiers à l'aide d'une des 3 méthodes.
"""

from sys import argv
from os import listdir, remove
from tarfile import open as tf_open
# from base64 import b64encode
from json import dump, loads
from cmp_rle.rle import encode_rle, decode_rle
from cmp_burrows.burrows_wheeler import inverse_bwt, transform_bwt
from cmp_huffman.huffman import compress_data, decompress_data


def open_file(name: str) -> str:
    """
    Ouvre un fichier et lit les infos dedans. Puis le ferme.
    """
    with open(name, "r", encoding="utf-8") as file:
        data = file.read()
        file.close()
    return data


def rewrite_file(txt: str, name: str) -> None:
    """
    Réécrit dans un fichier
    """
    with open(name, "a", encoding="utf-8") as file:
        file.truncate(0)
        file.write(txt)
        # file.read()
        file.close()


def compress(name: str, folder: list, method: str) -> None:
    """
    Fonction qui prend en paramètre le nom du fichier à compresser et
    en crée une archive
    """
    with tf_open(name, "w:gz") as temp:
        for files in folder:
            print(f"\nCompression de: {files}...")

            if method == "rle":
                coded = encode_rle(data=open_file(files))
                decoded = decode_rle(encoded_data=coded)
                rewrite_file(coded, files)
                temp.add(files)
                rewrite_file(decoded, files)

            elif method in ["huffman", "burrows_wheeler"]:
                coded = coded_datas(method, files)[0]
                decoded = coded_datas(method, files)[1]
                rewrite_file(coded[0], files)
                temp.add(files)
                rewrite_file(decoded, files)
                with open(".codes.json", "w", encoding="utf-8") as file:
                    dump({"msg": coded[0], "code": coded[1]}, file)
                    file.close()
                temp.add(".codes.json")
                remove(".codes.json")

            print(f"Compression de: {files} dans {name}: [\x1b[32mOK\x1b[0m]")
        temp.close()


def coded_datas(method: str, files: str):
    """
    Renvoie les données en fonction de la méthode
    """
    if method == "huffman":
        coded = compress_data(data=open_file(files))
        decoded = decompress_data(coded[0], coded[1])
    else:
        coded = transform_bwt(data=open_file(files))
        decoded = inverse_bwt(coded[0], coded[1])
    return coded, decoded


def uncompress(name: str) -> None:
    """
    Fonction qui décomppresse l'archive
    """
    print(f"\nDécompression de {name}...")
    with tf_open(name) as file:
        file.extractall(f"./{name[:-7]}")
        print(f"Décompression de {name}: [\x1b[32mOK\x1b[0m]")
        print(f"Éléments décompréssé(s): {file.getnames()}")
        file.close()
    return f"./{name[:-7]}"


def get_files(argvs: list) -> list:
    """
    Récupère les fichiers à compresser et les renvoie
    """
    file_add: list = []
    for i in range(4, len(argvs)):
        file_add.append(argvs[i])
    return file_add


def recode_file(path: str, method: str):
    """
    Recode le fichier après la décompression
    """
    methods = {"huffman": decompress_data, "burrows_wheeler": inverse_bwt}
    for file in listdir(path):
        data = open_file(f"{path}/{file}")
        if method in ["huffman", "burrows_wheeler"] and file == ".codes.json":
            data = loads(open_file(path + "/.codes.json"))
            decoded = methods[method](data["msg"], data["code"])
        elif method == "rle":
            decoded = decode_rle(encoded_data=data)
        rewrite_file(decoded, f"{path}/{file}")
    remove(path + "/.codes.json")


def check_targz(name: str) -> bool:
    """
    Vérifie si le nom du fichier est correct ou pas
    """
    for i, index in enumerate(name):
        if name[i] == ".":
            return name[i:] == ".tar.gz"
    return False


def check_arg_compression() -> bool:
    """
    Teste toutes les erreurs possibles
    """
    # Teste si le fichier est présent ou pas.
    for arg in get_files(argv):
        if arg not in listdir("."):
            print(f"\n\x1b[31mErreur: \x1b[0m{arg} n'existe pas.")
            return False
    # Teste le nom du fichier à compresser
    if not check_targz(argv[1]):
        print(f"\n\x1b[31mErreur: \x1b[0m{argv[1]} n'est pas un nom valide.")
        return False
    # Teste si l'utilisateur a saisi le bon nombre d'argument
    if len(argv) == 3:
        print("\n\x1b[31mErreur: \x1b[0mCommande non valide.")
        return False
    # Test si la méthode utilisée est valide
    if argv[3] not in ["rle", "huffman", "burrows_wheeler"]:
        print(f"\n\x1b[31mErreur: \x1b[0mArgument {argv[3]} non valide.")
        print(f"{argv[3]} n'est pas un algorithme proposé.")
        return False
    # Vérifie si il y a des fihciers à compresser
    if not get_files(argv):
        print("\n\x1b[31mErreur: \x1b[0mLes fichiers n'existent pas.")
        return False
    return True


def check_arg_extract() -> bool:
    """
    Vérifie les erreurs pour la décompression
    python3 0empaktor.py 1--extract 2rle 3nom_archive.tar.gz
    """
    if argv[2] not in ["rle", "huffman", "burrows_wheeler"]:
        print(f"\n\x1b[31mErreur: \x1b[0mArgument {argv[2]} non valide.")
        print(f"{argv[2]} n'est pas un algorithme proposé.")
        return False
    # Vérifie la présence du dossier à compresser
    if argv[3] not in listdir("."):
        print(f"\n\x1b[31mErreur: \x1b[0m{argv[3]} n'existe pas.")
        return False
    # Vérifie le nombre correct d'argument
    if len(argv) != 4:
        print("\n\x1b[31mErreur: \x1b[0mCe n'est pas la bonne commande.\n")
        return False
    return True


def method_manager() -> bool:
    """
    Lance le main pour permettre de décomprésser ou compresser
    """
    if argv == ["empaktor.py"]:
        print("\n\x1b[31mErreur: \x1b[0mVous n'avez rien saisi.\n")
        return False
    if len(argv) < 4:
        print("\n\x1b[31mErreur: \x1b[0mCe n'est pas la bonne commande.\n")
        return False
    # Vérifie si on veut compresser
    if argv[2] == "--compression":
        valid: bool = check_arg_compression()
        if valid:
            compress(argv[1], get_files(argv), argv[3])
        return valid
    # Vérifie si l'on veut décompresser
    if argv[1] == "--extract":
        valid: bool = check_arg_extract()
        if valid:
            path = uncompress(argv[3])
            recode_file(path, argv[2])
        return valid
    # Vérifie les erreurs
    print(f"\n\x1b[31mErreur: \x1b[0mArgument {argv[2]} non valide.")
    print("Il faut utiliser --compression ou --extract.")
    return False


def main() -> None:
    """
    Fonction qui permet de lancer le programme si l'utilisateur ne veux pas
    lire le tuto
    """
    if len(argv) != 1 and argv[1] == "--help":
        print(open_file("help.txt"))
    elif not method_manager():
        print(
            "Tapez: \x1b[32mpython3 empaktor.py --help\x1b[0m pour de l'aide.")


main()

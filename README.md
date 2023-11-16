<h1 align="center">EMPAKTOR</h1>

![Python](https://img.shields.io/badge/Python-grey?style=flat-square&logo=python)
![Version](https://img.shields.io/badge/2.1.0-green?style=flat-square&label=Version)
![Clément Fossorier](https://img.shields.io/badge/Clément_Fossorier-blue?style=flat-square)
![Olivier Vo](https://img.shields.io/badge/Olivier_Vo-blue?style=flat-square)

## Sommaire

1. [Installations](#installations)
    - [Installations classiques](#installations-classiques)
    - [Installations développeurs](#installations-développeurs)
2. [Utilisation](#utilisation)
    - [Compression](#compression)
    - [Décompression](#décompression)
3. [Empaktor](empaktor/empaktor.md)
4. [Algorithmes de compression utilisés](#algorithmes-de-compression-utilisés)
    - [Run-Length Encoding](empaktor/cmp_rle/rle.md)
    - [Burrows-Wheeler Transform](empaktor/cmp_burrows/burrows_wheeler.md)
    - [Huffman Encoding](empaktor/cmp_huffman/huffman.md)
5. [Auteurs](#auteurs)

## Installations
Pour ce projet, plusieurs configurations d'installation existent: la configuration classique permet d'installer les composants nécessaires au fonctionnement du programme, tandis que la configuration développeurs installe les outils nécessaires au développement du programme.

### Installations classiques
Pour effectuer les installations classiques, vous devez éxécuter la commande suivante:
```bash
bash build.sh
```
Celle-ci installe **python3** et **pip3**.

### Installations développeurs
Pour effectuer les installations développeurs, vous devez éxécuter la commande suivante:
```bash
bash build.sh --dev
```
Celle-ci installe **pycodestyle** et **pylint** en supplément.

## Utilisation

### Compression
```bash
python3 empaktor.py [nom_archive] --compression [algo_compression] [nom(s)_fichier(s)]
```
- **Paramètres**:
    - **nom_archive**: Nom de la future archive, doit contenir l'extension ```.tar.gz```
    - **algo_compression**: Algorithme de compression à utiliser (rle, burrows_wheeler, huffman)
    - **nom(s)_fichier(s)**: Nom d'un ou plusieurs fichiers à inclure dans l'archive
- **Sortie**: Archive du nom de [nom_archive]
- **Exemple**:
    - **Arborescence initiale**:
    ```
    |-- empaktor/
    |   |-- empaktor.py
    |   |-- ...
    |-- dossier1/
    |   |-- ...
    |-- fichier1
    |-- fichier2
    |-- ...  
    ```
    - **Commande**:
    ```bash
    python3 empaktor/empaktor.py mon_archive.tar.gz --compression rle fichier1 dossier1 fichier2
    ```
    - **Arboresence après éxécution**:
    ```
    |-- empaktor/
    |   |-- empaktor.py
    |   |-- ...
    |-- dossier1/
    |   |-- ...
    |-- fichier1
    |-- fichier2
    |-- mon_archive.tar.gz
    |-- ...  
    ```

### Décompression
```bash
python3 empaktor.py --extract [nom_archive]
```
- **Paramètres**:
    - **nom_archive**: Nom de l'archive ayant l'extension ```tar.gz``` à décompresser
- **Sortie**: Dossier ayant le nom de l'archive
- **Exemple**:
    - **Arborescence initiale**:
    ```
    |-- empaktor/
    |   |-- empaktor.py
    |   |-- ...
    |-- dossier1/
    |   |-- ...
    |-- fichier1
    |-- fichier2
    |-- mon_archive.tar.gz
    |-- ...  
    ```
    - **Commande**:
    ```bash
    python3 empaktor/empaktor.py --extract mon_archive.tar.gz 
    ```
    - **Arboresence après éxécution**:
    ```
    |-- empaktor/
    |   |-- empaktor.py
    |   |-- ...
    |-- mon_archive/
    |   |-- dossier1/
    |   |   |-- ...
    |   |-- fichier1
    |   |-- fichier2
    |-- dossier1/
    |   |-- ...
    |-- fichier1
    |-- fichier2
    |-- mon_archive.tar.gz
    |-- ...  
    ```

## Empaktor
Documentation de empaktor.py [ici](empaktor/empaktor.md).

## Algorithmes de compression utilisés
Documentation de chacun des algorithmes de compression utilisés:
- [Run-Length Encoding](empaktor/cmp_rle/rle.md)
- [Burrows-Wheeler Transform](empaktor/cmp_burrows/burrows_wheeler.md)
- [Huffman Encoding](empaktor/cmp_huffman/huffman.md)

## Auteurs
**Clément FOSSORIER**(fossor_c) & **Olivier VO**(vo_o)

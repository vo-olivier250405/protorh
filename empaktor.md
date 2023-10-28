# EMPAKTOR

## Compression
```shell
python3 empaktor.py [nom_archive] --compression [algo] [nom_fichier(s)]
```
- **Paramètres d'entrée:**  
    - **nom_archive**: chaine de caractère qui précise le nom de l'archive à créer.
    - **algo**: nom de la méthode de compression our encoder les fichiers
    - **nom_fichier(s)**: nom du ou des fichiers à compresser  

- **Sortie:** Fichier compréssé *nom_archive*
- **Description:**  
  Code le contenu du ou des fichiers avec la méthode spécifiée et renvoi ces mêmes
  fichiers contenu dans un dossier tar.gz
- **Exemple:**  

    **Entrée:**  
    ```shell
    olivier@olivier-Elimina-Iv-15:~/Documents/compression/group-1015076/empaktor$ ls

    cmp_burrows  cmp_huffman  cmp_rle  empaktor.py	help.txt  test.txt  

    olivier@olivier-Elimina-Iv-15:~/Documents/compression/group-1015076/ empaktor$ 
    ```  
    *Commande:*
    ```shell
    python3 empaktor.py test.tar.gz --compression rle test.txt
    ```
    **Sortie:**
    ```shell
    olivier@olivier-Elimina-Iv-15:~/Documents/compression/group-1015076/empaktor$ python3 empaktor.py test.tar.gz --compression rle test.txt

    Compression de: test.txt...
    Compression de: test.txt dans test.tar.gz: [OK]
    olivier@olivier-Elimina-Iv-15:~/Documents/compression/group-1015076/empaktor$ ls

    cmp_burrows  cmp_huffman  cmp_rle  empaktor.py	help.txt  test.tar.gz  test.txt
    ```
## Décompression  
```shell
python3 empaktor.py --extract [nom_archive.tar.gz]
```
- **Paramètres d'entrée:**  
    - **nom_archive.tar.gz**: Nom du dossier tar.gz à décompresser

- **Sortie:** Tout les fichiers contenus dans *nom_archive.ta.gz*
- **Description:**  
  Extrait tout les fichiers dans le dossier compressé et rencode tout leur contenu.

- **Exemple:**  

    **Entrée:**  
    ```shell
    olivier@olivier-Elimina-Iv-15:~/Documents/compression/group-1015076/empaktor$ ls

    cmp_burrows  cmp_huffman  cmp_rle  empaktor.py	help.txt  test.tar.gz  test.txt
    ```  
    *Commande:*
    ```shell
    python3 empaktor.py --extract test.tar.gz
    ```  
    **Sortie:**  
    ```shell
    olivier@olivier-Elimina-Iv-15:~/Documents/compression/group-1015076/empaktor$ python3 empaktor.py --extract rle test.tar.gz

    Décompression de test.tar.gz...
    Décompression de test.tar.gz: [OK]
    Éléments décompréssé(s): ['test.txt']
    olivier@olivier-Elimina-Iv-15:~/Documents/compression/group-1015076/empaktor$ ls
    cmp_burrows  cmp_huffman  cmp_rle  empaktor.py	help.txt  test	test.tar.gz  test.txt
    olivier@olivier-Elimina-Iv-15:~/Documents/compression/group-1015076/empaktor$ ls test
    test.txt
    olivier@olivier-Elimina-Iv-15:~/Documents/compression/group-1015076/empaktor$        
    ```
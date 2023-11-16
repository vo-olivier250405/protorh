# Empaktor

## Compression
```bash
python3 empaktor.py [nom_archive] --compression [algo_compression] [nom(s)_fichier(s)]
```
- **Paramètres**:
    - **nom_archive**: Nom de la future archive, doit contenir l'extension ```.tar.gz```
    - **algo_compression**: Algorithme de compression à utiliser (rle, burrows_wheeler, huffman)
    - **nom(s)_fichier(s)**: Nom d'un ou plusieurs fichiers à inclure dans l'archive
- **Sortie**: Archive du nom de [nom_archive]
- **Exemple**:
  - **Entrée**:  
  ```bash
  olivier@olivier-Elimina-Iv-15:~/Documents/compression/group-1015076/empaktor$ ls

  cmp_burrows  cmp_huffman  cmp_rle  empaktor.py	help.txt  test.txt  

  olivier@olivier-Elimina-Iv-15:~/Documents/compression/group-1015076/ empaktor$ 
  ```
  - **Commande**:
  ```bash
  python3 empaktor.py test.tar.gz --compression rle test.txt
  ```
  - **Sortie**:
  ```bash
  olivier@olivier-Elimina-Iv-15:~/Documents/compression/group-1015076/empaktor$ python3 empaktor.py test.tar.gz --compression rle test.txt

  Compression de: test.txt...
  Compression de: test.txt dans test.tar.gz: [OK]
  olivier@olivier-Elimina-Iv-15:~/Documents/compression/group-1015076/empaktor$ ls

  cmp_burrows  cmp_huffman  cmp_rle  empaktor.py	help.txt  test.tar.gz  test.txt
  ```

## Décompression
```bash
python3 empaktor.py --extract [nom_archive]
```
- **Paramètres**:
    - **nom_archive**: Nom de l'archive ayant l'extension ```tar.gz``` à décompresser
- **Sortie**: Dossier ayant le nom de l'archive
- **Exemple**:
  - **Entrée**:  
  ```bash
  olivier@olivier-Elimina-Iv-15:~/Documents/compression/group-1015076/empaktor$ ls

  cmp_burrows  cmp_huffman  cmp_rle  empaktor.py	help.txt  test.tar.gz  test.txt
  ```  
  -  **Commande**:
  ```bash
  python3 empaktor.py --extract test.tar.gz
  ```  
  - **Sortie**:  
  ```bash
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

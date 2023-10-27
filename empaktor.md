# EMPAKTOR

## Qu’est ce que Empaktor  ?

Empaktor est un programme permettant de compresser ou décomprésser un ou plusieurs fichiers.
Pour cela, celui-ci va utiliser les méthodes suivantes: Huffman, RLE ou Burrows Wheeler.
Lors de la compression, Empaktor va utiliser l’une des trois méthodes précédentes afin d’encoder le  le ou les fichiers. Cela va les rendre moins long, donc, plus légers.
À l’inverse, lors de la décompression, on va utiliser la même méthode afin de décoder ces fichiers et les rendre à leur état d’origine.
Notez qu’Empaktor modifie les fichiers de base lors de la compression et les rencode. N’ayez donc pas peur d’une potentielle perte de données.

## Comment utiliser Empaktor ?  
### Compression:  
*Tapez la commande suivante:*  
```py
python3 empaktor.py [Nom_archive] --compression [Nom_méthode] [nom_fichier1 nom_fichier2] 
```
*Saisissez donc le nom de l’archive à créer, le nom d’une des 3 méthodes de compression, et enfin le ou les fichiers à conpresser.*

### Décompression:  
*Tapez la commande suivante:*  
```py
python3 empaktor.py --extract [nom_archive.tar.gz]
```
*Saisissez seulement le nom de l’archive à extraire*

**Attention à respecter cette syntaxe, le code ne fonctionnera donc pas sans celle-ci.**



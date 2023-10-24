# Codage de Huffman

## Compression
```py
def compress_data(data: str) -> (str, Node)
```
- **Entrée:** Séquence de données à encoder
- **Sortie:** Séquence de données encodée et arnre binaire généré lors de l'encodage
- **Description:** Encode une séquence de données selon le codage de Huffman.
- **Exemple:**
```py
compress_data('aabbbccdddd') -> ('0000101010010111111111', tree)
```

## Décompression
```py
def decompress_data(compressed_data: str, root: Node) -> str
```
- **Entrée:** Séquence de données à encoder et racine de l'arbre binaire permettant la décompression
- **Sortie:** Séquence de données décodée
- **Description:** Décode une séquence de données selon le codage de Huffman.
- **Exemple:**
```py
decompress_data('0000101010010111111111', tree) -> 'aabbbccdddd'
```
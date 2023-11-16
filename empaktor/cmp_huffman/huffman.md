# Codage de Huffman

## Compression
```py
def compress_data(data: str) -> (str, dict)
```
- **Entrée:** Séquence de données à encoder
- **Sortie:** Séquence de données encodée et dictionnaire associant chaque caractère à son code binaire
- **Description:** Encode une séquence de données selon le codage de Huffman.
- **Exemple:**
```py
compress_data('aabbbccdddd') -> ('0000101010010111111111', codes)
```

## Décompression
```py
def decompress_data(compressed_data: str, codes: dict) -> str
```
- **Entrée:** Séquence de données encodée et dictionnaire associant chaque caractère à son code binaire
- **Sortie:** Séquence de données décodée
- **Description:** Décode une séquence de données selon le codage de Huffman.
- **Exemple:**
```py
decompress_data('0000101010010111111111', codes) -> 'aabbbccdddd'
```

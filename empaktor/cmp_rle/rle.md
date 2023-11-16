# Run-Length Encoding

## Codage
```py
def encode_rle(data: str) -> str
```
- **Entrée:** Séquence de données à encoder
- **Sortie:** Séquence de données encodée
- **Description:** Encode une séquence de données selon le codage RLE.
- **Exemple:**
```py
encode_rle('QQA') -> '2Q1A'
```
## Décodage
```py
def decode_rle(encoded_data: str) -> str
```
- **Entrée:** Séquence de données encodée
- **Sortie:** Séquence de données à encoder
- **Description:** Décode une séquence de données selon le codage RLE.
- **Exemple:**
```py
decode_rle('2Q1A') -> 'QQA'
```

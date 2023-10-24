# Run-Length Encoding

**Prototypes:**

```py
def encode_rle(data):
```

- **Paramètre entrée:** chaine de caractères que l'on va coder
- **Sortie:** chaine de caractères codée
- **Description:**  
  Renvoie une autre chaine de caractère codée. Chaque nombre qui précède une lettre est le nombre d'occurences consécutives de cette lettre.
- **Exemple:**

```py
encode_rle("QQA") -> "2Q1A"
```
# 

```py
def decode_rle(encoded_data):
```

- **Paramètre entrée:** chaine de caractères que l'on va décoder
- **Sortie:** chaine de caractères décodée
- **Description:**  
  Renvoie une autre chaine de caractère décodée. Prend le nombre n qui précède
  chaque lettre et ajoute n fois la lettre dans la variable de réultat
- **Exemple:**

```py
decode_rle("2Q1A") -> "QQA"
```

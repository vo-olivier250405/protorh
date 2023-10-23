# Burrows-Wheeler Transform

## Prototypes

### Transformtation
```py
def transform_bwt(data):
```
- **Entrée:** Séquence de données à transformer
- **Sortie:** Séquence de données transformée et clé
- **Description:** Applique la transformation Burrows-Wheeler (BWT) à une séquence de données.
- **Exemple:**
```py
transform_bwt('banana') -> ('nnbaaa', 3)
```

### Restauration
```py
def inverse_bwt(transformed_data, key):
```
- **Entrée:** Séquence de données à restaurer
- **Sortie:** Séquence de données restaurée
- **Description:** Restaure une séquence de données ayant subie une transformation Burrows-Wheeler (BWT).
- **Exemple:**
```py
inverse_bwt('nnbaaa', 3) -> 'banana'
```
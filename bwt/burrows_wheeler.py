def transform_bwt(data):
    '''
    Applique la transformation Burrows-Wheeler (BWT) à une séquence de données.
    Args:
        data: La séquence de données à transformer.
    Returns:
        str: La séquence transformée.
    '''

    # Copie les données d'entrée pour prévenir de toutes modifications
    data_copy = data
    # Crée une liste contenant chacune des lettres de data_copy
    words = list(data_copy)
    # Crée une liste vide qui stockera toutes les rotations possibles
    bwt = []

    # Parcourt la liste de lettres de data_copy pour générer les rotations
    for _ in range(len(words)):
        # Génère une rotation en plaçant la dernière lettre en première
        # position
        rotation = data_copy[-1] + data_copy[:-1]
        # Ajoute la rotation à la liste de rotations
        bwt.append(rotation)
        # Attribue la valeur de la rotation à data_copy pour la prochaine
        # itération
        data_copy = rotation

    # Trie la liste bwt
    bwt = sorted(bwt)

    # Parcourt la liste triée bwt pour récupérer la dernière lettre de chaque
    # rotation
    output = ''
    # Parcours bwt
    for i in range(len(bwt)):
        # Récupère la dernière lettre de la rotation à l'index i et l'ajoute à
        # la variable de sortie
        output = output + bwt[i][-1]
    # Retourne la séquence transformée
    return output


def inverse_bwt(transformed_data, key):
    return

# Nom du chef de projet zerari chaimaa, Master1,
# Liste des membres de l'équipe
# Zerari Chaimaa 6 et 7
# Benali Riham 1 et 2
# Benallal Wafaa 5
# Dib Djazia  8
# Snouci Hanane 3 et 4


import pandas as pd

# Données : Séquences ADN, Longueur, Pourcentage de GC
data = {
    "Séquence": ["ATGCGTACGTA", "GCTAGCTAGGCC", "ATGCGCGTAAGT", "TACGATCGTA", "ATGAAAGGCTT", "CGTACGTAGC", "TTAACCGGAT"],
    "Longueur": [12, 12, 12, 10, 11, 10, 10],
    "Pourcentage GC": [50, 66.67, 58.33, 40, 45.45, 60, 50]
}

# Création d'un DataFrame (tableau pandas)
df = pd.DataFrame(data)

print("**************** Creation et affichage *****************")
# 1) Affichage du tableau
print("Tableau des séquences ADN :\n")
print(df)
print("\n")

print("************** Operations ***************")
# 2) Sélectionner et afficher uniquement la colonne “Longueur”
longueur = df["Longueur"]
print("Colonne Longueur :\n")
print(longueur)
print("\n")

# 3) Filtrer les séquences dont la longueur est supérieure à 10
filtered_df = df[df["Longueur"] > 10]
print("************* Filtrage longueur > 10 *************")
print("Séquences avec longueur > 10 :\n")
print(filtered_df)
print("\n")

# 4) Calculer le pourcentage moyen de GC avec 3 chiffres après la virgule
average_gc = df["Pourcentage GC"].mean()
print("************* Calcul de la moyenne *************")
print(f"Pourcentage moyen de GC : {average_gc:.3f}%\n")

# 5) Ajouter une colonne “Catégorie GC”
def cat_gc(pct):
    if pct > 55:
        return "Riche"
    elif 45 <= pct <= 55:
        return "Moyen"
    else:
        return "Faible"

df["Catégorie GC"] = df["Pourcentage GC"].apply(cat_gc)
print("************* Ajout colonne Catégorie GC *************")
print("Tableau avec Catégorie GC :\n")
print(df)
print("\n")

# 6) Ajouter une colonne donnant le nombre de „G‟ dans chaque séquence
df["Nombre G"] = df["Séquence"].apply(lambda s: s.count('G'))
print("************* Ajout colonne Nombre G *************")
print("Tableau avec Nombre G :\n")
print(df)
print("\n")



# 7) Calculer l‟écart-type du %GC et de la longueur des séquences
std_gc = df["Pourcentage GC"].std()
std_len = df["Longueur"].std()
print("************* Calcul écart-type *************")
print(f"Écart-type %GC : {std_gc:.2f}")
print(f"Écart-type Longueur : {std_len:.2f}\n")



# 8) Sauvegarder le tableau final dans un fichier CSV
df.to_csv("sequences_adn.csv", index=False)
print("************* Sauvegarde CSV *************")
print("Tableau sauvegardé dans sequences_adn.csv")

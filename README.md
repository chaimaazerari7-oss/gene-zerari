# gene-zerari
it's the first projet for try
# ZERARI CHAIMAA
# M1 GENETIGUE 
9/12/2025
SALAM ALIKOM
# BENALI RIHAM 
12/12/2025
JOMOEA MOUBARAKA 
# Benallal wafaa
# SNOUCI HANANE KHADIDJA 
# Dib djazia



# Nom du chef de projet Zirari chaima, Master1,
# Liste des membres de l'équipe
# Benali Riham
# Benallal Wafaa
# Dib Djazia   
# Snouci Hanane


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

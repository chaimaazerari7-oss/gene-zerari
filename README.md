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


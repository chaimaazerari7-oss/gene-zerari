# Nom du chef de projet zerari chaima, Master1,
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
-------------------------------
# 3 et 4) Filtrage et calcul de la moyenne
# ----------------------------------------------------

print("************ Filtrage selon le pourcentage GC *************")
print("#3) Filtrer les séquences avec un pourcentage de GC supérieur à 50%")
filtered_df = df[df["Pourcentage GC"] > 50]
print(filtered_df)
print("\n\n")

# #4) Calcul de la moyenne du pourcentage de GC
print("************ Calcul de la moyenne *************")
print("#4) Calculer la moyenne du pourcentage de GC")
average_gc = df["Pourcentage GC"].mean()
print(f"Pourcentage moyen de GC : {average_gc:.2f}%")
print("\n\n")

# ----------------------------------------------------
# 5) Ajout de nouvelles colonnes
# ----------------------------------------------------
print("************ Ajouter une nouvelle colonne avec des calculs *************")
print("#5) Ajouter une nouvelle colonne basée sur la longueur")

# Ajouter une colonne catégorisant les longueurs
print("# Ajouter une colonne 'Catégorie Longueur'")
df["Catégorie Longueur"] = df["Longueur"].apply(lambda x: "Longue" if x > 10 else "Courte")
print(df)
print("\n")

# #6) Ajouter une colonne comptant le nombre de 'A'
print("#6) Ajouter une colonne comptant les 'A'")
df["Nombre de A"] = df["Séquence"].str.count("A")
print("Nombre de A ajoutés")
print(df)
print("\n\n")

# ----------------------------------------------------
# 7) Sauvegarde et chargement des données
# ----------------------------------------------------
print("************ Sauvegarder et charger les données avec pandas *************")

# Sauvegarder le DataFrame dans un fichier CSV
# df.to_csv("tableau_sequences.csv", index=False)
# print("Le DataFrame a été sauvegardé dans un fichier CSV.")
# print("\n")



إ

print("************** Operations ***************")
# 2) Sélectionner et afficher uniquement la colonne “Longueur”
longueur = df["Longueur"]
print("Colonne Longueur :\n")
print(longueur)
print("\n")

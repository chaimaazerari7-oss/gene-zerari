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
#projet of tp : zerari chaimaa et benali riham et benallal wafaa et snouci hanane et dib djazia 

print("Hello World")

import pandas as pd
import matplotlib.pyplot as plt

# ----------------------------------------------------
# 1) Création et affichage du tableau de données
# ----------------------------------------------------
print("************** Création et affichage ****************")

# Données initiales : séquences, longueurs et pourcentages de GC
sequences = ["ATGCGTAGCTA", "GCTAGCTAGGC", "ATGCGCGCTAAGT", "TACGATCGTA"]
longueur = [12, 12, 12, 10]
gc_content = [50, 66.67, 58.33, 40]

# Création d’un dictionnaire de données
data = {
    "Séquence": sequences,
    "Longueur": longueur,
    "Pourcentage GC": gc_content
}

# Création d’un DataFrame à partir du dictionnaire
df = pd.DataFrame(data)

# Affichage du tableau de données
print("Affichage du tableau des séquences ADN :")
print(df)
print("\n" * 2)

# ----------------------------------------------------
# 2) Opérations sur les tableaux : sélection d’une colonne et visualisation
# ----------------------------------------------------
print("************ Opérations sur les tableaux *************")

# #1) Sélection de la colonne "Séquence"
print("#1) Sélectionner la colonne 'Séquence'")
sequences_series = df["Séquence"]
print(sequences_series)
print("\n")

# #2) Affichage avec matplotlib.pyplot
print("#2) Affichage avec une bibliothèque de visualisation (matplotlib)")
# Diagramme en barres du pourcentage de GC pour chaque séquence
plt.figure(figsize=(10, 6))
plt.bar(df["Séquence"], df["Pourcentage GC"], color='skyblue')
plt.xlabel("Séquences")
plt.ylabel("Pourcentage GC")
plt.title("Pourcentage de GC par séquence")
# plt.show()  # Ligne commentée pour éviter l’affichage dans certaines plateformes
# 3) Filtrer les séquences dont la longueur est supérieure à 10
print("\n3) Filtrage : séquences avec longueur > 10")
filtered_long = df[df["Longueur"] > 10]
print(filtered_long)



# 4) Calculer le pourcentage moyen de GC avec 3 chiffres après la virgule
print("\n**************** Calcul de la moyenne **************")
average_gc = df["Pourcentage GC"].mean()
print(f"Pourcentage moyen de GC : {average_gc:.3f}%")

# 5) Ajouter une colonne "Catégorie GC"
print("\n**** Ajout de colonnes ****")

def categorise_gc(pct):
    if pct > 55:
        return "Riche"
    elif 45 <= pct <= 55:
        return "Moyen"
    else:
        return "Faible"

df["Catégorie GC"] = df["Pourcentage GC"].apply(categorise_gc)

# Ajouter une colonne "Catégorie Longueur"
df["Catégorie Longueur"] = df["Longueur"].apply(lambda x: "Longue" if x > 10 else "Courte")

print(df)

# 6) Ajouter une colonne : nombre de G dans chaque séquence
print("\n===== Nombre de G ajoutés =====")
df["Nombre de G"] = df["Séquence"].str.count("G")
print(df)
# 7) Calculer l'écart-type du %GC et de la longueur
print("\n**** Statistiques descriptives ****")
ecart_type_gc = df["Pourcentage GC"].std()
ecart_type_longueur = df["Longueur"].std()

print(f"Écart-type du %GC : {ecart_type_gc:.3f}")
print(f"Écart-type de la longueur : {ecart_type_longueur:.3f}")

# Sauvegarde CSV
df.to_csv("tableau_sequences_final.csv", index=False)
print("\nLe tableau final a été sauvegardé dans 'tableau_sequences_final.csv'")

# Affichage final complet
print("\n**** Tableau final complet ****")
print(df)

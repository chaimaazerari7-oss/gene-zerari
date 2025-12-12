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

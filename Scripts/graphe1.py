import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Le DataFrame passé par Power BI est nommé 'dataset'
# Colonnes attendues : dataset['CompanyName'] et dataset['Commandes_Livrees']

# 1. Trier les données par commandes livrées (en ordre décroissant)
dataset = dataset.sort_values(by='Nmbr_Commande_livree', ascending=False)
# 2. S'assurer qu'il n'y a que le Top 10 (même si Power BI filtre déjà)
dataset = dataset.head(10)

# 3. Calculer les couleurs pour le gradient
norm = plt.Normalize(dataset['Nmbr_Commande_livree'].min(), dataset['Nmbr_Commande_livree'].max())
cmap = plt.cm.Blues_r # Utiliser une palette inversée pour que les plus grandes valeurs soient plus foncées
colors = cmap(norm(dataset['Nmbr_Commande_livree']))

plt.figure(figsize=(10, 6))

# Création du diagramme en barres horizontales
plt.barh(dataset['CompanyName'], 
         dataset['Nmbr_Commande_livree'], 
         color=colors)

# Afficher les valeurs sur les barres
for index, value in enumerate(dataset['Nmbr_Commande_livree']):
    plt.text(value, index, f' {int(value)}', va='center', fontsize=10)

# Configuration des titres et axes
plt.title('Top 10 des Clients par Commandes Livrées', fontsize=14, pad=15)
plt.xlabel('Nombre de Commandes Livrées', fontsize=12)
plt.ylabel('Client', fontsize=12)
plt.gca().invert_yaxis() # Inverser l'axe Y pour avoir le Top 1 en haut

plt.tight_layout()
plt.show()

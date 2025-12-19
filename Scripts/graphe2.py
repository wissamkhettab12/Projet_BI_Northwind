import matplotlib.pyplot as plt
import pandas as pd

# Le DataFrame passé par Power BI est nommé 'dataset'
# Colonnes disponibles : dataset['mois_annee'], dataset['Nmbre_commande_livree'], dataset['Nmbr_Commande_Non_livree']

# 1. Définir les noms exacts des colonnes pour éviter les erreurs
TEMPS_COL = 'mois_annee'
LIVREE_COL = 'Nmbr_Commande_livree'
NON_LIVREE_COL = 'Nmbr_Commande_Non_livree'

# 2. CALCULER la somme totale des commandes dans une nouvelle colonne du DataFrame
# C'est la correction essentielle : additionner les deux colonnes disponibles.
dataset['Total_Commandes'] = dataset[LIVREE_COL] + dataset[NON_LIVREE_COL]


# S'assurer que le champ temporel est correctement ordonné
dataset = dataset.sort_values(TEMPS_COL)

# Création du graphique
plt.figure(figsize=(10, 5))

# Graphique en courbes avec zone remplie (Area Plot)
plt.plot(dataset[TEMPS_COL], dataset['Total_Commandes'], 
         color='#1E90FF', 
         linewidth=2, 
         label='Total Commandes')

# Remplir l'aire sous la courbe
# Correction de la faute de frappe ('mois_annees' -> 'mois_annee') et utilisation de la nouvelle colonne
plt.fill_between(dataset[TEMPS_COL], 
                 dataset['Total_Commandes'], 
                 color='#1E90FF', 
                 alpha=0.3)

# Configuration des titres et axes
plt.title('Évolution Temporelle du Volume Total des Commandes', fontsize=14, pad=15)
plt.xlabel('Mois-Année', fontsize=12)
plt.ylabel('Nombre de Commandes', fontsize=12)

# Améliorer la lisibilité des étiquettes d'axe X
num_points = len(dataset[TEMPS_COL])
step = max(1, num_points // 8) # Affiche seulement quelques étiquettes pour éviter la surcharge
plt.xticks(dataset[TEMPS_COL][::step], rotation=45, ha='right')
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Afficher la légende et ajuster la mise en page
plt.legend(loc='upper left')
plt.tight_layout()
plt.show()
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Le DataFrame passé par Power BI est nommé 'dataset'
# Colonnes attendues : dataset['RegionDescription'] et dataset['Nmbr_Commande_Non_livree']

# 1. Définir les noms exacts des colonnes
REGION_COL = 'Region'
NON_LIVREE_COL = 'Nmbr_Commande_Non_livree'

# S'assurer que les valeurs sont numériques et trier pour une meilleure présentation
dataset = dataset.sort_values(by=NON_LIVREE_COL, ascending=False)

# --- Configuration du graphique ---
plt.figure(figsize=(9, 9))

# 2. Définir les données et étiquettes
sizes = dataset[NON_LIVREE_COL].values
labels = dataset[REGION_COL].values

# Création des labels avec le pourcentage pour la légende
total = np.sum(sizes)
labels_percent = [f'{lab}\n({(size/total):.1%})' for lab, size in zip(labels, sizes)]

# Utilisation d'une palette de couleurs distincte pour les régions (par exemple, un ensemble de couleurs chaudes)
colors = plt.cm.Dark2.colors 

# 3. Créer le graphique en secteurs (pie chart)
# Le paramètre 'autopct' affichera les pourcentages à l'intérieur de la tranche
wedges, texts, autotexts = plt.pie(sizes, 
                                   autopct='%1.1f%%', 
                                   startangle=90,
                                   colors=colors,
                                   # Création de l'anneau (donut)
                                   wedgeprops=dict(width=0.4, edgecolor='w')) 

# 4. Améliorer la lisibilité des textes intérieurs (pourcentage)
for autotext in autotexts:
    autotext.set_color('white')  # Texte en blanc pour un meilleur contraste sur les couleurs sombres
    autotext.set_fontsize(10)
    
# 5. Centrer le cercle (texte au milieu pour le titre général)
centre_circle = plt.Circle((0,0), 0.6, color='white', fc='white', linewidth=1.25)
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

# 6. Ajouter le titre central et les légendes
plt.text(0, 0, 'Commandes Non Livrées\npar Région', 
         ha='center', 
         va='center', 
         fontsize=14, 
         fontweight='bold', 
         color='#8B0000') # Couleur rouge foncé pour souligner les problèmes régionaux

plt.title('Répartition des Commandes NON Livrées par Région', fontsize=16, pad=20)
plt.axis('equal') # Assure que le diagramme est un cercle.

# 7. Afficher la légende à droite
plt.legend(wedges, labels_percent,
           title="Régions (Part)",
           loc="center left",
           bbox_to_anchor=(1, 0, 0.5, 1))

plt.tight_layout()
plt.show() 

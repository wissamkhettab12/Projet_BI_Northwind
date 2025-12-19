#gprahe 5 
import matplotlib.pyplot as plt
import pandas as pd

# Le DataFrame passé par Power BI est nommé 'dataset'
# Colonnes attendues : 'mois_annee', 'Region', 'Nmbr_Commande_livree'

# 1. Définir les noms exacts des colonnes
TEMPS_COL = 'mois_annee'
REGION_COL = 'Region'
LIVREE_COL = 'Nmbr_Commande_livree'

# 2. S'assurer que le champ temporel est correctement ordonné
dataset = dataset.sort_values(TEMPS_COL)

# 3. Préparer les données pour chaque région
regions = dataset[REGION_COL].unique()

# 4. Créer la figure
plt.figure(figsize=(12, 6))

# 5. Tracer une ligne pour chaque région
for region in regions:
    data_region = dataset[dataset[REGION_COL] == region]
    plt.plot(
        data_region[TEMPS_COL], 
        data_region[LIVREE_COL], 
        label=region, 
        linewidth=2
    )

# 6. Configuration des titres et axes
plt.title('Évolution Mensuelle des Commandes Livrées par Région', fontsize=14, pad=15)
plt.xlabel('Mois-Année', fontsize=12)
plt.ylabel('Nombre de Commandes Livrées', fontsize=12)

# 7. Améliorer la lisibilité des étiquettes d'axe X
num_points = len(dataset[TEMPS_COL].unique())
step = max(1, num_points // 8)  # Affiche seulement quelques étiquettes
plt.xticks(dataset[TEMPS_COL].unique()[::step], rotation=45, ha='right')

# 8. Placer la légende à l'extérieur
plt.legend(title='Région', bbox_to_anchor=(1.05, 1), loc='upper left')

# 9. Ajouter une grille
plt.grid(axis='y', linestyle='--', alpha=0.7)

# 10. Ajuster le layout
plt.tight_layout()

# 11. Afficher le graphique
plt.show()


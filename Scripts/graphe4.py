
#graphe 4 
# Le code suivant, qui crée un dataframe et supprime les lignes dupliquées, est toujours exécuté et sert de préambule à votre script : 

# dataset = pandas.DataFrame(mois_annee)
# dataset = dataset.drop_duplicates()

# Collez ou tapez votre code de script ici :
import matplotlib.pyplot as plt
import pandas as pd

# Colonnes disponibles : dataset['Nmbre_commande_livree'] et dataset['Nmbr_Commande_Non_livree']

# 1. Extraire les valeurs agrégées. Power BI passe généralement une seule ligne (ou la première)
# si aucune dimension n'est sur l'axe.
livrees = dataset['Nmbr_Commande_livree'].iloc[0]
non_livrees = dataset['Nmbr_Commande_Non_livree'].iloc[0]

# 2. Créer un DataFrame temporaire pour le graphique en anneau
data_donut = pd.DataFrame({
    'Statut': ['Commandes Livrée', 'Commandes Non Livrée'],
    'Nombre_Commandes': [livrees, non_livrees]
})

# Création du graphique en anneau (Donut Chart)
plt.figure(figsize=(3, 3))

# 3. Définir les données et étiquettes
sizes = data_donut['Nombre_Commandes']
labels = data_donut['Statut']
colors = ['#B1C9EF','#395886'] # Vert pour Livrée, Orange pour Non Livrée

# 4. Créer le graphique en secteurs (pie chart)
plt.pie(sizes, 
        labels=labels, 
        colors=colors, 
        autopct='%1.1f%%', 
        pctdistance=0.85, 
        startangle=90,
        wedgeprops=dict(width=0.3, edgecolor='w')) 

# 5. Centrer le cercle (donut)
centre_circle = plt.Circle((0,0), 0.7, color='white', fc='white', linewidth=1.25)
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

# Configuration des titres


plt.tight_layout()
plt.show() 


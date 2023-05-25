import matplotlib.pyplot as plt

# Chargement des données
with open('ConsomationBatterieV1.txt', 'r') as f:
    data = f.readlines()

# Extraction des données de vitesse et de consommation d'énergie
batterie = []
distance = []
for line in data:
    tokens = line.split()
    batterie.append(float(tokens[0]))
    distance.append(float(tokens[1]))

# Création du graphique
plt.plot(batterie, distance, label='Simulation V1')
plt.xlabel('Distance (m)')
plt.ylabel('Consommation d\'énergie (Wh/km)')
plt.title('Consommation de la batterie en fonction de la distance du véhicule')
plt.legend()
plt.show()

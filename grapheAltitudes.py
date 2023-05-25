import matplotlib.pyplot as plt

# Chargement des données
with open('altitudes.txt', 'r') as f:
    data = f.readlines()

# Extraction des données de vitesse et de consommation d'énergie
altitudes = []
distance = []
for line in data:
    tokens = line.split()
    altitudes.append(float(tokens[0]))
    distance.append(float(tokens[1]))

# Création du graphique
plt.plot(altitudes, distance, label='Simulation V1')
plt.xlabel('Distance (m)')
plt.ylabel('Altitudes')
plt.title('L\'altitude en fonction de la distance du véhicule')
plt.legend()
plt.show()

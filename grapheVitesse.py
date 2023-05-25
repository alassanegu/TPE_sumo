import matplotlib.pyplot as plt

# Chargement des données
with open('VitesseV1.txt', 'r') as f:
    data = f.readlines()

# Extraction des données de vitesse et de consommation d'énergie
vitesse = []
distance = []
for line in data:
    tokens = line.split()
    vitesse.append(float(tokens[0]))
    distance.append(float(tokens[1]))

# Création du graphique
plt.plot(vitesse, distance, label='Simulation V1')
plt.xlabel('Distance (m)')
plt.ylabel('Vitesse km/h')
plt.title('La vitesse en fonction de la distance du véhicule')
plt.legend()
plt.show()

import matplotlib.pyplot as plt

# Chargement des données
with open('ConsomationEnergieV1.txt', 'r') as f:
    data = f.readlines()

# Extraction des données de vitesse et de consommation d'énergie
energie = []
distance = []
for line in data:
    tokens = line.split()
    energie.append(float(tokens[0]))
    distance.append(float(tokens[1]))

# Création du graphique
plt.plot(energie, distance, label='Simulation V1')
plt.xlabel('Distance (m)')
plt.ylabel('Consommation d\'énergie (Wh/km)')
plt.title('Consommation d\'énergie en fonction de la distance du véhicule')
plt.legend()
plt.show()

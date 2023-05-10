import matplotlib.pyplot as plt

# Chargement des données
with open('ConsomationEnergieV1.txt', 'r') as f:
    data = f.readlines()

# Extraction des données de vitesse et de consommation d'énergie
vitesse1 = []
consommation1 = []
for line in data:
    tokens = line.split()
    vitesse1.append(float(tokens[0]))
    consommation1.append(float(tokens[1]))


# Chargement des données
with open('ConsomationEnergieV2.txt', 'r') as f:
    data = f.readlines()

# Extraction des données de vitesse et de consommation d'énergie
vitesse2 = []
consommation2 = []
for line in data:
    tokens = line.split()
    vitesse2.append(float(tokens[0]))
    consommation2.append(float(tokens[1]))

# Chargement des données
with open('ConsomationEnergieV1.txt', 'r') as f:
    data = f.readlines()

# Extraction des données de vitesse et de consommation d'énergie
vitesse3 = []
consommation3 = []
for line in data:
    tokens = line.split()
    vitesse3.append(float(tokens[0]))
    consommation3.append(float(tokens[1]))

# Création du graphique
plt.plot(vitesse1, consommation1, label='Simulation V1')
plt.plot(vitesse2, consommation2, label='Simulation V2')
plt.plot(vitesse3, consommation3, label='Simulation v3')
plt.xlabel('Distance')
plt.ylabel('Consommation d\'énergie (Wh/km)')
plt.title('Consommation d\'énergie en fonction de la distance du véhicule')
plt.legend()
plt.show()

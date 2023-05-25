import matplotlib.pyplot as plt

# Chargement des données
with open('EmissionCO2V1.txt', 'r') as f:
    data = f.readlines()

# Extraction des données de vitesse et de consommation d'énergie
emissionCO2 = []
distance1 = []
for line in data:
    tokens = line.split()
    emissionCO2.append(float(tokens[0]))
    distance1.append(float(tokens[1]))

# Chargement des données
with open('EmissionCO2VehThermique.txt', 'r') as f:
    data = f.readlines()

# Extraction des données de vitesse et de consommation d'énergie
emissionTher = []
distance2 = []
for line in data:
    tokens = line.split()
    emissionTher.append(float(tokens[0]))
    distance2.append(float(tokens[1]))

# Création du graphique
plt.plot(emissionCO2, distance1, label='Simulation V1')
plt.plot(emissionTher, distance2, label='Simulation Veh Thermique')
plt.xlabel('Distance (m)')
plt.ylabel('Emission CO2')
plt.title('Emission CO2 en fonction de la distance du véhicule')
plt.legend()
plt.show()

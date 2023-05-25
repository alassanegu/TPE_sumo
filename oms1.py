import json
import os, sys

import matplotlib.pyplot as plt

import time

# Vérifie si l'environnement SUMO_HOME est défini
if 'SUMO_HOME' in os.environ:
    tools = os.path.join(os.environ['SUMO_HOME'], 'tools')
    sys.path.append(tools)
else:
    sys.exit("Veuillez déclarer la variable d'environnement 'SUMO_HOME'")

# Importe les modules TraCI et les constantes de TraCI
import traci
import traci.constants

# Démarre SUMO avec la configuration osm.sumocfg et affiche la fenêtre graphique
sumoCmd = ["sumo-gui", "-c", "osm.sumocfg", "--start"]
traci.start(sumoCmd)

# Change l'affichage de la vue 0 de SUMO pour qu'elle corresponde au "monde réel"
traci.gui.setSchema("View #0", "real world")

# Chargement du fichier coords.json
with open("coords.json", "r") as f:
    coords_data = json.load(f)

z = 20
idPolygon = "polygon"
for coord in coords_data['coordonnees']:
    # Définir les coordonnées du polygone
    polygon_coords = [(coord['y'] - z, coord['x'] - z), (coord['y'] - z, coord['x'] + z),
                      (coord['y'] + z, coord['x'] + z), (coord['y'] + z, coord['x'] - z)]
    # Ajouter le polygone à la simulation SUMO
    idPolygon = "p_" + "" + coord['adresse']
    if (coord['adresse'] == "Hub"):
        traci.polygon.add(idPolygon, polygon_coords, color=(0, 0, 255), fill=True, polygonType=coord['adresse'])
    else:
        traci.polygon.add(idPolygon, polygon_coords, color=(255, 0, 0), fill=True, polygonType=coord['adresse'])
    # print(idPolygon)


# Chargement du fichier lesTournees.json
with open("lesTournees.json", "r") as f:
    data_tournee = json.load(f)

tournee_id = ""
edges = []
for tournee in data_tournee['tournees']:
    tournee_id = "route_{}".format(tournee["tournee"])
    edges = tournee["edges"]
    traci.route.add(tournee_id, edges)

print(traci.route.getIDList())

# Ajouter trois véhicules à la position du hub avec une vitesse de 30 km/h
id_v1 = "V1"
id_v2 = "V2"
id_v3 = "V3"
id_vehThermique = "VehThermique"
route_id_v1 = "route_tournee_v1"
route_id_v2 = "route_tournee_v2"
route_id_v3 = "route_tournee_v3"


veh_type = "veh_electric"
class_type = "cl_electric"

traci.vehicle.add(id_v1, route_id_v1, typeID=veh_type, departSpeed="8.333")
traci.vehicle.add(id_v2, route_id_v2, typeID=veh_type, departSpeed="8.333")
traci.vehicle.add(id_v3, route_id_v3, typeID=veh_type, departSpeed="8.333")
traci.vehicle.add(id_vehThermique, route_id_v1, departSpeed="8.333")


# Chargement du fichier lesTournees.json
with open("coordonnees.json", "r") as f:
    data = json.load(f)

altitudes = []

# ouverture du fichier pour écrire les résultats
with open("altitudes.txt", "a") as f:
    # exécution de la simulation pendant quelques secondes
    for i in range(100):
        traci.simulationStep()
        for veh_type_id in traci.vehicle.getIDList():
            #if veh_type_id == id_v1 or veh_type_id == id_v2 or veh_type_id == id_v3:
            if veh_type_id == id_v1:

                speeds = 50/3.6
                #vitess max egal à 50km/h
                traci.vehicle.setSpeed(veh_type_id, speeds)

                vitesse = traci.vehicle.getSpeed(veh_type_id) * 3.6
                for coords in data['coordonnees']:
                    altitudes = coords['altitude']
                    f.write(f" {traci.vehicle.getDistance(veh_type_id)} {coords['altitude']}\n")
                    print("d = ", traci.vehicle.getDistance(veh_type_id), " al = ", coords['altitude'])
                #
                # total_energy_consumed = float(traci.vehicle.getParameter(veh_type_id, "device.battery.totalEnergyConsumed"))
                # electricity_consumption = traci.vehicle.getElectricityConsumption(veh_type_id)
                # if total_energy_consumed != 0:
                #     mWh = traci.vehicle.getDistance(veh_type_id) / total_energy_consumed
                #     #remainingRange = float(traci.vehicle.getParameter(id_v1, "device.battery.actualBatteryCapacity")) * mWh
                #     # f.write(f"La valeur du paramètre donné pour {veh_type_id} : {total_energy_consumed}\n")
                #     # f.write(f"La distance parcourue par {veh_type_id} : {traci.vehicle.getDistance(veh_type_id)}\n")
                #     # f.write(f"La consommation d'énergie de {veh_type_id} : {mWh}\n")
                #     # f.write(f"Pourcentage de Batterie restante : {remainingRange}\n")
                #     # f.write(f"la consommation d'électricité en Wh/s de {veh_type_id} : {electricity_consumption}\n")
                #     #f.write(f" {traci.vehicle.getDistance(veh_type_id)} {electricity_consumption}\n")
                #     f.write(f" {traci.vehicle.getDistance(veh_type_id)} {mWh}\n")
                # else:
                #     f.write(f"{traci.vehicle.getDistance(veh_type_id)} 0\n")


# Fermer la connexion à la simulation
traci.close()



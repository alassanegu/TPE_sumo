import json
import os, sys
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
import math

# Démarre SUMO avec la configuration osm.sumocfg et affiche la fenêtre graphique
sumoCmd = ["sumo-gui", "-c", "osm.sumocfg", "--start"]
traci.start(sumoCmd)

# Change l'affichage de la vue 0 de SUMO pour qu'elle corresponde au "monde réel"
traci.gui.setSchema("View #0", "real world")


# Lecture des données à partir du fichier JSON
with open('adresses.json', 'r') as f:
    data = json.load(f)

# # Conversion des coordonnées latitude et longitude en coordonnées x et y
# coords = []
# for adresse in data['adresses']:
#     cord = traci.simulation.convertGeo(adresse['longitude'], adresse['latitude'], True)
#     coords.append({'adresse': adresse['adresse'], 'x': cord[0], 'y': cord[1]})
#
# # Écriture des nouvelles coordonnées dans un nouveau fichier JSON
# with open('coords.json', 'w') as f:
#     json.dump(coords, f, indent=4)


# Chargement du fichier coords.json
with open("coords.json", "r") as f:
    coords_data = json.load(f)

z = 20
idPolygon = "polygon"
for coord in coords_data['coordonnees']:
    # Définir les coordonnées du polygone
    polygon_coords = [(coord['y'] - z, coord['x'] - z), (coord['y'] - z, coord['x'] + z), (coord['y'] + z, coord['x'] + z), (coord['y'] + z, coord['x'] - z)]
    # Ajouter le polygone à la simulation SUMO
    idPolygon = "p_"+""+coord['adresse']
    if(coord['adresse'] == "Hub"):
        traci.polygon.add(idPolygon, polygon_coords, color=(0, 0, 255), fill=True, polygonType=coord['adresse'])
    else:
        traci.polygon.add(idPolygon, polygon_coords, color=(255, 0, 0), fill=True,  polygonType=coord['adresse'])
    #print(idPolygon)

# def find_nearest_junction(x, y):
#     nearest_distance = float('inf')
#     nearest_junction = None
#
#     for junction in traci.junction.getIDList():
#         junction_coords = traci.junction.getPosition(junction)
#         dist = ((junction_coords[0]-y)**2 + (junction_coords[1]-x)**2)**0.5
#         if dist < nearest_distance:
#             nearest_distance = dist
#             nearest_junction = junction
#
#     return nearest_junction
#
# juncts = []
# # Parcours des coordonnées pour trouver la jonction la plus proche
# for coord in coords_data['coordonnees']:
#     x = coord['x']
#     y = coord['y']
#     adresse = coord['adresse']
#     nearest_junction = find_nearest_junction(x, y)
#     juncts.append({'adresse': adresse, 'x': x, 'y': y, 'junction_id': nearest_junction})
#     print(adresse, " ==>", nearest_junction)
#     print("Position junction ", adresse, " est : ", traci.junction.getPosition(nearest_junction))
#
# # Écriture des nouvelles coordonnées dans un nouveau fichier JSON
# with open('adressJunction.json', 'w') as f:
#     json.dump(juncts, f, indent=4)

# Charger le fichier edge.json
with open("edge.json") as f:
    data_edge = json.load(f)


route_hub_cantine_1 = []
hub_edge_id = ""
cantine1_edge_id = ""
# Parcourir les edges et récupérer les edges correspondantes
for edge in data_edge['edges']:
    if edge["adresse"] == "Hub":
        hub_edge_id = edge["edge_id"]
    elif edge["adresse"] == "Cantine 1":
        cantine1_edge_id = edge["edge_id"]
    # elif edge["adresse"] == "Cantine 2":
    #     cantine1_edge_id = edge["edge_id"]
    # elif edge["adresse"] == "Cantine 3":
    #     cantine1_edge_id = edge["edge_id"]
    # elif edge["adresse"] == "Cantine 4":
    #     cantine1_edge_id = edge["edge_id"]
    # elif edge["adresse"] == "Cantine 5":
    #     cantine1_edge_id = edge["edge_id"]
    # elif edge["adresse"] == "Cantine 6":
    #     cantine1_edge_id = edge["edge_id"]
    # elif edge["adresse"] == "Cantine 7":
    #     cantine1_edge_id = edge["edge_id"]
    # elif edge["adresse"] == "Cantine 8":
    #     cantine1_edge_id = edge["edge_id"]
    # elif edge["adresse"] == "Cantine 9":
    #     cantine1_edge_id = edge["edge_id"]
    # elif edge["adresse"] == "Cantine 10":
    #     cantine1_edge_id = edge["edge_id"]

route_hub_cantine_1 = traci.simulation.findRoute(hub_edge_id, cantine1_edge_id)

# routes = []
# # Récupérer la liste des edges de la route
# edges_route = route_hub_cantine_1.edges
#
# routes.append({'route': "route_hub_cantine_1", 'edges': edges_route})
#
# # Enregistrer la liste des edges dans un fichier JSON
# with open("routes.json", "w") as f:
#     json.dump(routes, f, indent=4)

# Chargement du fichier routes.json
with open("routes.json", "r") as f:
    data_routes = json.load(f)

route_id = ""
edges = []
for route in data_routes['routes']:
    route_id = route["route"]
    edges = route["edges"]
    route_1 = traci.route.add(route_id, edges)

print(traci.route.getEdges(route_id))

# Ajouter trois véhicules à la position du hub avec une vitesse de 30 km/h
for i in range(3):
    vehicle_id = "V{}".format(i + 1)
    route_id = "route_hub_cantine_1"
    # Ajouter le véhicule à SUMO
    traci.vehicle.add(vehicle_id, route_id, depart="0")
    print(vehicle_id)
    print(traci.vehicle.getRouteID(vehicle_id))





# exécution de la simulation pendant quelques secondes
for i in range(1000):
    traci.simulationStep()
    print(traci.vehicle.getIDList())


# Fermer la connexion à la simulation
traci.close()

import gzip
import json
import os
import sys
import xml.etree.ElementTree as ET

# Vérifie si l'environnement SUMO_HOME est défini
if 'SUMO_HOME' in os.environ:
    tools = os.path.join(os.environ['SUMO_HOME'], 'tools')
    sys.path.append(tools)
else:
    sys.exit("Veuillez déclarer la variable d'environnement 'SUMO_HOME'")

# Importe les modules TraCI et les constantes de TraCI
import traci.constants

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
#    json.dump({"coordonnees" : coords}, f, indent=4)


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


# for i in traci.edge.getIDList():
#     print(i, traci.simulation.convert2D(i, False))

# def find_nearest_edges(x, y):
#     nearest_distance = float('inf')
#     nearest_edges = None
#     for edg in traci.edge.getIDList():
#         edge_coords = traci.simulation.convert2D(edg, False)
#         dist = ((edge_coords[0] - y) ** 2 + (edge_coords[1] - x) ** 2) ** 0.5
#         if dist < nearest_distance:
#             nearest_distance = dist
#             nearest_edges = edg
#
#     return nearest_edges

# edges = []
# # Parcours des coordonnées pour trouver la jonction la plus proche
# for coord in coords_data['coordonnees']:
#     x = coord['x']
#     y = coord['y']
#     adresse = coord['adresse']
#     nearest_edges = find_nearest_edges(x, y)
#     edges.append({'adresse': adresse, 'x': x, 'y': y, 'edges_id': nearest_edges})
#     print(adresse, " ==>", nearest_edges)
#     print("Position edges ", adresse, " est : ", traci.simulation.convert2D(nearest_edges, False))
#     print("Position ", adresse, " est : (", y, ", ", x)
#
# # Écriture des nouvelles coordonnées dans un nouveau fichier JSON
# with open('adressEdges.json', 'w') as f:
#     json.dump({"edges" : edges}, f, indent=4)


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
#     #print(adresse, " ==>", nearest_junction)
#     #print("Position junction ", adresse, " est : ", traci.junction.getPosition(nearest_junction))

# Écriture des nouvelles coordonnées dans un nouveau fichier JSON
# with open('adressJunction.json', 'w') as f:
#     json.dump(juncts, f, indent=4)


# def getEdgeFromJonction(file, junction):
#     with gzip.open(file, 'r') as f:
#         xml_content = f.read()
#         root = ET.fromstring(xml_content)
#     for element in root.iter():
#         if element.attrib.get("from") == junction:
#             return element.attrib.get("id")
#
#
# # Charger le fichier edge.json
# with open("adressJunction.json") as f:
#     adressJunction = json.load(f)
#
# edges = []
# # Parcourir les edges et récupérer les edges correspondantes
# for junction in adressJunction['junctions']:
#     idJunction = junction["junction_id"]
#     adresse = junction["adresse"]
#     edges.append({'adresse': adresse, 'edges_id': getEdgeFromJonction('osm.net.xml.gz', idJunction)})
# Écriture des nouvelles coordonnées dans un nouveau fichier JSON
# with open('Edges.json', 'w') as f:
#     json.dump(edges, f, indent=4)

# Charger le fichier edge.json
with open("edge.json") as f:
    data_edge = json.load(f)

# pour v1
route_hub_cantine_6 = []
route_cantine_6_cantine_10 = []
route_cantine_10_cantine_8 = []
route_cantine_8_cantine_4 = []
route_cantine_4_hub = []
# pour v2
route_hub_cantine_7 = []
route_cantine_7_cantine_2 = []
route_cantine_2_cantine_1 = []
route_cantine_1_hub = []
# pour v3
route_hub_cantine_9 = []
route_cantine_9_cantine_5 = []
route_cantine_5_cantine_3 = []
route_cantine_3_hub = []

hub_edge_id = ""
cantine1_edge_id = ""
cantine2_edge_id = ""
cantine3_edge_id = ""
cantine4_edge_id = ""
cantine5_edge_id = ""
cantine6_edge_id = ""
cantine7_edge_id = ""
cantine8_edge_id = ""
cantine9_edge_id = ""
cantine10_edge_id = ""
# Parcourir les edges et récupérer les edges correspondantes
for edge in data_edge['edges']:
    if edge["adresse"] == "Hub":
        hub_edge_id = edge["edge_id"]
    elif edge["adresse"] == "Cantine 1":
        cantine1_edge_id = edge["edge_id"]
    elif edge["adresse"] == "Cantine 2":
        cantine2_edge_id = edge["edge_id"]
    elif edge["adresse"] == "Cantine 3":
        cantine3_edge_id = edge["edge_id"]
    elif edge["adresse"] == "Cantine 4":
        cantine4_edge_id = edge["edge_id"]
    elif edge["adresse"] == "Cantine 5":
        cantine5_edge_id = edge["edge_id"]
    elif edge["adresse"] == "Cantine 6":
        cantine6_edge_id = edge["edge_id"]
    elif edge["adresse"] == "Cantine 7":
        cantine7_edge_id = edge["edge_id"]
    elif edge["adresse"] == "Cantine 8":
        cantine8_edge_id = edge["edge_id"]
    elif edge["adresse"] == "Cantine 9":
        cantine9_edge_id = edge["edge_id"]
    elif edge["adresse"] == "Cantine 10":
        cantine10_edge_id = edge["edge_id"]

# POUR V1
route_hub_cantine_6 = traci.simulation.findRoute(hub_edge_id, cantine6_edge_id)
route_cantine_6_cantine_10 = traci.simulation.findRoute(cantine6_edge_id, cantine10_edge_id)
route_cantine_10_cantine_8 = traci.simulation.findRoute(cantine10_edge_id, cantine8_edge_id)
route_cantine_8_cantine_4 = traci.simulation.findRoute(cantine8_edge_id, cantine4_edge_id)
route_cantine_4_hub = traci.simulation.findRoute(cantine4_edge_id, hub_edge_id)

# POUR V2
route_hub_cantine_7 = traci.simulation.findRoute(hub_edge_id, cantine7_edge_id)
route_cantine_7_cantine_2 = traci.simulation.findRoute(cantine7_edge_id, cantine2_edge_id)
route_cantine_2_cantine_1 = traci.simulation.findRoute(cantine2_edge_id, cantine1_edge_id)
route_cantine_1_hub = traci.simulation.findRoute(cantine1_edge_id, hub_edge_id)

# POUR V3
route_hub_cantine_9 = traci.simulation.findRoute(hub_edge_id, cantine9_edge_id)
route_cantine_9_cantine_5 = traci.simulation.findRoute(cantine9_edge_id, cantine5_edge_id)
route_cantine_5_cantine_3 = traci.simulation.findRoute(cantine5_edge_id, cantine3_edge_id)
route_cantine_3_hub = traci.simulation.findRoute(cantine3_edge_id, hub_edge_id)

# Récupérer la liste des edges de la route
routes = []
tournees = []
# POUR V1
edges_hub_cantine_6 = route_hub_cantine_6.edges
edges_cantine_6_cantine_10 = route_cantine_6_cantine_10.edges
edges_cantine_10_cantine_8 = route_cantine_10_cantine_8.edges
edges_cantine_8_cantine_4 = route_cantine_8_cantine_4.edges
edges_cantine_4_hub = route_cantine_4_hub.edges

routes.append({'route': "route_hub_cantine_6", 'edges': edges_hub_cantine_6})
routes.append({'route': "route_cantine_6_cantine_10", 'edges': edges_cantine_6_cantine_10})
routes.append({'route': "route_cantine_10_cantine_8", 'edges': edges_cantine_10_cantine_8})
routes.append({'route': "route_cantine_8_cantine_4", 'edges': edges_cantine_8_cantine_4})
routes.append({'route': "route_cantine_4_hub", 'edges': edges_cantine_4_hub})

edges_v1 = edges_hub_cantine_6 + edges_cantine_6_cantine_10 + edges_cantine_10_cantine_8 + edges_cantine_8_cantine_4 + edges_cantine_4_hub
tournees.append({'tournee': "tournee_v1", 'edges1': edges_v1})

# POUR V2
edges_hub_cantine_7 = route_hub_cantine_7.edges
edges_cantine_7_cantine_2 = route_cantine_7_cantine_2.edges
edges_cantine_2_cantine_1 = route_cantine_2_cantine_1.edges
edges_cantine_1_hub = route_cantine_1_hub.edges

routes.append({'route': "route_hub_cantine_7", 'edges': edges_hub_cantine_7})
routes.append({'route': "route_cantine_7_cantine_2", 'edges': edges_cantine_7_cantine_2})
routes.append({'route': "route_cantine_2_cantine_1", 'edges': edges_cantine_2_cantine_1})
routes.append({'route': "route_cantine_1_hub", 'edges': edges_cantine_1_hub})

edges_v2 = edges_hub_cantine_7 + edges_cantine_7_cantine_2 + edges_cantine_2_cantine_1 + edges_cantine_1_hub
tournees.append({'tournee': "tournee_v2", 'edges2': edges_v2})

# POUR V3
edges_hub_cantine_9 = route_hub_cantine_9.edges
edges_cantine_9_cantine_5 = route_cantine_9_cantine_5.edges
edges_cantine_5_cantine_3 = route_cantine_5_cantine_3.edges
edges_cantine_3_hub = route_cantine_3_hub.edges

routes.append({'route': "route_hub_cantine_9", 'edges': edges_hub_cantine_9})
routes.append({'route': "route_cantine_9_cantine_5", 'edges': edges_cantine_9_cantine_5})
routes.append({'route': "route_cantine_5_cantine_3", 'edges': edges_cantine_5_cantine_3})
routes.append({'route': "route_cantine_3_hub", 'edges': edges_cantine_3_hub})

edges_v3 = edges_hub_cantine_9 + edges_cantine_9_cantine_5 + edges_cantine_5_cantine_3 + edges_cantine_3_hub
tournees.append({'tournee': "tournee_v3", 'edges3': edges_v3})

# # Enregistrer la liste des edges dans un fichier JSON
# with open("routes.json", "w") as f:
#     json.dump({"routes" : routes}, f, indent=4)

# #Enregistrer la liste des edges dans un fichier JSON
# with open("lesTournees.json", "w") as f:
#     json.dump({"tournees":tournees}, f, indent=4)


# Chargement du fichier lesTournees.json
with open("lesTournees.json", "r") as f:
    data_tournee = json.load(f)

tournee_id = ""
edges = []
for tournee in data_tournee['tournees']:
    tournee_id = "route_{}".format(tournee["tournee"])
    edges = tournee["edges"]
    traci.route.add(tournee_id, edges)

# Ajouter trois véhicules à la position du hub avec une vitesse de 30 km/h
id_v1 = "V1"
id_v2 = "V2"
id_v3 = "V3"
id_vT = "VT"
route_id_v1 = "route_tournee_v1"
route_id_v2 = "route_tournee_v2"
route_id_v3 = "route_tournee_v3"

veh_type = "veh_electric"
class_type = "cl_electric"

traci.vehicle.add(id_v1, route_id_v1, typeID=veh_type, departSpeed="8.333")
traci.vehicle.add(id_v2, route_id_v2, typeID=veh_type, departSpeed="8.333")
traci.vehicle.add(id_v3, route_id_v3, typeID=veh_type, departSpeed="8.333")
traci.vehicle.add(id_vT, route_id_v1, departSpeed="8.333")


# exécution de la simulation pendant quelques secondes
for i in range(30):
    traci.simulationStep()

    for veh_type_id in traci.vehicle.getIDList():
        #if veh_type_id == id_v1 or veh_type_id == id_v2 or veh_type_id == id_v3:
        if veh_type_id == id_vT:
            speeds = 50 / 3.6
            # vitess max egal à 50km/h
            traci.vehicle.setSpeed(veh_type_id, speeds)

            vitesse = traci.vehicle.getSpeed(veh_type_id) * 3.6
            print("La vitesse de ", veh_type_id, " : ", vitesse)

            print("Renvoie l'émission de CO2 en mg/s pour le dernier pas de temps.",
                  traci.vehicle.getCO2Emission(veh_type_id))

            total_energy_consumed = float(traci.vehicle.getParameter(veh_type_id, "device.battery.totalEnergyConsumed"))
            electricity_consumption = traci.vehicle.getElectricityConsumption(veh_type_id)
            if total_energy_consumed != 0:
                mWh = traci.vehicle.getDistance(veh_type_id) / total_energy_consumed
                remainingRange = float(traci.vehicle.getParameter(id_v1, "device.battery.actualBatteryCapacity")) * mWh
                print("La valeur du paramètre donné pour ", veh_type_id, " : ", total_energy_consumed)
                print("La distance parcourue par ", veh_type_id, " : ", traci.vehicle.getDistance(veh_type_id))
                print("La consommation d'énergie de ", veh_type_id, " : ", mWh)
                print("Pourcentage de Batterie restante :", remainingRange)
                print("la consommation d'électricité en Wh/s de ", veh_type_id, ":", electricity_consumption)
            else:
                print("La valeur du paramètre donné pour ", veh_type_id, " est égale à zéro")



# Fermer la connexion à la simulation
traci.close()

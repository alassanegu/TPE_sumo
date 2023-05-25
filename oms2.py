import os
import sys
import requests
import polyline
import json

from sumolib.datastructures.OrderedMultiSet import KEY


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

# Conversion des coordonnées latitude et longitude en coordonnées x et y
coords = []
for adresse in data['adresses']:
    cord = traci.simulation.convertGeo(adresse['longitude'], adresse['latitude'], True)
    coords.append({'adresse': adresse['adresse'], 'x': cord[0], 'y': cord[1]})


# Chargement du fichier coords.json
with open("coords.json", "r") as f:
    coords_data = json.load(f)

# # Récupération des tournées et de leurs edges depuis le fichier lesTournees.json
# with open('lesTournees.json', 'r') as f:
#     tournees_data = json.load(f)
#
# for tournee in tournees_data['tournees']:
#     tournee_name = tournee['tournee']
#     tournee_edges = tournee['edges']
#     tournee_coords= []
#
#     # Récupération des coordonnées des edges pour la tournée actuelle
#     for edge_id in tournee_edges:
#         edge_coords = traci.simulation.convert3D(edge_id, False)
#         tournee_coords.append({'edge_id': edge_id, 'x': edge_coords[1], 'y': edge_coords[0]})
#
#     # Écriture des coordonnées dans un fichier SUMO spécifique à la tournée
#     filename = f"{tournee_name}_coords.json"
#     with open(filename, 'w') as f:
#         json.dump({'coords': tournee_coords}, f, indent=2)
#
#     # Écriture des coordonnées dans un fichier SUMO spécifique à la tournée
#     filename = f"{tournee_name}_coords.json"
#     with open(filename, 'r') as f:
#         tournee_name_data = json.load(f)
#
#     coords_routes = []
#     for coords in tournee_name_data['coords']:
#         route_coords = traci.simulation.convertGeo(coords['x'], coords['y'], False)
#         coords_routes.append({'edge_id': coords['edge_id'], 'latitude': route_coords[1], 'longitude': route_coords[0]})
#
#
#     # Écriture des coordonnées dans un fichier SUMO spécifique à la tournée
#     filename = f"{tournee_name}_route.json"
#     with open(filename, 'w') as f:
#         json.dump({'coords': coords_routes}, f, indent=2)




# Charger les données du fichier adresses.json
with open('tournee_v1_route.json') as f:
    data = json.load(f)

# Récupérer les coordonnées du fichier adresses.json
coordinates = [(item['latitude'], item['longitude']) for item in data['coords']]

# Encodage des coordonnées en polyline
geom = polyline.encode(coordinates, 5)
print(geom)

# Corps de la requête
body = {"format_in": "encodedpolyline5", "geometry": geom}

# En-têtes de la requête
headers = {
    'Accept': 'application/json, application/geo+json, application/gpx+xml, img/png',
    'Authorization': '5b3ce3597851110001cf6248bf1aa98f33164a638143086d9eb447be',
    'Content-Type': 'application/json; charset=utf-8'
}

# Appel à l'API OpenRouteService pour obtenir l'altitude
call = requests.post('https://api.openrouteservice.org/elevation/line', json=body, headers=headers)

# Extraction des coordonnées avec altitude de la réponse
coordinates_with_altitude = json.loads(call.text)["geometry"]["coordinates"]

# Création du dictionnaire pour les coordonnées avec altitude
coordonnees = []
for i in range(len(coordinates_with_altitude)):
    coordonnee = {
        "latitude": coordinates[i][0],
        "longitude": coordinates[i][1],
        "altitude": coordinates_with_altitude[i][2]
    }
    coordonnees.append(coordonnee)

# Enregistrement des coordonnées dans le fichier coordonnees.json
with open('coordonnees.json', 'w') as f:
    json.dump({"coordonnees": coordonnees}, f, indent=4)

print("Coordonnées avec altitude enregistrées dans le fichier coordonnees.json.")



# exécution de la simulation pendant quelques secondes
for i in range(50):
    traci.simulationStep()


traci.close()

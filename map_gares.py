#create the map of the trains stations whith the data from "coords.geojson"

import folium
import pandas as pd
import json
import plotly.graph_objects as go
import plotly.express as px
import numpy as np

nouveaux_noms = {
    'Date'                                                                                          : 'Date',
    'Service'                                                                                       : 'Service',
    'Gare de départ'                                                                                : 'Gare_de_depart',
    'Gare d\'arrivée'                                                                               : 'Gare_d_arrivee',
    'Durée moyenne du trajet'                                                                       : 'Duree_moyenne_du_trajet',
    'Nombre de circulations prévues'                                                                : 'Nombre_de_circulations_prevues',
    'Nombre de trains annulés'                                                                      : 'Nombre_de_trains_annules',
    'Commentaire annulations'                                                                       : 'Commentaire_annulations',
    'Nombre de trains en retard au départ'                                                          : 'Nombre_de_trains_en_retard_au_depart',
    'Retard moyen des trains en retard au départ'                                                   : 'Retard_moyen_des_trains_en_retard_au_depart',
    'Retard moyen de tous les trains au départ'                                                     : 'Retard_moyen_de_tous_les_trains_au_depart',
    'Commentaire retards au départ'                                                                 : 'Commentaire_retards_au_depart',
    'Nombre de trains en retard à l\'arrivée'                                                       : 'Nombre_de_trains_en_retard_à_l_arrivee',
    'Retard moyen des trains en retard à  l\'arrivée'                                               : 'Retard_moyen_des_trains_en_retard_à_l_arrivee',
    'Retard moyen de tous les trains à  l\'arrivée'                                                 : 'Retard_moyen_de_tous_les_trains_à_l_arrivee',
    'Commentaire retards à  l\'arrivée'                                                             : 'Commentaire_retards_à_l_arrivee',
    'Nombre trains en retard > 15min'                                                               : 'Nombre_trains_en_retard',
    'Retard moyen trains en retard > 15 (si liaison concurrencée par vol)'                          : 'Retard_moyen_trains_en_retard_>_15_si_liaison_concurrencee_par_vol',
    'Nombre trains en retard > 30min'                                                               : 'Nombre_trains_en_retard_>_30min',
    'Nombre trains en retard > 60min'                                                               : 'Nombre_trains_en_retard_>_60min',
    'Prct retard pour causes externes'                                                              : 'Prct_retard_pour_causes_externes',
    'Prct retard pour cause infrastructure'                                                         : 'Prct_retard_pour_cause_infrastructure',
    'Prct retard pour cause gestion trafic'                                                         : 'Prct_retard_pour_cause_gestion_trafic',
    'Prct retard pour cause matériel roulant'                                                       : 'Prct_retard_pour_cause_materiel_roulant',
    'Prct retard pour cause gestion en gare et réutilisation de matériel'                           : 'Prct_retard_pour_cause_gestion_en_gare_et_reutilisation_de_materiel',
    'Prct retard pour cause prise en compte voyageurs (affluence, gestions PSH, correspondances)'   : 'Prct_retard_pour_cause_prise_en_compte_voyageurs_affluence,_gestions_PSH,_correspondances'
}

noms_gares = {
    'PARIS LYON' : 'PARIS',
    'PARIS MONTPARNASSE': 'PARIS',
    'LYON PART DIEU': 'LYON',
    'PARIS EST': 'PARIS',
    'PARIS NORD': 'PARIS',
    'MARSEILLE ST CHARLES': 'MARSEILLE',
    'LILLE': 'LILLE',
    'RENNES': 'RENNES',
    'NANTES': 'NANTES',
    'BORDEAUX ST JEAN': 'BORDEAUX',
    'STRASBOURG': 'STRASBOURG',
    'MARNE LA VALLEE': 'CHESSY',
    'MONTPELLIER': 'MONTPELLIER'
}

#read the data from geojson files
with open("coords.geojson") as f:
    geodata = json.load(f)

#import tes data from csv
data = pd.read_csv("data.csv", sep=";")
data.rename(columns=nouveaux_noms, inplace=True)

stations = data["Gare_de_depart"]
nombre_apparition = stations.value_counts()
stations_filtree = nombre_apparition.loc[nombre_apparition >= 100]
print("stations_filtree = ", stations_filtree)
print("\n")
print(type(stations_filtree))
print("\n")
stations_corigee = stations_filtree.rename(noms_gares)
print("stations_corigee = ", stations_corigee)

#Create the map
map = folium.Map(location=[46.227638,2.213749], tiles='OpenStreetMap', zoom_start=6)

deja_fait = []
not_in = {}

a = 0

#Create the markers
for i in range(len(geodata['features'])):

    if geodata['features'][i]['properties']['commune'] in stations_corigee and geodata['features'][i]['properties']['commune'] not in deja_fait:
        deja_fait.append(geodata['features'][i]['properties']['commune'])
    
        if geodata['features'][i]['properties']['commune'] == "CHESSY" and geodata['features'][i]['properties']['commune'] != "Marne-la-Vall\u00e9e-Chessy":
            continue

        folium.Marker([geodata['features'][i]['geometry']['coordinates'][1],
                        geodata['features'][i]['geometry']['coordinates'][0]],
                        popup=geodata['features'][i]['properties']['libelle']
        ).add_to(map)
    else:
        not_in[geodata['features'][i]['properties']['commune']] = geodata['features'][i]['properties']['commune']

print("\n")
print("deja_fait = ", deja_fait)
# print("\n")
# print("not_in = ", not_in)
print("\n")
print("a = ", a)

#Save the map
map.save(outfile='gare.html')

import dash
from dash import Dash, dcc, html, Input, Output
import numpy as np
import plotly.express as px
import pandas as pd
import random

import map_gares

app = Dash(__name__)

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

colors = {
    'background': '#C4F5FC',
    'text': '#000000',
    'axis' : '#000000'
}

data = pd.read_csv('data.csv', sep=';', header=0)
data.rename(columns=nouveaux_noms, inplace=True)

########### MAP + DATA PREMIER GRAPH GRAPH ###########
index_gares = map_gares.create_map()

########### PREMIER GRAPH ###########

list_index_gares = index_gares.tolist()
for param in list_index_gares:
    gare = data.query(f'Gare_de_depart == "{param}"')
    gare_moy = gare.groupby('Gare_de_depart', as_index=False)[["Duree_moyenne_du_trajet"]].mean()
compteur = data['Gare_de_depart'].value_counts()
compteur2 = compteur.where(compteur > 100)
compteur2 = compteur2.dropna()

figure = px.bar(y = compteur2, x = compteur2.index, barmode="group")    

figure.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text'],
    xaxis_title='Noms des gares',
    yaxis_title='Nombre de trajets',
    title="Nombre de trajets par gare de départ pour les gares ayant plus de 100 trajets au départ",
    xaxis = dict(linecolor=colors['axis']),
    yaxis = dict(linecolor=colors['axis']),
)

figure.update_traces(marker_line_color='black', marker_line_width=1)

random_colors = [random.choice(['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']) for i in range(len(data))]
figure.update_traces(marker_color=random_colors)

########### DEUXIEME GRAPH ###########

data['tps_arrondi'] = data['Duree_moyenne_du_trajet'].apply(lambda x: x/60)
tps_arrondi = data['tps_arrondi'].value_counts()

fig = px.histogram(data, x="tps_arrondi", labels={"tps_arrondi":"Temps de trajet (en heures)", "y" : "Nombre de trajets"})

fig.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text'],
    xaxis_title='Temps en heures',
    yaxis_title='Nombre de trajets',
    title="Temps de trajet arrondi à l'heure",
    xaxis = dict(linecolor=colors['axis']),
    yaxis = dict(linecolor=colors['axis'])
)

fig.update_traces(marker_line_color='black', marker_line_width=2)

######################################
########### STRUCTURE HTML ###########

app.layout = html.Div(
    style={'backgroundColor': colors['background']},
    children=[
    html.H1(
        children='Python Dashboard',
        style={
            'textAlign': 'center',
        }
    ),

    html.Div(children='Traitement d\'un data set sur les trains', 
    style={
        'textAlign': 'center',
        'color': colors['text'],
        'backgroundColor': colors['background'],
        'margin-bottom': '35px'
    }),

    ########### PRESENATION DATASET ###########

    html.Hr(),

    html.Div(
        children=[
            "Ce dashboard est réalisé à partir de deux data set de la SNCF sur les trains en France.",
            html.Br(),
            html.Br(),
            " Le fichier CSV contient des informations sur la régularité des trains TGV sur une période donnée,"
            " chaque ligne représentant les données de régularité pour un mois donné.",
            html.Br(),
            "Le fichier GeoJSON en question contient une liste de gares en France, avec des informations sur leur"
            " nom, leur localisation géographique (latitude et longitude), leur code de gare, leur type de gare"
            " (par exemple, TGV, TER, RER, etc.) ainsi que d'autres détails. Chaque gare est représentée sous la forme d'un"
            " objet JSON avec ces différentes propriétés.",
            html.Br(),
            html.Br(),
            " Ce data set contient les informations suivantes :",
            html.Br(),
            "Gare de départ - Gare d'arrivée - Durée moyenne du trajet - Nombre de trains au départ - Nombre de trains à l'arrivée"
            " - Nombre de trains annulés - Nombre",
            html.Br(),
            html.Br(),
            "Il contient d'autres colonnes avec des pourcentages en fonction de certaines données. Comme par exemple la régularité des trains,"
            " ce qui désigne" 
            " le pourcentage de trains qui arrivent à l'heure à leur destination finale. Cette donnée est calculée en comparant le nombre"
            " de trains arrivés à l'heure à leur destination finale au nombre total de trains prévus pour cette ligne."
        ],
        style={
            'textAlign': 'left',
            'color': colors['text'],
            'display': 'block',
            'margin-bottom': '20px'
        }
    ),

    html.Hr(),

    ########### PREMIER GRAPH ###########

    html.Div(
        children=[
            "Ce graphique représente le nombre de trajets par gare de départ pour les gares ayant plus de 100 trajets au départ.",
            html.Br(),
            "Cliquez sur une barre pour afficher les informations de la gare : Ville - Nombre de train au départ",
            html.Br(),
            "On remarque que la gare de Paris Gare de Lyon est la gare la plus importante avec plus de 1474 trajets au départ.",
            html.Br()
            ],
        style={
            'textAlign': 'left', 
            'color': colors['text'], 
            'display': 'block',
            'margin-bottom': '20px',
            'margin-top': '50px',
        }
    ),

    dcc.Graph(
        id='graph-test',
        figure=figure
    ),

    html.Div(
        style={
            'height': '80px'
            }
        ),

    ########### MAP ###########

    html.Div(
        children=[
            "Cette carte ci dessous représente toutes les gares dans les villes ayant au moins une gare importante.",
            html.Br(),
            "Une gare est considérée comme importante si elle a plus de 100 trajets au départ. (cf graphique ci dessus)",
            html.Br(),
            "Cliquez sur une gare pour afficher ses inoformations : Ville - libellé de la gare",
            html.Br()
            ],
        style={
            'textAlign': 'center', 
            'color': colors['text'], 
            'display': 'block',
            'margin-bottom': '20px'
        }
    ),

    html.Div(
        children=[
        html.Iframe(
                id='map',
                srcDoc=open('gare.html', 'r').read(),
                width='50%',
                height='600'
            )
        ],
        className='row',
        style={
            'display': 'flex', 
            'justify-content': 'center', 
            'color': colors['text'],
            'backgroundColor': colors['background'],
            'margin-bottom': '30px'
        }
    ),

    # html.Div(
    #     children=[
    #         "Pour plus de clareté sur la carte, les gares on été regroupées par villes",
    #         html.Br(),
    #         "C'est pour quoi a Paris par exemple, il n'y a qu'une seul gare",
    #         html.Br()
    #         ],
    #     style={
    #         'textAlign': 'center', 
    #         'color': colors['text'], 
    #         'display': 'block',
    #         'backgroundColor': colors['background'],
    #         'margin-bottom': '20px',
    #         'margin-top': '20px'
    #         }
    # ),

    ########### DEUXIEME GRAPH ###########

    dcc.Graph(
        id='example-graph',
        figure=fig
    ),

    html.Div(
        children=[
            "Le graphe ci dessus repésente le temps de trajet arrondi à l'heure pour l'ensemble des trajets présent dans le dataset : \"data.csv\"",
            html.Br(),
            "On peut voir que la majorité des trajets durent entre 1h et 4h et même plus précisément entre 1h et 2h.",
            ],
        style={
            'textAlign': 'center', 
            'color': colors['text'], 
            'display': 'block',
            'backgroundColor': colors['background'],
            'margin-bottom': '20px'
            }
    ),

    ########### TROISIEME GRAPH ###########

    html.Div(
        children=[
            "Le graphe ci dessous repésente ..............................",
            html.Br(),
            "On peut voir ................................................",
            ],
        style={
            'textAlign': 'center', 
            'color': colors['text'], 
            'display': 'block',
            'backgroundColor': colors['background'],
            'margin-top': '60px'
            }
    ),

    dcc.Graph(
        id='example-graph3'
    ),
    html.P("Mean:"),
    dcc.Slider(
        id="mean", 
        min=0, 
        max=150, 
        value=150, 
        marks={0: '0', 150: '150'}
    ),

    html.Footer(
    children=[
        html.Div(
            children=[
                "Projet réalisé par : Pierre ALLA et Ahmed Rais - Date : 2021 - Matière : Python"
                ],
                style={
                    'textAlign': 'center',
                    'color': colors['text'],
                    'backgroundColor': colors['background'],
                    'margin-top': '20px',
                    'margin-bottom': '5px'
                }
            )
        ]
    )
])
#######################################
########### TROISIEME GRAPH ###########

@app.callback(
    Output("example-graph3", "figure"), 
    Input("mean", "value"))

def display_color(mean):
    data = pd.read_csv('data.csv', sep=';', header=0)
    data.rename(columns=nouveaux_noms, inplace=True) 

    circulation = data.groupby("Gare_de_depart", as_index=False)[["Nombre_de_trains_en_retard_au_depart", "Retard_moyen_des_trains_en_retard_au_depart"]].sum()
    circulation["moyenne"] = circulation.apply(lambda x: (x.Retard_moyen_des_trains_en_retard_au_depart / x.Nombre_de_trains_en_retard_au_depart)*100, axis = 1)
    circulation = circulation[ circulation["moyenne"] < mean ]

    fig3 = px.histogram(circulation, x="moyenne", y = "Gare_de_depart", color="Gare_de_depart", range_x=[0,mean])
    
    fig3.update_layout(
        plot_bgcolor=colors['background'],
        paper_bgcolor=colors['background'],
        font_color=colors['text'],
        xaxis_title='Nom des gares',
        yaxis_title='Moyenne',
        title="Pourcentage de trains en retard par nombre de trains",
        xaxis = dict(linecolor=colors['axis']),
        yaxis = dict(linecolor=colors['axis'])
    )
    
    return fig3 

if __name__ == '__main__':
    app.run_server(debug=True)
    # app.run_server(debug=False)
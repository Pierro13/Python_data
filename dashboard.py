# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import dash
from dash import Dash, dcc, html, Input, Output
import numpy as np
import plotly.express as px
import pandas as pd

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
    'background': '#000000',
    'text': '#7FDBFF'
}

data = pd.read_csv('data.csv', sep=';', header=0)
data.rename(columns=nouveaux_noms, inplace=True)
gare = data.query('Gare_de_depart == "PARIS LYON" or Gare_de_depart == "MARSEILLE ST CHARLES" or Gare_de_depart == "AIX EN PROVENCE TGV"')
gare_moy = gare.groupby('Gare_de_depart', as_index=False)[["Duree_moyenne_du_trajet"]].mean()
timing = data["Duree_moyenne_du_trajet"].value_counts()

fig = px.bar(gare_moy, x="Gare_de_depart", y="Duree_moyenne_du_trajet", color="Gare_de_depart", barmode="group")

fig.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)

#list of the most frenquented stations


# data['tps_arrondi'] = data['tps'].apply(lambda x: round(x/30)*30 if(x < 240 and x > 0) else 240)
data['tps_arrondi'] = data['Duree_moyenne_du_trajet'].apply(lambda x: x/60)
tps_arrondi = data['tps_arrondi'].value_counts()

#creation d'un histogramme avec les temps arrondi à la demi heure et avec un pas de 60 en abscisse
fig2 = px.histogram(data, x="tps_arrondi", title="Temps de trajet arrondi à l'heure", 
                        labels={"tps_arrondi":"Temps de trajet (en heures)", "y" : "Nombre de trajets"})

fig2.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)

map_gares.create_map()

app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
        children='Python Dashboard',
        style={
            'textAlign': 'center',
        }
    ),

    html.Div(children='Traitement d\'un data set sur les trains', style={
        'textAlign': 'center',
        'color': colors['text']
    }),

    dcc.Graph(
        id='example-graph2',
        figure=fig
    ),

    dcc.Graph(
        id='example-graph',
        figure=fig2
    ),

    dcc.Graph(
        id='example-graph3'
    ),
    html.P("Mean:"),
    dcc.Slider(id="mean", min=0, max=150, value=150, 
        marks={0: '0', 150: '150'}),

    html.Div(
        children=[
            html.Iframe(
                id='map',
                srcDoc=open('gare.html', 'r').read(),
                width='50%',
                height='800'
            )
        ],
        className='row',
        style={'textAlign': 'center', 'color': '#7FDBFF'}
    )
])

@app.callback(
    Output("example-graph3", "figure"), 
    Input("mean", "value"))



def display_color(mean):
    data = pd.read_csv('data.csv', sep=';', header=0)
    data.rename(columns=nouveaux_noms, inplace=True) 

    circulation = data.groupby("Gare_de_depart", as_index=False)[["Nombre_de_trains_en_retard_au_depart", "Retard_moyen_des_trains_en_retard_au_depart"]].sum()
    circulation["moyenne"] = circulation.apply(lambda x: (x.Retard_moyen_des_trains_en_retard_au_depart / x.Nombre_de_trains_en_retard_au_depart)*100, axis = 1)
    # print(circulation.columns)
    #circulation["moyenne"] = circulation.apply(lambda x: print(x.Gare_de_depart), axis=1)
    #print(circulation["moyenne"])
    circulation = circulation[ circulation["moyenne"] < mean ]

    fig3 = px.histogram(circulation, x="moyenne", y = "Gare_de_depart", color="Gare_de_depart", range_x=[0,mean], title="Pourcentage de trains en retard par nombre de trains")
    return fig3

if __name__ == '__main__':
    app.run_server(debug=True)
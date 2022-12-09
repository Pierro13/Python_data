# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import dash
from dash import Dash, html, dcc
import numpy as np
import plotly.express as px
import pandas as pd

app = Dash(__name__)

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

data = pd.read_csv("data.csv")
gare = data.query('Gare_de_depart == "PARIS LYON" or Gare_de_depart == "MARSEILLE ST CHARLES" or Gare_de_depart == "AIX EN PROVENCE TGV"')
gare_moy = gare.groupby('Gare_de_depart', as_index=False)[["tps"]].mean()
timing = data["tps"].value_counts()

fig = px.bar(gare_moy, x="Gare_de_depart", y="tps", color="Gare_de_depart", barmode="group")

fig.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)

# data['tps_arrondi'] = data['tps'].apply(lambda x: round(x/30)*30 if(x < 240 and x > 0) else 240)
data['tps_arrondi'] = data['tps'].apply(lambda x: x/60)
tps_arrondi = data['tps_arrondi'].value_counts()

#creation d'un histogramme avec les temps arrondi à la demi heure et avec un pas de 60 en abscisse
fig2 = px.histogram(data, x="tps_arrondi", title="Temps de trajet arrondi à l'heure", 
                        labels={"tps_arrondi":"Temps de trajet (en heures)", "y" : "Nombre de trajets"})

fig2.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)


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

    html.Div(
        children=[
            html.Iframe(
                id='map',
                srcDoc=open('map3.html', 'r').read(),
                width='50%',
                height='400'
            )
        ],
        className='row',
        style={'textAlign': 'center', 'color': '#7FDBFF'}
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
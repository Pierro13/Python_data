# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import dash
from dash import Dash, html, dcc
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

# fig = px.scatter(gare, x="Gare_de_depart", y="tps", color="Gare_de_depart", size="tps", hover_data=['tps'])

fig = px.bar(gare_moy, x="Gare_de_depart", y="tps", color="Gare_de_depart", barmode="group")

fig.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)

app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
        children='Hello Dash',
        style={
            'textAlign': 'center',
        }
    ),

    html.Div(children='Dash: A web application framework for your data.', style={
        'textAlign': 'center',
        'color': colors['text']
    }),

    dcc.Graph(
        id='example-graph-2',
        figure=fig
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
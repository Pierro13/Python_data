#create the map of the trains stations whith the data from "coords.geojson"

import folium
import pandas as pd
import json
import plotly.graph_objects as go
import plotly.express as px
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

#read the data from geojson files
with open("coords.geojson") as f:
    geodata = json.load(f)

#Create the map
map = folium.Map(location=[48.7190835,2.4609723], tiles='OpenStreetMap', zoom_start=9)
#Create the markers
for i in range(len(geodata['features'])):
    folium.Marker([geodata['features'][i]['geometry']['coordinates'][1],geodata['features'][i]['geometry']['coordinates'][0]],popup=geodata['features'][i]['properties']['name']).add_to(map)

#Save the map
map.save(outfile='gare.html')

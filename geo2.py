import geojson, geopandas
import pandas as pd
import folium

pop_data = pd.read_csv('insee-pop-communes.csv', sep=';')
dpt_code = pop_data['DEPCOM']

mask = ( ( dpt_code.str.startswith('75')  )
        | ( dpt_code.str.startswith('77') )
        | ( dpt_code.str.startswith('78') )
        | ( dpt_code.str.startswith('91') )
        | ( dpt_code.str.startswith('92') )
        | ( dpt_code.str.startswith('93') )
        | ( dpt_code.str.startswith('94') )
        | ( dpt_code.str.startswith('95') ) )

pop_data = pop_data[mask]

coords = (48.7190835,2.4609723)
map = folium.Map(location=coords, tiles='OpenStreetMap', zoom_start=9)

# geodata = geopandas.read_file("idf.geojson")

with open("idf.geojson") as f:
    geodata = geojson.load(f)



folium.Choropleth(
    geo_data=geodata,
    name='choropleth',
    data=pop_data,
    columns=['DEPCOM', 'PTOT'], # data key/value pair
    key_on='feature.properties.code_commune', # corresponding layer in GeoJSON
    fill_color='YlGn',
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name='Population'
).add_to(map)

map.save(outfile='map3.html')
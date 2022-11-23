import folium, geopandas as gpd

coords = (46.227638,2.213749)
map = folium.Map(location=coords, tiles='OpenStreetMap', zoom_start=6)
data = gpd.read_file("Projet\regularite-mensuelle-tgv-aqst.csv")

geo = data.to_json()

import pandas as pd

data = pd.read_csv("data.csv")
gare = data.query('Gare_de_depart == "PARIS LYON" or Gare_de_depart == "MARSEILLE ST CHARLES" or Gare_de_depart == "AIX EN PROVENCE TGV"')
gare_moy = gare.groupby('Gare_de_depart', as_index=False)[["tps"]].mean()

print(gare)
print("")
print(gare_moy)
print("")
print(gare_moy.columns)
print(gare_moy.index)
print("")
print(gare.columns)
print(gare.index)
print("")
print(gare_moy.loc['PARIS LYON']["tps"])

import pandas as pd

data = pd.read_csv("data.csv")
gare = data.query('Gare_de_depart == "PARIS LYON" or Gare_de_depart == "MARSEILLE ST CHARLES" or Gare_de_depart == "AIX EN PROVENCE TGV"')
gare_moy = gare.groupby('Gare_de_depart', as_index=False)[["tps"]].mean()

# print(gare)
# print("")
# print(gare_moy)

timing = data["tps"].value_counts()
print("")
print(timing)
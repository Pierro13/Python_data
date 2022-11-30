import pandas as pd

data = pd.read_csv("data.csv")
gare = data.query('Gare_de_depart == "PARIS LYON" or Gare_de_depart == "MARSEILLE ST CHARLES" or Gare_de_depart == "AIX EN PROVENCE TGV"')
gare_moy = gare.groupby('Gare_de_depart', as_index=False)[["tps"]].mean()

# print(gare)
# print("")
# print(gare_moy)

# timing = data["tps"].value_counts()
# print("")
# print(timing)

#ajout d'une collone "temps arrondi" qui arrondi les temps de trajet à la demi heure
data['tps_arrondi'] = data['tps'].apply(lambda x: round(x/30)*30 if(x < 240 and x > 0) else 240)

#print de la collone "temps arrondi"
print(data['tps_arrondi'])
print("")

#print max et min de "temps arrondi"
print(data['tps_arrondi'].max())
print(data['tps_arrondi'].min())
print("")

#création d'un dataframe avec les temps arrondis
tps_arrondi = data['tps_arrondi'].value_counts()
print(tps_arrondi)



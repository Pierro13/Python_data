from urllib import request
import os

try : 
    file = open("data.csv")
    file.close()
    os.remove("data.csv")
    url = 'https://ressources.data.sncf.com/explore/dataset/regularite-mensuelle-tgv-aqst/download/?format=csv&timezone=Europe/Berlin&lang=fr&use_labels_for_header=true&csv_separator=%3B'
    fichier = 'data.csv'
    request.urlretrieve(url, fichier)
except FileNotFoundError:
    url = 'https://ressources.data.sncf.com/explore/dataset/regularite-mensuelle-tgv-aqst/download/?format=csv&timezone=Europe/Berlin&lang=fr&use_labels_for_header=true&csv_separator=%3B'
    fichier = 'data.csv'
    request.urlretrieve(url, fichier)

try :
    file2 = open("coords.geojson")
    file2.close()
    os.remove("coords.geojson")
    url2 = 'https://data.sncf.com/explore/dataset/liste-des-gares/download/?format=geojson&timezone=Europe/Paris&lang=fr'
    fichier2 = 'coords.geojson'
    request.urlretrieve(url2, fichier2)
except FileNotFoundError:
    url2 = 'https://data.sncf.com/explore/dataset/liste-des-gares/download/?format=geojson&timezone=Europe/Paris&lang=fr'
    fichier2 = 'coords.geojson'
    request.urlretrieve(url2, fichier2)

print("Les deux fichiers sont bien téléchargés et à jour !")
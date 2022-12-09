from urllib import request
url = 'https://ressources.data.sncf.com/explore/dataset/regularite-mensuelle-tgv-aqst/download/?format=csv&timezone=Europe/Berlin&lang=fr&use_labels_for_header=true&csv_separator=%3B'
fichier = 'data.csv'
url2 = 'https://data.sncf.com/explore/dataset/liste-des-gares/download/?format=geojson&timezone=Europe/Paris&lang=fr'
fichier2 = 'coords.geojson'
request.urlretrieve(url, fichier)
request.urlretrieve(url2, fichier2)
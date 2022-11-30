from urllib import request
url = 'https://ressources.data.sncf.com/explore/dataset/regularite-mensuelle-tgv-aqst/download/?format=csv&timezone=Europe/Berlin&lang=fr&use_labels_for_header=true&csv_separator=%3B'
fichier = 'data.csv'
request.urlretrieve(url, fichier)
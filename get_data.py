from urllib import request
url = 'https://ressources.data.sncf.com/explore/dataset/regularite-mensuelle-tgv-aqst/download/?format=json&timezone=Europe/Berlin&lang=fr'
fichier = 'data.json'
request.urlretrieve(url, fichier)
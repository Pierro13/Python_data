# Python dashboard

Autheurs : Pierre ALLA - Ahmed RAIS

Classe : E3 FI groupe 3

---

### User Guide

Ce dashboard est réalisé à partir de deux data set de la SNCF sur les trains en France.

Pour le visualiser, il faut d'abord que vous ayez installé les bonnes libraries et que vous téléchargiez les datasets grâce au fichier python : getdata.py

Pour avoir les bonnes libraries executez la commande : ``pip install -r requirements.txt``

Ensuite executer la commande : `python getdata.py` affin de télécharger ou de mettre à jours les datasets.

Puis pour démarrer le dashboard, il faut exécuter le fichier python avec la commande : `python main.py`

Enfin il faudra ouvrir un navigateur web et aller à l'adresse : `http://127.0.0.1:8050/` (ou celle spécifiée dans la console)

[Lien du data set](http://127.0.0.1:8050/ "`http://127.0.0.1:8050/`")

---

### Rapport d'analyse

Grâce à ce dashboard nous pouvons en conclure que les retards de la SNCF sont liées a la fréquentation de la gare. En effet plus une gare est fréquentée plus elle accumule de retard. 

Par exemple la gare : "Paris Gare de Lyon" est la gare la plus fréquentée avec 1474 départ de liaison.

Ce pendant elle n'a que 30% de train en retard ce qui n'est pas si important que ça en comparaison avec SAINT ETIENNE CHATEAUCREUX qui en compte 92%. Cela s'explique par le fait qu'il suffit que le peu de trains passant par SAINT ETIENNE CHATEAUCREUX soit en retard et ainsi donc avoir un poucentage élévé.

---

### Developper Guide

Le code est structuré en deux sections. 

La première permettant l'instalation des datasets nécéssaire et la seconde section qui s'occupe de la création du Dashboard est composé du `main.py` et du `map_gares.py`.

Nous avons décidé de sectionner la partie de création du Dashboard en deux parties car l'ors de l'écriture de nos fichiers de code,

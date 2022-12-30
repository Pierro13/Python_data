Pierro
#6279
💻Segmentation Fault

Pierro — 23/12/2022 16:22
et si tu peux tt relire pour vérifier que j'ai pas fait de fautes c'est top
Raisahmed — 23/12/2022 16:42
ok ça marche je relirais et j'ajouterais ce que tu m'as dis d'ajouter concernant mon graphe
Pierro — 23/12/2022 16:43
Ok tu gères tes ne boss
Raisahmed — 24/12/2022 12:02
Normalement j'ai push essaye de voir si tu peux récupérer ce que j'ai fait
Pierro — 24/12/2022 13:29
ouais c'est clean
je pense que le seul truc qu'on pourrait changer c'est sur le graph des temps moyen dans le tooltip changer l'affichage de l'heure
genre passer de 1.6-1.69h à 1h40-1h49
fin je sais pas si c'est ca le bon calcul
mais c'est une idée que j'ai eu
Raisahmed — 24/12/2022 14:20
Ouais en vrai on pourrait faire ça après c'est un peu compliqué parce que du coup les trucs à 1.70h faut les convertir et jsp trop comment on s'y prend
Pierro — 24/12/2022 15:24
Ouais bv
Je pense qu'on a fini mais je vais voir si jamais on a pas de nouvelle idée
Raisahmed — 24/12/2022 21:56
Désolé de te répondre que maintenant mais ouais en vrai si t’as des idées de trucs à rajouter vas y moi pour l’instant je pense c’est ok
Pierro — 25/12/2022 00:06
tkt tkt y a le temps bg 
Pierro — Hier à 11:56
ouais bg
on avait pas vu mais y a encore un truc a faire :
https://perso.esiee.fr/~courivad/3IPR2/miniprojetdata.html#miniprojet:~:text=travail%20sera%20%C3%A9valu%C3%A9.-,Remise%20du%20travail,-%C2%B6
faut écrire le readme.md avec plusieurs sections
j'ai pas mal commencé mais chaud que tu avances dessus aussi
j'ai tout push
Raisahmed — Hier à 11:59
j'ai lu vite fait ce qu'il devait y avoir dans le readme maintenant je comprends toi y'a quoi comme trucs que t'as mis dedans que je sache ce qu'il me reste à faire ?
Pierro — Hier à 12:00
Le Developper Guide j'ai pas tour fait
Et le reste faudrait que tu corrige / ajoute des trucs si tu vois des trucs qui manque
Raisahmed — Hier à 12:03
Ok bah vas y pas de soucis je fini le Developper Guide c'est le truc que j'ai le mieux compris et je regarderais pour le reste je te dis si ça peut être amélioré !
Pierro — Hier à 12:14
Ouais parfait 
Et après regarde sur le site en générale si on a bien tout fait
Raisahmed — Hier à 12:14
ouais c'est sûr faut être sur qu'on a tout bien fait et qu'il y ai pas un truc bizarre
Pierro — Hier à 12:19
Ye
Prcq y a plein de ptit truc en plus a faire
Raisahmed — Hier à 12:19
comme quoi ?
Pierro — Hier à 12:20
Le readme et apres pour le fichiers à joindre et le git je crois que c'est bon
Raisahmed — Hier à 12:20
ah donc faut juste faire le readme ?
Pierro — Hier à 12:20
Je crois
Check le reste
Raisahmed — Hier à 12:27
bah je viens de tout lire il me semble que c'est bon il faut juste que moi je rajoute des commentaires sur mes parties de codes pour expliquer tout ça et faire le readme sinon c'est bon
Pierro — Hier à 12:27
Ok parfait !
Pierro — Hier à 16:24
okay bg tu me diras quand t'auras ajouter ta parti comme ça je relirai tout (ça presse pas tkt)
faut juste qu'on fini demain pour avoir un jour de rab au cas ou
Raisahmed — Hier à 16:26
Ok bah je fini le taff à 17h le temps que je rentre chez moi et que je me mette bien il sera surement 19h donc ce soir j'essaye de faire tout ça si je suis pas trop k.o mais si je suis k.o je te préviendrais avant mais t'as raison c'est mieux de faire ça ce soir pour laissé un jour en plus on sait jamais
c'est pour quand max le dépôt ?
c'est samedi le max ?
Pierro — Hier à 16:41
ahhh ouais tu taff
le rendu c'est le samedi 31
dc on fini ce soir / demain et on vise de rendre demain soir comme ca si besoin on a samedi en rab
Raisahmed — Hier à 16:42
ok ok ça marche je vais essayer ce soir de finir t'façon normalement ça va pas être long le readme et les commentaires donc vas y on fait comme ça 
Pierro — Hier à 16:43
ouais c'est rapide de fou
Raisahmed — Hier à 20:45
Je viens de me poser devant le pc je sais pas si j'aurais le temps de finir ce soir parce que je dois me coucher tôt du coup mais je vais essayer d'avancer du mieux que je peux
Raisahmed — Hier à 22:54
 
#imports généraux
import dash
from dash import Dash, dcc, html, Input, Output
import numpy as np
import plotly.express as px
import pandas as pd
Afficher plus
main.py
17 Ko
désolé mec je te met les trucs que j'ai modifié ici parce que j'arrive pas à push
je sais pas pourquoi
j'ai modifié quelques trucs sur le main nottament des commentaires
et sur le README j'ai fini le developpeur guice 
# Python dashboard

Autheurs : Pierre ALLA - Ahmed RAIS

Classe : E3 FI groupe 3

Afficher plus
README.md
8 Ko
Pierro — Aujourd’hui à 10:38
ok parfait
je m'ccupe de rajouter tes trucs
﻿
#imports généraux
import dash
from dash import Dash, dcc, html, Input, Output
import numpy as np
import plotly.express as px
import pandas as pd
import random

#import de notre fichier map_gares.py qui nous permets de créer la map et nous retourne la liste des gares les plus fréquentées
import map_gares

#on crée notre app et on lui donne un titre
app = Dash(__name__)
app.title = "SNCF - Dashboard"

#on crée un dictionnaire qui nous permettra de renommer les colonnes de notre dataframe
nouveaux_noms = {
    'Date'                                                                                          : 'Date',
    'Service'                                                                                       : 'Service',
    'Gare de départ'                                                                                : 'Gare_de_depart',
    'Gare d\'arrivée'                                                                               : 'Gare_d_arrivee',
    'Durée moyenne du trajet'                                                                       : 'Duree_moyenne_du_trajet',
    'Nombre de circulations prévues'                                                                : 'Nombre_de_circulations_prevues',
    'Nombre de trains annulés'                                                                      : 'Nombre_de_trains_annules',
    'Commentaire annulations'                                                                       : 'Commentaire_annulations',
    'Nombre de trains en retard au départ'                                                          : 'Nombre_de_trains_en_retard_au_depart',
    'Retard moyen des trains en retard au départ'                                                   : 'Retard_moyen_des_trains_en_retard_au_depart',
    'Retard moyen de tous les trains au départ'                                                     : 'Retard_moyen_de_tous_les_trains_au_depart',
    'Commentaire retards au départ'                                                                 : 'Commentaire_retards_au_depart',
    'Nombre de trains en retard à l\'arrivée'                                                       : 'Nombre_de_trains_en_retard_à_l_arrivee',
    'Retard moyen des trains en retard à  l\'arrivée'                                               : 'Retard_moyen_des_trains_en_retard_à_l_arrivee',
    'Retard moyen de tous les trains à  l\'arrivée'                                                 : 'Retard_moyen_de_tous_les_trains_à_l_arrivee',
    'Commentaire retards à  l\'arrivée'                                                             : 'Commentaire_retards_à_l_arrivee',
    'Nombre trains en retard > 15min'                                                               : 'Nombre_trains_en_retard',
    'Retard moyen trains en retard > 15 (si liaison concurrencée par vol)'                          : 'Retard_moyen_trains_en_retard_>_15_si_liaison_concurrencee_par_vol',
    'Nombre trains en retard > 30min'                                                               : 'Nombre_trains_en_retard_>_30min',
    'Nombre trains en retard > 60min'                                                               : 'Nombre_trains_en_retard_>_60min',
    'Prct retard pour causes externes'                                                              : 'Prct_retard_pour_causes_externes',
    'Prct retard pour cause infrastructure'                                                         : 'Prct_retard_pour_cause_infrastructure',
    'Prct retard pour cause gestion trafic'                                                         : 'Prct_retard_pour_cause_gestion_trafic',
    'Prct retard pour cause matériel roulant'                                                       : 'Prct_retard_pour_cause_materiel_roulant',
    'Prct retard pour cause gestion en gare et réutilisation de matériel'                           : 'Prct_retard_pour_cause_gestion_en_gare_et_reutilisation_de_materiel',
    'Prct retard pour cause prise en compte voyageurs (affluence, gestions PSH, correspondances)'   : 'Prct_retard_pour_cause_prise_en_compte_voyageurs_affluence,_gestions_PSH,_correspondances'
}

# Le code ci-dessus crée un dictionnaire appelé colors. Le dictionnaire a trois clés : 
# background, texte, et axe. Chaque clé a une valeur qui est une chaîne de caractères.
colors = {
    'background': '#C4F5FC',
    'text': '#000000',
    'axis' : '#000000'
}

# on lit notre fichier csv et on renome les colonnes grâce à notre dictionnaire
data = pd.read_csv('data.csv', sep=';', header=0)
data.rename(columns=nouveaux_noms, inplace=True)

########### MAP + DATA PREMIER GRAPH GRAPH ###########
# on génere la map et on récupère la liste des gare les plus fréquentées
index_gares = map_gares.create_map()

########### PREMIER GRAPH ###########

# traitement des données concernant les gares les plus fréquentées
list_index_gares = index_gares.tolist()
for param in list_index_gares:
    gare = data.query(f'Gare_de_depart == "{param}"')
    gare_moy = gare.groupby('Gare_de_depart', as_index=False)[["Duree_moyenne_du_trajet"]].mean()
compteur = data['Gare_de_depart'].value_counts()
compteur2 = compteur.where(compteur > 100)
compteur2 = compteur2.dropna()

# création du graphique
figure = px.bar(y = compteur2, x = compteur2.index, barmode="group")    

# mise en forme du graphique
figure.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text'],
    xaxis_title='Noms des gares',
    yaxis_title='Nombre de trajets',
    title="Nombre de trajets par gare de départ pour les gares ayant plus de 100 trajets au départ",
    xaxis = dict(linecolor=colors['axis']),
    yaxis = dict(linecolor=colors['axis']),
)

# ajout de bordure noir autour du graphique
figure.update_traces(marker_line_color='black', marker_line_width=1)

# ajout d'une couleur aléatoire a chaque barre
random_colors = [random.choice(['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']) for i in range(len(data))]
figure.update_traces(marker_color=random_colors)

########### DEUXIEME GRAPH ###########

# traitement des données concernant le temps de trajet moyen par gare
data['tps_arrondi'] = data['Duree_moyenne_du_trajet'].apply(lambda x: x/60)
tps_arrondi = data['tps_arrondi'].value_counts()

# création du graphique
fig = px.histogram(data, x="tps_arrondi", labels={"tps_arrondi":"Temps de trajet (en heures)", "y" : "Nombre de trajets"})

# mise en forme du graphique
fig.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text'],
    xaxis_title='Temps en heures',
    yaxis_title='Nombre de trajets',
    title="Temps de trajet arrondi à l'heure",
    xaxis = dict(linecolor=colors['axis']),
    yaxis = dict(linecolor=colors['axis'])
)

# ajout de bordure noire au graphe
fig.update_traces(marker_line_color='black', marker_line_width=2)

######################################
########### STRUCTURE HTML ###########

app.layout = html.Div(
    style={'backgroundColor': colors['background']},
    children=[
    html.H1(
        children='Python Dashboard',
        style={
            'textAlign': 'center',
        }
    ),

    html.Div(children='Traitement d\'un data set sur les trains', 
    style={
        'textAlign': 'center',
        'color': colors['text'],
        'backgroundColor': colors['background'],
        'margin-bottom': '35px'
    }),

    ########### PRESENTATION DATASET ###########

    html.Hr(),

    html.Div(
        children=[
            "Ce dashboard est réalisé à partir de deux data set de la SNCF sur les trains en France de janvier 2018 à fin 2022. (date de téléchargement du dataset)",
            html.Br(),
            html.Br(),
            " Le fichier CSV contient des informations sur la régularité des trains TGV sur une période donnée,"
            " chaque ligne représentant les données de régularité pour un mois donné.",
            html.Br(),
            "Le fichier GeoJSON en question contient une liste de gares en France, avec des informations sur leur"
            " nom, leur localisation géographique (latitude et longitude), leur code de gare, leur type de gare"
            " (par exemple, TGV, TER, RER, etc.) ainsi que d'autres détails. Chaque gare est représentée sous la forme d'un"
            " objet JSON avec ces différentes propriétés.",
            html.Br(),
            html.Br(),
            " Ce data set contient les informations suivantes :",
            html.Br(),
            "Gare de départ - Gare d'arrivée - Durée moyenne du trajet - Nombre de trains au départ - Nombre de trains à l'arrivée"
            " - Nombre de trains annulés - Nombre",
            html.Br(),
            html.Br(),
            "Il contient d'autres colonnes avec des pourcentages en fonction de certaines données, comme par exemple la régularité des trains,"
            " ce qui désigne" 
            " le pourcentage de trains qui arrivent à l'heure à leur destination finale. Cette donnée est calculée en comparant le nombre"
            " de trains arrivés à l'heure à leur destination finale au nombre total de trains prévus pour cette ligne.",
            html.Br(),
            html.Br(),
            html.Br(),
            html.B(
            "Il est important de comprendre que dans le dataset les données sont présentées par liaisons. Une liaison est un trajet entre deux"
            " gares. Par exemple, la liaison Paris Gare de Lyon - Lyon Part-Dieu est un trajet entre la gare de Paris Gare de Lyon et la gare de Lyon Part-Dieu."
            " Ainsi, le dataset contient des informations sur les trajets entre toutes les gares de France, Mais aussi certaines gare étrangères"
            " comme Madrid par exemple."
            ),
            html.Br(),
            html.Br(),
            html.B(
            "Le fait que les données soit par rapport aux liaisions et non à chaque trajet est important car cela signifie que"
            " un trajet entre Paris Gare de Lyon et Marseille Saint-Charles est compté une seule fois par mois, alors que si on"
            " comptait les trajets individuels, il y aurait beaucoup plus de trajets redondants."
            )
        ],
        style={
            'textAlign': 'left',
            'color': colors['text'],
            'display': 'block',
            'margin-bottom': '20px'
        }
    ),

    html.Hr(),

    ########### PREMIER GRAPH ###########

    html.Div(
        children=[
            "Ce graphique représente le nombre de trajets par gare de départ pour les gares ayant plus de 100 trajets au départ.",
            html.Br(),
            "Cliquez sur une barre pour afficher les informations de la gare : Ville - Nombre de train au départ",
            html.Br(),
            "On remarque que la gare de Paris Gare de Lyon est la gare la plus importante avec plus de 1474 trajets au départ.",
            html.Br()
            ],
        style={
            'textAlign': 'left', 
            'color': colors['text'], 
            'display': 'block',
            'margin-bottom': '20px',
            'margin-top': '50px',
        }
    ),

    dcc.Graph(
        id='graph-test',
        figure=figure
    ),

    html.Div(
        style={
            'height': '80px'
            }
        ),

    ########### MAP ###########

    html.Div(
        children=[
            "Cette carte ci dessous place les gares les plus importantes sur une carte de France.",
            html.Br(),
            "Une gare est considérée comme importante si elle a plus de 100 trajets au départ. (cf graphique ci dessus)",
            html.Br(),
            "Cliquez sur une gare pour afficher ses inoformations : Ville - libellé de la gare",
            html.Br()
            ],
        style={
            'textAlign': 'center', 
            'color': colors['text'], 
            'display': 'block',
            'margin-bottom': '20px'
        }
    ),

    html.Div(
        children=[
        html.Iframe(
                id='map',
                srcDoc=open('gare.html', 'r').read(),
                width='50%',
                height='600'
            )
        ],
        className='row',
        style={
            'display': 'flex', 
            'justify-content': 'center', 
            'color': colors['text'],
            'backgroundColor': colors['background'],
            'margin-bottom': '30px'
        }
    ),

    ########### DEUXIEME GRAPH ###########

    dcc.Graph(
        id='example-graph',
        figure=fig
    ),

    html.Div(
        children=[
            "Le graphe ci dessus repésente le temps de trajet arrondi à l'heure pour l'ensemble des trajets présent dans le dataset : \"data.csv\"",
            html.Br(),
            "On peut voir que la majorité des trajets durent entre 1h et 4h et même plus précisément entre 1h et 2h.",
            ],
        style={
            'textAlign': 'center', 
            'color': colors['text'], 
            'display': 'block',
            'backgroundColor': colors['background'],
            'margin-bottom': '20px'
            }
    ),

    ########### TROISIEME GRAPH ###########

    html.Div(
        children=[
            "Le graphe ci dessous représente le pourcentage de trains en retard par nombre de trains pour chaque gare",
            html.Br(),
            "On peut voir que certaines gares ont plus de retard que d'autres, le calcul du pourcentage de retard se fait en fonction du nombre de trains",
            html.Br(),
            "Donc par exemple si une gare n'a que 3 trains qui partent, et que les 3 trains partent en retard alors son pourcentage de trains en retard sera de 100%",
            ],
        style={
            'textAlign': 'center', 
            'color': colors['text'], 
            'display': 'block',
            'backgroundColor': colors['background'],
            'margin-top': '60px'
            }
    ),

    dcc.Graph(
        id='example-graph3'
    ),
    html.P("Réglage du pourcentage maximum de retards :"),
    dcc.Slider(
        id="mean", 
        min=0, 
        max=100, 
        value=100, 
        marks={0: '0', 100: '100'},
        tooltip={"placement": "bottom", "always_visible": True}
    ),


########### BAS DE PAGE ###########

    html.Footer(
    children=[
        html.Div(
            children=[
                "Projet réalisé par : Pierre ALLA et Ahmed Rais - Date : 2021 - Matière : Python"
                ],
                style={
                    'textAlign': 'center',
                    'color': colors['text'],
                    'backgroundColor': colors['background'],
                    'margin-top': '20px',
                    'margin-bottom': '5px'
                }
            )
        ]
    )
])

#######################################
########### TROISIEME GRAPH TRAITEMENT ###########

@app.callback(
    Output("example-graph3", "figure"), 
    Input("mean", "value"))

def display_color(mean):
    # traitement des données selon le nombre de trains en retard par rapport au retard moyen des trains et calcul de la moyenne
    circulation = data.groupby("Gare_de_depart", as_index=False)[["Nombre_de_trains_en_retard_au_depart", "Retard_moyen_des_trains_en_retard_au_depart"]].sum()
    circulation["moyenne"] = circulation.apply(lambda x: (x.Retard_moyen_des_trains_en_retard_au_depart / x.Nombre_de_trains_en_retard_au_depart)*100, axis = 1)
    circulation = circulation[ circulation["moyenne"] < mean ]

    # on créer l'histogramme
    fig3 = px.histogram(circulation, x="moyenne", y = "Gare_de_depart", color="Gare_de_depart", range_x=[0,mean])
    
    # mise en forme du graphique
    fig3.update_layout(
        plot_bgcolor=colors['background'],
        paper_bgcolor=colors['background'],
        font_color=colors['text'],
        xaxis_title='Pourcentage de trains en retard',
        yaxis_title='Gares',
        title="Pourcentage de trains en retard par nombre de trains",
        xaxis = dict(linecolor=colors['axis']),
        yaxis = dict(linecolor=colors['axis'])
    )
    
    return fig3 

if __name__ == '__main__':
    #En passant le paramètre à True ou false cela permet entre autre d'afficher ou non le boutton bleu du mode
    # de debug de Dash
    # app.run_server(debug=True)
    app.run_server(debug=False)
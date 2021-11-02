# -*- coding: utf-8 -*-
# %% [markdown]
# # Analyse de Tweets

# %%
import pandas as pd

# %% [markdown]
# ## Chargement de la base de données
#
# Nous avons récupéré la liste de tous les tweets de Donald Trump via une base de données, nous allons al charger.
#
# **Q1**: charger et exporer les données de cette base de données
# - pouvez-vous deviner le nom de la fonction permettant de charger les fichiers au format JSON ?
#   (pensez à la façon dont on charge un CSV)
# - chargez le fichier de données et affichez-en les premières lignes
# - (optionnel) quel est l'index ? pouvons-nous choisir une meilleure colonne pour indexer ces données ?
# - quelle est la colonne qui contient le texte des tweets ? extrayez-la
#
# ### Analyse (optionnel)
# - quels sont les tweets les plus populaires ? 
# - quels sont les tweets les moins populaires ? 
# - quels sont les tweets les plus re-tweetés ? 
# - quels sont les tweets les moins re-tweetés ? 
#
# ### Analyse avancée (optionnel)
# - tracez le graphe du nombre de tweets par **jour** ?
# - quels jours DT a-t-il le plus tweeté ? 
# - combien a-t-il envoyé de tweets ce jour-là ?
# - quelle proportions des tweets envoyées contenaient une mention ?
# - etc. (à voir en cours)

# %% [markdown]
# ## Nettoyage des données
#
# Le contenu des tweets retrouvés au format précédent n'est pas très facile à utiliser, car il contient beaucoup d'éléments parasites tels que des emojis, de la ponctuation, des "mentions".
# Nous allons donc "nettoyer" notre base de données afin d'en faciliter la manipulation.
#
# NOTE: _même si pandas (et numpy d'ailleurs) est très efficace pour manipuler des données numériques, il n'en va pas de même si ces données sont des chaines de caractères. Ainsi nous allons passer du "monde Numpy/Pandas" au "monde Python" pour la suite de ce TP._
#
# **Q2**: nettoyez les données des tweets
# - créer une fonction `clean_text` qui recevra le contenu original du tweet et produira une version nettoyée.
# - on va stocker ces données "nettoyées", quel est le bon type de données pour cela ?
# - on voudra aussi garder les caractères de fin de phrase (`!`, `.` etc.) comme des *mots* à part

# %% [markdown]
# ## Statistiques par mot
#
# **Q3**: Nous cherchons à compter le nombre d'utilisation de chaque mot 
#
# - quelle est la bonne structure de données permettant d'associer un résultat à chaque **mot** ?
# - remplir cette structure avec le nombre d'occurrence que chaque mot
#
# ### Analyse (optionnel)
# - quels sont les mots les plus utilisés ? 
# - quels sont les mots les moins utilisés ?
# - tracez l'histogramme des mots des plus utilsés aux moins utilisés ?

# %% [markdown]
# ## Table des successeurs
# **Q4**: Nous cherchons à compter comment les mots s'enchainent, en faisant un compte des **successeurs** de chaque mot.
#
#         Par exemple:
#          - si DT utiliser souvent dans ses phrases "hello sir" (NB: il ne le fait pas)
#          - alors nous pourrons avoir le nombre de fois où ces deux mots se suivent en faisant:
#
#             ```
#             occurrences["hello"]["sir"]
#             # >> 512
#             ```
#
# - quelle est la bonne structure de données permettant d'associer un résultat à chaque **mot** ?
# - calculer le nombre de fois que deux mots se suivent

# %%
# Génération de texte "trumpien"
#
# **Q5**: on peut maintenant créer un algorithme qui créer une phrase à-la-trump aléatoirement
# - on part du mot "the"
# - puis on suit le graphe des mots avec la poids qu'on a chargé
# - trouvez une fonction qui permet de choisir aléatoirement un mot en prenant en compte des poids (avec et/ou sans numpy)

# %%
# Améliorations
#
# **Q6**: améliorons les résultats
# - plutôt que de partir d'un mot au hasard, extrayez une liste des mots de "début de phrase" et choisissez parmis ces mots
# - (dur) comment améliorer ce résultat ? ➡️ proposez des solutions et débattez-les en cours

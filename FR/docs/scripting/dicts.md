# Dictionnaires
Les dictionnaires sont une structure de données qui te permet de mapper des clés à des valeurs de la même manière qu'un vrai dictionnaire mappe des mots à leurs définitions et tu peux les rechercher très rapidement.

Un dictionnaire peut être créé comme ceci :
`right_of = {North:East, East:South, South:West, West:North}`

L'expression avant les deux-points est la clé et l'expression après les deux-points est la valeur à laquelle la clé est mappée.
Le dictionnaire ci-dessus mappe chaque direction à la direction à sa droite.

En voici un autre qui mappe la position du drone à l'entité qui se trouve dessus.
`x, y = get_pos_x(), get_pos_y()
entity_dict = {(x,y):get_entity_type()}`

Accéder à la valeur mappée à une clé est similaire à l'accès à un élément dans une liste :
`value = dict[key]`

Exemple :
`orientation = right_of[South]`
Ceci définit `orientation` sur `West`.

Tu peux ajouter une nouvelle paire clé-valeur à un dictionnaire comme ceci :
`dict[key] = value`

Exemple :
`entity_dict[(get_pos_x(), get_pos_y())] = get_entity_type()`
Ceci met à jour l'entité stockée pour la position actuelle.

Les clés sont uniques, donc l'ajout d'une clé qui existe déjà dans le dictionnaire écrasera la valeur précédente.

Utilise `dict.pop(key)` pour supprimer une paire clé-valeur de `dict`.

`key in dict` s'évalue à `True` si `key` est une clé dans le `dict` et `False` sinon.
Tu peux donc utiliser `if key in dict:` pour vérifier si `dict` contient la clé.

Mettre un dictionnaire dans une boucle for te permet d'itérer à travers toutes les clés :
`for key in dict:
	value = dict[key]`

Il n'y a aucune garantie sur l'ordre dans lequel les clés sont itérées.

Voir aussi [Sets](docs/scripting/sets.md)
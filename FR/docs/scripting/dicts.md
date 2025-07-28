# Dictionnaires
Les dictionnaires sont une structure de données qui vous permet de mapper des clés à des valeurs de la même manière qu'un vrai dictionnaire mappe des mots à leurs définitions et vous pouvez les rechercher très rapidement.

Un dictionnaire peut être créé comme ceci :
`right_of = {North:East, East:South, South:West, West:North}`

L'expression avant les deux-points est la clé et l'expression après les deux-points est la valeur à laquelle la clé est mappée.
Le dictionnaire ci-dessus mappe chaque direction à la direction à sa droite.

Voici un autre qui mappe la position du drone à l'entité qu'il survole.
`x, y = get_pos_x(), get_pos_y()
entity_dict = {(x,y):get_entity_type()}`

L'accès à la valeur mappée à une clé est similaire à l'accès à un élément dans une liste :
`value = dict[key]`

Exemple :
`orientation = right_of[South]`
Cela définit `orientation` sur `West`.

Vous pouvez ajouter une nouvelle paire clé-valeur à un dictionnaire comme ceci :
`dict[key] = value`

Exemple :
`entity_dict[(get_pos_x(), get_pos_y())] = get_entity_type()`
Cela met à jour l'entité stockée pour la position actuelle.

Les clés sont uniques, donc l'ajout d'une clé qui existe déjà dans le dictionnaire écrasera la valeur précédente.

Utilisez `dict.pop(key)` pour supprimer une paire clé-valeur de `dict`.

`key in dict` s'évalue à `True` si `key` est une clé dans `dict` et `False` sinon.
Vous pouvez donc utiliser `if key in dict:` pour vérifier si `dict` contient la clé.

Mettre un dictionnaire dans une boucle for vous permet d'itérer à travers toutes les clés :
`for key in dict:
	value = dict[key]`

Il n'y a aucune garantie sur l'ordre dans lequel les clés sont itérées.

Voir aussi [Ensembles](docs/scripting/sets.md)
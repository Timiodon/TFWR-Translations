# Dictionnaires
Les dictionnaires sont une structure de données qui te permet d'associer des clés à des valeurs, un peu comme un vrai dictionnaire qui associe des mots à leurs définitions, et tu peux les consulter très rapidement.

Un dictionnaire peut être créé comme ceci :
`rotation = {North:East, East:South, South:West, West:North}`

L'expression avant le deux-points est la clé et l'expression après le deux-points est la valeur à laquelle la clé est associée. Le dictionnaire ci-dessus associe chaque direction à la direction située à sa droite.

En voici un autre qui associe la position du drone à l'entité qu'il survole.
`x, y = get_pos_x(), get_pos_y()
entity_dict = {(x,y):get_entity_type()}`

Accéder à la valeur associée à une clé est similaire à accéder à un élément dans une liste :
`value = dict[key]`

Exemple :
`orientation = rotation[South]`
Cela définit `orientation` à `West`.

Pour ajouter une nouvelle paire clé-valeur à un dictionnaire, fais comme ceci :
`dict[key] = value`

Exemple :
`entity_dict[(get_pos_x(), get_pos_y())] = get_entity_type()`
Cela met à jour l'entité enregistrée pour la position actuelle.

Les clés sont uniques, donc ajouter une clé qui existe déjà dans le dictionnaire remplacera la valeur précédente.

Utilise `dict.pop(key)` pour enlever une paire clé-valeur de `dict`.

`key in dict` vaut `True` si `key` est une clé dans le `dict` et `False` autrement. Donc, tu peux utiliser `if key in dict:` pour vérifier si `dict` contient la clé.

Mettre un dictionnaire dans une boucle for te permet d'itérer à travers toutes les clés :
`for key in dict:
	value = dict[key]`

Il n'y a aucune garantie sur l'ordre dans lequel les clés sont itérées.

Voir aussi [Sets](docs/scripting/sets.md)
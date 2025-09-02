# Sets
Les sets sont comme les [dictionnaires](docs/scripting/dicts.md), mais sans valeurs. Ce sont juste un ensemble non ordonné de clés.

Ils sont créés comme des dictionnaires, mais sans valeurs.
`set = {North, East, West}`

Utilise `set()` pour créer un set vide. Note que `{}` crée un dictionnaire vide.

Utilise `set.add(elem)` pour ajouter un nouvel élément au set.

Utilise `set.remove(elem)` pour supprimer un élément d'un set.

Utilise `if elem in set:` pour vérifier si le set contient un élément.

Utilise `for elem in set:` pour itérer sur tous les éléments du set.
Pour les grands sets, l'opérateur `in` est beaucoup plus rapide que sur une liste.

Tout comme les dictionnaires, les sets sont non ordonnés, il n'y a donc aucune garantie sur l'ordre dans lequel les éléments sont itérés.

De plus, les éléments dans les sets sont uniques, donc ajouter un élément qui est déjà dans le set ne changera pas le set.
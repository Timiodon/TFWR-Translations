# Ensembles (Sets)
Les ensembles (sets) sont comme des [dictionnaires](docs/scripting/dicts.md), mais sans valeurs. Ce sont juste un ensemble de clés non ordonné.

Ils sont créés comme des dictionnaires, mais sans valeurs.
`set = {North, East, West}`

Utilisez `set()` pour créer un ensemble vide. Notez que `{}` crée un dictionnaire vide.

Utilisez `set.add(elem)` pour ajouter un nouvel élément à l'ensemble.

Utilisez `set.remove(elem)` pour supprimer un élément d'un ensemble.

Utilisez `if elem in set:` pour vérifier si l'ensemble contient un élément.

Utilisez `for elem in set:` pour itérer tous les éléments de l'ensemble.
Pour les ensembles plus grands, l'opérateur `in` est beaucoup plus rapide que sur une liste.

Tout comme les dictionnaires, les ensembles ne sont pas ordonnés, il n'y a donc aucune garantie sur l'ordre dans lequel les éléments sont itérés.

De plus, les éléments dans les ensembles sont uniques, donc ajouter un élément qui est déjà dans l'ensemble ne changera pas l'ensemble.
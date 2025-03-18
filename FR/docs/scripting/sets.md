# Sets
Les sets sont comme les [dictionaries](docs/scripting/dicts.md), mais sans valeurs. Ce sont simplement un ensemble non ordonné de clés.

Ils sont créés comme des dictionaries, mais sans valeurs.
`set = {North, East, West}`

Utilisez `set()` pour créer un set vide. Notez que `{}` crée un dictionary vide.

Utilisez `set.add(elem)` pour ajouter un nouvel élément au set.

Utilisez `set.remove(elem)` pour supprimer un élément d'un set.

Utilisez `if elem in set:` pour vérifier si un élément est dans le set.

Utilisez `for elem in set:` pour itérer tous les éléments du set.
Pour les sets plus grands, l'opérateur `in` est beaucoup plus rapide que sur une liste.

Tout comme les dictionaries, les sets sont non ordonnés, donc l'ordre dans lequel les éléments sont itérés n'est pas garanti.

De plus, les éléments dans un set sont uniques, donc ajouter un élément qui est déjà dans le set ne le changera pas.
# Listes
Les listes sont un moyen facile de stocker plusieurs valeurs dans une seule variable.
Tu peux créer de nouvelles listes comme ceci :

`some_list = [2, True, Items.Hay]`

La liste contient maintenant les valeurs `2`, `True` et `Items.Hay`.
Une liste peut aussi être vide :

`empty_list = []`

Tu peux accéder à un élément d'une liste par son index. L'index est `0` pour le premier élément, `1` pour le deuxième, `2` pour le troisième...

plante des carottes
`entities = [Entities.Tree, Entities.Carrot, Entities.Pumpkin]
plant(entities[1])`

Tu peux itérer sur une liste en utilisant une boucle for. L'exemple suivant additionne tous les éléments de la liste.

`numbers = [4, 7, 2, 5]
sum = 0
for number in numbers:
	sum += number`
`sum` est maintenant `18`

Les méthodes de liste suivantes te permettent d'ajouter et de supprimer des éléments :

`elements.append(elem)` ajoute un élément à la fin de la liste :

`numbers = [2, 6, 12]
numbers.append(7)`
`numbers` est maintenant `[2, 6, 12, 7]`

`elements.remove(elem)` supprime la première occurrence d'un élément d'une liste :

`numbers = [1, 2, 4, 2]
numbers.remove(2)`
`numbers` est maintenant `[1, 4, 2]`

`elements.insert(index, elem)` insère un élément à l'index donné :

`some_list = [Entities.Tree, Items.Hay]
some_list.insert(1, Items.Wood)`
`some_list` est maintenant `[Entities.Tree, Items.Wood, Items.Hay]`

`elements.pop(index)` supprime l'élément à l'index spécifié.
Si aucun index n'est spécifié, le dernier élément est supprimé.

`numbers = [3, 5, 8, 25]
numbers.pop()`
`numbers` est maintenant `[3, 5, 8]`
`numbers.pop(1)`
`numbers` est maintenant `[3, 8]`

La fonction `len()` renvoie la longueur de la liste.
`numbers = [3, 2, 1]
x = len(numbers)`
`x` est maintenant `3`

Les listes ont une sémantique de référence. Cela signifie qu'assigner une liste à une variable assigne le même objet liste à cette variable, plutôt que de faire une copie de la liste.
Si deux variables font référence à la même liste, les modifications apportées à la liste seront vues par les deux.

`a = [1, 2]
b = a
b.pop()`
`a` et `b` sont maintenant tous les deux `[1]`

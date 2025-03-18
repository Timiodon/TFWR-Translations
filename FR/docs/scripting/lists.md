# Listes
Les listes sont un moyen simple de stocker plusieurs valeurs dans une seule variable.
Tu peux créer de nouvelles listes comme ceci :

`list = [2, True, Items.Hay]`

La liste contient maintenant les valeurs `2`, `True` et `Items.Hay`.
Une liste peut aussi être vide :

`empty_list = []`

Tu peux accéder à un élément d'une liste par son index. L'index est `0` pour le premier élément, `1` pour le deuxième élément, `2` pour le troisième...

plants carrots
`list = [Entities.Tree, Entities.Carrot, Entities.Pumpkin]
plant(list[1])`

Tu peux parcourir une liste avec une boucle for. L'exemple suivant fait la somme de tous les éléments de la liste.

`list = [4, 7, 2, 5]
sum = 0
for number in list:
	sum += number`
`sum` est maintenant `18`

Les méthodes de liste suivantes te permettent d'ajouter et de supprimer des éléments :

`list.append(elem)` ajoute un élément à la fin de la liste :

`list = [2, 6, 12]
list.append(7)`
`list` est maintenant `[2, 6, 12, 7]`

`list.remove(elem)` supprime la première occurrence d'un élément d'une liste :

`list = [1, 2, 4, 2]
list.remove(2)`
`list` est maintenant `[1, 4, 2]`

`list.insert(index, elem)` insère un élément à l'index donné :

`list = [Entities.Tree, Items.Hay]
list.insert(1, Items.Wood)`
`list` est maintenant `[Entities.Tree, Items.Wood, Items.Hay]`

`list.pop(index)` supprime l'élément à l'index spécifié.
Si aucun index n'est spécifié, le dernier élément est supprimé.

`list = [3, 5, 8, 25]
list.pop()`
`list` est maintenant `[3, 5, 8]`
`list.pop(1)`
`list` est maintenant `[3, 8]`

La fonction `len()` renvoie la longueur de la liste.
`list = [3, 2, 1]
x = len(list)`
`x` est maintenant `3`

Les listes ont des sémantiques de référence. Cela signifie qu'assigner une liste à une variable assigne le même objet liste à cette variable, plutôt que de faire une copie de la liste.
Si deux variables réfèrent à la même liste, les modifications de la liste seront visibles par les deux.

`a = [1, 2]
b = a
b.pop()`
`a` et `b` sont maintenant tous les deux `[1]`
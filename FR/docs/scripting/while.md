# Boucle While
Tu as débloqué la boucle `while` et les valeurs `True` et `False`. La boucle `while` continue d'exécuter le corps de la boucle tant que la condition est `True`.

`while condition:
	#corps de la boucle`

Ne t'inquiète pas de créer des boucles infinies. Les délais dans l'exécution empêcheront le programme de se figer.

## Pour les Débutants
Peut-être que tu as déjà essayé de mettre plusieurs appels `harvest()` à la suite :

`harvest()
harvest()
harvest()`

Cela te permet de récolter plusieurs fois en une seule exécution du programme. 
Cependant, ce serait bien de récolter plus de trois fois, et écrire le même code plusieurs fois est une mauvaise pratique. 
La solution est une boucle. 
Une boucle te permet d'exécuter le même code plusieurs fois.

La boucle while prend une condition, qui est une valeur logique pouvant être dans l'un des deux états : `True` ou `False`. 
Une telle valeur est appelée une valeur booléenne.

La boucle exécute ensuite le code à l'intérieur de la boucle jusqu'à ce que la condition soit False.
La boucle while ressemble à ceci :

`while condition:
	#corps de la boucle
	#corps de la boucle
	#...`
	
Où tu dois remplacer "condition" par une valeur booléenne et `#corps de la boucle` par ce que tu veux faire dans la boucle.

Il y a deux valeurs booléennes constantes disponibles. Les constantes sont des valeurs qui ne changent jamais pendant le programme.

Pour créer une valeur booléenne constante qui est toujours `True`, tu peux simplement écrire `True`. Écris `False` comme une valeur booléenne constante qui sera toujours `False`.
Donc tu pourrais écrire soit

`while False:
	do_a_flip()`

ou

`while True:
	do_a_flip()`

La première ne fera jamais un flip et la seconde fera des flips à l'infini (une boucle infinie).

Normalement, créer une boucle infinie est une mauvaise idée car cela figera le programme, mais dans ce jeu, il y a des délais entre chaque itération de la boucle, donc cela fera faire un flip au drone jusqu'à ce que tu l'arrêtes manuellement en appuyant à nouveau sur le bouton d'exécution.

Remarque comment la ligne après les deux points est indentée. L'indentation comme celle-ci est utilisée pour séparer les blocs de code.
Appuie simplement sur Tab pour ajouter de l'indentation et sur Shift + Tab (ou Backspace) pour l'enlever.

La boucle répétera toutes les instructions indentées après les deux points.
Les instructions après le bloc indenté seront exécutées une fois que la boucle sera terminée.
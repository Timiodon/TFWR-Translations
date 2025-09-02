# Boucle While
Tu as débloqué la boucle `while` et les valeurs `True` et `False`. La boucle `while` continue d'exécuter le corps de la boucle tant que la condition est `True`.

`while condition:
	#corps de la boucle`

Ne t'inquiète pas de créer des boucles infinies. Les délais dans l'exécution empêcheront le programme de se figer.

## Pour les Débutants
Peut-être as-tu déjà essayé de mettre plusieurs appels `harvest()` à la suite :

`harvest()
harvest()
harvest()`

Cela te permet de récolter plusieurs fois en une seule exécution du programme.
Cependant, ce serait bien de récolter plus de trois fois, et écrire le même code plusieurs fois est une mauvaise pratique.
La solution est une boucle.
Une boucle te permet d'exécuter le même code plusieurs fois.

La boucle while prend une condition, qui est une valeur logique qui ne peut être que dans l'un des deux états : `True` ou `False`.
Une telle valeur est appelée une valeur booléenne.

La boucle exécute ensuite le code à l'intérieur de la boucle jusqu'à ce que la condition soit `False`.
La boucle while ressemble à ceci :

`while condition:
	#corps de la boucle
	#corps de la boucle
	#...`
	
Où tu dois remplacer "condition" par une valeur booléenne et `#corps de la boucle` par ce que tu veux faire dans la boucle.

Il y a deux valeurs booléennes constantes disponibles. Les constantes sont des valeurs qui ne changent jamais pendant le programme.

Pour créer une valeur booléenne constante qui est toujours `True`, tu peux simplement écrire `True`. Écris `False` pour une valeur booléenne constante qui sera toujours `False`.
Donc tu pourrais soit écrire


`while False:
	do_a_flip()`

ou

`while True:
	do_a_flip()`

Le premier ne fera jamais de looping et le second en fera pour toujours (une boucle infinie).

Normalement, créer une boucle infinie est une mauvaise idée car cela figera le programme, mais dans ce jeu, il y a des délais entre chaque itération de la boucle, donc cela fera que le drone continuera à faire des loopings jusqu'à ce que tu l'arrêtes manuellement en appuyant à nouveau sur le bouton d'exécution.

Remarque comment la ligne après les deux-points est indentée. Une indentation comme celle-ci est utilisée pour séparer les blocs de code.
Appuie simplement sur Tab pour ajouter une indentation et sur Maj + Tab (ou Retour arrière) pour la supprimer.

La boucle répétera toutes les instructions indentées après les deux-points.
Les instructions après le bloc indenté seront exécutées une fois la boucle terminée.
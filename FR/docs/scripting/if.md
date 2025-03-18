# If
Tu peux utiliser if, elif et else pour exécuter du code de manière conditionnelle.

`if condition1:
	do_a_flip()
elif condition2:
	harvest()
else:
	do_a_flip()
	harvest()`

## Syntaxe
Les `if` te permettent d'exécuter du code uniquement si une condition est `True`. C'est comme une boucle `while` qui ne boucle pas.
Le `if` prend une condition, tout comme la boucle `while`, et exécute le bloc de code if si la condition est évaluée à `True` :

`#faire un flip si la condition est True
if condition:
	do_a_flip()`

Tu peux aussi ajouter un `else` après le if qui définit le code à exécuter si la condition est évaluée à `False`.

Faire un flip si `condition` est True, sinon récolter.
`if condition:
	do_a_flip()
else:
	harvest()`

`elif` est l'abréviation de else if.

`if condition1:
	#a
else:
	if condition2:
		#b
	else:
		#c`

peut être raccourci en :

`if condition1:
	#a
elif condition2:
	#b
else:
	#c`
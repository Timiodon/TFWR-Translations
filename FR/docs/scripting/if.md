# If
Vous pouvez utiliser if, elif et else pour exécuter du code de manière conditionnelle.

`if condition1:
	do_a_flip()
elif condition2:
	harvest()
else:
	do_a_flip()
	harvest()`

## Syntaxe
Les `if` vous permettent d'exécuter du code seulement si une condition est `True`. Ils sont comme une boucle `while` qui ne boucle pas.
Le `if` prend une condition tout comme la boucle `while` et exécute le bloc de code du if si la condition s'évalue à `True` :

`#fait un flip si la condition est True
if condition:
	do_a_flip()`

Vous pouvez également ajouter un `else` après le if qui définit le code à exécuter si la condition s'évalue à `False`.

Fait un flip si la `condition` est True, sinon récolte.
`if condition:
	do_a_flip()
else:
	harvest()`

`elif` est un raccourci pour else if.

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
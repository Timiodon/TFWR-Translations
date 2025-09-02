# Break
`break` permet d'arrêter une boucle prématurément. Lorsque l'instruction `break` est atteinte, elle sortira immédiatement de la boucle la plus interne et commencera à exécuter le code après la boucle.

`for i in range(10):
	break
print(i)`
Cela affiche `0` car `i` est `0` à la première itération de la boucle, puis l'instruction break met fin à la boucle.

Cela fonctionne aussi avec les boucles `while`.

`while True:
	if can_harvest():
		break`

Ce code exécute la boucle `while` jusqu'à ce que `can_harvest()` soit `True`.
Il a le même effet que

`while not can_harvest():
	pass`

Dans les boucles imbriquées, `break` quitte toujours la boucle la plus interne.

`for i in range(10):
	for j in range(10):
		break
		print("ceci n'est jamais affiché")
	print("ceci est affiché 10 fois")`
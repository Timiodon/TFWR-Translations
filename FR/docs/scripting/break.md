# Break
`break` permet d'arrêter une boucle plus tôt. Lorsqu'on atteint l'instruction `break`, elle quitte immédiatement la boucle la plus intérieure et commence à exécuter le code après la boucle.

`for i in range(10):
	break
print(i)`
Cela affiche `0` car `i` est `0` lors de la première itération de la boucle et ensuite l'instruction break met fin à la boucle.

Ça fonctionne aussi avec les boucles `while`.

`while True:
	if can_harvest():
		break`

Ce code exécute la boucle `while` jusqu'à ce que `can_harvest()` soit `True`.
Il a le même effet que

`while not can_harvest():
	pass`

Dans les boucles imbriquées, `break` quitte toujours la boucle la plus intérieure.

`for i in range(10):
	for j in range(10):
		break
		print("this is never printed")
	print("this is printed 10 times")`
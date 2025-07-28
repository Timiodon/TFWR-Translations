# Continue
`continue` permet d'arrêter l'itération actuelle d'une boucle et de sauter à la prochaine itération de la boucle la plus interne.

`for i in range(10):
	continue
    print("ceci n'est jamais affiché")`

Cela exécute les 10 itérations de la boucle, mais l'instruction `print` après le `continue` est toujours sautée.

Cela fonctionne aussi avec les boucles `while`.

`while True:
	if not can_harvest():
		continue
    
    harvest()`

Ce code n'appelle `harvest()` que lorsque `can_harvest()` est `True`.
Il a le même effet que

`while True:
	if can_harvest():
		harvest()`

Dans les boucles imbriquées, `continue` affecte toujours la boucle la plus interne.

`for i in range(10):
	for j in range(10):
	    print("ceci est affiché 100 fois")
		continue
		print("ceci n'est jamais affiché")
	print("ceci est affiché 10 fois")`
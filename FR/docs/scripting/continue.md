# Continue
continue permet d'arrêter l'itération actuelle d'une boucle et de passer à l'itération suivante de la boucle la plus interne.

`for i in range(10):
	continue
    print("this is never printed")`

Cela exécute toutes les `10` itérations de la boucle, mais l'instruction `print` après le `continue` est toujours ignorée.

Cela fonctionne aussi sur les boucles `while`.

`while True:
	if not can_harvest():
		continue
    
    harvest()`

Ce code appelle seulement `harvest()` quand `can_harvest()` est `True`. 
Cela a le même effet que

`while True:
	if can_harvest():
		harvest()`

Dans les boucles imbriquées, `continue` affecte toujours la boucle la plus interne.

`for i in range(10):
	for j in range(10):
	    print("this is printed 100 times")
		continue
		print("this is never printed")
	print("this is printed 10 times")`
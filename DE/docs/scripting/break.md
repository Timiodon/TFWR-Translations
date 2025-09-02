# Break
`break` ermöglicht es, eine Schleife vorzeitig zu beenden. Wenn die `break`-Anweisung erreicht wird, wird die innerste Schleife sofort verlassen und der Code nach der Schleife ausgeführt.

`for i in range(10):
	break
print(i)`
Dies gibt `0` aus, weil `i` in der ersten Iteration der Schleife `0` ist und dann die `break`-Anweisung die Schleife beendet.

Es funktioniert auch bei `while`-Schleifen.

`while True:
	if can_harvest():
		break`

Dieser Code führt die `while`-Schleife aus, bis `can_harvest()` `True` ist.
Es hat den gleichen Effekt wie

`while not can_harvest():
	pass`

In verschachtelten Schleifen beendet `break` immer die innerste Schleife.

`for i in range(10):
	for j in range(10):
		break
		print("this is never printed")
	print("this is printed 10 times")`
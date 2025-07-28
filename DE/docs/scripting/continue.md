# Continue
`continue` ermöglicht es, die aktuelle Iteration einer Schleife zu beenden und zur nächsten Iteration der innersten Schleife zu springen.

`for i in range(10):
	continue
    print("this is never printed")`

Dies führt alle `10` Iterationen der Schleife aus, aber die `print`-Anweisung nach dem `continue` wird immer übersprungen.

Es funktioniert auch bei `while`-Schleifen.

`while True:
	if not can_harvest():
		continue
    
    harvest()`

Dieser Code ruft `harvest()` nur auf, wenn `can_harvest()` `True` ist. 
Er hat den gleichen Effekt wie

`while True:
	if can_harvest():
		harvest()`

In verschachtelten Schleifen wirkt sich `continue` immer auf die innerste Schleife aus.

`for i in range(10):
	for j in range(10):
	    print("this is printed 100 times")
		continue
		print("this is never printed")
	print("this is printed 10 times")`
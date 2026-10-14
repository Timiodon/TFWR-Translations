# Continue
A continue lehetővé teszi a ciklus aktuális iterációjának leállítását és a következő iterációra ugrást a legbelső ciklusban.

`for i in range(10):
	continue
    print("ez soha nem íródik ki")`

Ez a ciklus mind a 10 iterációját lefuttatja, de a `continue` utáni `print` utasítás mindig kimarad.

`while` ciklusokon is működik.

`while True:
	if not can_harvest():
		continue
    
    harvest()`

Ez a kód csak akkor hívja meg a `harvest()`-t, amikor a `can_harvest()` `True`.
Ugyanúgy működik, mint

`while True:
	if can_harvest():
		harvest()`

Beágyazott ciklusokban a `continue` mindig a legbelső ciklust érinti.

`for i in range(10):
	for j in range(10):
	    print("ez 100-szor íródik ki")
		continue
		print("ez soha nem íródik ki")
	print("ez 10-szer íródik ki")`
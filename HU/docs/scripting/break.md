# Break
A `break` lehetővé teszi a ciklus korai leállítását. Amikor a `break` utasításhoz ér, azonnal kilép a legbelső ciklusból és elkezdi futtatni a ciklus utáni kódot.

`for i in range(10):
	break
print(i)`
Ez kiírja a `0`-t, mert `i` `0` a ciklus első iterációjában, és utána a break utasítás befejezi a ciklust.

`while` ciklusokon is működik.

`while True:
	if can_harvest():
		break`

Ez a kód a `while` ciklust addig futtatja, amíg a `can_harvest()` `True` nem lesz.
Ugyanúgy működik, mint

`while not can_harvest():
	pass`

Beágyazott ciklusokban a `break` mindig a legbelső ciklusból lép ki.

`for i in range(10):
	for j in range(10):
		break
		print("ez soha nem íródik ki")
	print("ez 10-szer íródik ki")`
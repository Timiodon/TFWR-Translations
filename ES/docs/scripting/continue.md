# Continue
`continue` permite detener la iteración actual de un bucle y saltar a la siguiente iteración del bucle más interno.

`for i in range(10):
	continue
    print("this is never printed")`

Esto ejecuta las `10` iteraciones del bucle, pero la instrucción `print` después de `continue` siempre se omite.

También funciona en bucles `while`.

`while True:
	if not can_harvest():
		continue
    
    harvest()`

Este código solo llama a `harvest()` cuando `can_harvest()` es `True`. 
Tiene el mismo efecto que

`while True:
	if can_harvest():
		harvest()`

En bucles anidados, `continue` siempre afecta al bucle más interno.

`for i in range(10):
	for j in range(10):
	    print("this is printed 100 times")
		continue
		print("this is never printed")
	print("this is printed 10 times")`
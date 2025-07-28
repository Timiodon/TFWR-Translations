# Continue
`continue` permite detener la iteración actual de un bucle y saltar a la siguiente iteración del bucle más interno.

`for i in range(10):
	continue
    print("esto nunca se imprime")`

Esto ejecuta las `10` iteraciones del bucle, pero la sentencia `print` después de `continue` siempre se salta.

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
	    print("esto se imprime 100 veces")
		continue
		print("esto nunca se imprime")
	print("esto se imprime 10 veces")`
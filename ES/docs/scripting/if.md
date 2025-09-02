# If
Puedes usar `if`, `elif` y `else` para ejecutar código condicionalmente.

`if condition1:
	do_a_flip()
elif condition2:
	harvest()
else:
	do_a_flip()
	harvest()`

## Sintaxis
Los `if` te permiten ejecutar código solo si una condición es `True`. Son como un bucle `while` que no se repite.
El `if` toma una condición igual que el bucle `while` y ejecuta el bloque de código del `if` si la condición evalúa a `True`:

`#hacer un giro si la condición es True
if condition:
	do_a_flip()`

También puedes añadir un `else` después del `if` que define el código a ejecutar si la condición evalúa a `False`.

Haz un giro si la `condition` es `True`, de lo contrario, cosecha.
`if condition:
	do_a_flip()
else:
	harvest()`

`elif` es la abreviatura de `else if`.

`if condition1:
	#a
else:
	if condition2:
		#b
	else:
		#c`

se puede acortar a:

`if condition1:
	#a
elif condition2:
	#b
else:
	#c`
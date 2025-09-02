# Bucle For
El bucle `for` funciona como en Python. (Llamado bucle `foreach` en algunos lenguajes, no confundir con el bucle for de estilo C, que es algo diferente).

`for i in sequence:
	#hacer algo con i`

Similar al bucle `while`, el bucle `for` también llama repetidamente a un bloque de código. En lugar de iterar basándose en una condición, ejecuta el cuerpo del bucle una vez por cada elemento en una secuencia.

## Sintaxis
Un bucle for se ve así:

`for variable_name in sequence:
	#bloque de código`

`variable_name` puede ser cualquier nombre que elijas. Es una variable que almacena el elemento actual en la secuencia. `sequence` necesita ser algún valor que se pueda iterar, como un rango de números. El bloque de código se ejecuta para cada elemento con la variable del bucle asignada a ese elemento.

## Secuencias
[Rangos](functions/range)      <unlock=lists>[Listas](docs/scripting/lists.md)      </unlock><unlock=functions>[Tuplas](docs/scripting/tuples.md)      </unlock><unlock=dicts>[Diccionarios](docs/scripting/dicts.md)      </unlock><unlock=sets>[Conjuntos](docs/scripting/sets.md)</unlock>

## Ejemplo
`for i in range(5):
    harvest()`

Este bucle ejecuta el cuerpo un número fijo de veces. Es esencialmente lo mismo que escribir

`i = 0
harvest()
i = 1
harvest()
i = 2
harvest()
i = 3
harvest()
i = 4
harvest()`

Así que llama a `harvest()` 5 veces.

Ver también [Break](docs/scripting/break.md) y [Continue](docs/scripting/continue.md)
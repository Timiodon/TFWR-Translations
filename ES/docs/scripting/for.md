# Bucle For
El bucle `for` funciona igual que en Python. (En algunos lenguajes se llama bucle foreach, no debe confundirse con el bucle estilo C, que es algo diferente).

`for i in sequence:
	#do something with i`

Similar al bucle `while`, el bucle `for` también llama repetidamente a un bloque de código. En lugar de basarse en una condición, ejecuta el cuerpo del bucle una vez para cada elemento en una secuencia.

## Sintaxis
Un bucle for se ve así:

`for variable_name in sequence:
	#code block`

`variable_name` puede ser cualquier nombre que elijas. Es una variable que almacena el elemento actual de la secuencia. `sequence` necesita ser un valor que se pueda iterar como un rango o números. El bloque de código se ejecuta para cada elemento con la variable del bucle asignada a ese elemento.

## Secuencias
[Rangos](functions/range)      <unlock=lists>[Listas](docs/scripting/lists.md)      </unlock><unlock=functions>[Tuplas](docs/scripting/tuples.md)      </unlock><unlock=dicts>[Dictionaries](docs/scripting/dicts.md)      </unlock><unlock=sets>[Sets](docs/scripting/sets.md)</unlock>

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
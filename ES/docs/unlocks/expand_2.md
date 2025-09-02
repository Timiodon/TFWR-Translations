# Expansión 2
¡Tu granja se ha expandido de nuevo! Ahora las casillas ya no están en una bonita fila, así que necesitas encontrar una manera de recorrer una cuadrícula cuadrada.

Con el bucle `while` esto no es posible hasta que desbloquees los sentidos y los operadores.
Es hora de introducir el bucle `for`.

Puedes leer todo sobre el bucle `for` en la página [Bucle For](docs/scripting/for.md), pero por ahora solo lo necesitarás para repetir código un número fijo de veces.

`#hacer n giros
for i in range(5):
	do_a_flip()`

`range(n)` crea un rango de números de `0` a `n-1` que tiene `n` elementos. El bucle `for` ejecuta su cuerpo una vez por cada elemento en la secuencia. En este ejemplo, `do_a_flip()` se llamará `5` veces.

La función `get_world_size()` también está disponible ahora. Devuelve la longitud del lado de tu granja. De esta manera, puedes escribir código que no se romperá con la próxima mejora de expansión.

`for i in range(get_world_size()):
	harvest()
	move(North)`

Este ejemplo cosecha una columna de la granja para cualquier tamaño de granja.

Si estás atascado tratando de averiguar cómo mover el dron por la granja, consulta la pista de abajo.
<spoiler=show hint>Hay, por supuesto, varias formas de moverse por la granja.
Lo que buscamos es una forma de recorrerla de manera sistemática que no se rompa cuando la granja vuelva a crecer.
Una forma sistemática de llegar a todos los lugares de la granja sería repetir los siguientes 2 pasos para siempre:

1.Moverse hacia el `North` hasta que vuelva al principio.
2.Moverse hacia el `East`

`for i in range(get_world_size()):` puede ser útil para convertir esta idea en código.
</spoiler>
<spoiler=show possible solution> El recorrido básico podría ser así:

`for i in range(get_world_size()):
	for j in range(get_world_size()):
		#hacer un giro en cada casilla
		do_a_flip()
		move(North)
	move(East)`
</spoiler>
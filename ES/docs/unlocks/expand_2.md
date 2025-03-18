# Expandir 2
¡Tu granja se ha expandido otra vez! Ahora las baldosas ya no están en una fila ordenada, así que necesitas encontrar una manera de recorrer una cuadrícula.

Con el bucle `while` esto no es posible hasta que desbloquees sentidos y operadores.
Es hora de presentar el bucle `for`.

Puedes leer todo sobre el bucle `for` en la página [For Loop](docs/scripting/for.md), pero por ahora solo necesitarás usarlo para repetir código un número fijo de veces.

`#haz n volteretas
for i in range(5):
	do_a_flip()`

`range(n)` crea un rango de números desde `0` hasta `n-1` que tiene `n` elementos. El bucle `for` ejecuta su cuerpo del bucle una vez por cada elemento en la secuencia. En este ejemplo `do_a_flip()` se llamará `5` veces.

La función `get_world_size()` también está disponible ahora. Devuelve la longitud del lado de tu granja. De esta manera, puedes escribir código que no se romperá con la próxima actualización de expansión.

`for i in range(get_world_size()):
	harvest()
	move(North)`

Este ejemplo cosecha una columna de la granja para cualquier tamaño de granja.

Si estás atascado tratando de averiguar cómo mover el dron por la granja, mira la pista a continuación.
<spoiler=mostrar pista>Por supuesto, hay varias maneras de moverse por la granja.
Lo que buscamos es una manera de recorrerla de forma sistemática que no se rompa cuando la granja crezca de nuevo.
Una manera sistemática de llegar a todos los lugares de la granja sería repetir los siguientes 2 pasos para siempre:

1.Moverse al `North` hasta que se regrese.
2.Moverse al `East`.

`for i in range(get_world_size()):` puede ser útil para convertir esta idea en código.
</spoiler>
<spoiler=mostrar posible solución> El recorrido básico podría verse así:

`for i in range(get_world_size()):
	for j in range(get_world_size()):
		#haz una voltereta en cada baldosa
		do_a_flip()
		move(North)
	move(East)`
</spoiler>
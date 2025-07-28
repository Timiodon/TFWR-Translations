# Expandir 1
<unlock=for>Ver también [Expandir_2](docs/unlocks/expand_2.md)

</unlock>¡Tu granja ha crecido! Este espacio no es de mucha utilidad si no puedes mover el dron, así que hay una nueva función `move()` que mueve el dron. `move()` requiere que especifiques la dirección en la que quieres que se mueva el dron. Hay cuatro nuevas constantes para esto: `North, East, South, West`

Por ejemplo, `move(North)` moverá el dron una casilla hacia el norte.

Si te mueves por el borde de la granja, el dron será movido al otro lado de la granja.
El siguiente código de ejemplo seguirá moviendo el dron hacia el norte y volverá al principio cuando llegue al borde de la granja:

`while True:
	move(North)`

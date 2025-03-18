# Expandir 1
<unlock=for>Ver también [Expand_2](docs/unlocks/expand_2.md)

</unlock>¡Tu granja ha crecido! Este espacio no es de mucha utilidad si no puedes mover el drone, así que hay una nueva función `move()` que mueve el drone. `move()` requiere que especifiques la dirección en la que quieres mover el drone. Hay cuatro nuevas constantes para esto: `North, East, South, West`

Por ejemplo, `move(North)` moverá el drone una casilla hacia el norte.

Si te mueves más allá del borde de la granja, el drone será movido al otro lado de la granja. El siguiente código de ejemplo mantendrá al drone moviéndose hacia el norte y regresará al inicio cuando llegue al borde de la granja:

`while True:
	move(North)`
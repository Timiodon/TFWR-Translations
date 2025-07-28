# Expandir 1
<unlock=for>Vê também [Expandir_2](docs/unlocks/expand_2.md)

</unlock>A tua quinta cresceu! Este espaço não tem muita utilidade se não conseguires mover o drone, por isso há uma nova função `move()` que move o drone. `move()` requer que especifiques a direção na qual queres que o drone se mova. Existem quatro novas constantes para isto: `North, East, South, West`

Por exemplo, `move(North)` moverá o drone um quadrado para o norte.

Se te moveres para além da borda da quinta, o drone será movido para o outro lado da quinta.
O exemplo de código seguinte continuará a mover o drone para norte e dará a volta para o início quando atingir a borda da quinta:

`while True:
	move(North)`

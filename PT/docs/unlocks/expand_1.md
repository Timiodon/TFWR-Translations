# Expandir 1
<unlock=for>Veja também [Expand_2](docs/unlocks/expand_2.md)

</unlock>Sua fazenda cresceu! Este espaço não serve para muito se você não puder mover o drone, então há uma nova função `move()` que move o drone. `move()` requer que você especifique a direção para a qual deseja mover o drone. Existem quatro novas constantes para isso: `North, East, South, West`

Por exemplo, `move(North)` moverá o drone um quadrado para o norte.

Se você se mover além da borda da fazenda, o drone será movido para o outro lado da fazenda. O seguinte exemplo de código manterá o drone se movendo para o norte e voltará para o começo quando atingir a borda da fazenda:

`while True:
	move(North)`
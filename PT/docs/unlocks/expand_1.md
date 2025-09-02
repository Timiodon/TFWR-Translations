# Expansão 1
<unlock=for>Veja também [Expansão_2](docs/unlocks/expand_2.md)

</unlock>Sua fazenda cresceu! Este espaço não tem muita utilidade se você não pode mover o drone, então há uma nova função `move()` que move o drone. `move()` exige que você especifique a direção na qual deseja que o drone se mova. Existem quatro novas constantes para isso: `North, East, South, West`

Por exemplo, `move(North)` moverá o drone um quadrado para o norte.

Se você passar da borda da fazenda, o drone será movido para o outro lado da fazenda.
O exemplo de código a seguir continuará movendo o drone para o norte e voltará ao início quando atingir a borda da fazenda:

`while True:
	move(North)`

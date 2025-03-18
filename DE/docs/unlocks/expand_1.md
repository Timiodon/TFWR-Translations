# Expand 1
<unlock=for>Siehe auch [Expand_2](docs/unlocks/expand_2.md)

</unlock>Dein Bauernhof hat sich vergrößert! Dieser Raum nützt wenig, wenn du die Drohne nicht bewegen kannst, deshalb gibt es eine neue Funktion `move()`, die die Drohne bewegt. `move()` erfordert, dass du die Richtung angibst, in die du die Drohne bewegen möchtest. Es gibt vier neue Konstanten dafür: `North, East, South, West`

Zum Beispiel bewegt `move(North)` die Drohne ein Feld nach Norden.

Wenn du über den Rand des Bauernhofs hinaus gehst, wird die Drohne auf die andere Seite des Bauernhofs versetzt. Das folgende Beispielcode hält die Drohne in Bewegung nach Norden und kehrt zum Anfang zurück, wenn sie den Rand des Bauernhofs erreicht:

`while True:
	move(North)`
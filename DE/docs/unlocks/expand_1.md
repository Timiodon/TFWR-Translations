# Erweitern 1
<unlock=for>Siehe auch [Erweitern_2](docs/unlocks/expand_2.md)

</unlock>Deine Farm ist gewachsen! Dieser Platz nützt nicht viel, wenn du die Drohne nicht bewegen kannst, also gibt es eine neue Funktion `move()`, die die Drohne bewegt. `move()` erfordert, dass du die Richtung angibst, in die sich die Drohne bewegen soll. Dafür gibt es vier neue Konstanten: `North, East, South, West`

Zum Beispiel wird `move(North)` die Drohne ein Feld nach Norden bewegen.

Wenn du über den Rand der Farm hinausfährst, wird die Drohne auf die andere Seite der Farm versetzt.
Der folgende Beispielcode wird die Drohne immer weiter nach Norden bewegen und zum Anfang zurückkehren, wenn sie den Rand der Farm erreicht:

`while True:
	move(North)`

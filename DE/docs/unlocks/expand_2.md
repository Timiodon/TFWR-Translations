# Erweiterung 2
Dein Bauernhof hat sich wieder vergrößert! Nun sind die Felder nicht mehr schön in einer Reihe, also musst du einen Weg finden, um ein quadratisches Gitter zu durchqueren.

Mit der `while` Schleife ist das nicht möglich, bis du Sinne und Operatoren freischaltest. Es ist an der Zeit, die `for` Schleife einzuführen.

Alles über die `for` Schleife kannst du auf der [For Loop](docs/scripting/for.md) Seite nachlesen. Für den Moment benötigst du sie nur, um Code eine festgelegte Anzahl von Malen zu wiederholen.

`#do n flips
for i in range(5):
	do_a_flip()`

`range(n)` erzeugt eine Zahlenreihe von `0` bis `n-1`, die `n` Elemente enthält. Die `for` Schleife führt ihren Schleifenrumpf einmal für jedes Element in der Sequenz aus. In diesem Beispiel wird `do_a_flip()` 5 Mal aufgerufen.

Die Funktion `get_world_size()` ist jetzt auch verfügbar. Sie gibt die Seitenlänge deines Bauernhofs zurück. Auf diese Weise kannst du Code schreiben, der nicht durch das nächste Erweiterungs-Upgrade beschädigt wird.

`for i in range(get_world_size()):
	harvest()
	move(North)`

Dieses Beispiel erntet eine Spalte des Bauernhofs für jede beliebige Hofgröße.

Falls du nicht weiterkommst, um herauszufinden, wie man die Drohne über den Hof bewegt, sieh dir den Hinweis unten an.
<spoiler=Hinweis anzeigen>Es gibt natürlich mehrere Möglichkeiten, sich auf dem Hof zu bewegen.
Wir suchen nach einer systematischen Möglichkeit, ihn zu durchqueren, die nicht kaputtgeht, wenn der Hof erneut wächst.
Eine systematische Methode, um zu jedem Ort auf dem Hof zu gelangen, wäre es, die folgenden 2 Schritte immer wieder zu wiederholen:

1. Bewege dich `North`, bis es zurückspringt.
2. Bewege dich `East`

`for i in range(get_world_size()):` könnte hilfreich sein, um diese Idee in Code umzusetzen.
</spoiler>
<spoiler=zeige mögliche Lösung> Der grundlegende Durchlauf könnte so aussehen:

`for i in range(get_world_size()):
	for j in range(get_world_size()):
		#do a flip on every tile
		do_a_flip()
		move(North)
	move(East)`
</spoiler>
# Erweitern 2
Deine Farm hat sich wieder erweitert! Jetzt liegen die Felder nicht mehr in einer schönen Reihe, also musst du einen Weg finden, ein quadratisches Gitter zu durchqueren.

Mit der `while`-Schleife ist das nicht möglich, bis du Sinne und Operatoren freischaltest.
Es ist Zeit, die `for`-Schleife einzuführen.

Du kannst alles über die `for`-Schleife auf der Seite [For-Schleife](docs/scripting/for.md) lesen, aber vorerst benötigst du sie nur, um Code eine feste Anzahl von Malen zu wiederholen.

`#mache n Saltos
for i in range(5):
	do_a_flip()`

`range(n)` erzeugt einen Bereich von Zahlen von `0` bis `n-1`, der `n` Elemente enthält. Die `for`-Schleife führt ihren Schleifenkörper einmal für jedes Element in der Sequenz aus. In diesem Beispiel wird `do_a_flip()` `5` Mal aufgerufen.

Die Funktion `get_world_size()` ist jetzt auch verfügbar. Sie gibt die Seitenlänge deiner Farm zurück. Auf diese Weise kannst du Code schreiben, der beim nächsten Erweiterungs-Upgrade nicht kaputt geht.

`for i in range(get_world_size()):
	harvest()
	move(North)`

Dieses Beispiel erntet eine Spalte der Farm für jede Farmgröße.

Wenn du nicht weiterkommst und versuchst herauszufinden, wie du die Drohne auf der Farm bewegen kannst, sieh dir den Hinweis unten an.
<spoiler=zeige Hinweis>Es gibt natürlich mehrere Möglichkeiten, sich auf der Farm zu bewegen.
Was wir suchen, ist eine Möglichkeit, sie systematisch zu durchqueren, die nicht kaputt geht, wenn die Farm wieder wächst.
Eine systematische Methode, um jeden Ort auf der Farm zu erreichen, wäre, die folgenden 2 Schritte für immer zu wiederholen:

1.Bewege dich nach `North`, bis du wieder am Anfang ankommst.
2.Bewege dich nach `East`

`for i in range(get_world_size()):` könnte hilfreich sein, um diese Idee in Code umzusetzen.
</spoiler>
<spoiler=zeige mögliche Lösung> Die grundlegende Durchquerung könnte so aussehen:

`for i in range(get_world_size()):
	for j in range(get_world_size()):
		#mache einen Salto auf jedem Feld
		do_a_flip()
		move(North)
	move(East)`
</spoiler>
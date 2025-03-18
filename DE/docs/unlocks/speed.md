# Geschwindigkeitsupgrade
Die Ausführungsgeschwindigkeit wurde verdoppelt. Das Problem ist, dass die Drohne jetzt schneller erntet, als das Gras nachwachsen kann, was zu keiner Ernte führt. Um damit umzugehen, sind jetzt [if](docs/scripting/if.md)-Verzweigungen und die [can_harvest](functions/can_harvest)-Funktion freigeschaltet.

## Prüfung vor dem Ernten
Bisher hatten wir nur `True` und `False` als Bedingungen, was natürlich mit `if` nicht sehr hilfreich ist. 

Die neue Funktion can_harvest() bietet eine bessere Bedingung. `can_harvest()` gibt `True` zurück, wenn die Pflanze unter der Drohne geerntet werden kann und `False` andernfalls.

`if can_harvest():
	#do something`

Der Grund, warum du diese Funktion als Bedingung so verwenden kannst, ist, dass sie einen booleschen Wert zurückgibt.

Ein Rückgabewert bedeutet im Wesentlichen, dass nach Ausführung der Funktionalität der Funktionsaufruf-Ausdruck auf den zurückgegebenen Wert ausgewertet wird.

Was passiert, wenn der obige Code läuft:
	-das if wird ausgeführt
	-`can_harvest()` wird aufgerufen
	-`can_harvest()` tut sein Ding
	-`can_harvest()` gibt `True` oder `False` zurück
	-die Anweisung ist nun `if True:` oder `if False:`
	-der Codeblock wird nur ausgeführt, wenn geerntet werden kann

Jetzt können wir `if` verwenden, um zu verhindern, dass die Drohne zu früh erntet.
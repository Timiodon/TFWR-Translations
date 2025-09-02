# Zeitmessung
Wenn du deine Methoden wirklich optimieren willst, musst du verstehen, wie die Zeit in diesem Spiel gemessen wird. Darum geht es bei dieser Freischaltung.

## Neue Funktionen
Es gibt zwei nützliche Funktionen, um zu messen, wie lange Dinge dauern:

`get_time()` gibt die Zeit in Sekunden seit dem Spielstart zurück.

`get_tick_count()` gibt die Anzahl der Ticks seit dem Start der Ausführung zurück.

Diese beiden Funktionen sowie `quick_print()` sind komplett kostenlos. Sogar der Aufruf selbst ist für sie kostenlos.

## Laufzeitdetails

### Wichtiger Hinweis
So funktioniert Performance in der echten Welt nicht. Dies sind nur Regeln, die für dieses Spiel aufgestellt wurden, um ein konsistentes und verständliches Zeitmessungsmodell zu haben.
Das wird dich wahrscheinlich nur interessieren, wenn du deinen Code hyper-optimieren willst.


Die grundlegende Zeiteinheit für die Code-Ausführung wird "Tick" genannt. Ohne Geschwindigkeits-Upgrades und Energie läuft die Ausführung mit einer Rate von `400` Ticks pro Sekunde.

Im Allgemeinen dauern Operationen, die zwei Werte kombinieren, wie `+, -, *, /, //, %, and, or, ...`, einen Tick.
Ein-Wert-Operationen `-` und `not` sind kostenlos.
Eine `if`-Verzweigung dauert ebenfalls einen Tick (zusätzlich zur Zeit, die für die Auswertung des Bedingungsausdrucks benötigt wird).
Funktionsaufrufe und das Lesen und Schreiben von Variablen sind kostenlos, aber Funktionsdefinitionen dauern 1 Tick.
`import`-Anweisungen sind kostenlos.
Der Zugriff auf ein importiertes Modul mit dem `.`-Operator ist kostenlos.
Wenn eine Funktion oder ein Modul über Argumente oder Variablenzuweisungen übergeben wurde, kostet die Verwendung 1 Tick anstatt 0.
`for`- und `while`-Schleifen dauern einen Tick zum Starten, aber die Iterationen sind kostenlos (die Zeit zur Auswertung der Bedingungs-/Sequenzausdrücke nicht mitgerechnet).
`return`, `break` und `continue` sind alle kostenlos.
`pass` dauert einen Tick, sodass es verwendet werden kann, um präzise Verzögerungen zu erzeugen.
Die Indizierung in eine Datenstruktur dauert einen Tick für den Index-Operator und, im Falle eines Dictionaries oder Sets, zusätzliche Ticks abhängig von der Größe des Schlüssels.

Die Anzahl der Ticks, die eingebaute Funktionen zur Ausführung benötigen, ist in der Dokumentation jeder Funktion einzeln dokumentiert.
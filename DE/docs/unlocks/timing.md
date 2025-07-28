# Timing
Wenn du deine Methoden wirklich optimieren möchtest, musst du verstehen, wie die Zeit in diesem Spiel gemessen wird. Bei dieser Freischaltung geht es genau darum.

## Neue Funktionen
Es gibt zwei nützliche Funktionen, um zu messen, wie lange Dinge dauern:

`get_time()` gibt die Zeit in Sekunden seit dem Spielstart zurück.

`get_tick_count()` gibt die Anzahl der Ticks zurück, die seit Beginn der Ausführung durchgeführt wurden.

Diese beiden Funktionen, sowie `quick_print()`, sind komplett kostenlos. Sogar der Aufruf-Vorgang ist für sie kostenlos.

## Laufzeit-Details

### Achtung
So funktioniert Performance nicht in der echten Welt. Das sind nur Regeln, die für dieses Spiel erfunden wurden, um ein konsistentes und verständliches Timing-Modell zu haben.
Das wird dich wahrscheinlich nur interessieren, wenn du deinen Code hyper-optimieren willst.


Die Grundeinheit der Zeit für die Code-Ausführung wird als "Tick" bezeichnet. Ohne Geschwindigkeits-Upgrades und Energie läuft die Ausführung mit einer Rate von `400` Ticks pro Sekunde.

Im Allgemeinen dauern Operationen, die zwei Werte kombinieren, wie `+, -, *, /, //, %, and, or, ...`, einen Tick.
Einzelwert-`-` und `not` sind kostenlos.
Eine `if`-Verzweigung dauert ebenfalls einen Tick (zusätzlich zur Zeit, die zur Auswertung des Bedingungsausdrucks benötigt wird).
Funktionsaufrufe sowie das Lesen und Schreiben von Variablen sind kostenlos, aber Funktionsdefinitionen dauern 1 Tick.
`import`-Anweisungen sind kostenlos.
Der Zugriff auf ein importiertes Modul mit dem `.`-Operator ist kostenlos.
Wenn eine Funktion oder ein Modul über Argumente oder Variablenzuweisungen übergeben wurde, kostet die Verwendung 1 Tick anstatt 0.
`for`- und `while`-Schleifen dauern einen Tick zum Starten, aber die Iterationen sind kostenlos (die Zeit zur Auswertung der Bedingungs-/Sequenzausdrücke nicht mitgezählt).
`return`, `break` und `continue` sind alle kostenlos.
`pass` dauert einen Tick, sodass es verwendet werden kann, um präzise Verzögerungen zu erzeugen.
Das Indizieren in eine Datenstruktur dauert einen Tick für den Index-Operator und, im Falle eines Dictionarys oder Sets, zusätzliche Ticks abhängig von der Größe des Keys.

Die Anzahl der Ticks, die eingebaute Funktionen zur Ausführung benötigen, ist in der Dokumentation jeder einzelnen Funktion dokumentiert.
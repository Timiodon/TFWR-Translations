# Timing
Wenn du wirklich deine Methoden optimieren möchtest, musst du verstehen, wie Zeit in diesem Spiel gemessen wird. Diese Freischaltung dreht sich genau darum.

## Neue Funktionen
Es gibt zwei nützliche Funktionen, um zu messen, wie lange Dinge dauern:

`get_time()` gibt die Zeit in Sekunden seit Spielbeginn zurück.

`get_tick_count()` gibt die Anzahl der Ticks seit dem Start der Ausführung zurück.

Diese beiden Funktionen, sowie `quick_print()`, sind vollkommen kostenlos. Sogar der Aufrufvorgang ist für sie kostenlos.

## Details zur Laufzeit

### Hinweis
Das ist nicht, wie Leistung in der realen Welt funktioniert. Diese Regeln wurden speziell für dieses Spiel entwickelt, um ein konsistentes und verständliches Zeitmodell zu schaffen.
Das ist wahrscheinlich nur relevant für dich, wenn du deinen Code hyper-optimieren möchtest.

Die Grundeinheit der Zeit für die Codeausführung wird "Tick" genannt. Ohne Geschwindigkeitsupgrades und Energie läuft die Ausführung mit einer Rate von `400` Ticks pro Sekunde.

Im Allgemeinen benötigen Operationen, die zwei Werte kombinieren, wie `+, -, *, /, //, %, and, or, ...`, einen Tick zur Ausführung.
Einzelne Werte `-` und `not` sind kostenlos.
Ein `if`-Zweig benötigt ebenfalls einen Tick zur Ausführung (zusätzlich zur Zeit, die benötigt wird, um den Bedingungsausdruck zu bewerten).
Funktionsaufrufe und das Lesen und Schreiben von Variablen sind kostenlos, aber Funktionsdefinitionen benötigen 1 Tick.
`import`-Anweisungen sind kostenlos.
Der Zugriff auf ein importiertes Modul mit dem `.`-Operator ist kostenlos.
Wenn eine Funktion oder ein Modul über Argumente oder Variablenzuweisungen übergeben wurde, kostet deren Nutzung 1 Tick anstelle von 0.
`for`- und `while`-Schleifen benötigen einen Tick, um zu starten, aber die Iterationen sind kostenlos (ohne die Zeit, um die Bedingung/Sequenzausdrücke zu bewerten).
`return`, `break` und `continue` sind alle kostenlos.
`pass` benötigt einen Tick und kann daher verwendet werden, um präzise Verzögerungen zu erzeugen.
Das Indizieren in eine Datenstruktur benötigt einen Tick für den Indexoperator und, im Falle eines Dictionary oder Set, zusätzliche Ticks abhängig von der Größe des Schlüssels.

Die Anzahl der Ticks, die eingebaute Funktionen zur Ausführung benötigen, ist in der Dokumentation jeder Funktion individuell dokumentiert.
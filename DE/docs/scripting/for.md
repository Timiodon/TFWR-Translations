# For-Schleife
Die `for`-Schleife funktioniert wie in Python. (In einigen Sprachen auch als foreach-Schleife bezeichnet, nicht zu verwechseln mit der C-Style for-Schleife, die etwas anderes ist).

`for i in sequence:
    #etwas mit i machen`

Ähnlich der `while`-Schleife ruft die `for`-Schleife ebenfalls wiederholt einen Codeblock auf. Statt basierend auf einer Bedingung zu schleifen, führt sie den Schleifenrumpf einmal für jedes Element in einer Sequenz aus.

## Syntax
Eine for-Schleife sieht so aus:

`for variable_name in sequence:
    #Codeblock`

`variable_name` kann beliebig gewählt werden. Es ist eine Variable, die das aktuelle Element in der Sequenz speichert. `sequence` muss ein Wert sein, der wie eine Reihe oder Zahlen durchlaufen werden kann. Der Codeblock wird für jedes Element mit der Schleifenvariablen, die diesem Element zugewiesen ist, ausgeführt.

## Sequenzen
[Ranges](functions/range)      <unlock=lists>[Listen](docs/scripting/lists.md)      </unlock><unlock=functions>[Tupel](docs/scripting/tuples.md)      </unlock><unlock=dicts>[Dictionaries](docs/scripting/dicts.md)      </unlock><unlock=sets>[Sets](docs/scripting/sets.md)</unlock>

## Beispiel
`for i in range(5):
    harvest()`

Diese Schleife führt den Rumpf eine feste Anzahl von Malen aus. Es ist im Wesentlichen dasselbe wie zu schreiben:

`i = 0
harvest()
i = 1
harvest()
i = 2
harvest()
i = 3
harvest()
i = 4
harvest()`

Es ruft also `harvest()` 5 Mal auf.

Siehe auch [Break](docs/scripting/break.md) und [Continue](docs/scripting/continue.md)
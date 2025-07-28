# For-Schleife
Die `for`-Schleife funktioniert wie in Python. (Wird in einigen Sprachen als foreach-Schleife bezeichnet, nicht zu verwechseln mit der C-artigen for-Schleife, die etwas anderes ist).

`for i in sequence:
	#etwas mit i tun`

Ähnlich wie die `while`-Schleife ruft auch die `for`-Schleife wiederholt einen Codeblock auf. Anstatt basierend auf einer Bedingung zu schleifen, führt sie den Schleifenkörper einmal für jedes Element in einer Sequenz aus.

## Syntax
Eine for-Schleife sieht so aus:

`for variable_name in sequence:
	#Codeblock`

`variable_name` kann ein beliebiger Name sein, den du wählst. Es ist eine Variable, die das aktuelle Element in der Sequenz speichert. `sequence` muss ein Wert sein, der durchlaufen werden kann, wie ein Bereich von Zahlen. Der Codeblock wird für jedes Element ausgeführt, wobei die Schleifenvariable diesem Element zugewiesen wird.

## Sequenzen
[Bereiche](functions/range)      <unlock=lists>[Listen](docs/scripting/lists.md)      </unlock><unlock=functions>[Tupel](docs/scripting/tuples.md)      </unlock><unlock=dicts>[Dictionaries](docs/scripting/dicts.md)      </unlock><unlock=sets>[Sets](docs/scripting/sets.md)</unlock>

## Beispiel
`for i in range(5):
    harvest()`

Diese Schleife führt den Körper eine feste Anzahl von Malen aus. Es ist im Wesentlichen dasselbe wie das Schreiben von

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

Also ruft es `harvest()` 5 Mal auf.

Siehe auch [Break](docs/scripting/break.md) und [Continue](docs/scripting/continue.md)
# Funktionen
Benutze das `def`-Schlüsselwort, um eine neue Funktion zu definieren:
`def f(arg1, arg2 = False):
	#Funktionscode`

Du kannst den Aufruf-Operator `()` benutzen, um die Funktion aufzurufen:
`f(42)`

Siehe auch [Geltungsbereiche (Scopes)](docs/scripting/scopes.md), um mehr über lokale und globale Variablen in Funktionen zu erfahren.

## Einführung
Du hast bereits eingebaute Funktionen wie `harvest()` gesehen.
Du kannst auch deine eigenen Funktionen definieren, was es dir ermöglicht, deinen Code modular zu strukturieren. Im Grunde genommen kannst du damit einem Codeblock einen Namen geben, sodass du ihn von überall aufrufen kannst.

## Funktionsdefinitionen
Zum Beispiel könntest du eine Funktion definieren, die die Drohne mehrmals bewegt.

`def move_n_dir(n, dir):
	for i in range(n):
		move(dir)`

Das `def`-Schlüsselwort signalisiert, dass dies eine Funktionsdefinition ist.
`move_n_dir` ist der Name, an den die Funktion gebunden wird. Dies kann jeder gültige Variablenname sein und wird verwendet, um die Funktion aufzurufen.
`n` und `dir` sind Parameter. Das sind Variablen, die die Werte enthalten, die an die Funktion übergeben werden (diese Werte werden auch Argumente genannt). Du kannst einer Funktionsdefinition so viele Parameter hinzufügen, wie du möchtest.
Nach dem `:` kommt der Codeblock, der ausgeführt wird, wenn die Funktion aufgerufen wird.

Mit der obigen Definition bewegt der folgende Code die Drohne `10` Felder nach `North` und `2` Felder nach `West`.

`move_n_dir(10, North)
move_n_dir(2, West)`

Wenn du `def function():` siehst, solltest du es dir wirklich als eine Variablenzuweisung wie diese vorstellen:
`function = create_new_function_object()`
Wie bei allen Zuweisungen kannst du die Variable nicht verwenden, bevor ihr ein Wert zugewiesen wurde!
Die `def`-Anweisung muss vor allen Funktionsaufrufen ausgeführt werden.
Dieser Code wird einen Fehler auslösen:

`func()
def func():
	pass`

## Rückgabewerte
Benutze das `return`-Schlüsselwort, um eine Funktion einen Wert zurückgeben zu lassen.
Zum Beispiel definiert die folgende Funktion die Exklusiv-Oder-Operation. Das Exklusiv-Oder gibt `True` zurück, wenn ein Wert `True` und der andere `False` ist:

`def xor(a, b):
	return a != b

if xor(True, False):
	do_a_flip()`

[Tupel](docs/scripting/tuples.md) ermöglichen die Rückgabe mehrerer Werte.

## Standardargumente
Du kannst auch Standardwerte zuweisen, die verwendet werden, wenn keine Argumente übergeben werden.

`def f(a = False):
	if a:
		do_a_flip()

f()

f(True)`

Einem Argument, das einen Standardwert hat, kann kein Argument folgen, das keinen Standardwert hat.

## Fortgeschrittene Funktionsnutzung
Funktionen sind Werte wie jeder andere Wert auch, und die `def`-Anweisung verhält sich einfach wie eine Zuweisungsanweisung, die die Funktion dem Namen zuweist, den du ihr gibst.
Das ermöglicht Dinge wie diese:

`def f():
	def d():
		do_a_flip()
	return d

f()()`

Hier ruft `f()` die Funktion `f` auf, welche eine neue Funktion `d` definiert und zurückgibt. Das zweite `()` führt dann die zurückgegebene Funktion aus und macht einen Salto.
(Solche Dinge zu tun ist normalerweise keine gute Idee, weil es schwer zu durchschauen ist, was passiert)

Funktionen, die andere Funktionen als Argumente entgegennehmen, lassen dich richtig kreativ werden:

`def f(g, arg):
	for _ in range(10):
		g(arg)

f(move, North)
f(use_item, Items.Fertilizer)`

Dieser Code bewegt die Drohne 10 Mal nach `North` und verwendet dann 10 Mal Dünger.
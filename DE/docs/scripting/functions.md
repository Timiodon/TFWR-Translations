# Funktionen
Verwende das `def`-Schlüsselwort, um eine neue Funktion zu definieren:
`def f(arg1, arg2 = False):
	#Funktionscode`

Du kannst den Aufruf-Operator `()` verwenden, um die Funktion aufzurufen:
`f(42)`

Sieh dir auch [Scopes](docs/scripting/scopes.md) an, um über lokale und globale Variablen in Funktionen zu lernen.

## Einführung
Du hast bereits eingebaute Funktionen wie `harvest()` gesehen.
Du kannst auch eigene Funktionen definieren, was dir erlaubt, deinen Code modular zu strukturieren. Es ermöglicht dir im Grunde, einem Codeblock einen Namen zu geben, sodass du ihn von überall aus aufrufen kannst.

## Funktionsdefinitionen
Zum Beispiel könntest du eine Funktion definieren, die die Drohne mehrmals bewegt.

`def move_n_dir(n, dir):
	for i in range(n):
		move(dir)`

Das `def`-Schlüsselwort signalisiert, dass dies eine Funktionsdefinition ist. 
`move_n_dir` ist der Name, an den die Funktion gebunden wird. Dies kann jeder gültige Variablenname sein und wird verwendet, um die Funktion aufzurufen.
`n` und `dir` sind Parameter. Sie sind Variablen, die die Werte halten, die in die Funktion übergeben werden (Diese Werte werden auch Argumente genannt). Du kannst einer Funktionsdefinition so viele Parameter hinzufügen, wie du möchtest.
Nach dem `:` folgt der Codeblock, der ausgeführt wird, wenn die Funktion aufgerufen wird.

Mit der obigen Definition bewegt der folgende Code die Drohne dann `10` Felder `North` und `2` Felder `West`.

`move_n_dir(10, North)
move_n_dir(2, West)`

Wenn du `def function():` siehst, solltest du eigentlich daran denken, dass es wie eine Variablenzuweisung ist, so:
`function = create_new_function_object()`
Wie bei allen Zuweisungen kannst du die Variable nicht verwenden, bevor sie zugewiesen wurde!
Die `def`-Anweisung muss ausgeführt werden, bevor irgendwelche Funktionsaufrufe stattfinden.
Dieser Code wird einen Fehler werfen:

`func()
def func():
	pass`

## Rückgabewerte
Verwende das `return`-Schlüsselwort, um eine Funktion einen Wert zurückgeben zu lassen. 
Zum Beispiel definiert die folgende Funktion die exklusive oder Operation. Das exklusive oder gibt `True` zurück, wenn ein Wert `True` ist und der andere `False`:

`def xor(a, b):
	return a != b

if xor(True, False):
	do_a_flip()`

[Tuples](docs/scripting/tuples.md) ermöglichen es, mehrere Werte zurückzugeben.

## Standardargumente
Du kannst auch Standardwerte festlegen, die verwendet werden, wenn keine Argumente übergeben werden.

`def f(a = False):
	if a:
		do_a_flip()

f()

f(True)`

Ein Argument mit einem Standardwert kann nicht von einem Argument gefolgt werden, das keinen Standardwert hat.

## Erweiterte Funktionsnutzung
Funktionen sind Werte genau wie jeder andere Wert, und die `def`-Anweisung handelt einfach wie eine Zuweisungsanweisung, die die Funktion dem von dir vergebenen Namen zuweist.
Dies ermöglicht Dinge wie Folgendes:

`def f():
	def d():
		do_a_flip()
	return d

f()()`

Hier ruft `f()` die Funktion `f` auf, die eine neue Funktion `d` definiert und zurückgibt. Das zweite `()` führt dann die zurückgegebene Funktion aus und führt den Flip aus.
(Dinge auf diese Weise zu tun, ist normalerweise keine gute Idee, weil es schwer zu erkennen ist, was vor sich geht)

Funktionen, die andere Funktionen als Argumente akzeptieren, lassen deiner Kreativität freien Lauf:

`def f(g, arg):
	for _ in range(10):
		g(arg)

f(move, North)
f(use_item, Items.Fertilizer)`

Dieser Code bewegt die Drohne `North` 10 Mal und verwendet dann 10 Mal Dünger.
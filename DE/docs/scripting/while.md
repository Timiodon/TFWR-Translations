# While-Schleife
Du hast die `while`-Schleife und die Werte `True` und `False` freigeschaltet. Die `while`-Schleife führt den Schleifenrumpf so lange aus, wie die Bedingung `True` ist.

`while condition:
	#loop body`

Mach dir keine Sorgen über endlose Schleifen. Die Verzögerungen bei der Ausführung verhindern, dass das Programm einfriert.

## Für Anfänger
Vielleicht hast du bereits versucht, mehrere `harvest()`-Aufrufe hintereinander zu setzen:

`harvest()
harvest()
harvest()`

Dies ermöglicht es dir, mehrmals in einem Programmablauf zu ernten. 
Allerdings wäre es schön, mehr als dreimal zu ernten, und denselben Code mehrfach zu schreiben, ist keine gute Praxis. 
Die Lösung ist eine Schleife. 
Eine Schleife ermöglicht es dir, denselben Code mehrmals auszuführen.

Die while-Schleife nimmt eine Bedingung, die ein logischer Wert ist, der nur in einem von zwei Zuständen sein kann: `True` oder `False`. 
Ein solcher Wert wird als boolescher Wert bezeichnet.

Die Schleife führt dann den Code im Inneren der Schleife aus, bis die Bedingung False ist.
Die while-Schleife sieht so aus:

`while condition:
	#loop body
	#loop body
	#...`

Dabei musst du "condition" durch einen booleschen Wert und `#loop body` mit dem ersetzen, was du in der Schleife tun möchtest.

Es gibt zwei konstante boolesche Werte. Konstanten sind Werte, die sich während des Programms nicht ändern.

Um einen konstanten booleschen Wert zu erstellen, der immer `True` ist, kannst du einfach `True` schreiben. Schreib `False` als einen konstanten booleschen Wert, der immer `False` sein wird.
Also könntest du entweder schreiben:

`while False:
	do_a_flip()`

oder

`while True:
	do_a_flip()`

Das Erste wird nie einen Flip machen und das Zweite wird unendlich Flips machen (eine endlose Schleife).

Normalerweise ist es eine schlechte Idee, eine endlose Schleife zu erstellen, weil das Programm einfriert, aber in diesem Spiel gibt es Verzögerungen zwischen jeder Iteration der Schleife, sodass der Drohne einfach weiterhin Flips machen wird, bis du sie manuell stoppst, indem du erneut auf den Ausführen-Button drückst.

Beachte, wie die Zeile nach dem Doppelpunkt eingerückt ist. Einrückungen wie diese werden verwendet, um Codeblöcke zu trennen.
Drücke einfach Tab, um eine Einrückung hinzuzufügen und Shift + Tab (oder Backspace), um sie zu entfernen.

Die Schleife wird alle nach dem Doppelpunkt eingerückten Anweisungen wiederholen.
Anweisungen nach dem eingerückten Block werden ausgeführt, nachdem die Schleife beendet ist.
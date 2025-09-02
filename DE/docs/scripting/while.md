# While-Schleife
Du hast die `while`-Schleife und die Werte `True` und `False` freigeschaltet. Die `while`-Schleife führt den Schleifenkörper so lange aus, wie die Bedingung `True` ist.

`while condition:
	#Schleifenkörper`

Mach dir keine Sorgen über Endlosschleifen. Die Verzögerungen in der Ausführung verhindern, dass das Programm einfriert.

## Für Anfänger
Vielleicht hast du schon versucht, mehrere `harvest()`-Aufrufe hintereinander zu setzen:

`harvest()
harvest()
harvest()`

Dies ermöglicht es dir, mehrmals in einem Programmlauf zu ernten.
Es wäre jedoch schön, mehr als dreimal zu ernten, und denselben Code mehrmals zu schreiben, ist schlechte Praxis.
Die Lösung ist eine Schleife.
Eine Schleife ermöglicht es dir, denselben Code mehrmals auszuführen.

Die while-Schleife benötigt eine Bedingung, die ein logischer Wert ist, der nur einen von zwei Zuständen haben kann: `True` oder `False`.
Ein solcher Wert wird als boolescher Wert bezeichnet.

Die Schleife führt dann den Code innerhalb der Schleife aus, bis die Bedingung `False` ist.
Die while-Schleife sieht so aus:

`while condition:
	#Schleifenkörper
	#Schleifenkörper
	#...`
	
Wobei du "condition" durch einen booleschen Wert und `#loop body` durch das ersetzen musst, was du in der Schleife tun möchtest.

Es gibt zwei konstante boolesche Werte. Konstanten sind Werte, die sich während des Programms nie ändern.

Um einen konstanten booleschen Wert zu erstellen, der immer `True` ist, kannst du einfach `True` schreiben. Schreibe `False` für einen konstanten booleschen Wert, der immer `False` sein wird.
Du könntest also entweder schreiben


`while False:
	do_a_flip()`

oder

`while True:
	do_a_flip()`

Die erste wird niemals einen Salto machen und die zweite wird für immer Saltos machen (eine Endlosschleife).

Normalerweise ist das Erstellen einer Endlosschleife eine schlechte Idee, da sie das Programm zum Absturz bringen würde, aber in diesem Spiel gibt es Verzögerungen zwischen jeder Iteration der Schleife, sodass die Drohne so lange Saltos macht, bis du sie manuell stoppst, indem du erneut auf den Ausführen-Button drückst.

Beachte, wie die Zeile nach dem Doppelpunkt eingerückt ist. Solche Einrückungen werden verwendet, um Codeblöcke zu trennen.
Drücke einfach die Tab-Taste, um eine Einrückung hinzuzufügen, und Umschalt + Tab (oder Rücktaste), um sie zu entfernen.

Die Schleife wiederholt alle eingerückten Anweisungen nach dem Doppelpunkt.
Anweisungen nach dem eingerückten Block werden ausgeführt, nachdem die Schleife beendet ist.

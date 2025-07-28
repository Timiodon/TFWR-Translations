# While-Schleife
Du hast die `while`-Schleife und die Werte `True` und `False` freigeschaltet. Die `while`-Schleife führt den Schleifenkörper so lange aus, wie die Bedingung `True` ist.

`while bedingung:
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

Die while-Schleife benötigt eine Bedingung, die ein logischer Wert ist, der nur in einem von zwei Zuständen sein kann: `True` oder `False`.
Ein solcher Wert wird als boolescher Wert bezeichnet.

Die Schleife führt dann den Code innerhalb der Schleife aus, bis die Bedingung False ist.
Die while-Schleife sieht so aus:

`while bedingung:
	#Schleifenkörper
	#Schleifenkörper
	#...`
	
Wobei du "bedingung" durch einen booleschen Wert und `#Schleifenkörper` durch das ersetzen musst, was du in der Schleife tun möchtest.

Es gibt zwei konstante boolesche Werte. Konstanten sind Werte, die sich während des Programms nie ändern.

Um einen konstanten booleschen Wert zu erstellen, der immer `True` ist, kannst du einfach `True` schreiben. Schreibe `False` für einen konstanten booleschen Wert, der immer `False` sein wird.
Du könntest also entweder schreiben


`while False:
	do_a_flip()`

oder

`while True:
	do_a_flip()`

Die erste wird niemals einen Salto machen und die zweite wird für immer Saltos machen (eine Endlosschleife).

Normalerweise ist das Erstellen einer Endlosschleife eine schlechte Idee, weil sie das Programm einfrieren lässt, aber in diesem Spiel gibt es Verzögerungen zwischen jeder Iteration der Schleife, so dass die Drohne so lange Saltos macht, bis du sie manuell stoppst, indem du erneut auf den Ausführen-Button drückst.

Beachte, wie die Zeile nach dem Doppelpunkt eingerückt ist. Eine solche Einrückung wird verwendet, um Codeblöcke zu trennen.
Drücke einfach Tab, um eine Einrückung hinzuzufügen, und Shift + Tab (oder Backspace), um sie zu entfernen.

Die Schleife wiederholt alle eingerückten Anweisungen nach dem Doppelpunkt.
Anweisungen nach dem eingerückten Block werden ausgeführt, nachdem die Schleife beendet ist.

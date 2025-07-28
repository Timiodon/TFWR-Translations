# Tupel
Tupel sind eine großartige Möglichkeit, mehrere Werte zu einem einzigen Wert zu kombinieren.
Um ein Tupel zu erstellen, trenne die Werte einfach mit Kommas:

`tuple = 1, 2`

Du kannst sie auch wieder in mehrere Variablen entpacken. Im folgenden Code wird das Tupel `(1,2)` in zwei Variablen `a` und `b` entpackt.

`a, b = 1, 2`

Tupel können wie Listen indiziert werden, aber sie sind unveränderlich und können nach ihrer Erstellung nicht mehr geändert werden.

`tuple = 1, 2`

`print(tuple[1])`
gibt `2` aus

`tuple[0] = 3`
löst einen Error aus
<unlock=dicts>
Im Gegensatz zu Listen können Tupel als Keys in Dictionaries verwendet werden.

`d = {(1,2):(4,5)}

print(d[(1,2)])`
`gibt` (4,5)</unlock>

Sie können auch nützlich sein, um mehrere Werte in einer Funktion zurückzugeben.

`def f():
    return 1, 2

a, b = f()`
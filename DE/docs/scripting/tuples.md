# Tupel
Tupel sind eine großartige Möglichkeit, mehrere Werte in einem einzigen Wert zu kombinieren.
Um ein Tupel zu erstellen, trenne einfach die Werte mit Kommas:

`tuple = 1, 2`

Du kannst sie auch wieder in mehrere Variablen entpacken. Im untenstehenden Code wird das Tupel `(1,2)` in zwei Variablen `a` und `b` entpackt.

`a, b = 1, 2`

Tupel können wie Listen indexiert werden, aber sie sind unveränderlich und können nach der Erstellung nicht mehr geändert werden.

`tuple = 1, 2`

`print(tuple[1])`
gibt `2` aus

`tuple[0] = 3`
wirft einen error
<unlock=dicts>  
Im Gegensatz zu Listen können Tupel als Schlüssel in dictionaries verwendet werden.

`d = {(1,2):(4,5)}

print(d[(1,2)])`
`gibt aus` (4,5)</unlock>

Sie können auch nützlich sein, um mehrere Werte in einer Funktion zurückzugeben.

`def f():
    return 1, 2

a, b = f()`
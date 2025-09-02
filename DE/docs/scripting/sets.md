# Sets
Sets sind wie [Dictionaries](docs/scripting/dicts.md), aber ohne Werte. Sie sind nur eine ungeordnete Menge von Schlüsseln.

Sie werden wie Dictionaries erstellt, aber ohne Werte.
`set = {North, East, West}`

Verwende `set()`, um ein leeres Set zu erstellen. Beachte, dass `{}` ein leeres Dictionary erstellt.

Verwende `set.add(elem)`, um ein neues Element zum Set hinzuzufügen.

Verwende `set.remove(elem)`, um ein Element aus einem Set zu entfernen.

Verwende `if elem in set:`, um zu prüfen, ob das Set ein Element enthält.

Verwende `for elem in set:`, um alle Elemente im Set zu durchlaufen.
Bei größeren Sets ist der `in`-Operator viel schneller als bei einer Liste.

Genau wie Dictionaries sind Sets ungeordnet, daher gibt es keine Garantien bezüglich der Reihenfolge, in der die Elemente durchlaufen werden.

Außerdem sind Elemente in Sets einzigartig. Das Hinzufügen eines Elements, das bereits im Set enthalten ist, ändert das Set also nicht.
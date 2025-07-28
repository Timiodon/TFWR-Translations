# Sets
Sets sind wie [Dictionaries](docs/scripting/dicts.md), aber ohne Values. Sie sind nur eine ungeordnete Menge von Keys.

Sie werden wie Dictionaries erstellt, aber ohne Values.
`set = {North, East, West}`

Benutze `set()`, um ein leeres Set zu erstellen. Beachte, dass `{}` ein leeres Dictionary erstellt.

Benutze `set.add(elem)`, um ein neues Element zum Set hinzuzufügen.

Benutze `set.remove(elem)`, um ein Element aus einem Set zu entfernen.

Benutze `if elem in set:`, um zu prüfen, ob das Set ein Element enthält.

Benutze `for elem in set:`, um alle Elemente im Set zu durchlaufen.
Bei größeren Sets ist der `in`-Operator viel schneller als bei einer Liste.

Genau wie Dictionaries sind Sets ungeordnet, daher gibt es keine Garantie für die Reihenfolge, in der die Elemente durchlaufen werden.

Außerdem sind die Elemente in Sets einzigartig. Das Hinzufügen eines Elements, das bereits im Set ist, ändert das Set nicht.
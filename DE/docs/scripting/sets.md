# Sets
Sets sind wie [dictionaries](docs/scripting/dicts.md), aber ohne Werte. Sie sind einfach eine ungeordnete Menge von Schlüsseln.

Sie werden wie dictionaries erstellt, aber ohne Werte. 
`set = {North, East, West}`

Verwende `set()`, um ein leeres set zu erstellen. Beachte, dass `{}` ein leeres dictionary erstellt.

Nutze `set.add(elem)`, um ein neues Element zum set hinzuzufügen.

Verwende `set.remove(elem)`, um ein Element aus einem set zu entfernen.

Nutze `if elem in set:` um zu prüfen, ob das set ein Element enthält.

Verwende `for elem in set:`, um alle Elemente im set durchzugehen.
Für größere sets ist der `in`-Operator viel schneller als bei einer Liste.

Genau wie dictionaries sind sets ungeordnet, es gibt also keine Garantie über die Reihenfolge, in der die Elemente durchlaufen werden.

Außerdem sind Elemente in sets einzigartig, das Hinzufügen eines bereits vorhandenen Elements ändert das set nicht.
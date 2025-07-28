# Dictionaries
Dictionaries sind eine Datenstruktur, die es dir ermöglicht, Keys auf Values abzubilden, so wie ein echtes Wörterbuch Wörter auf ihre Definitionen abbildet, und du kannst sie sehr schnell nachschlagen.

Ein Dictionary kann so erstellt werden:
`right_of = {North:East, East:South, South:West, West:North}`

Der Ausdruck vor dem Doppelpunkt ist der Key und der Ausdruck nach dem Doppelpunkt ist der Value, auf den der Key abbildet.
Das obige Dictionary bildet jede Richtung auf die Richtung rechts davon ab.

Hier ist ein weiteres, das die Position der Drohne auf die darüber befindliche Entity abbildet.
`x, y = get_pos_x(), get_pos_y()
entity_dict = {(x,y):get_entity_type()}`

Der Zugriff auf den einem Key zugeordneten Value ist ähnlich wie der Zugriff auf ein Element in einer Liste:
`value = dict[key]`

Beispiel:
`orientation = right_of[South]`
Dies setzt `orientation` auf `West`.

Du kannst ein neues Key-Value-Paar zu einem Dictionary so hinzufügen:
`dict[key] = value`

Beispiel:
`entity_dict[(get_pos_x(), get_pos_y())] = get_entity_type()`
Dies aktualisiert die für die aktuelle Position gespeicherte Entity.

Keys sind einzigartig, daher überschreibt das Hinzufügen eines bereits im Dictionary vorhandenen Keys den vorherigen Wert.

Verwende `dict.pop(key)`, um ein Key-Value-Paar aus `dict` zu entfernen.

`key in dict` wird zu `True` ausgewertet, wenn `key` ein Key in `dict` ist, und andernfalls `False`.
Du kannst also `if key in dict:` verwenden, um zu prüfen, ob `dict` den Key enthält.

Wenn du ein Dictionary in eine for-Schleife einfügst, kannst du durch alle Keys iterieren:
`for key in dict:
	value = dict[key]`

Es gibt keine Garantien bezüglich der Reihenfolge, in der die Keys durchlaufen werden.

Siehe auch [Sets](docs/scripting/sets.md)
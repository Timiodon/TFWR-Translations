# Dictionaries
Dictionaries sind eine Datenstruktur, die es dir ermöglicht, Schlüssel auf Werte abzubilden, so wie ein echtes Wörterbuch Wörter auf ihre Definitionen abbildet, und du kannst sie sehr schnell nachschlagen.

Ein Dictionary kann so erstellt werden:
`right_of = {North:East, East:South, South:West, West:North}`

Der Ausdruck vor dem Doppelpunkt ist der Schlüssel und der Ausdruck nach dem Doppelpunkt ist der Wert, auf den der Schlüssel abbildet.
Das obige Dictionary bildet jede Richtung auf die Richtung rechts davon ab.

Hier ist ein weiteres, das die Position der Drohne auf die Entität abbildet, über der sie sich befindet.
`x, y = get_pos_x(), get_pos_y()
entity_dict = {(x,y):get_entity_type()}`

Der Zugriff auf den Wert, der einem Schlüssel zugeordnet ist, ähnelt dem Zugriff auf ein Element in einer Liste:
`value = dict[key]`

Beispiel:
`orientation = right_of[South]`
Dies setzt `orientation` auf `West`.

Du kannst ein neues Schlüssel-Wert-Paar zu einem Dictionary hinzufügen, so wie hier:
`dict[key] = value`

Beispiel:
`entity_dict[(get_pos_x(), get_pos_y())] = get_entity_type()`
Dies aktualisiert die für die aktuelle Position gespeicherte Entität.

Schlüssel sind einzigartig, daher überschreibt das Hinzufügen eines Schlüssels, der bereits im Dictionary vorhanden ist, den vorherigen Wert.

Verwende `dict.pop(key)`, um ein Schlüssel-Wert-Paar aus `dict` zu entfernen.

`key in dict` wird zu `True` ausgewertet, wenn `key` ein Schlüssel im `dict` ist, und andernfalls zu `False`.
Du kannst also `if key in dict:` verwenden, um zu prüfen, ob `dict` den Schlüssel enthält.

Wenn du ein Dictionary in eine for-Schleife setzt, kannst du alle Schlüssel durchlaufen:
`for key in dict:
	value = dict[key]`

Es gibt keine Garantien bezüglich der Reihenfolge, in der die Schlüssel durchlaufen werden.

Siehe auch [Sets](docs/scripting/sets.md)
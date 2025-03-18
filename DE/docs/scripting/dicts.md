# Dictionaries
Dictionaries sind eine Datenstruktur, mit der du Schlüssel auf Werte abbilden kannst, ähnlich wie ein echtes Wörterbuch Wörter auf ihre Definitionen abbildet. Du kannst sie sehr schnell nachschlagen.

Ein Dictionary kann so erstellt werden:
`rotation = {North:East, East:South, South:West, West:North}`

Der Ausdruck vor dem Doppelpunkt ist der Schlüssel und der Ausdruck nach dem Doppelpunkt ist der Wert, auf den der Schlüssel abgebildet wird. Obiges Dictionary bildet jede Richtung auf die Richtung zu ihrer rechten Seite ab.

Hier ist noch eins, das die Position der Drone auf die Entity abbildet, die sie überfliegt.
`x, y = get_pos_x(), get_pos_y() entity_dict = {(x,y):get_entity_type()}`

Der Zugriff auf den Wert, der einem Schlüssel zugeordnet ist, ähnelt dem Zugriff auf ein Element in einer Liste:
`value = dict[key]`

Beispiel:
`orientation = rotation[South]`
Dies setzt `orientation` auf `West`.

Du kannst ein neues Schlüssel-Wert-Paar zu einem Dictionary hinzufügen, so:
`dict[key] = value`

Beispiel:
`entity_dict[(get_pos_x(), get_pos_y())] = get_entity_type()`
Dies aktualisiert die gespeicherte Entity für die aktuelle Position.

Schlüssel sind eindeutig, das Hinzufügen eines Schlüssels, der bereits im Dictionary existiert, wird den vorherigen Wert überschreiben.

Verwende `dict.pop(key)`, um ein Schlüssel-Wert-Paar aus `dict` zu entfernen.

`key in dict` ergibt `True`, wenn `key` ein Schlüssel im `dict` ist, und `False` andernfalls. Du kannst also `if key in dict:` verwenden, um zu überprüfen, ob `dict` den Schlüssel enthält.

Ein Dictionary in eine for-Schleife zu setzen, erlaubt es dir, durch alle Schlüssel zu iterieren:
`for key in dict: value = dict[key]`

Es gibt keine Garantien über die Ordnung, in der die Schlüssel iteriert werden.

Siehe auch [Sets](docs/scripting/sets.md)
# Sinne
Die Drohne kann jetzt sehen!

Die Funktionen `get_pos_x()` und `get_pos_y()` geben die aktuelle x- und y-Position der Drohne zurück. Am Startpunkt sind beide `0`. Die x-Position erhöht sich um `1` pro Feld in Richtung `East` und die y-Position erhöht sich um `1` pro Feld in Richtung `North`.

`num_items(item)` gibt zurück, wie viele von einem bestimmten Item du hast.
Zum Beispiel gibt `num_items(Items.Hay)` an, wie viel Heu du hast.

`get_entity_type()` und `get_ground_type()` geben den Typ der Entität oder des Bodens an, der sich unter der Drohne befindet.

Mach einen Flip, wenn du über einem Busch bist:
`if get_entity_type() == Entities.Bush:
	do_a_flip()`

Das `None` Schlüsselwort ist jetzt auch freigeschaltet! `None` ist ein Wert, der anzeigt, dass es keinen Wert gibt.
Zum Beispiel wird eine Funktion, die keine `return`-Anweisung hat, tatsächlich `None` zurückgeben.

`get_entity_type()` gibt `None` zurück, wenn sich keine Entität unter der Drohne befindet.
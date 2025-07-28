# Sinne
Die Drohne kann jetzt sehen!

Die Funktionen `get_pos_x()` und `get_pos_y()` geben die aktuelle x- und y-Position der Drohne zurück. An der Startposition sind beide `0`. Die x-Position erhöht sich um `1` pro Feld in Richtung `East` und die y-Position erhöht sich um `1` pro Feld in Richtung `North`.

`num_items(item)` gibt zurück, wie viele eines Items du hast.
Zum Beispiel gibt `num_items(Items.Hay)` zurück, wie viel Heu du hast.

`get_entity_type()` und `get_ground_type()` geben den Typ der Entity oder des Bodens unter der Drohne zurück.

Mache einen Salto, wenn du über einem Busch bist:
`if get_entity_type() == Entities.Bush:
	do_a_flip()`

Das `None`-Schlüsselwort ist jetzt auch freigeschaltet! `None` ist ein Wert, der darstellt, dass es keinen Wert gibt.
Zum Beispiel wird eine Funktion, die keine `return`-Anweisung hat, tatsächlich `None` zurückgeben.

`get_entity_type()` gibt `None` zurück, wenn sich keine Entity unter der Drohne befindet.

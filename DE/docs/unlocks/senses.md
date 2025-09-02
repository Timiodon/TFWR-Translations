# Sinne
Die Drohne kann jetzt sehen!

Die Funktionen `get_pos_x()` und `get_pos_y()` geben die aktuelle x- und y-Position der Drohne zurück. An der Startposition sind beide `0`. Die x-Position erhöht sich um `1` pro Feld in Richtung `East` und die y-Position erhöht sich um `1` pro Feld in Richtung `North`.

`num_items(item)` gibt an, wie viele von einem Gegenstand du hast.
Zum Beispiel gibt `num_items(Items.Hay)` an, wie viel Heu du hast.

`get_entity_type()` und `get_ground_type()` geben den Typ der Entität oder des Bodens an, der sich unter der Drohne befindet.

Mache einen Salto, wenn du über einem Busch bist:
`if get_entity_type() == Entities.Bush:
	do_a_flip()`

Das `None`-Schlüsselwort ist jetzt auch freigeschaltet! `None` ist ein Wert, der darstellt, dass es keinen Wert gibt.
Zum Beispiel wird eine Funktion, die keine `return`-Anweisung hat, tatsächlich `None` zurückgeben.

`get_entity_type()` gibt `None` zurück, wenn sich keine Entität unter der Drohne befindet.


Wenn du herausfinden willst, wie viele von einer bestimmten Freischaltung du hast, verwende die Funktion `num_unlocked(unlock)`.

Zum Beispiel gibt `num_unlocked(Unlocks.Speed)` die Anzahl der Geschwindigkeits-Upgrades zurück, die du hast.

`num_unlocked(Unlocks.Senses)` gibt `1` zurück, wenn die Sinne freigeschaltet sind, und `0`, wenn nicht.

Du kannst `num_unlocked()` auch auf Items, Entities oder Grounds anwenden. Dies gibt `1` zurück, wenn es freigeschaltet ist, andernfalls `0`.

Sei vorsichtig, `num_unlocked(Unlocks.Carrots)` gibt die Anzahl der Male zurück, die es freigeschaltet/aufgerüstet wurde.
`num_unlocked(Items.Carrot)` gibt nur `0` oder `1` zurück. (Dasselbe gilt für andere Pflanzen)
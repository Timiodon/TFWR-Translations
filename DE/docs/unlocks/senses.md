# Sinne
Die Drohne kann jetzt sehen! 

Die Funktionen `get_pos_x()` und `get_pos_y()` geben die aktuelle x- und y-Position der Drohne zurück. An der Startposition sind beide `0`. Die x-Position erhöht sich um `1` pro Feld in Richtung `East` und die y-Position erhöht sich um `1` pro Feld in Richtung `North`.

`num_items(item)` gibt zurück, wie viele von einem Item du hast.
Zum Beispiel gibt `num_items(Items.Hay)` zurück, wie viel Heu du hast.

`get_entity_type()` und `get_ground_type()` geben den Typ der Entity oder des Bodens unter der Drohne zurück.

Mache einen Salto, wenn du über einem Busch bist:
`if get_entity_type() == Entities.Bush:
	do_a_flip()`

Das `None`-Schlüsselwort ist jetzt auch freigeschaltet! `None` ist ein Wert, der darstellt, dass es keinen Wert gibt.
Zum Beispiel gibt eine Funktion, die keine `return`-Anweisung hat, tatsächlich `None` zurück.

`get_entity_type()` gibt `None` zurück, wenn sich keine Entity unter der Drohne befindet.


Wenn du herausfinden möchtest, wie viele von einer bestimmten Freischaltung du hast, benutze die `num_unlocked(unlock)`-Funktion.

Zum Beispiel gibt `num_unlocked(Unlocks.Speed)` die Anzahl der Geschwindigkeits-Upgrades zurück, die du hast.

`num_unlocked(Unlocks.Senses)` gibt `1` zurück, wenn Sinne freigeschaltet sind, und `0`, wenn nicht.

Du kannst `num_unlocked()` auch auf Items, Entities oder Grounds anwenden. Dies gibt `1` zurück, wenn es freigeschaltet ist, andernfalls `0`.

Sei vorsichtig, `num_unlocked(Unlocks.Carrots)` gibt zurück, wie oft es freigeschaltet/aufgewertet wurde.
`num_unlocked(Items.Carrot)` gibt nur `0` oder `1` zurück. (Gleiches gilt für andere Pflanzen)
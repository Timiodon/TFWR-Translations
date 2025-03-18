# Polykultur
Du hast vielleicht schon bemerkt, dass Pflanzen manchmal mehr Ertrag liefern, wenn sie zusammen gepflanzt werden.
Gras, Büsche, Bäume und Karotten liefern mehr Ertrag, wenn sie den richtigen Pflanzenbegleiter haben. Jede Pflanze hat eine andere Begleiter-Präferenz, die nicht vorhersehbar ist. Zum Glück kann die Begleiter-Präferenz der Pflanze unter der Drohne mit `get_companion()` gemessen werden. Es gibt ein Tupel zurück, in dem das erste Element der Pflanzentyp ist, den die Pflanze als Begleiter möchte, und das zweite Element die Position, an der der Begleiter sein soll.

`plant, (x, y) = get_companion()`

Wenn du zum Beispiel einen Busch pflanzt und dann `get_companion()` aufrufst, wird etwas zurückgegeben wie `(Entities.Carrot, (3, 5))`. Das bedeutet, dass dieser Busch gerne Karotten an der Position `(3,5)` hätte. Wenn du also Karotten an `(3,5)` pflanzt und dann den Busch erntest, wird er mehr Holz liefern. Das Wachstumsstadium der Karotte spielt dabei keine Rolle.

Die Begleiter-Präferenz einer Pflanze kann `Entities.Grass`, `Entities.Bush`, `Entities.Tree` oder `Entities.Carrot` sein. Jede Pflanze wählt dies zufällig, aber sie wird immer eine andere Pflanzenart als sie selbst wählen. Die Position kann auch jede Position innerhalb von 3 Zügen von der Pflanze sein, außer der Position der Pflanze selbst.

Wenn sich keine Pflanze mit einer Begleiter-Präferenz unter der Drohne befindet, wird `get_companion()` `None` zurückgeben.

Der Ertragsmultiplikator beträgt `5` plus die Anzahl der Polykultur-Verbesserungen.
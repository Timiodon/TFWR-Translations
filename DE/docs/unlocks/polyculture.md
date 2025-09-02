# Polykultur
Du hast vielleicht schon bemerkt, dass Pflanzen manchmal mehr Ertrag bringen, wenn sie zusammen gepflanzt werden.
Gras, Büsche, Bäume und Karotten bringen mehr Ertrag, wenn sie den richtigen Pflanzenbegleiter haben. Die Begleiter-Präferenz ist für jede einzelne Pflanze unterschiedlich und kann nicht vorhergesagt werden. Glücklicherweise kann die Begleiter-Präferenz der Pflanze unter der Drohne mit `get_companion()` gemessen werden. Es gibt ein Tupel zurück, bei dem das erste Element die Art der Pflanze ist, die sie als Begleiter haben möchte, und das zweite Element die Position, an der sie ihren Begleiter haben möchte.

`plant_type, (x, y) = get_companion()`

Wenn du zum Beispiel einen Busch pflanzt und dann `get_companion()` aufrufst, wird es etwas wie `(Entities.Carrot, (3, 5))` zurückgeben. Das bedeutet, dass dieser Busch gerne Karotten an der Position `(3,5)` hätte. Wenn du also Karotten bei `(3,5)` pflanzt und dann den Busch erntest, wird er mehr Holz einbringen. Das Wachstumsstadium der Karotte spielt keine Rolle.

Die Begleiter-Präferenz einer Pflanze kann entweder `Entities.Grass`, `Entities.Bush`, `Entities.Tree` oder `Entities.Carrot` sein. Jede Pflanze wählt dies zufällig, aber sie wird immer eine andere Pflanze als sich selbst wählen. Die Position kann auch jede Position innerhalb von 3 Zügen von der Pflanze entfernt sein, außer der Position der Pflanze selbst.

Wenn sich keine Pflanze unter der Drohne befindet, die eine Begleiter-Präferenz hat, gibt `get_companion()` `None` zurück.

Bevor die Polykultur freigeschaltet ist, beträgt der Ertragsmultiplikator `5`. Er verdoppelt sich bei jedem Upgrade.
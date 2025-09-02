# Karotten
Bevor du mit `plant(Entities.Carrot)` Karotten pflanzen kannst, musst du den Boden pflügen. Dadurch wird der Boden zu `Grounds.Soil`. Um den Boden zu pflügen, rufe einfach `till()` auf. Ein erneuter Aufruf von `till()` ändert ihn wieder in `Grounds.Grassland`.

Das Pflanzen von Karotten kostet Holz und Heu. Diese Gegenstände werden automatisch entfernt, wenn du `plant(Entities.Carrot)` aufrufst.

Die Kosten jeder Pflanze kannst du auf ihrer [eigenen Seite](objects/carrot) einsehen.
# Bewässern
Pflanzen wachsen schneller, wenn sie bewässert werden. Der Boden hat einen Wasserlevel, der von `0` bis `1` reicht.
Die Funktion `get_water()` gibt den Wasserlevel des Bodens zurück, über dem sie sich befindet.

Die Wachstumsgeschwindigkeit einer Pflanze skaliert linear von 1x Geschwindigkeit bei Wasserlevel 0 bis zu 5x Geschwindigkeit bei Wasserlevel 1.

Der Boden trocknet mit der Zeit aus: Im Durchschnitt verliert er 1 % seines aktuellen Wassers pro Sekunde, aber es gibt einige zufällige Schwankungen. Einen hohen Wasserlevel zu halten, verbraucht viel mehr Wasser als einen niedrigen Wasserlevel zu halten.

Du kannst Wasser auf deine Pflanzen nutzen. Ein Wassertank wird automatisch alle 10 Sekunden zu deinem Inventar hinzugefügt.
Ein Upgrade auf `Unlocks.Watering` gibt dir alle 10 Sekunden einen zusätzlichen Wassertank.

Ein Tank fasst `0.25` Wasser.

Verwende `use_item(Items.Water)` über jedem Boden, um den Boden zu bewässern.
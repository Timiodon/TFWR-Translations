# Bewässern
Pflanzen wachsen schneller, wenn sie bewässert werden. Der Boden hat einen Wasserlevel, der von `0` bis `1` reicht.
Die Funktion `get_water()` gibt den Wasserlevel des Bodens zurück, über dem sie sich befindet.

Die Wachstumsrate einer Pflanze skaliert linear von 1x Geschwindigkeit bei Wasserlevel 0 bis zu 5x Geschwindigkeit bei Wasserlevel 1.

Der Boden trocknet mit der Zeit aus: Im Durchschnitt verliert er 1 % seines aktuellen Wassers pro Sekunde, aber es gibt eine gewisse zufällige Abweichung. Ein hoher Wasserlevel verbraucht viel mehr Wasser als ein niedriger Wasserlevel.

Du kannst Wassertanks benutzen, um deine Pflanzen zu bewässern. Ein Wassertank wird alle 10 Sekunden automatisch zu deinem Inventar hinzugefügt.
Durch das Upgrade `Unlocks.Watering` bekommst du zusätzlich alle 10 Sekunden einen weiteren Wassertank.

Ein Tank fasst `0.25` Wasser.

Rufe `use_item(Items.Water)` über irgendeinem Boden auf, um den Boden zu bewässern.
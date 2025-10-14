# Bewässerung
Pflanzen wachsen schneller, wenn sie bewässert werden. Der Boden hat einen Wasserstand von `0` bis `1`.
Die Funktion `get_water()` gibt den Wasserstand des Bodens zurück, über dem sie sich befindet.

Die Wachstumsgeschwindigkeit einer Pflanze skaliert linear von 1x Geschwindigkeit bei Wasserstand 0 bis 5x Geschwindigkeit bei Wasserstand 1.

Der Boden trocknet mit der Zeit aus: Im Durchschnitt verliert er 1% seines aktuellen Wassers pro Sekunde, aber es gibt dabei eine gewisse zufällige Abweichung. Ein hoher Wasserstand verbraucht viel mehr Wasser als ein niedriger Wasserstand.

Du kannst Wasser für deine Pflanzen verwenden. Alle 10 Sekunden wird automatisch ein Wassertank zu deinem Inventar hinzugefügt.
Ein Upgrade von `Unlocks.Watering` verdoppelt die Menge an Wasser, die du alle 10 Sekunden bekommst.

Ein Tank fasst `0.25` Wasser.

Rufe `use_item(Items.Water)` über einem beliebigen Boden auf, um den Boden zu bewässern.

# Kaktus
Wie andere Pflanzen können [Kakteen](objects/cactus) auf Erde gepflanzt und wie üblich geerntet werden.

Allerdings gibt es sie in verschiedenen Größen und sie haben einen seltsamen Sinn für Ordnung.

Wenn du einen ausgewachsenen Kaktus erntest und alle benachbarten Kakteen in sortierter Reihenfolge sind, werden ebenfalls alle benachbarten Kakteen rekursiv mitgeerntet.

Ein Kaktus gilt als in sortierter Reihenfolge, wenn alle benachbarten Kakteen im `North` und `East` vollständig gewachsen und größer oder gleich groß sind und alle benachbarten Kakteen im `South` und `West` vollständig gewachsen und kleiner oder gleich groß sind.

Die Ernte wird sich nur ausbreiten, wenn alle angrenzenden Kakteen vollständig gewachsen und in sortierter Reihenfolge sind.
Das bedeutet, wenn ein Quadrat aus gewachsenen Kakteen nach Größe sortiert ist und du einen Kaktus erntest, wird das gesamte Quadrat geerntet.

Du erhältst Kaktus entsprechend der Anzahl der geernteten Kakteen im Quadrat. Wenn du also `n` Kakteen gleichzeitig erntest, erhältst du `n**2` `Items.Cactus`.

Die Größe eines Kaktus kann mit `measure()` gemessen werden.
Es ist immer eine dieser Zahlen: `0,1,2,3,4,5,6,7,8,9`.

Du kannst auch eine Richtung in `measure(direction)` übergeben, um das benachbarte Feld in dieser Richtung des Drones zu messen.

Du kannst einen Kaktus mit seinem Nachbarn in jede Richtung mit dem `swap()`-Befehl tauschen.
`swap(direction)` tauscht das Objekt unter dem Drone mit dem Objekt ein Feld in der `direction` des Drones.

## Beispiele
In jedem dieser Gitter sind alle Kakteen in sortierter Reihenfolge und die Ernte wird sich über das ganze Feld ausbreiten:
`3 4 5    3 3 3    1 2 3    1 5 9
2 3 4    2 2 2    1 2 3    1 3 8
1 2 3    1 1 1    1 2 3    1 3 4`

In diesem Gitter ist nur der Kaktus unten links in sortierter Reihenfolge, was nicht ausreicht, um sich auszubreiten:
`1 5 3
4 9 7
3 3 2`

<spoiler=Tipp anzeigen 1>
Wenn jede Spalte und jede Zeile des Feldes sortiert ist, dann ist das gesamte Feld sortiert.
</spoiler>
<spoiler=Tipp anzeigen 2>
Wenn du mit Sortieralgorithmen nicht vertraut bist, könntest du sie online nachschlagen und überlegen, welche auf dieses Problem angepasst werden könnten.
</spoiler>
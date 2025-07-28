# Kaktus
Wie andere Pflanzen können [Kakteen](objects/cactus) auf Erde angebaut und wie gewohnt geerntet werden.

Allerdings gibt es sie in verschiedenen Größen und sie haben einen seltsamen Sinn für Ordnung.

Wenn du einen ausgewachsenen Kaktus erntest und alle benachbarten Kakteen in sortierter Reihenfolge sind, werden auch alle benachbarten Kakteen rekursiv geerntet.

Ein Kaktus gilt als sortiert, wenn alle benachbarten Kakteen im `North` und `East` ausgewachsen und größer oder gleich groß sind und alle benachbarten Kakteen im `South` und `West` ausgewachsen und kleiner oder gleich groß sind.

Die Ernte breitet sich nur aus, wenn alle angrenzenden Kakteen ausgewachsen und sortiert sind.
Das bedeutet, wenn ein Quadrat aus gewachsenen Kakteen nach Größe sortiert ist und du einen Kaktus erntest, wird das gesamte Quadrat geerntet.

Ein ausgewachsener Kaktus erscheint braun, wenn er nicht sortiert ist. Sobald er sortiert ist, wird er wieder grün.

Du erhältst Kakteen in Höhe der Anzahl der geernteten Kakteen im Quadrat. Wenn du also `n` Kakteen gleichzeitig erntest, erhältst du `n**2` `Items.Cactus`.

Die Größe eines Kaktus kann mit `measure()` gemessen werden.
Es ist immer eine dieser Zahlen: `0,1,2,3,4,5,6,7,8,9`.

Du kannst auch eine Richtung in `measure(direction)` übergeben, um das benachbarte Feld in dieser Richtung von der Drohne aus zu messen.

Du kannst einen Kaktus mit seinem Nachbarn in jede Richtung mit dem `swap()`-Befehl tauschen.
`swap(direction)` tauscht das Objekt unter der Drohne mit dem Objekt ein Feld in der `direction` der Drohne.

## Beispiele
In jedem dieser Gitter sind alle Kakteen sortiert und die Ernte breitet sich über das gesamte Feld aus:
`3 4 5    3 3 3    1 2 3    1 5 9
2 3 4    2 2 2    1 2 3    1 3 8
1 2 3    1 1 1    1 2 3    1 3 4`

In diesem Gitter ist nur der untere linke Kaktus sortiert, was nicht ausreicht, damit es sich ausbreitet:
`1 5 3
4 9 7
3 3 2`

<spoiler=Hinweis 1 anzeigen>
Wenn die Reihen bereits sortiert sind, wird das Sortieren der Spalten die Reihen nicht unsortieren.
</spoiler>
<spoiler=Hinweis 2 anzeigen>
Wenn du mit Sortieralgorithmen nicht vertraut bist, solltest du sie vielleicht online nachschlagen und überlegen, welche für dieses Problem angepasst werden könnten. Bedenke, dass nicht alle funktionieren, da du nur benachbarte Kakteen tauschen kannst.
</spoiler>
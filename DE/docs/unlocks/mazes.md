# Labyrinthe
`Items.Weird_Substance` (seltsame Substanz), die man durch das [Düngen](docs/unlocks/fertilizer.md) von Pflanzen erhält, hat einen seltsamen Effekt auf Büsche. Wenn die Drohne über einem Busch ist und du `use_item(Items.Weird_Substance, amount)` aufrufst, wächst der Busch zu einem Labyrinth aus Hecken.
Die Größe des Labyrinths hängt von der Menge der verwendeten `Items.Weird_Substance` ab (dem zweiten Argument des `use_item()`-Aufrufs).
Ohne Labyrinth-Upgrades führt die Verwendung von `n` `Items.Weird_Substance` zu einem `n`x`n` Labyrinth. Jede Labyrinth-Upgrade-Stufe verdoppelt den Schatz, aber sie verdoppelt auch die benötigte Menge an `Items.Weird_Substance`. 
Um also ein Labyrinth in voller Feldgröße zu erstellen:

`plant(Entities.Bush)
substance = get_world_size() * 2**(num_unlocked(Unlocks.Mazes) - 1)
use_item(Items.Weird_Substance, substance)`


Aus irgendeinem Grund kann die Drohne nicht über die Hecken fliegen, obwohl sie nicht so hoch aussehen.

Irgendwo in der Hecke ist ein Schatz versteckt. Benutze `harvest()` auf den Schatz, um Gold in Höhe der Fläche des Labyrinths zu erhalten. (Zum Beispiel bringt ein 5x5 Labyrinth 25 Gold.)

Wenn du `harvest()` irgendwo anders benutzt, verschwindet das Labyrinth einfach.

`get_entity_type()` ist gleich `Entities.Treasure`, wenn die Drohne über dem Schatz ist, und `Entities.Hedge` überall sonst im Labyrinth.

Labyrinthe enthalten keine Schleifen, es sei denn, du verwendest das Labyrinth wieder (siehe unten, wie man ein Labyrinth wiederverwendet). Es gibt also keine Möglichkeit für die Drohne, an dieselbe Position zurückzukehren, ohne umzukehren.

Du kannst prüfen, ob es eine Mauer gibt, indem du versuchst, dich durch sie zu bewegen. 
`move()` gibt `True` zurück, wenn es erfolgreich war, andernfalls `False`.

Wenn du keine Ahnung hast, wie du zum Schatz kommst, schau dir Hinweis 1 an. Er zeigt dir, wie man ein solches Problem angeht.


Für eine zusätzliche Herausforderung kannst du das Labyrinth auch wiederverwenden, indem du dieselbe Menge an `Items.Weird_Substance` erneut auf den Schatz anwendest. 
Dies erhöht die Goldmenge im Schatz um ein ganzes Labyrinth und verschiebt ihn an eine zufällige Position im Labyrinth.

Die Verwendung von `measure()` auf einen Schatz gibt die Position, zu der er sich bewegen wird, als Tupel zurück.
`next_x, next_y = measure()`

Jedes Mal, wenn der Schatz bewegt wird, kann eine zufällige Mauer aus dem Labyrinth entfernt werden. Wiederverwendete Labyrinthe können also Schleifen enthalten.

Beachte, dass Schleifen im Labyrinth es viel schwieriger machen, weil es bedeutet, dass du an dieselbe Stelle zurückkehren kannst, ohne umzukehren.
Ein Labyrinth wiederzuverwenden gibt dir nicht mehr Gold, als einfach ein neues Labyrinth zu ernten und zu erzeugen.
Dies ist zu 100% eine zusätzliche Herausforderung, die du einfach überspringen kannst.
Es lohnt sich nur, wenn die zusätzlichen Informationen und die Abkürzungen dir helfen, das Labyrinth schneller zu lösen.

Dasselbe Labyrinth kann maximal 300 Mal gelöst werden. Das entspricht 299 Verschiebungen. Danach erhöht die Verwendung von seltsamer Substanz auf den Schatz das Gold darin nicht mehr und `measure()` gibt `None` zurück.

<spoiler=zeige Hinweis 1>Hier ist ein allgemeiner Ansatz, um das Problem zu lösen:

Erstelle ein Labyrinth und stell dir vor, du wärst die Drohne.

Überlege, wie du versuchen würdest, den Schatz zu finden, wenn du im Labyrinth wärst.

Schreibe deine Strategie Schritt für Schritt auf, sodass jemand anderes ihr folgen könnte, ohne nachzudenken.

Versuche nun, deine Schritte in Code zu übersetzen.
</spoiler>
<spoiler=zeige Hinweis 2>Solange es keine Schleifen gibt: Alle Mauern sind eigentlich nur eine große, zusammenhängende Mauer. Wenn du der Mauer folgst, wird sie dich durch das ganze Labyrinth führen.
Dieser Ansatz erfordert sehr wenig Code und du musst nicht verfolgen, wo du schon warst. Ungefähr 10 Zeilen Code sind alles, was du brauchst.</spoiler>
<spoiler=zeige Hinweis 3>Anstatt die Drohne in absoluten Richtungen wie Ost oder West zu bewegen, kann es sehr nützlich sein, die Drohne in relativen Richtungen wie „rechts abbiegen“ oder „links abbiegen“ zu bewegen. Dazu musst du verfolgen, in welche Richtung sich die Drohne gerade bewegt. Die Drohne dreht sich nie wirklich, aber du kannst trotzdem eine „virtuelle“ Drehung im Code beibehalten.
Der folgende Index-Trick ist dafür hilfreich:

`directions = [North, East, South, West]
index = 0`

Benutze `% 4`, um eine Drehung „im Kreis“ zu ermöglichen, sodass es nach `West` wieder zu `North` zurückkehrt.
`# rechts abbiegen
index = (index + 1) % 4`

`# links abbiegen
index = (index - 1) % 4

move(directions[index])`</spoiler>
<spoiler=zeige Hinweis 4>Wenn du es nicht lösen kannst, kannst du es dir immer einfach machen und es weniger effizient tun. 
Ein `1`x`1` Labyrinth zu lösen ist trivial.</spoiler>
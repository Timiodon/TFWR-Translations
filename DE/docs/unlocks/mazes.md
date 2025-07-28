# Labyrinthe
`Items.Weird_Substance`, das durch das [Düngen](docs/unlocks/fertilizer.md) von Pflanzen erhalten wird, hat eine seltsame Wirkung auf Büsche. Wenn sich die Drohne über einem Busch befindet und du `use_item(Items.Weird_Substance, amount)` aufrufst, wächst der Busch zu einem Labyrinth aus Hecken heran.
Die Größe des Labyrinths hängt von der Menge der verwendeten `Items.Weird_Substance` ab (dem zweiten Argument des `use_item()`-Aufrufs).
Ohne Labyrinth-Upgrades führt die Verwendung von `n` `Items.Weird_Substance` zu einem `n`x`n` großen Labyrinth. Jedes Labyrinth-Upgrade-Level verdoppelt den Schatz, verdoppelt aber auch die benötigte Menge an `Items.Weird_Substance`.
Um also ein Labyrinth in voller Feldgröße zu erstellen:

`plant(Entities.Bush)
n_substance = get_world_size() * 2**(num_unlocked(Unlocks.Mazes) - 1)
use_item(Items.Weird_Substance, n_substance)`


Aus irgendeinem Grund kann die Drohne nicht über die Hecken fliegen, obwohl sie nicht so hoch aussehen.

Irgendwo in der Hecke ist ein Schatz versteckt. Benutze `harvest()` auf dem Schatz, um Gold in Höhe der Fläche des Labyrinths zu erhalten. (Zum Beispiel ergibt ein 5x5-Labyrinth 25 Gold.)

Wenn du `harvest()` an einer anderen Stelle verwendest, verschwindet das Labyrinth einfach.

`get_entity_type()` ist gleich `Entities.Treasure`, wenn sich die Drohne über dem Schatz befindet, und `Entities.Hedge` überall sonst im Labyrinth.

Labyrinthe enthalten keine Schleifen, es sei denn, du verwendest das Labyrinth wieder (siehe unten, wie man ein Labyrinth wiederverwendet). Es gibt also keine Möglichkeit für die Drohne, ohne zurückzugehen wieder an derselben Position zu landen.

Du kannst prüfen, ob eine Wand da ist, indem du versuchst, durch sie hindurch zu bewegen.
`move()` gibt `True` zurück, wenn es erfolgreich war, und andernfalls `False`.

Wenn du keine Ahnung hast, wie du zum Schatz kommst, schau dir Hinweis 1 an. Er zeigt dir, wie man ein solches Problem angeht.


Für eine zusätzliche Herausforderung kannst du das Labyrinth auch wiederverwenden, indem du dieselbe Menge an `Items.Weird_Substance` erneut auf den Schatz anwendest.
Dies erhöht die Goldmenge im Schatz um ein volles Labyrinth und verschiebt ihn an eine zufällige Position im Labyrinth.

Die Verwendung von `measure()` auf einem Schatz gibt die Position, zu der er sich bewegen wird, als Tupel zurück.
`next_x, next_y = measure()`

Jedes Mal, wenn der Schatz bewegt wird, kann eine zufällige Wand aus dem Labyrinth entfernt werden. Wiederverwendete Labyrinthe können also Schleifen enthalten.

Beachte, dass Schleifen im Labyrinth es viel schwieriger machen, weil es bedeutet, dass du wieder an denselben Ort gelangen kannst, ohne zurückzugehen.
Das Wiederverwenden eines Labyrinths gibt dir nicht mehr Gold als das Ernten und Spawnen eines neuen Labyrinths.
Dies ist zu 100% eine zusätzliche Herausforderung, die du einfach überspringen kannst.
Es lohnt sich nur, wenn dir die zusätzlichen Informationen und die Abkürzungen helfen, das Labyrinth schneller zu lösen.

Dasselbe Labyrinth kann maximal 300 Mal gelöst werden. Dies entspricht 299 Umzügen. Danach erhöht die Verwendung von seltsamer Substanz auf dem Schatz das Gold darin nicht mehr und `measure()` gibt `None` zurück.

<spoiler=Hinweis 1 anzeigen>Hier ist ein allgemeiner Ansatz zur Lösung des Problems:

Erstelle ein Labyrinth und stell dir vor, du wärst die Drohne.

Überlege, wie du versuchen würdest, den Schatz zu finden, wenn du im Labyrinth wärst.

Schreibe deine Strategie Schritt für Schritt auf, damit jemand anderes sie befolgen könnte, ohne nachzudenken.

Versuche nun, deine Schritte in Code zu übersetzen.
</spoiler>
<spoiler=Hinweis 2 anzeigen>Solange es keine Schleifen gibt: Alle Wände sind wirklich nur eine große zusammenhängende Wand. Wenn du der Wand folgst, führt sie dich durch das ganze Labyrinth.
Dieser Ansatz erfordert sehr wenig Code und du musst nicht verfolgen, wo du schon warst. Ungefähr 10 Zeilen Code sind alles, was du brauchst.</spoiler>
<spoiler=Hinweis 3 anzeigen>Anstatt die Drohne in absolute Richtungen wie Ost oder West zu bewegen, kann es sehr nützlich sein, die Drohne in relative Richtungen wie "rechts abbiegen" oder "links abbiegen" zu bewegen. Dazu musst du verfolgen, in welche Richtung sich die Drohne gerade bewegt. Die Drohne dreht sich nie wirklich, aber du kannst trotzdem eine "virtuelle" Drehung im Code beibehalten.
Der folgende Index-Trick ist dafür hilfreich:

`directions = [North, East, South, West]
index = 0`

Verwende `% 4`, damit sie sich "im Kreis" drehen kann, so dass sie nach `West` wieder zu `North` zurückkehrt.
`# rechts abbiegen
index = (index + 1) % 4`

`# links abbiegen
index = (index - 1) % 4

move(directions[index])`</spoiler>
<spoiler=Hinweis 4 anzeigen>Wenn du es nicht lösen kannst, kannst du dir das Leben immer leicht machen und es weniger effizient tun.
Ein `1`x`1`-Labyrinth zu lösen ist trivial.</spoiler>
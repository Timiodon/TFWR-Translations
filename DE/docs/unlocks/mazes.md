# Labyrinthe
`Items.Weird_Substance`, das durch das [Düngen](docs/unlocks/fertilizer.md) von Pflanzen erhalten wird, hat eine seltsame Wirkung auf Büsche. Wenn die Drohne über einem Busch ist und du `use_item(Items.Weird_Substance, amount)` aufrufst, wächst der Busch zu einem Labyrinth aus Hecken heran.
Die Größe des Labyrinths hängt von der Menge der verwendeten `Items.Weird_Substance` ab (das zweite Argument des `use_item()`-Aufrufs).
Ohne Labyrinth-Upgrades führt die Verwendung von `n` `Items.Weird_Substance` zu einem `n`x`n`-Labyrinth. Jede Labyrinth-Upgrade-Stufe verdoppelt den Schatz, aber sie verdoppelt auch die benötigte Menge an `Items.Weird_Substance`.
Um also ein Labyrinth in voller Feldgröße zu erstellen:

`plant(Entities.Bush)
substance = get_world_size() * 2**(num_unlocked(Unlocks.Mazes) - 1)
use_item(Items.Weird_Substance, substance)`


Aus irgendeinem Grund kann die Drohne nicht über die Hecken fliegen, obwohl sie nicht so hoch aussehen.

Irgendwo in der Hecke ist ein Schatz versteckt. Verwende `harvest()` auf dem Schatz, um Gold in Höhe der Fläche des Labyrinths zu erhalten. (Zum Beispiel wird ein 5x5-Labyrinth 25 Gold einbringen.)

Wenn du `harvest()` irgendwo anders verwendest, verschwindet das Labyrinth einfach.

`get_entity_type()` ist gleich `Entities.Treasure`, wenn die Drohne über dem Schatz ist, und `Entities.Hedge` überall sonst im Labyrinth.

Labyrinthe enthalten keine Schleifen, es sei denn, du verwendest das Labyrinth wieder (siehe unten, wie man ein Labyrinth wiederverwendet). Es gibt also keine Möglichkeit für die Drohne, wieder an derselben Position zu landen, ohne zurückzugehen.

Du kannst prüfen, ob eine Wand da ist, indem du versuchst, dich durch sie hindurch zu bewegen.
`move()` gibt `True` zurück, wenn es erfolgreich war, und `False` andernfalls.

`can_move()` kann verwendet werden, um zu prüfen, ob eine Wand da ist, ohne sich zu bewegen.

Wenn du keine Ahnung hast, wie du zum Schatz kommst, schau dir Hinweis 1 an. Er zeigt dir, wie man ein solches Problem angeht.

Die Verwendung von `measure()` irgendwo im Labyrinth gibt die Position des Schatzes zurück.
`x, y = measure()`

Für eine zusätzliche Herausforderung kannst du das Labyrinth auch wiederverwenden, indem du dieselbe Menge an `Items.Weird_Substance` erneut auf den Schatz anwendest.
Dies erhöht die Menge an Gold im Schatz um ein volles Labyrinth und verschiebt es an eine zufällige Position im Labyrinth.

Jedes Mal, wenn der Schatz bewegt wird, können einige der Wände des Labyrinths zufällig entfernt werden. Wiederverwendete Labyrinthe können also Schleifen enthalten.

Beachte, dass Schleifen im Labyrinth es viel schwieriger machen, da es bedeutet, dass du wieder an denselben Ort gelangen kannst, ohne zurückzugehen.
Ein Labyrinth wiederzuverwenden bringt nicht mehr Gold, als es einfach zu ernten und ein neues zu erschaffen.
Dies ist zu 100% eine zusätzliche Herausforderung, die du einfach überspringen kannst.
Es lohnt sich nur, wenn die zusätzlichen Informationen und die Abkürzungen dir helfen, das Labyrinth schneller zu lösen.

Dasselbe Labyrinth kann maximal 300 Mal gelöst werden. Dies entspricht 299 Verlagerungen. Danach erhöht die Verwendung von seltsamer Substanz auf dem Schatz das Gold darin nicht mehr und er wird sich nicht mehr bewegen.

<spoiler=zeige Hinweis 1>Hier ist ein allgemeiner Ansatz zur Lösung des Problems:

Erstelle ein Labyrinth und stelle dir vor, du wärst die Drohne.

Überlege, wie du versuchen würdest, den Schatz zu finden, wenn du im Labyrinth wärst.

Schreibe deine Strategie Schritt für Schritt auf, damit jemand anderes sie ohne nachzudenken befolgen könnte.

Versuche nun, deine Schritte in Code zu übersetzen.
</spoiler>
<spoiler=zeige Hinweis 2>Solange es keine Schleifen gibt: Alle Wände sind eigentlich nur eine große zusammenhängende Wand. Wenn du der Wand folgst, führt sie dich durch das ganze Labyrinth.
Dieser Ansatz erfordert sehr wenig Code und du musst nicht verfolgen, wo du schon warst. Ungefähr 10 Zeilen Code sind alles, was du brauchst.</spoiler>
<spoiler=zeige Hinweis 3>Anstatt die Drohne in absolute Richtungen wie Ost oder West zu bewegen, kann es sehr nützlich sein, die Drohne in relative Richtungen wie "rechts abbiegen" oder "links abbiegen" zu bewegen. Dazu musst du verfolgen, in welche Richtung sich die Drohne gerade bewegt. Die Drohne dreht sich nie wirklich, aber du kannst trotzdem eine "virtuelle" Drehung im Code beibehalten.
Der folgende Index-Trick ist dafür hilfreich:

`directions = [North, East, South, West]
index = 0`

Verwende `% 4`, damit sie sich "im Kreis" drehen kann, so dass sie nach `West` wieder zu `North` zurückkehrt.
`# rechts abbiegen
index = (index + 1) % 4`

`# links abbiegen
index = (index - 1) % 4

move(directions[index])`</spoiler>
<spoiler=zeige Hinweis 4>Wenn du es nicht lösen kannst, kannst du es dir immer einfach machen und es weniger effizient tun.
Ein `1`x`1`-Labyrinth zu lösen ist trivial.</spoiler>
# Labyrinthe
`Items.Weird_Substance`, das man durch [Düngen](docs/unlocks/fertilizer.md) von Pflanzen erhält, hat eine seltsame Wirkung auf Büsche. Wenn die Drohne über einem Busch schwebt und du `use_item(Items.Weird_Substance, amount)` aufrufst, verwandelt sich der Busch in ein Labyrinth aus Hecken. Die Größe des Labyrinths hängt von der Menge des verwendeten `Items.Weird_Substance` ab (das zweite Argument des `use_item()`-Aufrufs). Ohne Labyrinth-Upgrades ergibt die Verwendung von `n` `Items.Weird_Substance` ein `n`x`n` Labyrinth. Jede Stufe des Labyrinth-Upgrades verdoppelt den Schatz, aber sie verdoppelt auch die benötigte Menge an `Items.Weird_Substance`. Um ein vollständiges Feldlabyrinth zu erstellen:

`plant(Entities.Bush)
n_substance = get_world_size() * 2**(num_unlocked(Unlocks.Mazes) - 1)
use_item(Items.Weird_Substance, n_substance)`

Aus irgendeinem Grund kann die Drohne nicht über die Hecken fliegen, obwohl sie nicht so hoch aussehen.

Es ist ein Schatz irgendwo in der Hecke versteckt. Verwende `harvest()` auf dem Schatz, um Gold in Höhe der Fläche des Labyrinths zu erhalten. (Zum Beispiel, ein 5x5 Labyrinth bringt 25 Gold.)

Wenn du `harvest()` an einer anderen Stelle verwendest, verschwindet das Labyrinth einfach.

`get_entity_type()` ist gleich `Entities.Treasure`, wenn die Drohne über dem Schatz ist, und `Entities.Hedge` überall sonst im Labyrinth.

Labyrinthe enthalten keine Schleifen, es sei denn, du verwendest das Labyrinth erneut (siehe unten, wie man ein Labyrinth wiederverwendet). So gibt es keine Möglichkeit für die Drohne, wieder an dieselbe Position zu gelangen, ohne zurückzugehen.

Du kannst überprüfen, ob eine Wand vorhanden ist, indem du versuchst, durch sie hindurchzugehen. `move()` gibt `True` zurück, wenn es erfolgreich war, und `False` andernfalls.

Wenn du keine Ahnung hast, wie du zum Schatz gelangen sollst, schau dir Hinweis 1 an. Er zeigt dir, wie du ein solches Problem angehen kannst.

Für eine zusätzliche Herausforderung kannst du das Labyrinth auch wiederverwenden, indem du die gleiche Menge an `Items.Weird_Substance` erneut auf den Schatz verwendest. Dies erhöht die Goldmenge im Schatz um ein ganzes Labyrinth und bewegt es an eine zufällige Position im Labyrinth.

Die Verwendung von `measure()` auf einem Schatz gibt die Position zurück, zu der er sich bewegt, als ein Tupel.
`next_x, next_y = measure()`

Jedes Mal, wenn der Schatz bewegt wird, kann eine zufällige Wand aus dem Labyrinth entfernt werden. So können wiederverwendete Labyrinthe Schleifen enthalten.

Beachte, dass Schleifen im Labyrinth es erheblich schwieriger machen, weil sie bedeuten, dass du wieder zur gleichen Position gelangen kannst, ohne zurückzugehen.
Ein Labyrinth wiederzuverwenden, gibt dir nicht mehr Gold als einfach zu ernten und ein neues Labyrinth zu erzeugen.
Es ist ein 100% zusätzliches Herausforderungselement, das du einfach überspringen kannst.
Es lohnt sich nur, wenn dir die zusätzlichen Informationen und die Abkürzungen helfen, das Labyrinth schneller zu lösen.

Das gleiche Labyrinth kann maximal 300 Mal gelöst werden. Das entspricht 299 Verlagerungen. Danach wird die Verwendung von seltsamer Substanz auf dem Schatz das Gold darin nicht mehr erhöhen und `measure()` wird `None` zurückgeben.

<spoiler=show hint 1>Hier ist ein allgemeiner Ansatz zur Lösung des Problems:

Erstelle ein Labyrinth und stelle dir vor, du bist die Drohne.

Überlege, wie du versuchen würdest, den Schatz zu finden, wenn du im Labyrinth wärst.

Schreibe deine Strategie Schritt für Schritt auf, damit jemand anderes sie ohne Überlegung folgen kann.

Versuche nun, deine Schritte in Code zu übersetzen.
</spoiler>
<spoiler=show hint 2>Solange es keine Schleifen gibt: Alle Wände sind wirklich nur eine große verbundene Wand. Wenn du der Wand folgst, wird sie dich durch das ganze Labyrinth führen.
Dieser Ansatz erfordert sehr wenig Code und du musst nicht verfolgen, wo du schon warst. Ungefähr 10 Zeilen Code sind alles, was du brauchst.</spoiler>
<spoiler=show hint 3>Anstatt die Drohne in absoluten Richtungen wie Osten oder Westen zu bewegen, kann es sehr nützlich sein, die Drohne in relativen Richtungen wie "nach rechts drehen" oder "nach links drehen" zu bewegen. Um dies zu tun, musst du verfolgen, in welche Richtung die Drohne sich gerade bewegt. Die Drohne dreht sich nie wirklich, aber du kannst trotzdem eine "virtuelle" Drehung im Code beibehalten.
Der folgende Index-Trick ist hilfreich dafür:

`directions = [North, East, South, West]
index = 0`

Verwende `% 4`, um eine Drehung "im Kreis herum" zu ermöglichen, so dass nach `West` zurück zu `North` gelangt wird.
`# nach rechts drehen
index = (index + 1) % 4`

`# nach links drehen
index = (index - 1) % 4

move(directions[index])`</spoiler>
<spoiler=show hint 4>Wenn du es nicht lösen kannst, kannst du es dir immer leicht machen und es weniger effizient gestalten. 
Ein `1`x`1` Labyrinth zu lösen, ist trivial.</spoiler>
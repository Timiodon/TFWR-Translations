# Labyrinthe
`Items.Weird_Substance`, das man durch [Düngen](docs/unlocks/fertilizer.md) von Pflanzen erhält, hat eine seltsame Wirkung auf Büsche. Wenn die Drohne über einem Busch schwebt und du `use_item(Items.Weird_Substance, amount)` aufrufst, verwandelt sich der Busch in ein Labyrinth aus Hecken. Die Größe des Labyrinths hängt von der Menge des verwendeten `Items.Weird_Substance` ab (das zweite Argument des `use_item()`-Aufrufs). Ohne Labyrinth-Upgrades ergibt `n` `Items.Weird_Substance` ein `n`x`n` Labyrinth. Für jedes Labyrinth-Upgrade-Level brauchst du ein zusätzliches `n` `Items.Weird_Substance`, um denselben Effekt zu erzielen. 
Um ein vollständiges Feldlabyrinth zu erstellen:

`plant(Entities.Bush)
n_substance = get_world_size() * num_unlocked(Unlocks.Mazes)
use_item(Items.Weird_Substance, n_substance)`

Aus irgendeinem Grund kann die Drohne nicht über die Hecken fliegen, obwohl sie nicht so hoch aussehen.

Im Labyrinth ist irgendwo ein Schatz versteckt. Verwende `harvest()` auf dem Schatz, um Gold in Höhe der Fläche des Labyrinths zu erhalten. (Zum Beispiel ergibt ein 5x5 Labyrinth 25 Gold.)

Wenn du `harvest()` an einer anderen Stelle verwendest, verschwindet das Labyrinth einfach.

`get_entity_type()` ist gleich `Entities.Treasure`, wenn die Drohne über dem Schatz ist, und `Entities.Hedge` überall sonst im Labyrinth.

Labyrinthe enthalten keine Schleifen, es sei denn, du verwendest das Labyrinth (siehe unten, wie du ein Labyrinth neu verwendest). Es gibt also keine Möglichkeit, dass die Drohne wieder an derselben Position landet, ohne zurückzugehen.

Du kannst prüfen, ob eine Wand vorhanden ist, indem du versuchst, durch sie hindurchzugehen.
`move()` gibt `True` zurück, wenn es erfolgreich war, und `False` andernfalls.

Wenn du keine Ahnung hast, wie du zum Schatz gelangst, schau dir Hinweis 1 an. Er zeigt dir, wie du ein solches Problem angehen kannst.

Für eine zusätzliche Herausforderung kannst du das Labyrinth erneut verwenden, indem du die gleiche Menge an `Items.Weird_Substance` erneut auf den Schatz anwendest. Dies wird die Goldmenge im Schatz um ein vollständiges Labyrinth erhöhen und es an eine zufällige Position im Labyrinth bewegen.

Wenn du `measure()` auf einem Schatz verwendest, wird die Position, an die er sich bewegt, als Tupel zurückgegeben.
`next_x, next_y = measure()`

Jedes Mal, wenn der Schatz bewegt wird, kann eine zufällige Wand aus dem Labyrinth entfernt werden. So können wiederverwendete Labyrinthe Schleifen enthalten.

Beachte, dass Schleifen im Labyrinth es viel schwieriger machen, da sie bedeuten, dass du erneut an denselben Ort gelangen kannst, ohne zurückzugehen. Ein Labyrinth erneut zu verwenden, bringt nicht mehr Gold ein, als es einfach zu ernten und ein neues Labyrinth zu erstellen. Das ist zu 100% eine zusätzliche Herausforderung, die du einfach überspringen kannst. Es lohnt sich nur, wenn dir die zusätzlichen Informationen und Abkürzungen helfen, das Labyrinth schneller zu lösen.

Dasselbe Labyrinth kann maximal 300 Mal gelöst werden, was 299 Neuplatzierungen entspricht. Danach wird die Verwendung von komischem Stoff auf dem Schatz das Gold darin nicht weiter erhöhen und `measure()` wird `None` zurückgeben.

<spoiler=zeigen Hinweis 1>Hier ist ein allgemeiner Ansatz, um das Problem zu lösen:

Erstelle ein Labyrinth und stelle dir vor, du bist die Drohne.

Überlege, wie du versuchen würdest, den Schatz zu finden, wenn du im Labyrinth wärst.

Schreibe deine Strategie Schritt für Schritt auf, damit jemand anderes sie ohne weiteres Nachdenken befolgen kann.

Versuche nun, deine Schritte in Code zu übersetzen.
</spoiler>
<spoiler=zeigen Hinweis 2>Solange es keine Schleifen gibt: Alle Wände sind wirklich nur eine große zusammenhängende Wand. Wenn du der Wand folgst, wird sie dich durch das ganze Labyrinth führen. Dieser Ansatz erfordert sehr wenig Code und du musst nicht verfolgen, wo du bereits gewesen bist. Ungefähr 10 Zeilen Code sind alles, was du brauchst.</spoiler>
<spoiler=zeigen Hinweis 3>Anstatt die Drohne in absoluten Richtungen wie Osten oder Westen zu bewegen, kann es sehr nützlich sein, die Drohne in relativen Richtungen wie „nach rechts drehen“ oder „nach links drehen“ zu bewegen. Dazu musst du verfolgen, in welche Richtung die Drohne gerade bewegt wird. Die Drohne dreht sich eigentlich nie, aber du kannst trotzdem eine "virtuelle" Drehung im Code beibehalten. Der folgende Index-Trick ist hilfreich dafür:

`directions = [North, East, South, West]
index = 0`

Verwende `% 4`, um es "um den Kreis" rotieren zu lassen, sodass es nach `West` wieder zu `North` wird.
`# nach rechts drehen
index = (index + 1) % 4`

`# nach links drehen
index = (index - 1) % 4

move(directions[index])`</spoiler>
<spoiler=zeigen Hinweis 4>Wenn du es nicht lösen kannst, kannst du es dir immer einfach machen und es weniger effizient erledigen. Ein `1`x`1` Labyrinth zu lösen, ist trivial.</spoiler>
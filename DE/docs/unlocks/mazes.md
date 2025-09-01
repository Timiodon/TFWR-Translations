# Labyrinthe
`Items.Weird_Substance`, das man durch das [Düngen](docs/unlocks/fertilizer.md) von Pflanzen erhält, hat eine seltsame Wirkung auf Büsche. Wenn sich die Drohne über einem Busch befindet und du `use_item(Items.Weird_Substance, amount)` aufrufst, wächst der Busch zu einem Labyrinth aus Hecken heran.
Die Größe des Labyrinths hängt von der Menge an `Items.Weird_Substance` ab, die verwendet wird (das zweite Argument des `use_item()`-Aufrufs).
Ohne Labyrinth-Upgrades führt die Verwendung von `n` `Items.Weird_Substance` zu einem `n`x`n`-Labyrinth. Jedes Labyrinth-Upgrade-Level verdoppelt den Schatz, aber es verdoppelt auch die benötigte Menge an `Items.Weird_Substance`. 
Um ein ganzes Feld als Labyrinth zu erstellen:

`plant(Entities.Bush)
substance = get_world_size() * 2**(num_unlocked(Unlocks.Mazes) - 1)
use_item(Items.Weird_Substance, substance)`


Aus irgendeinem Grund kann die Drohne nicht über die Hecken fliegen, obwohl sie nicht so hoch aussehen.

Irgendwo in der Hecke ist ein Schatz versteckt. Benutze `harvest()` auf dem Schatz, um Gold im Wert der Fläche des Labyrinths zu erhalten. (Zum Beispiel ergibt ein 5x5-Labyrinth 25 Gold.)

Wenn du `harvest()` an einer anderen Stelle verwendest, verschwindet das Labyrinth einfach.

`get_entity_type()` ist gleich `Entities.Treasure`, wenn die Drohne über dem Schatz ist, und `Entities.Hedge` überall sonst im Labyrinth.

Labyrinthe enthalten keine Schleifen, es sei denn, du verwendest das Labyrinth wieder (siehe unten, wie man ein Labyrinth wiederverwendet). Es gibt also keine Möglichkeit für die Drohne, ohne zurückzugehen wieder an derselben Position zu landen.

Du kannst überprüfen, ob eine Wand da ist, indem du versuchst, dich hindurchzubewegen. 
`move()` gibt `True` zurück, wenn es erfolgreich war, und andernfalls `False`.

`can_move()` kann verwendet werden, um zu überprüfen, ob eine Wand da ist, ohne sich zu bewegen.

Wenn du keine Ahnung hast, wie du zum Schatz kommst, schau dir Hinweis 1 an. Er zeigt dir, wie man ein solches Problem angeht.

Die Verwendung von `measure()` irgendwo im Labyrinth gibt die Position des Schatzes zurück.
`x, y = measure()`

Für eine zusätzliche Herausforderung kannst du das Labyrinth auch wiederverwenden, indem du die gleiche Menge `Items.Weird_Substance` erneut auf den Schatz anwendest. 
Dies erhöht die Goldmenge im Schatz um den Wert eines ganzen Labyrinths und verschiebt ihn an eine zufällige Position im Labyrinth.

Jedes Mal, wenn der Schatz bewegt wird, kann eine zufällige Wand aus dem Labyrinth entfernt werden. Wiederverwendete Labyrinthe können also Schleifen enthalten.

Beachte, dass Schleifen im Labyrinth es viel schwieriger machen, weil es bedeutet, dass du wieder an denselben Ort gelangen kannst, ohne zurückzugehen.
Ein Labyrinth wiederzuverwenden gibt dir nicht mehr Gold, als einfach ein neues Labyrinth zu ernten und zu erstellen.
Dies ist zu 100% eine zusätzliche Herausforderung, die du einfach überspringen kannst.
Es lohnt sich nur, wenn dir die zusätzlichen Informationen und die Abkürzungen helfen, das Labyrinth schneller zu lösen.

Dasselbe Labyrinth kann maximal 300 Mal gelöst werden. Dies entspricht 299 Verlagerungen. Danach wird die Verwendung von seltsamer Substanz auf dem Schatz das Gold darin nicht mehr erhöhen und `measure()` wird `None` zurückgeben.

<spoiler=zeige Hinweis 1>Hier ist ein allgemeiner Ansatz, um das Problem zu lösen:

Erstelle ein Labyrinth und stell dir vor, du wärst die Drohne.

Überlege dir, wie du versuchen würdest, den Schatz zu finden, wenn du im Labyrinth wärst.

Schreibe deine Strategie Schritt für Schritt auf, damit jemand anderes sie ohne nachzudenken befolgen kann.

Versuche nun, deine Schritte in Code zu übersetzen.
</spoiler>
<spoiler=zeige Hinweis 2>Solange es keine Schleifen gibt: Alle Wände sind in Wirklichkeit nur eine einzige große zusammenhängende Wand. Wenn du der Wand folgst, wird sie dich durch das ganze Labyrinth führen.
Dieser Ansatz erfordert sehr wenig Code und du musst nicht verfolgen, wo du schon warst. Ungefähr 10 Zeilen Code sind alles, was du brauchst.</spoiler>
<spoiler=zeige Hinweis 3>Anstatt die Drohne in absoluten Richtungen wie Ost oder West zu bewegen, kann es sehr nützlich sein, die Drohne in relativen Richtungen wie "rechts abbiegen" oder "links abbiegen" zu bewegen. Dazu musst du verfolgen, in welche Richtung sich die Drohne gerade bewegt. Die Drohne dreht sich nie wirklich, aber du kannst trotzdem eine "virtuelle" Drehung im Code beibehalten.
Der folgende Index-Trick ist dafür hilfreich:

`directions = [North, East, South, West]
index = 0`

Benutze `% 4`, damit es sich "im Kreis drehen" kann, sodass es nach `West` wieder zu `North` zurückkehrt.
`# rechts abbiegen
index = (index + 1) % 4`

`# links abbiegen
index = (index - 1) % 4

move(directions[index])`</spoiler>
<spoiler=zeige Hinweis 4>Wenn du es nicht lösen kannst, kannst du es dir immer leicht machen und es weniger effizient tun. 
Ein `1`x`1`-Labyrinth zu lösen ist trivial.</spoiler>
[<- Dünger](docs/unlocks/fertilizer.md) <right>[Mega-Farm ->](docs/unlocks/megafarm.md)
---
# Labyrinthe
`Items.Weird_Substance` hat eine seltsame Wirkung auf Büsche. Befindet sich die Drohne über einem Busch und rufst du `use_item(Items.Weird_Substance, amount)` auf, wächst der Busch zu einem Heckenlabyrinth heran.
Die Größe des Labyrinths hängt von der Menge der verwendeten `Items.Weird_Substance` ab (das zweite Argument des `use_item()`-Aufrufs).
Ohne Labyrinth-Upgrades führt die Verwendung von `n` `Items.Weird_Substance` zu einem `n`x`n`-Labyrinth. Jede Labyrinth-Upgrade-Stufe verdoppelt den Schatz, aber sie verdoppelt auch die benötigte Menge an `Items.Weird_Substance`.
Um also ein Labyrinth in voller Feldgröße zu erstellen:

{{codeexample 
{
    "camera_position": {"x": -1, "y": 2.4, "z": 5},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [{"item": "weird_substance", "n": 10}],
    "world_size": {"x": 4, "y": 4},
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 1,
    "seed": -1,
    "exclude_unlocks": ["watering"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
plant(Entities.Bush)
size = get_world_size()
substance = size * 2**(num_unlocked(Unlocks.Mazes) - 1)
use_item(Items.Weird_Substance, substance)
}}


Aus irgendeinem Grund kann die Drohne nicht über die Hecken fliegen, obwohl sie nicht so hoch aussehen.

Irgendwo im Labyrinth ist ein Schatz versteckt. Verwende `harvest()` beim Schatz, um eine Goldmenge zu erhalten, die der Fläche des Labyrinths entspricht. Ein 5x5 großes Labyrinth liefert beispielsweise 25 Gold.

Wenn du `harvest()` irgendwo anders verwendest, verschwindet das Labyrinth einfach.

`get_entity_type()` ist gleich `Entities.Treasure`, wenn die Drohne über dem Schatz ist, und `Entities.Hedge` überall sonst im Labyrinth.

Labyrinthe enthalten keine Schleifen, es sei denn, du verwendest das Labyrinth wieder (siehe unten, wie man ein Labyrinth wiederverwendet). Es gibt also keine Möglichkeit für die Drohne, wieder an derselben Position zu landen, ohne zurückzugehen.

Du kannst prüfen, ob eine Wand da ist, indem du versuchst, dich durch sie hindurch zu bewegen.
`move()` gibt `True` zurück, wenn es erfolgreich war, und `False` andernfalls.

`can_move()` kann verwendet werden, um zu prüfen, ob eine Wand da ist, ohne sich zu bewegen.

{{codeexample 
{
    "camera_position": {"x": -1, "y": 2.4, "z": 5},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "items": [{"item": "weird_substance", "n": 10}],
    "world_size": {"x": 4, "y": 4},
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 100,
    "seed": 1,
    "exclude_unlocks": ["watering"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
move(East)
plant(Entities.Bush)
size = get_world_size()
substance = size * 2**(num_unlocked(Unlocks.Mazes) - 1)
use_item(Items.Weird_Substance, substance)
#CODE
quick_print(
    can_move(North), 
    can_move(East), 
    can_move(South), 
    can_move(West)
)
if move(North) and get_entity_type() == Entities.Treasure:
    harvest()
}}

Wenn du keine Ahnung hast, wie du zum Schatz kommst, schau dir Hinweis 1 an. Er zeigt dir, wie man ein solches Problem angeht.

Die Verwendung von `measure()` irgendwo im Labyrinth gibt die Position des Schatzes zurück.
`x, y = measure()`

Für eine zusätzliche Herausforderung kannst du das Labyrinth auch wiederverwenden, indem du dieselbe Menge an `Items.Weird_Substance` erneut auf den Schatz anwendest.
Dies sammelt den Schatz ein und erzeugt einen neuen Schatz an einer zufälligen Position im Labyrinth.

Jedes Mal, wenn der Schatz bewegt wird, können einige der Wände des Labyrinths zufällig entfernt werden. Wiederverwendete Labyrinthe können also Schleifen enthalten.

Beachte, dass Schleifen im Labyrinth es viel schwieriger machen, da es bedeutet, dass du wieder an denselben Ort gelangen kannst, ohne zurückzugehen.
Ein Labyrinth wiederzuverwenden bringt nicht mehr Gold, als es einfach zu ernten und ein neues zu erschaffen.
Dies ist zu 100% eine zusätzliche Herausforderung, die du einfach überspringen kannst.
Es lohnt sich nur, wenn die zusätzlichen Informationen und die Abkürzungen dir helfen, das Labyrinth schneller zu lösen.

Der Schatz kann bis zu 300 Mal verschoben werden. Danach erhältst du durch die Verwendung von seltsamer Substanz auf dem Schatz kein Gold mehr und der Schatz wird nicht mehr verschoben.

<spoiler=zeige Hinweis 1>
Hier ist ein allgemeiner Ansatz zur Lösung des Problems:

Erstelle ein Labyrinth und stelle dir vor, du wärst die Drohne.

Überlege, wie du versuchen würdest, den Schatz zu finden, wenn du im Labyrinth wärst.

Schreibe deine Strategie Schritt für Schritt auf, damit jemand anderes sie ohne nachzudenken befolgen könnte.

Versuche nun, deine Schritte in Code zu übersetzen.
</spoiler>
<spoiler=zeige Hinweis 2>
Solange es keine Schleifen gibt: Alle Wände sind eigentlich nur eine große zusammenhängende Wand. Wenn du der Wand folgst, führt sie dich durch das ganze Labyrinth.
Dieser Ansatz erfordert sehr wenig Code und du musst nicht nachverfolgen, wo du bereits warst. Etwa 10 Zeilen Code sind alles, was du dafür brauchst.
{{codeexample 
{
    "camera_position": {"x": -1, "y": 2.4, "z": 5},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": false,
    "show_inventory": true,
    "show_output": true,
    "collapsing": false,
    "autoplay": true,
    "items": [{"item": "weird_substance", "n": 10}],
    "world_size": {"x": 4, "y": 4},
    "execution_speed": 2,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 1,
    "seed": -1,
    "exclude_unlocks": ["watering"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
plant(Entities.Bush)
size = get_world_size()
substance = size * 2**(num_unlocked(Unlocks.Mazes) - 1)
use_item(Items.Weird_Substance, substance)
#CODE
directions = [North, East, South, West]
index = 0
while get_entity_type() != Entities.Treasure:
    index = (index - 1) % 4
    for _ in range(4):
        if move(directions[index]):
            break
        index = (index + 1) % 4
do_a_flip()
harvest()
}}
</spoiler>
<spoiler=zeige Hinweis 3>
Anstatt die Drohne in absolute Richtungen wie Ost oder West zu bewegen, kann es sehr nützlich sein, die Drohne in relative Richtungen wie "rechts abbiegen" oder "links abbiegen" zu bewegen. Dazu musst du verfolgen, in welche Richtung sich die Drohne gerade bewegt. Die Drohne dreht sich nie wirklich, aber du kannst trotzdem eine "virtuelle" Drehung im Code beibehalten.
Der folgende Index-Trick ist dafür hilfreich:

{{codeexample 
{
    "camera_position": {"x": -1, "y": 1.8, "z": 5},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "items": [{"item": "weird_substance", "n": 10}],
    "world_size": {"x": 3, "y": 3},
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 1,
    "exclude_unlocks": ["watering"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
directions = [North, East, South, West]
index = 0
move(directions[index])

#nach rechts drehen
index = (index + 1) % 4
move(directions[index])

#nach links drehen
index = (index - 1) % 4
move(directions[index])
}}


Mit `% 4` kann sich die Richtung „im Kreis drehen“, sodass `3 (West) + 1` wieder `0 (North)` ergibt, weil `4 % 4 == 0` und `-1 % 4 == 3` gilt.</spoiler>
<spoiler=zeige Hinweis 4>
Wenn du es nicht lösen kannst, kannst du es dir immer einfach machen und es weniger effizient tun.
Ein `1`x`1`-Labyrinth zu lösen ist ganz einfach.</spoiler>

---

[Statistiken](docs/stats.md)      [Listen](docs/scripting/lists.md)      [Dictionaries](docs/scripting/dicts.md)      [Tupel](docs/scripting/tuples.md)

[harvest()](functions/harvest)      [plant()](functions/plant)      [can_move()](functions/can_move)      [move()](functions/move)      [use_item()](functions/use_item)

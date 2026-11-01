[<- Bergbau](docs/unlocks/mining.md)
---
# Unterirdische Sinne
Statten wir deine Drohne mit einigen Sensoren aus, damit sie sich unter der Erde zurechtfindet.

## Z-Position
Du kannst jetzt mit `get_pos_z()` die Höhe der Drohne abfragen. Sie beginnt bei 0 und wird negativ, während die Drohne nach unten fliegt.

{{codeexample 
{
    "camera_position": {"x": -1.5, "y": 0, "z": 10},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "exclude_unlocks": ["watering", "fertilizer"],
    "items": [],
    "world_size": {"x": 5, "y": 5},
    "execution_speed": 2,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 1
}
#SETUP
move(North)
move(North)
move(East)
move(East)
#CODE
print(get_pos_z())
dig()
dig()
dig()
print(get_pos_z())
}}

## Bodentyp
`get_ground_type()` gibt die Art des Bodens unter der Drohne zurück. Du kannst eine Richtung als Argument übergeben – zum Beispiel `get_ground_type(North)` –, um die Bodenart eines benachbarten Feldes abzufragen.

So prüfst du, ob der Block unter der Drohne aus Erde besteht:

{{codeexample 
{
    "camera_position": {"x": -1.5, "y": 0, "z": 8},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "exclude_unlocks": ["watering", "fertilizer"],
    "world_size": {"x": 4, "y": 4},
    "execution_speed": 2,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 1
}
#CODE
dig()
if get_ground_type() == Grounds.Dirt:
    do_a_flip()
}}

## Härte und Stabilität
`get_hardness()` gibt die Härte des Bodenfeldes unter der Drohne zurück. Du kannst eine Richtung als Argument übergeben, etwa `get_hardness(North)`. Je härter ein Feld ist, desto länger dauert es, es abzubauen.

`get_stability()` gibt die Stabilität des Bodenfeldes unter der Drohne zurück. Du kannst eine Richtung als Argument übergeben, etwa `get_stability(North)`. Eine Stabilität von 1 bedeutet, dass der Block einen Höhenunterschied von 1 aushält, bevor er einstürzt.

{{codeexample 
{
    "camera_position": {"x": -1, "y": 0, "z": 10},
    "show_image": true,
    "image_size": {"x": 800, "y": 250},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "exclude_unlocks": ["watering", "fertilizer"],
    "world_size": {"x": 5, "y": 5},
    "execution_speed": 2,
    "action_ticks": 200,
    "operation_ticks": 20,
    "seed": 0
}
#SETUP
jump(Unlocks.Rice)
#CODE
print(get_hardness(), "|", get_stability())
while get_hardness() == 1:
    dig()

print(get_hardness(), "|", get_stability())
while get_hardness() == 2 and get_stability() == 3:
    dig()
}}

Beachte, dass die vier Blöcke direkt neben der Drohne unabhängig von ihrer Stabilität entfernt werden, während sich die Drohne nach unten gräbt – außer ein Block erfüllt eine besondere Funktion. Ton, Eisen und Quarz werden von dieser Regel beispielsweise nicht entfernt. Bei mangelnder Stabilität können sie jedoch weiterhin einstürzen.
---

[Bergbau](docs/unlocks/mining.md)      [Sinne](docs/unlocks/senses.md)

[get_pos_z()](functions/get_pos_z)      [get_ground_type()](functions/get_ground_type)      [get_hardness()](functions/get_hardness)      [get_stability()](functions/get_stability)

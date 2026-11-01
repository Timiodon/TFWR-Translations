[<- Karotten](docs/unlocks/carrots.md) <right>[Dünger ->](docs/unlocks/fertilizer.md)
<right>[Sonnenblumen ->](docs/unlocks/sunflowers.md)
---
# Bewässerung
Pflanzen wachsen schneller, wenn sie bewässert werden. Der Boden hat einen Wasserstand von `0` bis `1`.
Die Funktion `get_water()` gibt den Wasserstand des Bodens unter der Drohne zurück.

Die Wachstumsgeschwindigkeit einer Pflanze skaliert linear von 1x Geschwindigkeit bei Wasserstand 0 bis 5x Geschwindigkeit bei Wasserstand 1.

Der Boden trocknet mit der Zeit aus: Im Durchschnitt verliert er 1% seines aktuellen Wassers pro Sekunde, aber es gibt dabei eine gewisse zufällige Abweichung. Ein hoher Wasserstand verbraucht viel mehr Wasser als ein niedriger Wasserstand.

Du kannst Wasser für deine Pflanzen verwenden. Alle 10 Sekunden wird automatisch ein Wassertank zu deinem Inventar hinzugefügt.
Ein Upgrade von `Unlocks.Watering` verdoppelt die Menge an Wasser, die du alle 10 Sekunden bekommst.

Ein Tank fasst `0.25` Wasser.

Rufe `use_item(Items.Water)` über einem beliebigen Boden auf, um den Boden zu bewässern.
{{codeexample 
{
    "camera_position": {"x": -4, "y": 1, "z": 6},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [{"item": "water", "n": 10}],
    "world_size": {"x": 9, "y": 1},
    "execution_speed": 2,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 1,
    "seed": 1,
    "exclude_unlocks": ["fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
for _ in range(9):
    till()
    move(East)
#CODE
for i in range(5):
    if i > 0:
        use_item(Items.Water, i)
    plant(Entities.Tree)
    print(get_water())
    move(East)
    move(East)
}}

---

[Dünger](docs/unlocks/fertilizer.md)

[use_item()](functions/use_item)      [get_water()](functions/get_water)

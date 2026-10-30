[<- Bäume](docs/unlocks/trees.md) <right>[Polykultur ->](docs/unlocks/polyculture.md)
<right>[Kaktus ->](docs/unlocks/cactus.md)
---
# Kürbisse
[Kürbisse](objects/pumpkin) wachsen wie Karotten auf gepflügtem Boden. Das Pflanzen kostet Karotten.

Wenn alle Kürbisse in einem Quadrat ausgewachsen sind, wachsen sie zu einem Riesenkürbis zusammen. Leider haben Kürbisse eine 20%ige Chance zu sterben, sobald sie ausgewachsen sind, also musst du die toten neu pflanzen, wenn du möchtest, dass sie verschmelzen.

{{codeexample 
{
    "camera_position": {"x": -1, "y": 1.8, "z": 5},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": false,
    "show_inventory": true,
    "show_output": false,
    "collapsing": false,
    "autoplay": true,
    "items": [{"item": "carrot", "n": 11}],
    "world_size": {"x": 3, "y": 3},
    "execution_speed": 5,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 1,
    "seed": 3,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
for i in range(get_world_size()):
	for j in range(get_world_size()):
		till()
		plant(Entities.Pumpkin)
		move(North)
	move(East)
do_a_flip()
do_a_flip()
move(North)
move(North)
plant(Entities.Pumpkin)
do_a_flip()
plant(Entities.Pumpkin)
do_a_flip()
do_a_flip()
do_a_flip()
do_a_flip()
harvest()
}}

Wenn ein Kürbis stirbt, hinterlässt er einen toten Kürbis, der beim Ernten nichts abwirft. Das Pflanzen einer neuen Pflanze an seiner Stelle entfernt den toten Kürbis automatisch, es ist also nicht nötig, ihn zu ernten. `can_harvest()` gibt bei toten Kürbissen immer `False` zurück.

Der Ertrag eines Riesenkürbisses hängt von der Größe des Kürbisses ab.

Ein 1x1 Kürbis ergibt `1*1*1 = 1` Kürbisse.
Ein 2x2 Kürbis ergibt `2*2*2 = 8` Kürbisse statt `4`.
Ein 3x3 Kürbis ergibt `3*3*3 = 27` Kürbisse statt `9`.
Ein 4x4 Kürbis ergibt `4*4*4 = 64` Kürbisse statt `16`.
Ein 5x5 Kürbis ergibt `5*5*5 = 125` Kürbisse statt `25`.
Ein `n`x`n` Kürbis ergibt `n*n*6` Kürbisse für `n >= 6`.

Es ist eine gute Idee, mindestens 6x6 große Kürbisse zu bekommen, um den vollen Multiplikator zu erhalten.

Das bedeutet, dass selbst wenn du auf jedem Feld eines Quadrats einen Kürbis pflanzt, einer der Kürbisse sterben und das Wachsen des Mega-Kürbisses verhindern kann.

---

[Statistiken](docs/stats.md)      [Operatoren](docs/scripting/operators.md)      [Variablen](docs/scripting/variables.md)      [Sinne](docs/unlocks/senses.md)

[harvest()](functions/harvest)      [can_harvest()](functions/can_harvest)      [plant()](functions/plant)      [move()](functions/move)      [till()](functions/till)

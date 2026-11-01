[<- Bergbau](docs/unlocks/mining.md) <right>[Bambus ->](docs/unlocks/bamboo.md)
<right>[Versteinerte Kürbisse ->](docs/unlocks/petrified_pumpkins.md)
<right>[Perlit und Lehmboden ->](docs/unlocks/special_soils.md)
---
# Reis
Unter der Oberfläche und der `Grounds.Dirt`-Schicht findest du eine dünne Schicht `Grounds.Clay`. Dieser fruchtbare, durchnässte Boden eignet sich hervorragend zum Pflanzen von Reis.

Der folgende Code kann dir helfen, bis zum Ton zu graben und Reis zu pflanzen:
{{codeexample 
{
    "camera_position": {"x": -1, "y": 0, "z": 8},
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
    "execution_speed": 8,
    "digging_speed": 4,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 1
}
#SETUP
move(East)
#CODE
while get_ground_type() != Grounds.Clay:
    dig()
plant(Entities.Rice)
}}

Solange deine Drohne über einem `Grounds.Clay`-Block schwebt, kannst du mit `plant(Entities.Rice)` Reis in den Ton pflanzen, mit `can_harvest()` prüfen, ob er ausgewachsen ist, und ihn schließlich mit `harvest()` ernten.

## Terrassen
Sobald du Reis pflanzt, wird der Boden zu `Grounds.Rice_Terrace`, damit der Reis unter idealen Bedingungen reifen kann. Sobald der Reis ausgewachsen ist, trocknet der Boden aus, wird zu `Grounds.Dry_Rice_Terrace` und kann nicht mehr zum Pflanzen von Reis verwendet werden. Zum Glück ist die Schicht einige Blöcke dick. Du kannst den Block also mit `dig()` abbauen und auf der `Grounds.Clay` darunter neuen Reis pflanzen. Wenn die Schicht aufgebraucht ist, kannst du die Welt jederzeit mit `clear()` zurücksetzen und bis zu einer neuen Schicht graben.

---

[Statistiken](docs/stats.md)      [Bergbau](docs/unlocks/mining.md)      [Unterirdische Sinne](docs/unlocks/underground_senses.md)      [If](docs/scripting/if.md)      [For-Schleife](docs/scripting/for.md)

[harvest()](functions/harvest)      [plant()](functions/plant)      [move()](functions/move)      [dig()](functions/dig)      [get_ground_type()](functions/get_ground_type)

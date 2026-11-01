[<- Kohle](docs/unlocks/coal.md) <right>[Quarz ->](docs/unlocks/quartz.md)
<right>[Eisensuche ->](docs/unlocks/prospecting.md)
<right>[Schatzkarte ->](docs/unlocks/treasure_map.md)
---
# Eisen
Nachdem du Kohle in `Grounds.Dirt` gefunden hast, kannst du tiefer durch die `Grounds.Clay`-Schicht in `Grounds.Rock` graben, um Eisen zu finden.

Im Gegensatz zu Kohleadern erstrecken sich Eisenadern auch senkrecht. Alle Eisenblöcke einer Ader grenzen jedoch immer direkt aneinander und sind nie nur diagonal verbunden.

Eisenadern sind anfangs klein, und du brauchst etwas Glück, um sie zu finden. Weitere Eisen-Upgrades erhöhen die maximale Größe der Adern, sodass du etwas leichter zufällig auf sie stößt. Um sie zuverlässig zu finden, solltest du aber [Erzsuche](docs/unlocks/prospecting.md) freischalten.

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
    "items": [{"item": "hay", "n": 100}, {"item": "wood", "n": 100}],
    "world_size": {"x": 5, "y": 5},
    "execution_speed": 1,
    "digging_speed": 10,
    "action_ticks": 200,
    "operation_ticks": 50,
    "seed": 5,
    "exclude_unlocks": ["watering", "fertilizer", "mushrooms", "quartz"]
}
#SETUP
#CODE
# Graben, bis ein Eisenblock erscheint
while get_ground_type() != Grounds.Iron:
    dig()

# Eisen abbauen
dig()
}}

---

[Statistiken](docs/stats.md)      [Bergbau](docs/unlocks/mining.md)      [Eisensuche](docs/unlocks/prospecting.md)      [Unterirdische Sinne](docs/unlocks/underground_senses.md)

[move()](functions/move)      [dig()](functions/dig)

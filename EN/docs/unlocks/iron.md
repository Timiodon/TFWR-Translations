[<- Coal](docs/unlocks/coal.md) <right>[Quartz ->](docs/unlocks/quartz.md)
<right>[Iron Prospecting ->](docs/unlocks/prospecting.md)
<right>[Treasure Map ->](docs/unlocks/treasure_map.md)
---
# Iron
After finding coal in `Grounds.Dirt`, you can dig further down past the `Grounds.Clay` layer and into `Grounds.Rock` to find iron.

In contrast to coal veins, iron veins also extend vertically. But all iron blocks in a vein are always directly adjacent to each other, the blocks never connect only diagonally.

But iron veins start small and you'll need some luck to find them. Further unlocking iron will increase the maximum vein size and make them a bit easier to find by chance. But to find them reliably, you should unlock [prospecting](docs/unlocks/prospecting.md).

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
# Dig until an iron block appears
while get_ground_type() != Grounds.Iron:
    dig()

# Mine the iron
dig()
}}

---

[Stats](docs/stats.md)      [Mining](docs/unlocks/mining.md)      [Iron Prospecting](docs/unlocks/prospecting.md)      [Underground Senses](docs/unlocks/underground_senses.md)

[move()](functions/move)      [dig()](functions/dig)

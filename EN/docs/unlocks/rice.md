[<- Mining](docs/unlocks/mining.md) <right>[Bamboo ->](docs/unlocks/bamboo.md)
<right>[Petrified Pumpkins ->](docs/unlocks/petrified_pumpkins.md)
<right>[Perlite and Loam ->](docs/unlocks/special_soils.md)
---
# Rice
Below the surface and the `Grounds.Dirt` layer you will find a thin sheet of `Grounds.Clay`. As it turns out, this fertile and soaked ground is perfect for planting rice seedlings.

You might find the following code useful to dig down until you find clay and plant rice:
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

As long as your drone is above a `Grounds.Clay` block, you can use `plant(Entities.Rice)` to plant rice seedlings into the clay, then `can_harvest()` to check if the rice has fully grown, and finally `harvest()` to gain rice.

## Terraces
Once you plant rice, the ground will turn into `Grounds.Rice_Terrace` to provide the perfect environment for the rice to mature. Once the rice is fully grown, the ground will dry out and turn into `Grounds.Dry_Rice_Terrace` and cannot be used to plant more rice. Luckily, the sheet is a few blocks thick, so you can `dig()` the block away and plant new rice on the `Grounds.Clay` below. And, if the sheet runs out, you can always just `clear()` the world and dig down to a fresh sheet.

---

[Stats](docs/stats.md)      [Mining](docs/unlocks/mining.md)      [Underground Senses](docs/unlocks/underground_senses.md)      [If](docs/scripting/if.md)      [For Loop](docs/scripting/for.md)

[harvest()](functions/harvest)      [plant()](functions/plant)      [move()](functions/move)      [dig()](functions/dig)      [get_ground_type()](functions/get_ground_type)

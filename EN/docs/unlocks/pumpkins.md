[<- Trees](docs/unlocks/trees.md) <right>[Polyculture ->](docs/unlocks/polyculture.md)
<right>[Cactus ->](docs/unlocks/cactus.md)
---
# Pumpkins
[Pumpkins](objects/pumpkin) grow like carrots on tilled soil. Planting them costs carrots.

When all the pumpkins in a square are fully grown, they will grow together to form a giant pumpkin. Unfortunately, pumpkins have a 20% chance of dying once they are fully grown, so you will need to replant the dead ones if you want them to merge. 

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

When a pumpkin dies, it leaves behind a dead pumpkin that won't drop anything when harvested. Planting a new plant in its place automatically removes the dead pumpkin, so there is no need to harvest it. `can_harvest()` always returns `False` on dead pumpkins.

The yield of a giant pumpkin depends on the size of the pumpkin.

A 1x1 pumpkin yields `1*1*1 = 1` pumpkins.
A 2x2 pumpkin yields `2*2*2 = 8` pumpkins instead of `4`.
A 3x3 pumpkin yields `3*3*3 = 27` pumpkins instead of `9`.
A 4x4 pumpkin yields `4*4*4 = 64` pumpkins instead of `16`.
A 5x5 pumpkin yields `5*5*5 = 125` pumpkins instead of `25`.
An `n`x`n` pumpkin yields `n*n*6` pumpkins for `n >= 6`.

It's a good idea to grow pumpkins at least 6x6 in size to get the full multiplier.

This means that even if you plant a pumpkin on every tile in a square, one of the pumpkins may die and prevent the mega pumpkin from growing.

---

[Stats](docs/stats.md)      [Operators](docs/scripting/operators.md)      [Variables](docs/scripting/variables.md)      [Senses](docs/unlocks/senses.md)

[harvest()](functions/harvest)      [can_harvest()](functions/can_harvest)      [plant()](functions/plant)      [move()](functions/move)      [till()](functions/till)

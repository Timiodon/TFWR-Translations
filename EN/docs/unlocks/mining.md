[<- Expand 1](docs/unlocks/expand_1.md) <right>[Underground Senses ->](docs/unlocks/underground_senses.md)
<right>[Rice ->](docs/unlocks/rice.md)
<right>[Coal ->](docs/unlocks/coal.md)
---
# Mining
Your drone has gained access to a primitive drill, which allows it to search the underground for treasures.

You can use the `dig()` command to dig into the block below you.

For now, let's collect some blocks:

{{codeexample 
{
    "camera_position": {"x": -1, "y": 0, "z": 8},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": false,
    "autoplay": true,
    "items": [{"item": "hay", "n": 100}, {"item": "wood", "n": 100}],
    "world_size": {"x": 4, "y": 4},
    "execution_speed": 2,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer", "mushrooms", "coal", "special_soils"]
}
#SETUP
move(North)
move(East)
#CODE
dig()
do_a_flip()
dig()
do_a_flip()
dig()
do_a_flip()
clear()
}}

If you want to return to the surface, you can use `clear()` at any point. This also restores your farm.

Hovering over a block will show its name, stability, and hardness.

# Drill
As you dig farther down, you'll notice the blocks becoming harder, which causes digging to take more time. It's a good thing we can upgrade our drill to help with this!

To help your drone make sense of the underground, you should quickly unlock [underground senses](docs/unlocks/underground_senses.md). This will allow it to check its own z-position as well as the type of ground below, its hardness and stability.

For example, with [underground senses](docs/unlocks/underground_senses.md) you can use `get_hardness()` to check the hardness of the block below you. If you run into a patch of particularly hard blocks, it might be wise to move around them, so you can progress faster:

`while True:
    if get_hardness() < 5:
        dig()
    else:
        move(East)`

Of course, blocks get tougher and tougher as you move down, so while this strategy helps, it can only get you so far.

## Cave-ins
Digging down will cause surrounding blocks to cave-in. The four blocks next to the drone are always destroyed. After that, the cave-in propagates according to the ground's stability. A block with stability 1, such as grassland, can withstand a height difference of 1. In other words, if grassland has a vertical or horizontal neighbor whose z-coordinate is 2 or more blocks deeper, the grassland will get destroyed.

The stability of a block is included in its hover tooltip.

When a block caves in, it will also remove all blocks above it. You receive resources only from blocks the drone digs directly, so any blocks lost in a cave-in are destroyed without yielding resources.

---

[Underground Senses](docs/unlocks/underground_senses.md)      [While Loop](docs/scripting/while.md)

[move()](functions/move)      [dig()](functions/dig)

[<- Rice](docs/unlocks/rice.md) <right>[Colorful Blocks ->](docs/unlocks/debug_place.md)
<right>[Pyramids ->](docs/unlocks/pyramid.md)
---
# Bamboo
Bamboo is a plant that grows upward. Your drone will need to pluck its brown fruit regularly so it can keep growing. We can achieve this with the newly unlocked `hover` command.

Bamboo needs to be planted on tilled soil (`Grounds.Soil`) and planting it costs rice.

The following code plants bamboo and waits for it to grow until its first fruit.
{{codeexample
{
"camera_position": {"x": -1, "y": 0, "z": 10},
"show_image": true,
"image_size": {"x": 800, "y": 500},
"show_code": true,
"show_inventory": true,
"show_output": false,
"collapsing": true,
"autoplay": false,
"items": [{"item": "rice", "n": 100}],
"world_size": {"x": 4, "y": 4},
"execution_speed": 2,
"action_ticks": 200,
"operation_ticks": 200,
"seed": 1,
"exclude_unlocks": ["watering", "fertilizer", "mushrooms", "coal"]
}
#SETUP
move(North)
move(East)
#CODE
till()
plant(Entities.Bamboo)
move(East) # move away so the bamboo can grow
}}

## Fruits
Bamboo grows exactly 1 block per second.

Bamboo produces fruits every few blocks. When this happens, the bamboo stops growing and you will need to fly into it with your drone to destroy the fruit.

To pluck fruits, you will first need to `hover` to the correct height. Then you should `move` into the fruit to pluck it and `move` away again so the bamboo can continue to grow.

You can `measure()` the bamboo to check at which height the next fruit will appear. `measure()` starts counting at `0`, so `hover(measure())` will bring your drone to the height where the fruit will be.

{{codeexample
{
"camera_position": {"x": -1, "y": 0, "z": 10},
"show_image": true,
"image_size": {"x": 800, "y": 500},
"show_code": true,
"show_inventory": true,
"show_output": false,
"collapsing": true,
"autoplay": false,
"items": [{"item": "rice", "n": 100}],
"world_size": {"x": 4, "y": 4},
"execution_speed": 2,
"action_ticks": 200,
"operation_ticks": 200,
"seed": 1,
"exclude_unlocks": ["watering", "fertilizer", "mushrooms", "coal"]
}
#SETUP
move(North)
move(East)
#CODE
till()
plant(Entities.Bamboo)
hover(measure()) # hover such that drone will be next to fruit

move(East) # move away and wait for it to grow
for i in range(3):
    do_a_flip()

move(West) # pluck fruit
move(East) # move away again
}}

## Hover
The `hover` command takes one argument, the height at which to hover, which is a number from `0` to `18`. The default hover height of the drone is `1`. `hover` cannot move downwards into solid entities, so if your drone is already above bamboo, you cannot move into it by executing `hover(0)`.

`hover` returns `True` if the drone successfully hovered to the specified height, and `False` otherwise.

Additionally, there is the command `get_hover`, which returns the drone's current hover height.

If you use `dig`, `harvest` or `plant` while hovering, the drone will return to its default hovering height (`1`).

Finally, `get_pos_z()` is unaffected by hover. It always returns the z-position of the block under the drone.

## Harvesting Bamboo
While you could use `harvest()`, the recommended way to harvest bamboo fields is to move into a bamboo with your drone at hover height `0` (`hover(0)`). This harvests the entire plant at once.

If you would like to harvest the bamboo without destroying it, you can `move` into it at any height, for example `hover(3)`. This harvests all the bamboo pieces from that height upwards but will keep the bamboo alive. A bamboo that was partially harvested in this way will regrow its fruits, so you will need to pluck them again.

In either case, your yield is equal to the square of the number of destroyed bamboo pieces, so the taller the bamboo plant, the better your yield.

---

[Stats](docs/stats.md)      [For Loop](docs/scripting/for.md)      [Variables](docs/scripting/variables.md)      [If](docs/scripting/if.md)      [Functions](docs/scripting/functions.md)      [Rice](docs/unlocks/rice.md)

[harvest()](functions/harvest)      [plant()](functions/plant)      [move()](functions/move)      [till()](functions/till)      [measure()](functions/measure)

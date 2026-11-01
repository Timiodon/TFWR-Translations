[<- Quartz](docs/unlocks/quartz.md) <right>[Dynamite ->](docs/unlocks/dynamite.md)
---
# Mushroom
Many types of mushrooms grow in colonies underground. Look for a stratum of `Grounds.Mushroom` while digging. You can then `measure()` the ground to get the mushroom type as a number, ranging from `0` to `5`.

The following code finds some mushrooms and prints their type:
{{codeexample 
{
    "camera_position": {"x": -1, "y": 0, "z": 6},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 4, "y": 4},
    "execution_speed": 2,
    "digging_speed": 6,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 9,
    "exclude_unlocks": ["watering", "fertilizer", "dynamite", "iron"]
}
#SETUP
jump(Unlocks.Mushrooms)
#CODE
# Process a row of mushrooms
for i in range(get_world_size()):
    # Dig down to the top mushroom block
    while get_ground_type() != Grounds.Mushroom:
        dig()

    # Print the mushroom type number
    print(measure())

    move(East)
}}

## How to Collect Mushrooms
Mushrooms of the same type like to be together, but they are a bit too shy to grow on top of each other. Push the mushroom block below the drone with `push(direction)`.

Stack two mushroom blocks of the same type on top of each other and the blocks will be harvested automatically for their mushrooms.

The code below makes space and then pushes a mushroom until it matches the mushroom below:
{{codeexample 
{
    "camera_position": {"x": -1, "y": 0, "z": 6},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 4, "y": 4},
    "execution_speed": 2,
    "digging_speed": 6,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 3,
    "exclude_unlocks": ["watering", "fertilizer", "dynamite", "iron", "special_soils"]
}
#SETUP
jump(Unlocks.Mushrooms)
#CODE
while get_ground_type() != Grounds.Mushroom:
    dig()

depth = get_pos_z()
for i in range(2):
    # Make space to push the mushroom block east
    move(East)
    while get_pos_z() > depth - 1:
        dig()
    # Move back, push, and follow the pushed block
    move(West)
    push(East) # Push the mushroom!
    move(East)
}}

# Pushing Blocks
You can use `can_push(direction)` to check whether the block under the drone can be pushed and if anything is blocking it in the given direction.

`push(direction)` pushes the block and returns whether the push was successful.

Only mushroom blocks can be pushed, blocks cannot be pushed upwards and the push will fail if another block is in the way. When pushed into the air, blocks fall and land on the next block below them.

# Strategy
<spoiler=hint>
Remember that you can call `place(Grounds.Dirt)` to place blocks below the drone. This can be useful for filling in holes, so that you can push blocks over them.
</spoiler>

---

[Stats](docs/stats.md)      [Underground Senses](docs/unlocks/underground_senses.md)      [Dictionaries](docs/scripting/dicts.md)

[move()](functions/move)      [measure()](functions/measure)      [can_push()](functions/can_push)      [push()](functions/push)      [place()](functions/place)      [get_ground_type()](functions/get_ground_type)

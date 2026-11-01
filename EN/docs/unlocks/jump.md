[<- Coal](docs/unlocks/coal.md)
---
# Jumping
Your drone has unlocked the `jump()` command. You use it by passing it an unlock as an argument, such as `Unlocks.Iron`.

This command allows you to target certain resources that are hidden in the ground and instantly jump down to them. It is especially useful for debugging or skipping to an ore vein that you have recently missed.

After jumping, the target resource should be within 3 blocks of the top block surface. `jump()` can only be used once per program execution, further jump attempts will produce an error.

The following example jumps down to [rice](docs/unlocks/rice.md), finds the clay layer and plants a row of rice terraces:
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
    "items": [{"item": "hay", "n": 10}],
    "world_size": {"x": 4, "y": 4},
    "execution_speed": 1,
    "digging_speed": 4,
    "action_ticks": 200,
    "operation_ticks": 20,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer", "mushrooms"],
    "starting_chunk": 0
}
#CODE
# Jump close to the rice resource
jump(Unlocks.Rice)

# Plant a row of rice terraces
for i in range(get_world_size()):
    # Jump is not exact, dig away the last blocks
    while get_ground_type() != Grounds.Clay:
        dig()

    plant(Entities.Rice)

    move(East)
}}

## Compatible Unlocks
`jump()` only works with the following mining unlocks:
- Coal
- Iron
- Quartz
- Rice
- Petrified_Pumpkins
- Special_Soils
- Pyramid
- Treasure_Map
- Mushrooms
- Dynamite

---

[jump()](functions/jump)

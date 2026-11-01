[<- Bamboo](docs/unlocks/bamboo.md)
---
# Colorful Blocks
As you might already know, you can use `place()` to make your drone place a block. This unlock adds three colored blocks that are visually distinct from their surroundings, `Grounds.Block_Red`, `Grounds.Block_Green` and `Grounds.Block_Blue`.

Colored blocks can be used to mark things or make pretty patterns.

To place the new blocks:
{{codeexample 
{
    "camera_position": {"x": -1, "y": 0, "z": 10},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": false,
    "autoplay": true,
    "items": [{"item": "block", "n": 100}],
    "world_size": {"x": 5, "y": 5},
    "execution_speed": 5,
    "digging_speed": 4,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer", "mushrooms", "coal"],
    "starting_chunk": 2
}
#SETUP
move(East)
move(North)
#CODE
place(Grounds.Block_Green)
move(East)

place(Grounds.Block_Blue)
move(East)

place(Grounds.Block_Green)
move(North)

place(Grounds.Block_Blue)
move(North)

place(Grounds.Block_Green)
move(West)

place(Grounds.Block_Blue)
move(West)

place(Grounds.Block_Green)
move(South)

place(Grounds.Block_Blue)
move(East)

place(Grounds.Block_Red)
place(Grounds.Block_Red)

do_a_flip()
}}

---

[Debug](docs/scripting/debug.md)      [Debug 2](docs/unlocks/debug2.md)      [Bamboo](docs/unlocks/bamboo.md)

[place()](functions/place)

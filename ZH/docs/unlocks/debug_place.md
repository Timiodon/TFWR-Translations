[<-竹子](docs/unlocks/bamboo.md)
---
# 彩色地块
你可能已经知道，可以用 `place()` 让无人机放置地块。此解锁项新增了三种颜色鲜明、容易与周围区分的地块：`Grounds.Block_Red`、`Grounds.Block_Green` 和 `Grounds.Block_Blue`。

彩色地块可以用来标记位置，或制作漂亮的图案。

放置新地块的方法如下：
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

[调试](docs/scripting/debug.md)      [调试 2](docs/unlocks/debug2.md)      [竹子](docs/unlocks/bamboo.md)

[place()](functions/place)

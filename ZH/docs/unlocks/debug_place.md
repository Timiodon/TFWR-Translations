[<-竹子](docs/unlocks/bamboo.md)
---
# 彩色地块

你已经知道，可以用 `place()` 让无人机放置地块。此解锁项新增了几种颜色鲜明、容易与周围区分的地块。

放置新地块的方法如下：

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
    "execution_speed": 1,
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
dig()
dig()
dig()
#CODE
place(Grounds.Red_Block)
place(Grounds.Green_Block)
place(Grounds.Blue_Block)
}}
---

[调试](docs/scripting/debug.md)      [调试 2](docs/unlocks/debug2.md)      [竹子](docs/unlocks/bamboo.md)

[place()](functions/place)

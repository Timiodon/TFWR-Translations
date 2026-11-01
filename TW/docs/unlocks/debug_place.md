[<-竹子](docs/unlocks/bamboo.md)
---
# 彩色地塊
你可能已經知道，可以用 `place()` 讓無人機放置地塊。此解鎖項新增了三種顏色鮮明、容易與周圍區分的地塊：`Grounds.Block_Red`、`Grounds.Block_Green` 和 `Grounds.Block_Blue`。

彩色地塊可以用來標記位置，或製作漂亮的圖案。

放置新地塊的方法如下：
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

[偵錯](docs/scripting/debug.md)      [偵錯 2](docs/unlocks/debug2.md)      [竹子](docs/unlocks/bamboo.md)

[place()](functions/place)

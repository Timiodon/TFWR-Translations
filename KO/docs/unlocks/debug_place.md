[<- 대나무](docs/unlocks/bamboo.md)
---
# 알록달록 블록

이미 알고 있듯이 `place()`를 사용하면 드론에게 블록을 배치하도록 할 수 있습니다. 이 해금 항목으로 주변과 시각적으로 구분되는 색상 블록을 추가할 수 있습니다.

새 블록을 배치하려면

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

[디버그](docs/scripting/debug.md)      [디버그 2](docs/unlocks/debug2.md)      [대나무](docs/unlocks/bamboo.md)

[place()](functions/place)

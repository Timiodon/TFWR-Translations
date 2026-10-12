[<-采矿](docs/unlocks/mining.md) <right>[铁矿->](docs/unlocks/iron.md)
<right>[跳转->](docs/unlocks/jump.md)
---
# 煤炭

原来，地表下方就是寻找煤炭矿床的好地方。

煤炭会随机生成厚度为 1 个地块的水平煤层。煤层面积会随世界规模变化。因此，想找到更多煤炭，不妨扩大农场！

下面的程序很适合用来寻找煤炭。它会向下挖掘寻找煤炭层，然后往东西两侧挖掘，试着找到更多煤炭。

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
    "execution_speed": 4,
    "digging_speed": 2,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 2
}
#SETUP
move(North)
move(East)
move(East)
#CODE
while get_ground_type() != Grounds.Coal:
    dig()
dig()
move(East)
dig()
move(West)
move(West)
dig()
}}

---

[统计数据](docs/stats.md)      [采矿](docs/unlocks/mining.md)      [地下感官](docs/unlocks/underground_senses.md)

[move()](functions/move)      [get_ground_type()](functions/get_ground_type)      [dig()](functions/dig)

[<-採礦](docs/unlocks/mining.md) <right>[鐵礦->](docs/unlocks/iron.md)
<right>[跳轉->](docs/unlocks/jump.md)
---
# 煤炭

原來，地表下方就是尋找煤炭礦床的好地方。

煤炭會隨機產生厚度為 1 個地塊的水平煤層。煤層面積會隨世界規模變化。因此，想找到更多煤炭，不妨擴大農場！

下面的程式很適合用來尋找煤炭。它會向下挖掘尋找煤炭層，然後往東西兩側挖掘，試著找到更多煤炭。

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

[統計資料](docs/stats.md)      [採礦](docs/unlocks/mining.md)      [地下感官](docs/unlocks/underground_senses.md)

[move()](functions/move)      [get_ground_type()](functions/get_ground_type)      [dig()](functions/dig)

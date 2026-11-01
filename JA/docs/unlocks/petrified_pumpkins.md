[<- 稲](docs/unlocks/rice.md)
---
# 石化したカボチャ
地下ではカボチャが見つかるようです。固まって石化していますが、目的には十分使えます。`dig()`で掘るとカボチャが手に入ります。

地上で栽培せずにカボチャを手に入れる、もう1つの方法です。栽培する方が好きなら、石化したカボチャは気にしなくても構いません。

{{codeexample 
{
    "camera_position": {"x": -2, "y": 1, "z": 8},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": false,
    "show_inventory": true,
    "show_output": false,
    "collapsing": false,
    "autoplay": true,
    "items": [],
    "exclude_unlocks": ["mushrooms", "watering", "fertilizer", "pyramid", "dynamite", "quartz"],
    "world_size": {"x": 6, "y": 6},
    "execution_speed": 8,
    "digging_speed": 16,
    "action_ticks": 200,
    "operation_ticks": 1,
    "seed": 3
}
#SETUP
jump(Unlocks.Petrified_Pumpkins)
move(East)
move(North)
move(North)
move(North)
#CODE
while get_ground_type() != Grounds.Petrified_Pumpkin:
    dig()
z = get_pos_z()
for i in range(get_world_size()):
    for j in range(get_world_size()):
        while get_pos_z() > z - 2 and get_ground_type() != Grounds.Petrified_Pumpkin:
            dig()
        move(North)
    move(East)
for _ in range(3):
    dig()
    move(East)
    dig()
    move(South)
    dig()
    move(West)
    dig()
    move(West)
    dig()
    move(North)
    dig()
    move(North)
    dig()
    move(East)
    dig()
    move(East)
    dig()
    move(South)
    move(West)
}}

石化したカボチャは、地下に3x3x3または5x5x5の塊として現れます。確実な探し方はないので、ドローンが偶然掘り当てることを願うしかありません。石と鉄の層の下にある硬い土の中にあり、石英をアンロックしていれば石英と同じくらいの深さにあります。

---

[統計](docs/stats.md)      [採掘](docs/unlocks/mining.md)      [地下の感覚](docs/unlocks/underground_senses.md)

[move()](functions/move)      [dig()](functions/dig)      [get_ground_type()](functions/get_ground_type)

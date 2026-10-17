[<-水稻](docs/unlocks/rice.md)
---
# 石化南瓜

地下也能找到南瓜。它们已经变硬、石化，但对我们来说仍然够用。

石化南瓜会以 3x3x3 或 5x5x5 的地块群出现在地下。没有万无一失的寻找方法，只能期待无人机恰好挖中。不过，它们出现在岩石和铁矿层下方的硬质泥土中，高度与石英大致相同（如果你已解锁石英）。

这提供了另一种获取南瓜的方式，无需在地上种植。如果你更喜欢种植，完全可以忽略石化南瓜。

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
    "items": [{"item": "hay", "n": 100}],
    "exclude_unlocks": ["mushrooms", "watering", "fertilizer", "pyramid", "dynamite"],
    "world_size": {"x": 6, "y": 6},
    "execution_speed": 8,
    "digging_speed": 16,
    "action_ticks": 200,
    "operation_ticks": 200,
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
        while get_pos_z() > z:
            dig()
        move(North)
    move(East)
}}

---

[统计数据](docs/stats.md)      [采矿](docs/unlocks/mining.md)      [地下感官](docs/unlocks/underground_senses.md)

[move()](functions/move)      [dig()](functions/dig)      [get_ground_type()](functions/get_ground_type)

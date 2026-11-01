[<-水稻](docs/unlocks/rice.md)
---
# 石化南瓜
地下也能找到南瓜。它們已經變硬、石化，但對我們來說仍然夠用。使用 `dig()` 挖掘它們可以獲得南瓜。

這提供了另一種取得南瓜的方法，不必在地面上種植。若你偏好種植，也可以完全忽略石化南瓜。

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

石化南瓜會以 3x3x3 或 5x5x5 的地塊群出現在地下。沒有萬無一失的尋找方法，只能期待無人機恰好挖中。不過，它們出現在岩石和鐵礦層下方的硬質泥土中，高度與石英大致相同（如果你已解鎖石英）。

---

[統計資料](docs/stats.md)      [採礦](docs/unlocks/mining.md)      [地下感官](docs/unlocks/underground_senses.md)

[move()](functions/move) [dig()](functions/dig) [get_ground_type()](functions/get_ground_type)

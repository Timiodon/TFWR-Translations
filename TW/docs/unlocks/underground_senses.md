[<-採礦](docs/unlocks/mining.md)
---
# 地下感官
給無人機裝上幾個感測器，讓它能在地下找到方向。

## Z 座標
現在可以使用 `get_pos_z()` 取得無人機的高度（從 0 開始，隨著無人機下降變為負數）。

{{codeexample 
{
    "camera_position": {"x": -1.5, "y": 0, "z": 10},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "exclude_unlocks": ["watering", "fertilizer"],
    "items": [],
    "world_size": {"x": 5, "y": 5},
    "execution_speed": 2,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 1
}
#SETUP
move(North)
move(North)
move(East)
move(East)
#CODE
print(get_pos_z())
dig()
dig()
dig()
print(get_pos_z())
}}

## 地面類型
`get_ground_type()` 回傳無人機下方地塊的類型。你可以傳入方向參數，例如 `get_ground_type(North)`，來取得相鄰地塊的類型。

下面演示如何檢查無人機下方是否為泥土地塊：

{{codeexample 
{
    "camera_position": {"x": -1.5, "y": 0, "z": 8},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "exclude_unlocks": ["watering", "fertilizer"],
    "world_size": {"x": 4, "y": 4},
    "execution_speed": 2,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 1
}
#CODE
dig()
if get_ground_type() == Grounds.Dirt:
    do_a_flip()
}}

## 硬度與穩定度
`get_hardness()` 回傳無人機下方地塊的硬度。你也可以傳入方向參數，例如 `get_hardness(North)`。地塊硬度越高，挖掘所需時間越長。

`get_stability()` 回傳無人機下方地塊的穩定度。你也可以傳入方向參數，例如 `get_stability(North)`。穩定度為 1 表示地塊在塌方前能承受 1 格的高度差。

{{codeexample 
{
    "camera_position": {"x": -1, "y": 0, "z": 10},
    "show_image": true,
    "image_size": {"x": 800, "y": 250},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "exclude_unlocks": ["watering", "fertilizer"],
    "world_size": {"x": 5, "y": 5},
    "execution_speed": 2,
    "action_ticks": 200,
    "operation_ticks": 20,
    "seed": 0
}
#SETUP
jump(Unlocks.Rice)
#CODE
print(get_hardness(), "|", get_stability())
while get_hardness() == 1:
    dig()

print(get_hardness(), "|", get_stability())
while get_hardness() == 2 and get_stability() == 3:
    dig()
}}

注意：無人機向下挖掘時，緊鄰它的四個地塊會被移除，無論其穩定度如何；具有特殊功能的地塊除外。例如，黏土、鐵礦和石英不會因此被移除。不過，穩定度不足時，它們仍可能塌方。
---

[採礦](docs/unlocks/mining.md)      [感官](docs/unlocks/senses.md)

[get_pos_z()](functions/get_pos_z)      [get_ground_type()](functions/get_ground_type)      [get_hardness()](functions/get_hardness)      [get_stability()](functions/get_stability)

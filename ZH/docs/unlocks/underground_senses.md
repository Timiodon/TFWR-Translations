[<-采矿](docs/unlocks/mining.md)
---
# 地下感官
给无人机装上几个传感器，让它能在地下找到方向。

## Z 坐标
现在可以使用 `get_pos_z()` 获取无人机的高度（从 0 开始，随着无人机下降变为负数）。

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

## 地面类型
`get_ground_type()` 返回无人机下方地块的类型。你可以传入方向参数，例如 `get_ground_type(North)`，来获取相邻地块的类型。

下面演示如何检查无人机下方是否为泥土地块：

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

## 硬度与稳定度
`get_hardness()` 返回无人机下方地块的硬度。你也可以传入方向参数，例如 `get_hardness(North)`。地块硬度越高，挖掘所需时间越长。

`get_stability()` 返回无人机下方地块的稳定度。你也可以传入方向参数，例如 `get_stability(North)`。稳定度为 1 表示地块在塌方前能承受 1 格的高度差。

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

注意：无人机向下挖掘时，紧邻它的四个地块会被移除，无论其稳定度如何；具有特殊功能的地块除外。例如，黏土、铁矿和石英不会因此被移除。不过，稳定度不足时，它们仍可能塌方。
---

[采矿](docs/unlocks/mining.md)      [感官](docs/unlocks/senses.md)

[get_pos_z()](functions/get_pos_z)      [get_ground_type()](functions/get_ground_type)      [get_hardness()](functions/get_hardness)      [get_stability()](functions/get_stability)

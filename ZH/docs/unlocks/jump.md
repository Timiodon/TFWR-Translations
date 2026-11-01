[<-煤炭](docs/unlocks/coal.md)
---
# 跳转
无人机已解锁 `jump()` 命令。使用时，传入一个解锁项作为参数，例如 `Unlocks.Iron`。

此命令可以指定地下的某些资源，并瞬间向下跳到它们附近。调试程序，或者回头寻找刚刚错过的矿脉时，这特别有用。

跳跃后，目标资源应该位于最上方地块表面以下 3 格以内。每次执行程序只能使用一次 `jump()`。再次尝试会报错。

下面的示例跳到[水稻](docs/unlocks/rice.md)附近，找到黏土层，再种下一排水稻梯田：
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
    "items": [{"item": "hay", "n": 10}],
    "world_size": {"x": 4, "y": 4},
    "execution_speed": 1,
    "digging_speed": 4,
    "action_ticks": 200,
    "operation_ticks": 20,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer", "mushrooms"],
    "starting_chunk": 0
}
#CODE
# 跳到水稻资源附近
jump(Unlocks.Rice)

# 种下一排水稻梯田
for i in range(get_world_size()):
    # 跳跃不精确，挖掉剩余地块
    while get_ground_type() != Grounds.Clay:
        dig()

    plant(Entities.Rice)

    move(East)
}}

## 支持的解锁项
`jump()` 只适用于以下采矿解锁项：
- 煤炭
- 铁矿
- 石英
- 水稻
- 石化南瓜
- 特殊土壤
- 金字塔
- 藏宝图
- 蘑菇
- 炸药

---

[jump()](functions/jump)

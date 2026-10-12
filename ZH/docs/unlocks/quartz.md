[<-铁矿](docs/unlocks/iron.md) <right>[蘑菇->](docs/unlocks/mushroom.md)
---
# 石英

石英矿脉呈针状，生长在岩石层底部附近及其下方的硬质泥土中。矿脉形成垂直的柱状结构，单凭碰运气很难挖掘到。

好在我们可以把铁矿加工成类似探矿杖的东西，更容易找到石英矿脉。对应的命令是 `prospect_quartz()`。

`prospect_quartz()` 的工作方式与 `prospect_iron()` 不同。它不会返回最近石英矿石的方向，而是返回到最近石英的欧几里得距离（三维距离）。执行 `prospect_quartz()` 命令需消耗 1 份铁矿，最好省着用。

如果附近没有石英，或者铁矿不足以执行探查，`prospect_quartz()` 就会返回 `None`。

下面的代码片段会让无人机挖穿泥土，深入岩石层。运气好的话，附近就有一条石英矿脉，无人机会打印出到它的距离。

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
    "items": [{"item": "hay", "n": 100}, {"item": "iron", "n": 100}],
    "world_size": {"x": 3, "y": 3},
    "execution_speed": 8,
    "digging_speed": 16,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 9,
    "exclude_unlocks": ["watering", "fertilizer", "mushrooms", "dynamite"]
}

#CODE
move(East)
move(North)
while get_ground_type() != Grounds.Rock:
    dig()
for i in range(30):
    dig()
do_a_flip()
do_a_flip()
print(prospect_quartz())
}}

---

[统计数据](docs/stats.md)      [采矿](docs/unlocks/mining.md)      [地下感官](docs/unlocks/underground_senses.md)      [变量](docs/scripting/variables.md)      [运算符](docs/scripting/operators.md)

[move()](functions/move)      [dig()](functions/dig)      [get_ground_type()](functions/get_ground_type)      [prospect_quartz()](functions/prospect_quartz)

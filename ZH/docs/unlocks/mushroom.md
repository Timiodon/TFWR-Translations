[<-石英](docs/unlocks/quartz.md) <right>[炸药->](docs/unlocks/dynamite.md)
---
# 蘑菇

地下有许多种蘑菇成群生长。挖掘时寻找一层 `Grounds.Mushroom`。随后，可以对地块使用 `measure()`，获取从 `0` 开始编号的蘑菇类型。

{{codeexample 
{
    "camera_position": {"x": -1, "y": 0, "z": 6},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [{"item": "hay", "n": 100}, {"item": "iron", "n": 100}],
    "world_size": {"x": 4, "y": 4},
    "execution_speed": 2,
    "digging_speed": 6,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 9,
    "exclude_unlocks": ["watering", "fertilizer", "dynamite", "iron"]
}

#SETUP
jump(Unlocks.Mushrooms)
#CODE
while get_ground_type() != Grounds.Mushroom:
    dig()
do_a_flip()
print(measure())
}}

同类蘑菇喜欢长在一起，却又很害羞，不会叠着长。把一个蘑菇地块推到另一个相同类型的蘑菇地块上，两者就会消失，而你会获得蘑菇作为奖励。

使用 `can_push(direction)` 可以检查无人机下方的地块能否推动，以及指定方向上是否有东西挡路。`push(direction)` 会推动地块，并返回是否成功。

地块不能向上推动；如果有其他地块挡路，推动也会失败。地块被推到空中后，会落到下方的第一个地块上。

别忘了，可以调用 `place(Grounds.Dirt)` 在无人机下方放置地块。这有助于填平坑洞，让你能将其他地块推过去。

---

[统计数据](docs/stats.md)      [地下感官](docs/unlocks/underground_senses.md)      [字典](docs/scripting/dicts.md)

[move()](functions/move)      [measure()](functions/measure)      [can_push()](functions/can_push)      [push()](functions/push)      [place()](functions/place)      [get_ground_type()](functions/get_ground_type)

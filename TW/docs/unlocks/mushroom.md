[<-石英](docs/unlocks/quartz.md) <right>[炸藥->](docs/unlocks/dynamite.md)
---
# 蘑菇

地下有許多種蘑菇成群生長。挖掘時尋找一層 `Grounds.Mushroom`。隨後，可以對地塊使用 `measure()`，取得從 `0` 開始編號的蘑菇類型。

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

同類蘑菇喜歡長在一起，卻又很害羞，不會疊著長。把一個蘑菇地塊推到另一個相同類型的蘑菇地塊上，兩者就會消失，而你會獲得蘑菇作為獎勵。

使用 `can_push(direction)` 可以檢查無人機下方的地塊能否推動，以及指定方向上是否有東西擋路。`push(direction)` 會推動地塊，並回傳是否成功。

地塊不能向上推動；如果有其他地塊擋路，推動也會失敗。地塊被推到空中後，會落到下方的第一個地塊上。

別忘了，可以呼叫 `place(Grounds.Dirt)` 在無人機下方放置地塊。這有助於填平坑洞，讓你能將其他地塊推過去。

---

[統計資料](docs/stats.md)      [地下感官](docs/unlocks/underground_senses.md)      [字典](docs/scripting/dicts.md)

[move()](functions/move)      [measure()](functions/measure)      [can_push()](functions/can_push)      [push()](functions/push)      [place()](functions/place)      [get_ground_type()](functions/get_ground_type)

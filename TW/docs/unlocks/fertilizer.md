[<- 澆水](docs/unlocks/watering.md) <right>[迷宮 ->](docs/unlocks/mazes.md)
---
# 肥料
有些時候，等待植物生長非常影響效率。
與水類似，你每 10 秒會自動獲得 1 份肥料，每次升級數量翻倍。

肥料可以使植物加速生長。`use_item(Items.Fertilizer)` 會將無人機下方植物的剩餘生長時間縮短 2 秒。

{{codeexample 
{
    "camera_position": {"x": 0, "y": 1, "z": 5},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [{"item": "fertilizer", "n": 10}],
    "world_size": {"x": 1, "y": 1},
    "execution_speed": 2,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 1,
    "seed": 1,
    "exclude_unlocks": ["watering"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
plant(Entities.Tree)
use_item(Items.Fertilizer)
use_item(Items.Fertilizer)
use_item(Items.Fertilizer)
harvest()
}}

但肥料存在副作用。
施肥生長的植物會被感染。

植物被感染後，收穫時一半的產量會變成奇異物質 `Items.Weird_Substance`。
奇異物質也可以用在植物上，其效果是切換該植物及所有相鄰植物的感染狀態。

所以如果在受感染的植物上呼叫 `use_item(Items.Weird_Substance)` 會治愈植物，但在健康的植物上呼叫它，則會感染植物。

如果在有健康鄰居的受感染植物上使用它，在治愈該植物的同時會感染鄰居，反之亦然。

{{codeexample 
{
    "camera_position": {"x": -1, "y": 1.8, "z": 5},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [{"item": "weird_substance", "n": 10}],
    "world_size": {"x": 3, "y": 3},
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 1,
    "seed": 1,
    "exclude_unlocks": ["watering"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
for _ in range(3):
    for _ in range(3):
        plant(Entities.Tree)
        move(East)
    move(North)

move(North)
move(East)

for _ in range(60):
    do_a_flip()
#CODE
for _ in range(6):
    use_item(Items.Weird_Substance)
    move(East)
}}

---

[統計資料](docs/stats.md)      [澆水](docs/unlocks/watering.md)      [迷宮](docs/unlocks/mazes.md)

[use_item()](functions/use_item)

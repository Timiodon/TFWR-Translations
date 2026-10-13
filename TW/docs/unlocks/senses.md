[<- 運算子](docs/scripting/operators.md)
---
# 感官
無人機現在擁有視覺能力了！

呼叫 `get_pos_x()` 和 `get_pos_y()` 函式會回傳無人機目前的 x 和 y 座標。在起始位置時，兩者都回傳 `0`。x 的座標向 `East` （右）方向每格增加 `1`，y 的座標向 `North` （上）方向每格增加 `1`。
{{codeexample 
{
    "camera_position": {"x": -1, "y": 1.8, "z": 4},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 2, "y": 2},
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 100,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
move(East)
#CODE
print("x =", get_pos_x(), "y =", get_pos_y())
if get_pos_x() == 1 and get_pos_y() == 0:
    do_a_flip()
}}

呼叫 `num_items(item)` 函式會回傳你現在擁有某種物品的數量。
{{codeexample 
{
    "camera_position": {"x": 0, "y": 1.5, "z": 4},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "items": [{"item": "hay", "n": 10}],
    "world_size": {"x": 1, "y": 1},
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 100,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
print(num_items(Items.Hay))
}}

呼叫 `get_entity_type()` 和 `get_ground_type()` 函式會回傳無人機目前下方實體或地塊類型。

{{codeexample 
{
    "camera_position": {"x": 0, "y": 1.5, "z": 6},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 1, "y": 1},
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 100,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
plant(Entities.Bush)
#CODE
print(get_entity_type())
if get_entity_type() == Entities.Bush:
	do_a_flip()

print(get_ground_type())
if get_ground_type() != Grounds.Soil:
	do_a_flip()
}}

`None` 關鍵字現在也解鎖了！`None` 是一個表示沒有值的值。
例如，呼叫一個沒有 `return` 陳述式的函式實際上就會回傳 `None`。

如果無人機下方沒有實體，呼叫 `get_entity_type()` 函式會回傳 `None`。


如果想知道你現在擁有的某個特定科技樹項目的數量，可以呼叫 `num_unlocked(unlock)` 函式。

例如，呼叫 `num_unlocked(Unlocks.Speed)` 函式會回傳你現在擁有的速度的等級。

如果感官已解鎖，呼叫 `num_unlocked(Unlocks.Senses)` 函式會回傳 `1`，否則回傳 `0`。

你也可以對物品或實體呼叫 `num_unlocked()` 函式，已解鎖會回傳 `1`，否則回傳 `0`。

請注意：呼叫 `num_unlocked(Unlocks.Carrots)` 函式會回傳胡蘿蔔是否被解鎖或者胡蘿蔔目前的等級。
呼叫 `num_unlocked(Items.Carrot)` 函式則只會回傳 `0` 或 `1`。（其他植物也一樣）

---

[If 陳述式](docs/scripting/if.md)      [運算子](docs/scripting/operators.md)      [變數](docs/scripting/variables.md)      [元組](docs/scripting/tuples.md)      [字典](docs/scripting/dicts.md)      [地下感官](docs/unlocks/underground_senses.md)

[get_pos_x()](functions/get_pos_x)      [get_pos_y()](functions/get_pos_y)      [get_entity_type()](functions/get_entity_type)      [get_ground_type()](functions/get_ground_type)      [num_items()](functions/num_items)      [num_unlocked()](functions/num_unlocked)

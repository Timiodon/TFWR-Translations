[<- 串列](docs/scripting/lists.md) <right>[成本 ->](docs/unlocks/costs.md)
---
# 字典
字典是一種將鍵對應到值的資料結構，就像現實中的字典將詞語對應到釋義一樣。它能讓你非常快速地尋找對應的值。

字典建立的方式如下：
{{codeexample 
{
    "show_image": false,
    "show_code": true,
    "show_inventory": false,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 100,
    "seed": 0,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
right_of = {North:East, East:South, South:West, West:North}
}}

冒號前面是鍵，冒號後面是鍵對應的值。
上面的字典將每個方向對應到它右邊的方向。

下面是另一個將無人機位置對應到它下方實體的字典。
{{codeexample 
{
    "show_image": false,
    "show_code": true,
    "show_inventory": false,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 100,
    "seed": 0,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
x, y = get_pos_x(), get_pos_y()
entity_dict = {(x,y):get_entity_type()}
}}

取得鍵對應的值的方式類似於存取串列中的元素：
`value = dict[key]`

{{codeexample 
{
    "show_image": false,
    "show_code": true,
    "show_inventory": false,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 100,
    "seed": 0,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
right_of = {North:East, East:South, South:West, West:North}
print(right_of[South])
}}

向字典新增 1 個新的鍵值對的方式如下：
`dict[key] = value`

範例：
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
    "items": [],
    "world_size": {"x": 3, "y": 1},
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
plant(Entities.Bush)
move(East)
plant(Entities.Tree)
move(East)
#CODE
entity_dict = {}
for _ in range(3):
	entity_dict[(get_pos_x(), get_pos_y())] = get_entity_type()
	move(East)
print(entity_dict)
}}
這會更新目前位置儲存的實體。

鍵是唯一的，所以在同一個字典中新增已存在的鍵會覆蓋之前對應的值。

呼叫 `dict.pop(key)` 函式可以從 `dict` 中刪除某個鍵值對，每次刪除 1 個。

如果某個 `key` 存在於 `dict` 中，則 `key in dict` 回傳的結果為 `True`，如果不存在則為 `False`。
所以你可以使用 `if key in dict:` 來判斷 `dict` 是否包含該鍵。

將字典放入 `for` 迴圈中可以迭代所有的鍵：
{{codeexample 
{
    "show_image": false,
    "show_code": true,
    "show_inventory": false,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 100,
    "seed": 0,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
right_of = {North:East, East:South, South:West, West:North}
print(North in right_of)
for key in right_of:
	value = right_of[key]
	print(key, ":", value)
}}

迭代鍵的順序無法保證。

另請參閱[集合](docs/scripting/sets.md)

---

[串列](docs/scripting/lists.md)      [集合](docs/scripting/sets.md)      [元組](docs/scripting/tuples.md)      [成本](docs/unlocks/costs.md)

[len()](functions/len)

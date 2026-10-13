[<- 速度升級](docs/unlocks/speed.md)
---
# If 陳述式
作用是條件判斷，你可以使用 `if`、`elif` 和 `else` 來選擇性地執行程式碼。

{{codeexample 
{
    "camera_position": {"x": 0, "y": 1.5, "z": 4},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
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
#CODE
condition1 = False
condition2 = False
condition3 = True

if condition1:
	do_a_flip()
elif condition2:
	harvest()
else:
	do_a_flip()
	harvest()
}}

## 語法
`if` 陳述式會讓程式碼區塊滿足某個條件為 `True` 時執行，如同一個不迴圈的 `while` 迴圈。
`if` 陳述式就像 `while` 迴圈一樣會判斷條件，如果判斷結果為 `True`，則執行程式碼區塊：

{{codeexample 
{
    "camera_position": {"x": 0, "y": 1.5, "z": 4},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
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
#CODE
condition = True

if condition:
	do_a_flip()
}}

你還可以在 `if` 之後新增 1 個 `else`，`else` 程式碼區塊會在條件為 `False` 時執行。

{{codeexample 
{
    "camera_position": {"x": 0, "y": 1.5, "z": 4},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
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
#CODE
condition = False

if condition:
	do_a_flip()
else:
	harvest()
}}

`elif` 是 else if 的縮寫。

`if condition1:
	#a
else:
	if condition2:
		#b
	else:
		#c`

可以縮短為：

`if condition1:
	#a
elif condition2:
	#b
else:
	#c`

---

[While 迴圈](docs/scripting/while.md)      [運算子](docs/scripting/operators.md)      [感官](docs/unlocks/senses.md)

[<- While 迴圈](docs/scripting/while.md)
---
# Break 陳述式
`break` 陳述式的作用是：提前停止它所在的迴圈。當執行到 `break` 陳述式時，會立即跳出該迴圈，並開始執行該迴圈之後的程式碼。

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
for i in range(10):
	break
print(i)
}}

這段程式碼會列印 `0`，因為在迴圈的第 1 次迭代中 `i` 是 `0`，然後 `break` 陳述式跳出了迴圈。

該陳述式也適用於 `while` 迴圈。

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
plant(Entities.Tree)
#CODE
while True:
	if can_harvest():
		break
harvest()
}}

這段程式碼會一直執行 `while` 迴圈，直到 `can_harvest()` 函式執行的結果為 `True`。
其效果與以下程式碼相同：

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
plant(Entities.Tree)
#CODE
while not can_harvest():
	pass
harvest()
}}

在巢狀迴圈中，`break` 陳述式始終退出它所在的迴圈。

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
for i in range(10):
	for j in range(10):
		break
		print("這句永遠不會列印")
	print("這句會列印 10 次")
}}

---

[While 迴圈](docs/scripting/while.md)      [For 迴圈](docs/scripting/for.md)      [Continue 陳述式](docs/scripting/continue.md)

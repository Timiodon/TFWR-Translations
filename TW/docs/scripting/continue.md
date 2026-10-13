[<- While 迴圈](docs/scripting/while.md)
---
# Continue 陳述式
`continue` 陳述式的作用是：停止它所在迴圈的本次迭代，並跳轉到該迴圈的下一次迭代。

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
	print("這句每次都會列印")
	continue
    print("這句永遠不會列印")
}}

這會執行迴圈的所有 `10` 次迭代，但 `continue` 陳述式之後的 `print` 陳述式每次都會被跳過。

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
	if not can_harvest():
		continue
    
    harvest()
}}

這段程式碼只有當 `can_harvest()` 函式執行的結果為 `True` 時，才會呼叫 `harvest()` 函式。
效果與以下程式碼相同：

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
		harvest()
}}

在巢狀迴圈中，`continue` 陳述式始終影響它所在的迴圈。

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
for i in range(2):
	for j in range(2):
	    print("這句會列印 4 次")
		continue
		print("這句永遠不會列印")
	print("這句會列印 2 次")
}}

---

[While 迴圈](docs/scripting/while.md)      [For 迴圈](docs/scripting/for.md)      [Break 陳述式](docs/scripting/break.md)

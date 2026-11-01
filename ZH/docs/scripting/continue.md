[<- While 循环](docs/scripting/while.md)
---
# Continue 语句
`continue` 语句的作用是：停止它所在循环的本次迭代，并跳转到该循环的下一次迭代。

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
	print("这句每次都会打印")
	continue
	print("这句永远不会打印")
}}

这会运行循环的所有 `10` 次迭代，但 `continue` 语句之后的 `print` 语句每次都会被跳过。

该语句也适用于 `while` 循环。

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

这段代码只有当 `can_harvest()` 函数运行的结果为 `True` 时，才会调用 `harvest()` 函数。
效果与以下代码相同：

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

在嵌套循环中，`continue` 语句始终影响它所在的循环。

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
		print("这句会打印 4 次")
		continue
		print("这句永远不会打印")
	print("这句会打印 2 次")
}}

---

[While 循环](docs/scripting/while.md)      [For 循环](docs/scripting/for.md)      [Break 语句](docs/scripting/break.md)

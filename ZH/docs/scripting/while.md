[<- 第一个程序](docs/first_program.md) <right>[速度升级 ->](docs/unlocks/speed.md)
---
# While 循环
你已经解锁了 `while` 循环和 `True`、`False` 这两个值。`while` 循环会在条件为 `True` 的情况下一直执行循环体。

`while 条件:
	#循环体`

不用担心创建无限循环。无人机可能会卡住，但整个游戏不会冻结。只要停止当前程序，就能再试一次。

## 面向初学者
也许你已经试过连续写好几个 `harvest()` 函数：

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
    "operation_ticks": 200,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
do_a_flip()
#CODE
harvest()
harvest()
harvest()
}}
这样，你只需运行 1 次 程序，即可收获多次。
然而，如果能收获超过 3 次就更好了，而多次出现重复代码会很快让程序变得杂乱。
解决方法是使用循环。
循环能让你多次运行相同的代码。

while 循环需要 1 个条件来判断，条件比较的结果为逻辑值，只能是两种状态之一：`True` 或 `False`。
这样的值被称为布尔值。

然后循环就会执行循环内的代码，直到条件变为 False。
while 循环的形式如下：

`while 条件:
	#循环体
	#循环体
	#...`

你需要将“条件”换成布尔值，将 `#循环体` 换成循环中想做的事情。

有 2 个可用的常量布尔值。常量是在程序运行期间永远不会改变的值。

要创建布尔常量，只需写 `True` 或 `False`。
所以你可以写

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
    "operation_ticks": 200,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
while False:
	do_a_flip()
}}
或者

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
    "operation_ticks": 200,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
while True:
	do_a_flip()
}}
第一个永远不会翻转，第二个会永远重复翻转（一个无限循环）。

创建无限循环通常不是个好主意，因为会导致程序卡死，但在这款游戏中，循环的每次迭代之间都有延迟，所以它只会让无人机一直翻转，直到你再次按下执行按钮手动让它停下。

注意冒号后面的行是如何缩进的。这样的缩进是用来分隔代码块的。
按 Tab 键即可添加缩进，按 Shift + Tab（或 Backspace）即可移除缩进。选中多行时，Tab 和 Shift + Tab 会对所有选中行生效。

注意：如果通过 Steam 游玩，按 Shift + Tab 会打开 Steam 界面。你可以在游戏选项中重新绑定取消缩进快捷键，或在 Steam 设置中更改界面快捷键。

这里，`do_a_flip()` 和 `pet_the_piggy()` 位于缩进的 `while` 代码块中，因此会被反复调用。而 `harvest()` 在代码块之后，永远不会运行。
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
    "operation_ticks": 200,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
while True:
	do_a_flip()
	pet_the_piggy()
harvest()
}}

---

[For 循环](docs/scripting/for.md)      [If 语句](docs/scripting/if.md)      [Break 语句](docs/scripting/break.md)      [Continue 语句](docs/scripting/continue.md)      [外部编辑器](docs/external_editor.md)

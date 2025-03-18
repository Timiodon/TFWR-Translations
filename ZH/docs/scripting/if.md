# If
你可以使用 if、elif 和 else 来有条件地运行代码。

`if condition1:
	do_a_flip()
elif condition2:
	harvest()
else:
	do_a_flip()
	harvest()`

## 语法
`if` 允许你仅在某些条件为 `True` 时运行代码。它们就像一个不循环的 `while` 循环。
`if` 需要一个条件，就像 `while` 循环，如果条件判断为 `True`，则执行 if 块中的代码：

`#如果条件为 True，就翻转
if condition:
	do_a_flip()`

你也可以在 if 后面添加一个 `else`，用于定义当条件判断为 `False` 时要执行的代码。

如果 `condition` 为 True 就翻转，否则就收获。
`if condition:
	do_a_flip()
else:
	harvest()`

`elif` 是 else if 的缩写。

`if condition1:
	#a
else:
	if condition2:
		#b
	else:
		#c`

可以简化为：

`if condition1:
	#a
elif condition2:
	#b
else:
	#c`
# If 语句
你可以使用 if、elif 和 else 来有条件地运行代码。

`if condition1:
	do_a_flip()
elif condition2:
	harvest()
else:
	do_a_flip()
	harvest()`

## 语法
`if` 语句允许你仅在某个条件为 `True` 时运行代码。它们就像一个不循环的 `while` 循环。
`if` 语句接受一个条件，就像 `while` 循环一样，如果条件求值为 `True`，则执行 if 代码块：

`#如果条件为 True，则翻转
if condition:
	do_a_flip()`

你还可以在 if 之后添加一个 `else`，它定义了当条件求值为 `False` 时要执行的代码。

如果 `condition` 为 True，则翻转，否则收获。
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

可以缩短为：

`if condition1:
	#a
elif condition2:
	#b
else:
	#c`
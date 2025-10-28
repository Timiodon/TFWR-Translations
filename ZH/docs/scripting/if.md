# If 语句
作用是条件判断，你可以使用 if、elif 和 else 来选择性地运行代码。

`if condition1:
	do_a_flip()
elif condition2:
	harvest()
else:
	do_a_flip()
	harvest()`

## 语法
`if` 语句会让代码块满足某个条件为 `True` 时运行，如同一个不循环的 `while` 循环。
`if` 语句就像 `while` 循环一样会判断条件，如果判断结果为 `True`，则执行 if 代码块：

`#如果条件为 True，则翻转
if condition:
	do_a_flip()`

你还可以在 `if` 之后添加 1 个 `else`，后者定义的是当 `if` 判断结果的为 `False` 时需要执行的代码。

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

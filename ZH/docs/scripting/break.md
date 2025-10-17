# Break 语句
`break` 语句的作用是：提前停止它所在的循环。当执行到 `break` 语句时，会立即跳出该循环，并开始运行该循环之后的代码。

`for i in range(10):
	break
print(i)`

这段代码会打印 `0`，因为在循环的第 1 次迭代中 `i` 是 `0`，然后 `break` 语句跳出了循环。

“迭代”的意思就是：俗称的循环 1 次，循环中的每次循环就是 1 次“迭代”。

该语句也适用于 `while` 循环。

`while True:
	if can_harvest():
		break`

这段代码会一直运行 `while` 循环，直到 `can_harvest()` 函数运行的结果为 `True`。
其效果与以下代码相同：

`while not can_harvest():
	pass`

在嵌套循环中，`break` 语句始终退出它所在的循环。

`for i in range(10):
	for j in range(10):
		break
		print("这句永远不会打印")
	print("这句会打印 10 次")`
# Break
`break` 允许提前停止循环。当执行到 `break` 语句时，它将立即退出最内层的循环，并开始运行循环之后的代码。

`for i in range(10):
	break
print(i)`
这会打印 `0`，因为在循环的第一次迭代中 `i` 是 `0`，然后 break 语句结束了循环。

它也适用于 `while` 循环。

`while True:
	if can_harvest():
		break`

这段代码会一直运行 `while` 循环，直到 `can_harvest()` 为 `True`。
它的效果与下面相同：

`while not can_harvest():
	pass`

在嵌套循环中，`break` 总是退出最内层的循环。

`for i in range(10):
	for j in range(10):
		break
		print("这行永远不会被打印")
	print("这行被打印 10 次")`
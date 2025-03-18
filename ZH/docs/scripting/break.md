# Break
`break` 允许提前停止循环。当遇到 `break` 语句时，它将立即退出最内层的循环，开始执行循环之后的代码。

`for i in range(10):
	break
print(i)`
这段代码会打印 `0`，因为在循环的第一次迭代中，`i` 是 `0`，然后 break 语句结束了循环。

它同样适用于 `while` 循环。

`while True:
	if can_harvest():
		break`

这段代码在 `can_harvest()` 为 `True` 前会一直运行 `while` 循环。
它的效果与

`while not can_harvest():
	pass`

相同。

在嵌套循环中，`break` 总是退出最内层的循环。

`for i in range(10):
	for j in range(10):
		break
		print("this is never printed")
	print("this is printed 10 times")`
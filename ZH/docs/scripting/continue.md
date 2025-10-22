# Continue 语句
`continue` 语句的作用是：停止它所在循环的本次迭代，并跳转到该循环的下一次迭代。

`for i in range(10):
	continue
    print("这句永远不会打印")`

这会运行循环的所有 `10` 次迭代，但 `continue` 语句之后的 `print` 语句每次都会被跳过。

该语句也适用于 `while` 循环。

`while True:
	if not can_harvest():
		continue
    
    harvest()`

这段代码只有当 `can_harvest()` 函数运行的结果为 `True` 时，才会调用 `harvest()` 函数。
效果与以下代码相同：

`while True:
	if can_harvest():
		harvest()`

在嵌套循环中，`continue` 语句始终影响它所在的循环。

`for i in range(10):
	for j in range(10):
	    print("这句会打印 100 次")
		continue
		print("这句永远不会打印")
	print("这句会打印 10 次")`
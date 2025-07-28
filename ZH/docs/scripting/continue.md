# Continue
continue 允许停止循环的当前迭代，并跳转到最内层循环的下一次迭代。

`for i in range(10):
	continue
    print("这行永远不会被打印")`

这会运行循环的所有 `10` 次迭代，但在 `continue` 之后的 `print` 语句总是被跳过。

它也适用于 `while` 循环。

`while True:
	if not can_harvest():
		continue
    
    harvest()`

这段代码只有在 `can_harvest()` 为 `True` 时才调用 `harvest()`。
它的效果与下面相同：

`while True:
	if can_harvest():
		harvest()`

在嵌套循环中，`continue` 总是影响最内层的循环。

`for i in range(10):
	for j in range(10):
	    print("这行被打印 100 次")
		continue
		print("这行永远不会被打印")
	print("这行被打印 10 次")`
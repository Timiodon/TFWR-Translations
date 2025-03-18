# Continue
`continue` 用于停止当前循环的迭代，并跳到最内层循环的下一次迭代。

`for i in range(10):
	continue
    print("this is never printed")`

这个代码运行了循环的全部 `10` 次迭代，但 `continue` 后面的 `print` 语句总是被跳过。

它也适用于 `while` 循环。

`while True:
	if not can_harvest():
		continue
    
    harvest()`

这段代码只有在 `can_harvest()` 为 `True` 时才会调用 `harvest()`。
这与以下代码效果相同

`while True:
	if can_harvest():
		harvest()`

在嵌套循环中，`continue` 总是影响最内层的循环。

`for i in range(10):
	for j in range(10):
	    print("this is printed 100 times")
		continue
		print("this is never printed")
	print("this is printed 10 times")`
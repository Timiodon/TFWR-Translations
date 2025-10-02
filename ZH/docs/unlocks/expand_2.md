# 扩张 2
你的农场又扩张了！现在地块不再是整齐的一行，所以你需要想办法遍历一个方形网格。

在使用 `while` 循环的情况下，若尚未解锁感官和运算符，则无法实现这一点。
那么是时候介绍 `for` 循环了。

在 [For 循环](docs/scripting/for.md)页面上可以阅读所有关于 `for` 循环的内容，但目前你只需要用它来重复执行代码固定的次数。

`#做 n 次翻转
for i in range(5):
	do_a_flip()`

`range(n)` 创建了一个从 `0` 到 `n-1` 的数字范围，其中包含 `n` 个元素。`for` 循环对序列中的每个元素执行一次循环体。在这个例子中，`do_a_flip()` 将被调用 `5` 次。

函数 `get_world_size()` 现在也可以使用了。它会返回你农场的边长，以便你编写的代码在下次扩张升级后不会失效。

`for i in range(get_world_size()):
	harvest()
	move(North)`

在此示例中，不论农场多大，无人机都会收获农场的一列。

如果想不出来该如何使无人机覆盖整个农场移动，请看下面的提示。
<spoiler=显示提示>当然，在农场范围内移动的方法有好几种。
我们要找的是一种系统性的遍历方法，确保代码在农场再次扩大时不会失效。
若要覆盖到农场的每个地块，其中一种系统性方法便是永远重复以下两个步骤：

1.向 `North` 移动，直到绕回原点。
2.向 `East` 移动。

`for i in range(get_world_size()):` 可能有助于将这个想法转化为代码。
</spoiler>
<spoiler=显示可能的解决方案> 基本的遍历可能如下所示：

`for i in range(get_world_size()):
	for j in range(get_world_size()):
		#在每个地块上翻转一次
		do_a_flip()
		move(North)
	move(East)`
</spoiler>
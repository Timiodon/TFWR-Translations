# 扩张 2
你的农场又扩张了！现在地块不再是整齐的一行，所以你需要找到一种方法来遍历一个方形网格。

在使用 `while` 循环的情况下，在你解锁感官和运算符之前这是不可能的。
是时候介绍 `for` 循环了。

你可以在[For 循环](docs/scripting/for.md)页面上阅读所有关于 `for` 循环的内容，但现在你只需要用它来重复执行代码固定的次数。

`#做 n 次翻转
for i in range(5):
	do_a_flip()`

`range(n)` 创建了一个从 `0` 到 `n-1` 的数字范围，其中包含 `n` 个元素。`for` 循环对序列中的每个元素执行一次循环体。在这个例子中，`do_a_flip()` 将被调用 `5` 次。

函数 `get_world_size()` 现在也可用了。它返回你农场的边长。这样你就可以编写在下次扩张升级后不会失效的代码。

`for i in range(get_world_size()):
	harvest()
	move(North)`

这个例子在任何农场大小下都会收获农场的一列。

如果你在如何移动无人机绕农场一圈的问题上卡住了，请看下面的提示。
<spoiler=显示提示>当然，有几种方法可以在农场里移动。
我们正在寻找一种系统性的方法来遍历它，这种方法在农场再次扩大时不会失效。
一种到达农场上每个地方的系统性方法是永远重复以下两个步骤：

1.向 `North` 移动，直到它绕回。
2.向 `East` 移动

`for i in range(get_world_size()):` 可能有助于将这个想法转化为代码。
</spoiler>
<spoiler=显示可能的解决方案> 基本的遍历可能看起来像这样：

`for i in range(get_world_size()):
	for j in range(get_world_size()):
		#在每个地块上翻转
		do_a_flip()
		move(North)
	move(East)`
</spoiler>
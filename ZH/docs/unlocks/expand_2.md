# 扩展 2
你的农场又扩展了！现在地块不再是一条整齐的行，所以你需要找到一种方法来遍历一个方形网格。

用 `while` 循环在解锁感应和运算符之前是无法做到的。是时候介绍 `for` 循环了。

你可以在 [For Loop](docs/scripting/for.md) 页面上阅读所有关于 `for` 循环的内容，但现在你只需要用它来重复执行代码固定次数。

`#翻转 n 次
for i in range(5):
	do_a_flip()`

`range(n)` 创建一个从 `0` 到 `n-1` 的数字范围，其中包含 `n` 个元素。`for` 循环对序列中的每个元素运行一次循环体。在这个例子中，`do_a_flip()` 将被调用 `5` 次。

现在还可以使用函数 `get_world_size()`。它返回你的农场的边长。这样你就可以编写不会因为下一次扩展升级而出错的代码。

`for i in range(get_world_size()):
	harvest()
	move(North)`

这个例子为任何农场大小收割一列地块。

如果你在如何让无人机在农场上移动感到困惑，可以查看下面的提示。
<spoiler=显示提示>当然，有几种方法可以在农场上移动。
我们在寻找一种不会因为农场再次扩展而出问题的系统化遍历方式。
一个系统化走遍农场每个地方的方法是永远重复以下2个步骤：

1. 向 `North` 移动，直到它回绕。
2. 向 `East` 移动。

`for i in range(get_world_size()):` 可能对将这个思路转化为代码有所帮助。
</spoiler>
<spoiler=显示可能的解决方案> 基本的遍历可能看起来像这样：

`for i in range(get_world_size()):
	for j in range(get_world_size()):
		#在每个瓷砖上翻转一次
		do_a_flip()
		move(North)
	move(East)`
</spoiler>
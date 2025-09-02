# 速度升级
执行速度加倍了。问题是，无人机现在收获的速度比草生长的速度还快，导致根本没有收成。为了解决这个问题，现在解锁了 [if](docs/scripting/if.md) 分支和 [can_harvest](functions/can_harvest) 函数。

## 在收获前检查
到目前为止，我们只用 `True` 和 `False` 作为条件，这对于 `if` 来说当然不是很有用。

新函数 can_harvest() 提供了一个更好的条件。如果无人机下方的植物可以被收获，`can_harvest()` 返回 `True`，否则返回 `False`。

`if can_harvest():
	#做点什么`

你可以像这样使用这个函数作为条件的原因是，它返回一个布尔值。

返回值本质上意味着在功能执行后，函数调用表达式的求值结果就是返回的值。

当上面的代码运行时会发生什么：
	-if 语句运行
	-`can_harvest()` 被调用
	-`can_harvest()` 执行其功能
	-`can_harvest()` 返回 `True` 或 `False`
	-语句现在变成了 `if True:` 或 `if False:`
	-只有在可以收获时，代码块才会被执行

现在我们可以使用 `if` 来防止无人机过早收获。
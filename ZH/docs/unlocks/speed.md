# 速度升级
执行速度已经翻倍。问题是，现在无人机收获的速度比草生长的速度还快，导致根本无法收获。为了解决这个问题，现在解锁了 [if](docs/scripting/if.md) 分支和 [can_harvest](functions/can_harvest) 函数。

## 收获前检查
到目前为止，我们只用 `True` 和 `False` 作为条件，这对于 `if` 来说当然不是很有用。

新的 `can_harvest()` 函数提供了一个更好的条件。`can_harvest()` 会在无人机下方的植物可以被收获时返回 `True`，否则返回 `False`。

`if can_harvest():
	#do something`

你可以像这样使用这个函数作为条件，因为它返回一个布尔值。

返回值基本上意味着在功能执行后，函数调用表达式会计算为返回的值。

当以上代码运行时会发生什么：
	- if 运行
	- `can_harvest()` 被调用
	- `can_harvest()` 做它的事情
	- `can_harvest()` 返回 `True` 或 `False`
	- 语句现在是 `if True:` 或 `if False:`
	- 只有在可以收获时，代码块才会被执行

现在我们可以使用 `if` 来防止无人机过早地收获了。
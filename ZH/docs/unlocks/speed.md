# 速度升级
执行速度已经翻倍。问题是，现在无人机收获的速度比草生长的速度要快，导致完全没有收成。为了解决这个问题，[if](docs/scripting/if.md) 分支和 [can_harvest](functions/can_harvest) 函数现在已解锁。

## 收获前的检查
到目前为止，我们只有 `True` 和 `False` 作为条件，这当然对于 `if` 来说不是很有用。

新的函数 can_harvest() 提供了更好的条件。`can_harvest()` 如果无人机下的植物可以收获，则返回 `True`，否则返回 `False`。

`if can_harvest():
	#do something`

你可以这样使用这个函数作为条件的原因是它返回一个布尔值。

返回值基本上意味着在功能执行后，函数调用表达式会计算为返回的值。

以上代码运行时发生的情况：
	- if 运行
	- 调用 `can_harvest()`
	- `can_harvest()` 执行其功能
	- `can_harvest()` 返回 `True` 或 `False`
	- 语句现在是 `if True:` 或 `if False:`
	- 代码块只有在可以收获时才会执行

现在我们可以使用 `if` 来防止无人机过早收获。
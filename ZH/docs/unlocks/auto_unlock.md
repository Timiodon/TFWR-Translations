# 自动解锁
要完全自动化游戏，可以使用 `unlock()` 函数来自动解锁功能。
例如，你可以使用 `unlock(Unlocks.Speed)` 和 `unlock(Unlocks.Expand)` 来解锁速度和扩张功能。

要确定解锁的成本，只需像对植物或物品一样使用 `get_cost()` 函数。
示例：
`get_cost(Unlocks.Loops)`
返回 `{Items.Hay:5}`

# 自动解锁
你可以调用 `unlock()` 函数使科技树中的项目进行自动解锁，这可以实现完全自动化，解放双手！
例如，你可以调用 `unlock(Unlocks.Speed)` 和 `unlock(Unlocks.Expand)` 函数来解锁速度和扩张土地。

对科技树中的项目使用 `get_cost()` 函数，就可以获取该项目解锁或者升级所需的耗材数量，就像对植物或物品使用函数那样。
示例：
`get_cost(Unlocks.Loops)`
返回 `{Items.Hay:5}`

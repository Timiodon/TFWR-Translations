# 自动解锁
要完全自动化游戏，你可以使用 `unlock()` 函数来自动解锁功能。
例如，你可以使用 `unlock(Unlocks.Speed)` 和 `unlock(Unlocks.Expand)` 来解锁速度和扩张功能。

要确定解锁的成本，只需像对植物或物品那样使用 `get_cost()` 函数。
示例：
`get_cost(Unlocks.Loops)`
返回 `{Items.Hay:5}`

如果你想知道你拥有某个特定解锁的数量，请使用 `num_unlocked(unlock)` 函数。

例如，`num_unlocked(Unlocks.Speed)` 将返回你拥有的速度升级数量。

`num_unlocked(Unlocks.Senses)` 如果感官已解锁，则返回 `1`，否则返回 `0`。

你也可以对物品、实体或地块使用 `num_unlocked()`。如果已解锁，它将返回 `1`，否则返回 `0`。

请注意，`num_unlocked(Unlocks.Carrots)` 将返回它被解锁/升级的次数。
`num_unlocked(Items.Carrot)` 只会返回 `0` 或 `1`。（对其他植物也一样）
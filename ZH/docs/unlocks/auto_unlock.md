# 自动解锁
要完全自动化游戏，您可以使用`unlock()`函数自动解锁功能。
例如，您可以使用`unlock(Unlocks.Speed)`和`unlock(Unlocks.Expand)`来解锁速度和扩展功能。

要确定解锁的成本，只需像查询植物或物品一样使用`get_cost()`函数。
例子：
`get_cost(Unlocks.Loops)`
返回`{Items.Hay:5}`

如果您想知道您拥有某个特定解锁的数量，使用`num_unlocked(unlock)`函数。

例如，`num_unlocked(Unlocks.Speed)`将返回您拥有的速度升级的数量。

`num_unlocked(Unlocks.Senses)`如果感知功能已解锁则返回`1`，否则返回`0`。

您也可以在Items、Entities或Grounds上使用`num_unlocked()`。如果已解锁则返回`1`，否则返回`0`。

注意，`num_unlocked(Unlocks.Carrots)`将返回它被解锁/升级的次数。
`num_unlocked(Items.Carrot)`只会返回`0`或`1`。（其他植物也是一样）
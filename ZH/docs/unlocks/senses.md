# 感官
无人机现在能看见了！

函数 `get_pos_x()` 和 `get_pos_y()` 返回无人机当前的 x 和 y 坐标。在起始位置，它们都是 `0`。x 坐标向 `East` 方向每格增加 `1`，y 坐标向 `North` 方向每格增加 `1`。

`num_items(item)` 返回你拥有多少某个物品。
例如 `num_items(Items.Hay)` 返回你拥有多少干草。

`get_entity_type()` 和 `get_ground_type()` 返回无人机下方的实体或地面类型。

如果你在一棵灌木上，就翻个跟头：
`if get_entity_type() == Entities.Bush:
	do_a_flip()`

`None` 关键字现在也解锁了！`None` 是一个表示没有值的值。
例如，一个没有 `return` 语句的函数实际上会返回 `None`。

如果无人机下方没有实体，`get_entity_type()` 会返回 `None`。


如果你想知道你拥有多少某个特定的解锁项，请使用 `num_unlocked(unlock)` 函数。

例如，`num_unlocked(Unlocks.Speed)` 会返回你拥有的速度升级数量。

`num_unlocked(Unlocks.Senses)` 如果感官已解锁则返回 `1`，否则返回 `0`。

你也可以对物品、实体或地面使用 `num_unlocked()`。如果它已解锁则返回 `1`，否则返回 `0`。

小心 `num_unlocked(Unlocks.Carrots)` 会返回它被解锁/升级的次数。
`num_unlocked(Items.Carrot)` 只会返回 `0` 或 `1`。（其他植物也一样）
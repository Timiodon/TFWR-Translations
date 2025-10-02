# 感官
无人机现在能看见了！

函数 `get_pos_x()` 和 `get_pos_y()` 返回无人机当前的 x 和 y 坐标。在起始位置时，返回的都是 `0`。x 坐标向 `East` 方向每格增加 `1`，y 坐标向 `North` 方向每格增加 `1`。

`num_items(item)` 返回你拥有某种物品的数量。
例如，`num_items(Items.Hay)` 就会返回你拥有的干草数量。

`get_entity_type()` 和 `get_ground_type()` 返回无人机下方的实体或地块类型。

如果在灌木上方，就翻转一次：
`if get_entity_type() == Entities.Bush:
	do_a_flip()`

`None` 关键字现在也解锁了！`None` 是一个表示没有值的值。
例如，一个没有 `return` 语句的函数实际上就会返回 `None`。

如果无人机下方没有实体，`get_entity_type()` 会返回 `None`。


如果想知道你拥有的某个特定解锁项的数量，请使用 `num_unlocked(unlock)` 函数。

例如，`num_unlocked(Unlocks.Speed)` 会返回你拥有的速度升级的数量。

如果感官已解锁，`num_unlocked(Unlocks.Senses)` 会返回 `1`，否则返回 `0`。

你也可以对物品、实体或地块使用 `num_unlocked()`，已解锁会返回 `1`，否则返回 `0`。

注意，`num_unlocked(Unlocks.Carrots)` 会返回胡萝卜被解锁/升级的次数。
`num_unlocked(Items.Carrot)` 则只会返回 `0` 或 `1`。（其他植物也一样）
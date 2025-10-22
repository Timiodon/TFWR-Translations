# 感官
无人机现在拥有视觉能力了！

调用 `get_pos_x()` 和 `get_pos_y()` 函数会返回无人机当前的 x 和 y 坐标。在起始位置时，返回的都是 `(0,0)` 。x 的坐标向 `East` （右）方向每格增加 `1`，y 的坐标向 `North` （上）方向每格增加 `1`。

调用 `num_items(item)` 函数会返回你现在拥有某种物品的数量。
例如，调用 `num_items(Items.Hay)` 函数就会返回你现在拥有的干草数量。

调用 `get_entity_type()` 和 `get_ground_type()` 函数会返回无人机当前下方实体或地块类型。

如果在灌木上方，就翻转一次：
`if get_entity_type() == Entities.Bush:
	do_a_flip()`

`None` 关键字现在也解锁了！`None` 是一个表示没有值的值。
例如，调用一个没有 `return` 语句的函数实际上就会返回 `None`。

如果无人机下方没有实体，调用 `get_entity_type()` 函数会返回 `None`。


如果想知道你现在拥有的某个特定科技树项目的数量，可以调用 `num_unlocked(unlock)` 函数。

例如，调用 `num_unlocked(Unlocks.Speed)` 函数会返回你现在拥有的速度的等级。

如果感官已解锁，调用 `num_unlocked(Unlocks.Senses)` 函数会返回 `1`，否则返回 `0`。

你也可以对物品、实体或地块调用 `num_unlocked()` 函数，已解锁会返回 `1`，否则返回 `0`。

请注意：调用 `num_unlocked(Unlocks.Carrots)` 函数会返回胡萝卜是否被解锁或者胡萝卜当前的等级。
调用 `num_unlocked(Items.Carrot)` 函数则只会返回 `0` 或 `1`。（其他植物也一样）
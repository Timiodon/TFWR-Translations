# 感官
无人机现在能看见东西了！

函数 `get_pos_x()` 和 `get_pos_y()` 返回无人机当前的 x 和 y 坐标。在起始位置，它们都是 `0`。x 坐标向 `East` 每移动一格增加 `1`，y 坐标向 `North` 每移动一格增加 `1`。

`num_items(item)` 返回你拥有多少某个物品。
例如 `num_items(Items.Hay)` 返回你有多少干草。

`get_entity_type()` 和 `get_ground_type()` 返回无人机下方的 entity 或地面的类型。

如果你在一棵灌木上，就做一个翻转：
`if get_entity_type() == Entities.Bush:
	do_a_flip()`

现在 `None` 关键字也解锁了！`None` 是一个表示“没有值”的值。
例如，一个没有 `return` 语句的函数实际上会返回 `None`。

如果无人机下方没有 entity，`get_entity_type()` 会返回 `None`。
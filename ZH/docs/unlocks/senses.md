# 感知
无人机现在可以看见了！

函数 `get_pos_x()` 和 `get_pos_y()` 返回无人机当前的 x 和 y 位置。在起始位置，它们都是 `0`。x 位置每个方格向 `East` 增加 `1`，y 位置每个方格向 `North` 增加 `1`。

`num_items(item)` 返回你拥有多少个某物品。
例如 `num_items(Items.Hay)` 返回你有多少干草。

`get_entity_type()` 和 `get_ground_type()` 返回无人机下方的实体类型或地面类型。

如果你在一个灌木丛上方，就翻个跟斗：
`if get_entity_type() == Entities.Bush:
	do_a_flip()`

关键字 `None` 现在也可以用了！`None` 是一个表示没有值的值。
例如，没有 `return` 语句的函数实际上会返回 `None`。

如果无人机下没有实体，`get_entity_type()` 会返回 `None`。
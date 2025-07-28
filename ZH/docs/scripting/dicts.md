# Dictionaries
Dictionary 是一种数据结构，它允许你将 key 映射到 value，就像一本真正的词典将单词映射到它们的定义一样，你可以非常快速地查找它们。

可以像这样创建一个 dictionary：
`right_of = {North:East, East:South, South:West, West:North}`

冒号前的表达式是 key，冒号后的表达式是 key 映射到的 value。
上面的 dictionary 将每个方向映射到它右边的方向。

这是另一个将无人机的位置映射到它上方 entity 的例子。
`x, y = get_pos_x(), get_pos_y()
entity_dict = {(x,y):get_entity_type()}`

访问映射到 key 的 value 类似于访问 list 中的元素：
`value = dict[key]`

示例：
`orientation = right_of[South]`
这将 `orientation` 设置为 `West`。

你可以像这样向 dictionary 添加一个新的键值对：
`dict[key] = value`

示例：
`entity_dict[(get_pos_x(), get_pos_y())] = get_entity_type()`
这会更新当前位置存储的 entity。

Key 是唯一的，所以添加一个 dictionary 中已经存在的 key 会覆盖之前的值。

使用 `dict.pop(key)` 从 `dict` 中移除一个键值对。

如果 `key` 是 `dict` 中的一个 key，`key in dict` 的评估结果为 `True`，否则为 `False`。
所以你可以使用 `if key in dict:` 来检查 `dict` 是否包含该 key。

将一个 dictionary 放入 for 循环中，可以让你遍历所有的 key：
`for key in dict:
	value = dict[key]`

对于 key 的迭代顺序没有任何保证。

另见 [Sets](docs/scripting/sets.md)
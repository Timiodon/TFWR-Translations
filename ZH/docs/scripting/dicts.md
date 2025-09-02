# 字典
字典是一种数据结构，它允许你将键映射到值，就像真实世界中的字典将单词映射到它们的定义一样，你可以非常快速地查找它们。

可以这样创建一个字典：
`right_of = {North:East, East:South, South:West, West:North}`

冒号前的表达式是键，冒号后的表达式是键映射到的值。
上面的字典将每个方向映射到它右边的方向。

这是另一个将无人机位置映射到其上方实体的字典。
`x, y = get_pos_x(), get_pos_y()
entity_dict = {(x,y):get_entity_type()}`

访问映射到键的值类似于访问列表中的元素：
`value = dict[key]`

示例：
`orientation = right_of[South]`
这将 `orientation` 设置为 `West`。

你可以这样向字典添加一个新的键值对：
`dict[key] = value`

示例：
`entity_dict[(get_pos_x(), get_pos_y())] = get_entity_type()`
这会更新当前位置存储的实体。

键是唯一的，所以添加一个字典中已存在的键会覆盖之前的值。

使用 `dict.pop(key)` 从 `dict` 中移除一个键值对。

如果 `key` 是 `dict` 中的一个键，`key in dict` 的结果为 `True`，否则为 `False`。
所以你可以使用 `if key in dict:` 来检查 `dict` 是否包含该键。

将字典放入 for 循环中可以让你遍历所有的键：
`for key in dict:
	value = dict[key]`

对于键的迭代顺序没有任何保证。

另请参阅[集合](docs/scripting/sets.md)
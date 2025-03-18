# Dictionaries
Dictionaries 是一种数据结构，可以将键映射到值，就像真实的字典将单词映射到它们的定义一样，你可以很快地查找它们。

可以这样创建一个 dictionary：
`rotation = {North:East, East:South, South:West, West:North}`

冒号前的表达式是键，冒号后的表达式是键所映射的值。
上述 dictionary 将每个方向映射到其右侧的方向。

这里有另一个 dictionary，将无人机的位置映射到它上方的 entity。
`x, y = get_pos_x(), get_pos_y()
entity_dict = {(x,y):get_entity_type()}`

访问映射到某个键的值与访问列表中的元素类似：
`value = dict[key]`

例子：
`orientation = rotation[South]`
这会将 `orientation` 设置为 `West`。

你可以这样向 dictionary 添加新的键值对：
`dict[key] = value`

例子：
`entity_dict[(get_pos_x(), get_pos_y())] = get_entity_type()`
这会更新当前位置信息所存储的 entity。

键是唯一的，所以在 dictionary 中添加已存在的键会覆盖先前的值。

使用 `dict.pop(key)` 从 `dict` 中移除一个键值对。

`key in dict` 如果 `key` 是 `dict` 中的一个键则返回 `True`，否则返回 `False`。
所以你可以使用 `if key in dict:` 来检查 `dict` 是否包含该键。

将 dictionary 放入 for 循环中可以遍历所有键：
`for key in dict:
	value = dict[key]`

对于键的迭代顺序没有保证。

另请参阅 [Sets](docs/scripting/sets.md)
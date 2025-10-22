# 字典
字典是一种可以将键 (`key`) 映射到值 (`value`) 的数据结构，就像现实生活中的菜单。没错，我的意思就是餐馆的菜单，每道菜对应 1 个价格，菜的价格可以重复，但是菜品只有一个。

字典创建的方式如下：
`right_of = {North:East, East:South, South:West, West:North}`

冒号前面是 `key` ，冒号后面是 `key` 对应的 `value` 。
上面的字典将每个方向映射到它右边的方向。

下面是另一个将无人机位置映射到它下方实体的字典。
`x, y = get_pos_x(), get_pos_y()
entity_dict = {(x,y):get_entity_type()}`

获取 `key` 对应的 `value` 的方式类似于访问列表中的元素：
`value = dict[key]`

示例：
`orientation = right_of[South]`
这会将 `orientation` 设置为 `West`。

向字典添加 1 个新的键值对的方式如下：
`dict[key] = value`

示例：
`entity_dict[(get_pos_x(), get_pos_y())] = get_entity_type()`
这会更新当前位置存储的实体。

`key` 是唯一的，所以在同一个字典中添加已存在的 `key` 会覆盖之前对应的 `value` 。

调用 `dict.pop(key)` 函数可以从 `dict` 中删除某个键值对，每次删除 1 个。

如果某个 `key` 存在于 `dict` 中，则 `key in dict` 返回的结果为 `True`，如果不存在则为 `False`。
所以你可以使用 `if key in dict:` 来判断 `dict` 是否存在该 `key` 。

将字典放入 for 循环中可以迭代所有的 `key` ：
`for key in dict:
	value = dict[key]`

在迭代过程中，无法保证 `key` 的迭代顺序。

另请参阅[集合](docs/scripting/sets.md)
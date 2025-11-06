# 字典
字典是一種可將鍵映射到值的資料結構，就像現實世界中的字典將單字映射到其定義一樣，便於我們進行快速查找。

字典的建立方式如下：

`right_of = {North:East, East:South, South:West, West:North}`

冒號前的表達式是鍵，冒號後的表達式是鍵映射到的值。
上面的字典將每個方向映射到其右邊的方向。

以下是另一個將無人機位置映射到其下方實體的字典。

```
x, y = get_pos_x(), get_pos_y()
entity_dict = {(x,y):get_entity_type()}
```

存取映射到鍵的值類似於存取串列中的元素：
```
value = dict[key]
```

範例：

```
orientation = right_of[South]
```

這會將 `orientation` 設為 `West`。

你可以這樣向字典新增一個新的鍵值對：

```
dict[key] = value
```

範例：

```
entity_dict[(get_pos_x(), get_pos_y())] = get_entity_type()
```

這會更新目前位置儲存的實體。

鍵是唯一的，所以新增一個字典中已存在的鍵會覆蓋先前的值。

使用 `dict.pop(key)` 從 `dict` 中移除一個鍵值對。

如果 `key` 是 `dict` 中的一個鍵，則對 `key in dict` 求值的結果為 `True`，否則為 `False`。
所以你可以使用 `if key in dict:` 來檢查 `dict` 是否包含該鍵。

將字典放入 for 迴圈中可以迭代所有的鍵：

```
for key in dict:
	value = dict[key]
```

但無法保證鍵的迭代順序。

另請詳閱[集合](docs/scripting/sets.md)

# 列表
列表可以通过 1 个变量存储多个值。
新列表的创建方式如下：

`list = [2, True, Items.Hay]`

这个列表现在包含了 `2`、`True` 和 `Items.Hay` 这些值。
列表也可以是空的：

`empty_list = []`

你可以通过索引访问列表中的元素。第一个元素的索引是 `0`，第二个是 `1`，第三个是 `2`……

种植胡萝卜
`list = [Entities.Tree, Entities.Carrot, Entities.Pumpkin]
plant(list[1])`

你可以使用 for 循环迭代列表。下面的例子计算了列表中所有元素的和。

`list = [4, 7, 2, 5]
sum = 0
for number in list:
	sum += number`
`sum` 现在是 `18`

使用以下列表方法可添加和删除元素：

`list.append(elem)` 在列表末尾添加 1 个元素：

`list = [2, 6, 12]
list.append(7)`
`list` 现在是 `[2, 6, 12, 7]`

`list.remove(elem)` 从列表中移除某个元素第一次出现的项：

`list = [1, 2, 4, 2]
list.remove(2)`
`list` 现在是 `[1, 4, 2]`

`list.insert(index, elem)` 在给定索引处插入 1 个元素：

`list = [Entities.Tree, Items.Hay]
list.insert(1, Items.Wood)`
`list` 现在是 `[Entities.Tree, Items.Wood, Items.Hay]`

`list.pop(index)` 移除指定索引处的元素。
如果未指定索引，则移除最后一项。

`list = [3, 5, 8, 25]
list.pop()`
`list` 现在是 `[3, 5, 8]`
`list.pop(1)`
`list` 现在是 `[3, 8]`

`len()` 函数返回列表的长度。
`list = [3, 2, 1]
x = len(list)`
`x` 现在是 `3`

列表具有引用语义。也就是说，将 1 个列表赋给 1 个变量，会将相应的列表对象赋给该变量，而不是创建列表的副本。
如果多个变量引用同一个列表，更改列表会同时影响这些变量。

`a = [1,2]
b = a
b.pop()`
`a` 和 `b` 现在都是 `[1]`

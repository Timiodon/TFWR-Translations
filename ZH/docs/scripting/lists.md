# List (列表)
List 是在一个变量中存储多个值的简单方法。
你可以这样创建一个新的 list：

`list = [2, True, Items.Hay]`

现在这个 list 包含 `2`、`True` 和 `Items.Hay` 这几个值。
一个 list 也可以是空的：

`empty_list = []`

你可以通过索引来访问 list 的元素。第一个元素的索引是 `0`，第二个是 `1`，第三个是 `2`……

种胡萝卜
`list = [Entities.Tree, Entities.Carrot, Entities.Pumpkin]
plant(list[1])`

你可以使用 for 循环来遍历一个 list。下面的例子计算了 list 中所有元素的和。

`list = [4, 7, 2, 5]
sum = 0
for number in list:
	sum += number`
`sum` 现在是 `18`

下面的 list 方法可以让你添加和移除元素：

`list.append(elem)` 在 list 的末尾添加一个元素：

`list = [2, 6, 12]
list.append(7)`
`list` 现在是 `[2, 6, 12, 7]`

`list.remove(elem)` 从 list 中移除第一次出现的某个元素：

`list = [1, 2, 4, 2]
list.remove(2)`
`list` 现在是 `[1, 4, 2]`

`list.insert(index, elem)` 在给定的索引处插入一个元素：

`list = [Entities.Tree, Items.Hay]
list.insert(1, Items.Wood)`
`list` 现在是 `[Entities.Tree, Items.Wood, Items.Hay]`

`list.pop(index)` 移除指定索引处的元素。
如果没有指定索引，则移除最后一个元素。

`list = [3, 5, 8, 25]
list.pop()`
`list` 现在是 `[3, 5, 8]`
`list.pop(1)`
`list` 现在是 `[3, 8]`

`len()` 函数返回 list 的长度。
`list = [3, 2, 1]
x = len(list)`
`x` 现在是 `3`

List 具有引用语义。这意味着将一个 list 赋给一个变量，会把同一个 list 对象赋给那个变量，而不是创建 list 的一个副本。
如果两个变量引用同一个 list，对 list 的更改对两者都可见。

`a = [1,2]
b = a
b.pop()`
`a` 和 `b` 现在都是 `[1]`
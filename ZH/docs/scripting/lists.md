# 列表
列表是一种简单的方法，可以在一个变量中存储多个值。  
你可以这样创建新的列表：

`list = [2, True, Items.Hay]`

现在列表包含了值 `2`、`True` 和 `Items.Hay`。  
列表也可以是空的：

`empty_list = []`

你可以通过索引来访问列表中的元素。索引为 `0` 表示第一个元素，`1` 表示第二个元素，`2` 表示第三个元素……

种植胡萝卜
`list = [Entities.Tree, Entities.Carrot, Entities.Pumpkin]
plant(list[1])`

你可以使用for循环遍历一个列表。下面的例子计算了列表中所有元素的总和。

`list = [4, 7, 2, 5]
sum = 0
for number in list:
	sum += number`
`sum` 现在是 `18`

以下列表方法允许你添加和移除元素：

`list.append(elem)` 将元素添加到列表的末尾：

`list = [2, 6, 12]
list.append(7)`
`list` 现在是 `[2, 6, 12, 7]`

`list.remove(elem)` 移除列表中第一个出现的元素：

`list = [1, 2, 4, 2]
list.remove(2)`
`list` 现在是 `[1, 4, 2]`

`list.insert(index, elem)` 在指定索引位置插入一个元素：

`list = [Entities.Tree, Items.Hay]
list.insert(1, Items.Wood)`
`list` 现在是 `[Entities.Tree, Items.Wood, Items.Hay]`

`list.pop(index)` 移除指定索引处的元素。  
如果没有指定索引，最后一个元素将被移除。

`list = [3, 5, 8, 25]
list.pop()`
`list` 现在是 `[3, 5, 8]`
`list.pop(1)`
`list` 现在是 `[3, 8]`

`len()` 函数返回列表的长度。  
`list = [3, 2, 1]
x = len(list)`
`x` 现在是 `3`

列表具有引用语义。这意味着将一个列表赋值给一个变量时，是将相同的列表对象分配给该变量，而不是复制列表。  
如果两个变量引用同一个列表，对列表所做的更改将对两个变量都可见。

`a = [1,2]
b = a
b.pop()`
`a` 和 `b` 现在都是 `[1]`
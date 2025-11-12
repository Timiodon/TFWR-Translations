# 串列
串列是將多個值儲存在單一變數中的簡易方式。
可以這樣建立新的串列：

```
list = [2, True, Items.Hay]
```

該串列現在包含值 `2`、`True` 和 `Items.Hay`。
串列也可以為空：

```
empty_list = []
```

你可以透過索引存取串列的元素。第一個元素的索引為 `0`，第二個為 `1`，第三個為 `2`，以此類推。

種植胡蘿蔔：

```
list = [Entities.Tree, Entities.Carrot, Entities.Pumpkin]
plant(list[1])
```

你可以使用 for 迴圈對串列進行迭代。以下範例會將串列中所有元素加總：

```
list = [4, 7, 2, 5]
sum = 0
for number in list:
	sum += number
```

`sum` 現在為 `18`

下列串列方法允許你新增和移除元素：

`list.append(elem)` 在串列末端加入一個元素：

```
list = [2, 6, 12]
list.append(7)
```

`list` 現在為 `[2, 6, 12, 7]`

`list.remove(elem)` 移除串列中第一個出現的指定元素：

```
list = [1, 2, 4, 2]
list.remove(2)
```

`list` 現在為 `[1, 4, 2]`

`list.insert(index, elem)` 在指定索引位置插入一個元素：

```
list = [Entities.Tree, Items.Hay]
list.insert(1, Items.Wood)
```

`list` 現在為 `[Entities.Tree, Items.Wood, Items.Hay]`

`list.pop(index)` 移除指定索引處的元素。
如果沒指定索引，預設移除最後一項。

```
list = [3, 5, 8, 25]
list.pop()
```

`list` 現在為 `[3, 5, 8]`

```
list.pop(1)
```

`list` 現在為 `[3, 8]`

`len()` 函式會回傳串列的長度。

```
list = [3, 2, 1]
x = len(list)
```

此時 `x` 為 `3`

串列具有參考語意。這表示將某個串列指派給變數，會將相同的串列物件指派給該變數，而不是複製串列。
如果兩個變數參考同一個串列，對該串列所做的更動會被兩者看到。

```
a = [1,2]
b = a
b.pop()
```
此時 `a` 和 `b` 都是 `[1]`
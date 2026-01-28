# Lists
Lists are an easy way to store multiple values in a single variable.
You can create new lists like this:

`list = [2, True, Items.Hay]`

The list now contains the values `2`, `True` and `Items.Hay`.
A list can also be empty:

`empty_list = []`

You can access an element of a list by its index. The index is `0` for the first element, `1` for the second element, `2` for the third...

plants carrots
`list = [Entities.Tree, Entities.Carrot, Entities.Pumpkin]
plant(list[1])`

You can iterate over a list using a for loop. The following example sums the all elements in the list.

`list = [4, 7, 2, 5]
sum = 0
for number in list:
	sum += number`
`sum` is now `18`

The following list methods allow you to add and remove elements:

`list.append(elem)` adds an element to the end of the list:

`list = [2, 6, 12]
list.append(7)`
`list` is now `[2, 6, 12, 7]`

`list.remove(elem)` removes the first occurrence of an element from a list:

`list = [1, 2, 4, 2]
list.remove(2)`
`list` is now `[1, 4, 2]`

`list.insert(index, elem)` inserts an element at the given index:

`list = [Entities.Tree, Items.Hay]
list.insert(1, Items.Wood)`
`list` is now `[Entities.Tree, Items.Wood, Items.Hay]`

`list.pop(index)` removes the element at the specified index.
If no index is specified, the last item is removed.

`list = [3, 5, 8, 25]
list.pop()`
`list` is now `[3, 5, 8]`
`list.pop(1)`
`list` is now `[3, 8]`

The `len()` function returns the length of the list.
`list = [3, 2, 1]
x = len(list)`
`x` is now `3`

Lists have reference semantics. This means that assigning a list to a variable assigns the same list object to that variable, rather than making a copy of the list.
If two variables reference the same list, changes to the list will be seen by both.

`a = [1,2]
b = a
b.pop()`
`a` and `b` are now both `[1]`

# Lists

Lists are an easy way to store multiple values in a single variable.
You can create new lists like this:

`some_list = [2, True, Items.Hay]`

The list now contains the values `2`, `True` and `Items.Hay`.
A list can also be empty:

`empty_list = []`

You can access an element of a list by its index. The index is `0` for the first element, `1` for the second element, `2` for the third...

plants carrots
`entities = [Entities.Tree, Entities.Carrot, Entities.Pumpkin]
plant(entities[1])`
Providing a negative index wil1 calculate an index relative to the end of the list. An index of `-1` producces an actual index of `length of list - 1`

plants pumpkins
`entities = [Entities.Tree, Entities.Carrot, Entities.Pumpkin]
plant(entities[-1]) # this gives an index of 2 since 3 -1 = 2`

You can iterate over a list using a for loop. The following example sums the all elements in the list.

`numbers = [4, 7, 2, 5]
sum = 0
for number in numbers:
	sum += number`
`sum` is now `18`

The following list methods allow you to add and remove elements:

`elements.append(elem)` adds an element to the end of the list:

`numbers = [2, 6, 12]
numbers.append(7)`
`numbers` is now `[2, 6, 12, 7]`

`elements.remove(elem)` removes the first occurrence of an element from a list:

`numbers = [1, 2, 4, 2]
numbers.remove(2)`
`numbers` is now `[1, 4, 2]`

`elements.insert(index, elem)` inserts an element at the given index:

`some_list = [Entities.Tree, Items.Hay]
some_list.insert(1, Items.Wood)`
`some_list` is now `[Entities.Tree, Items.Wood, Items.Hay]`

`elements.pop(index)` removes the element at the specified index.
If no index is specified, the last item is removed.

`numbers = [3, 5, 8, 25]
numbers.pop()`
`numbers` is now `[3, 5, 8]`
`numbers.pop(1)`
`numbers` is now `[3, 8]`

The `len()` function returns the length of the list.
`numbers = [3, 2, 1]
x = len(numbers)`
`x` is now `3`

Lists have reference semantics. This means that assigning a list to a variable assigns the same list object to that variable, rather than making a copy of the list.
If two variables reference the same list, changes to the list will be seen by both.

`a = [1, 2]
b = a
b.pop()`
`a` and `b` are now both `[1]`

When indexing into a list you can also provide a start and up to an end point to return a sublist. This is called a slice of the list. Not providing an end point will produce a slice from the start point to the end end of the list.

`numbers = [1, 2, 3, 4, 5, 6]
print(numbers[0:3])`
This will print the first 3 numbers and produce the output `[0,1,2]`.

You can also provide a step for the slice which will make a sublist that has jumped over some elements.

`numbers = [1, 2, 3, 4, 5, 6]
print(numbers[0::2])`
This will print all of the odd numbers in the numbers list since they are positioned every 2 elements in the list start from the `0` element `1`. This gives the output `[1,3,5]`.

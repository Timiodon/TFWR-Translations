# Sets
Sets 就像 [dictionaries](docs/scripting/dicts.md)，但没有值。它们只是无序的键集合。

它们的创建方式类似于 dictionaries，但不需要值。
`set = {North, East, West}`

使用 `set()` 创建一个空的 set。注意 `{}` 会创建一个空的 dictionary。

使用 `set.add(elem)` 来向 set 中添加一个新元素。

使用 `set.remove(elem)` 从 set 中移除一个元素。

使用 `if elem in set:` 来检查 set 是否包含某个元素。

使用 `for elem in set:` 来遍历 set 中所有元素。
对于较大的 sets，`in` 操作符的性能比在列表上快得多。

和 dictionaries 一样，sets 是无序的，所以元素迭代的顺序没有保证。

此外，sets 中的元素都是唯一的，因此添加已在 set 中的元素不会改变 set。
# Set (集合)
Set 就像 [dictionary](docs/scripting/dicts.md)，但是没有值。它们只是一个无序的 key 集合。

它们的创建方式和 dictionary 类似，但是没有值。
`set = {North, East, West}`

使用 `set()` 创建一个空 set。注意 `{}` 创建的是一个空 dictionary。

使用 `set.add(elem)` 向 set 中添加一个新元素。

使用 `set.remove(elem)` 从 set 中移除一个元素。

使用 `if elem in set:` 来检查 set 是否包含一个元素。

使用 `for elem in set:` 来遍历 set 中的所有元素。
对于较大的 set，`in` 运算符的执行速度比在 list 上快得多。

就像 dictionary 一样，set 是无序的，所以无法保证元素遍历的顺序。

此外，set 中的元素是唯一的，所以添加一个已存在于 set 中的元素不会改变 set。
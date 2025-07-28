# Tuple (元组)
Tuple 是将多个值组合成一个单一值的好方法。
要创建一个 tuple，只需用逗号分隔值即可：

`tuple = 1, 2`

你也可以再次将它们解包到多个变量中。在下面的代码中，tuple `(1,2)` 被解包到两个变量 `a` 和 `b` 中。

`a, b = 1, 2`

Tuple 可以像 list 一样进行索引，但它们是不可变的，创建后不能更改。

`tuple = 1, 2`

`print(tuple[1])`
打印 `2`

`tuple[0] = 3`
抛出一个 error
<unlock=dicts>
与 list 不同，tuple 可以用作 dictionary 中的 key。

`d = {(1,2):(4,5)}

print(d[(1,2)])`
`打印` (4,5)</unlock>

它们在函数中返回多个值时也很有用。

`def f():
    return 1, 2

a, b = f()`
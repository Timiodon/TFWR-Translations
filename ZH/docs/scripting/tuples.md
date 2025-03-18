# Tuples
Tuples 是将多个值组合成一个值的好方法。
要创建一个 tuple，只需用逗号分隔这些值：

`tuple = 1, 2`

你也可以将它们解包到多个变量中。在下面的代码中，tuple `(1,2)` 被解包成两个变量 `a` 和 `b`。

`a, b = 1, 2`

Tuples 可以像列表一样通过索引访问，但它们是不可变的，创建后不能更改。

`tuple = 1, 2`

`print(tuple[1])`
打印出 `2`

`tuple[0] = 3`
会抛出一个 error
<unlock=dicts>
与列表不同，tuples 可以用作字典中的键。

`d = {(1,2):(4,5)}

print(d[(1,2)])`
`打印出` (4,5)</unlock>

它们在函数中返回多个值时也非常有用。

`def f():
    return 1, 2

a, b = f()`
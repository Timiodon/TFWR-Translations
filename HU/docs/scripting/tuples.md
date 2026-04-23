# Tuples
Tuples are a great way to combine multiple values into a single value.
To create a tuple, just separate the values with commas:

`tuple = 1, 2`

You can also unpack them into several variables again. In the code below, the tuple `(1,2)` is unpacked into two variables `a` and `b`.

`a, b = 1, 2`

Tuples can be indexed like lists, but they are immutable and cannot be changed after creation.

`tuple = 1, 2`

`print(tuple[1])`
prints `2`

`tuple[0] = 3`
throws an error
<unlock=dicts>
Unlike lists tuples can be used as keys in dictionaries.

`d = {(1,2):(4,5)}

print(d[(1,2)])`
`prints` (4,5)</unlock>

They can also be useful for returning multiple values in a function.

`def f():
    return 1, 2

a, b = f()`
# For 循环
`for` 循环在 Python 中的工作方式相同。（在某些语言中称为 foreach 循环，请不要与 C 风格的 for 循环混淆，它是不同的东西）。

`for i in sequence:
	#do something with i`

与 `while` 循环类似，`for` 循环也会重复调用一段代码。不同的是，它不是基于条件循环，而是对序列中的每个元素执行一次循环体。

## 语法
一个 for 循环看起来像这样：

`for variable_name in sequence:
	#code block`

`variable_name` 可以是你选择的任何名称。它是一个变量，用于存储序列中的当前元素。`sequence` 需要是一个可以被迭代的值，比如一个范围或数字。代码块会对每个元素执行，并将循环变量赋值为该元素。

## 序列
[Ranges](functions/range)      <unlock=lists>[Lists](docs/scripting/lists.md)      </unlock><unlock=functions>[Tuples](docs/scripting/tuples.md)      </unlock><unlock=dicts>[Dictionaries](docs/scripting/dicts.md)      </unlock><unlock=sets>[Sets](docs/scripting/sets.md)</unlock>

## 示例
`for i in range(5):
    harvest()`

这个循环会运行固定次数的循环体。这基本上与下面的代码相同：

`i = 0
harvest()
i = 1
harvest()
i = 2
harvest()
i = 3
harvest()
i = 4
harvest()`

所以它会调用 `harvest()` 五次。

另请参见 [Break](docs/scripting/break.md) 和 [Continue](docs/scripting/continue.md)
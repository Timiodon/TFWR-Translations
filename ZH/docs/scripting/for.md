# For 循环
`for` 循环的运行方式与 Python 中类似。（在某些语言中称为 foreach 循环，但不要与 C 风格的 for 循环混淆，那是不同的概念）。

`for i in sequence:
	#用 i 做点什么`

与 `while` 循环类似，`for` 循环也会重复调用一个代码块。但它不是基于条件循环，而是为序列中的每个元素执行一次循环体。

## 语法
for 循环的形式如下：

`for variable_name in sequence:
	#代码块`

`variable_name` 可以是你选择的任何名称。它是一个存储序列中当前元素的变量。`sequence` 需要是某个可以迭代的值，比如一个数字范围。代码块会为循环变量被赋值到的每个元素执行一次。

## 序列
[范围](functions/range)      <unlock=lists>[列表](docs/scripting/lists.md)      </unlock><unlock=functions>[元组](docs/scripting/tuples.md)      </unlock><unlock=dicts>[字典](docs/scripting/dicts.md)      </unlock><unlock=sets>[集合](docs/scripting/sets.md)</unlock>

## 示例
`for i in range(5):
    harvest()`

这个循环会固定次数地执行循环体，基本上等同于如下代码：

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

所以它会调用 `harvest()` 5 次。

另请参阅[Break](docs/scripting/break.md)和[Continue](docs/scripting/continue.md)。
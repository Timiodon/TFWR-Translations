# 函数
使用 `def` 关键字来定义一个新函数：
`def f(arg1, arg2 = False):
	#函数代码`

你可以使用调用运算符 `()` 来调用函数：
`f(42)`

另请参阅[作用域 (Scopes)](docs/scripting/scopes.md)来了解函数中的局部和全局变量。

## 介绍
你已经见过像 `harvest()` 这样的内置函数了。
你也可以定义自己的函数，这可以让你以模块化的方式组织代码。它基本上允许你给一个代码块命名，这样你就可以从任何你想要的地方调用它。

## 函数定义
例如，你可以定义一个让无人机移动数次的函数。

`def move_n_dir(n, dir):
	for i in range(n):
		move(dir)`

`def` 关键字表示这是一个函数定义。
`move_n_dir` 是该函数绑定的名称。这可以是任何有效的变量名，并将用于调用该函数。
`n` 和 `dir` 是参数。它们是持有传入函数的值的变量（这些值也称为实参）。你可以根据需要向函数定义中添加任意数量的参数。
`:` 后面是函数被调用时将运行的代码块。

通过上面的定义，以下代码将使无人机向`North`移动 `10` 格，向`West`移动 `2` 格。

`move_n_dir(10, North)
move_n_dir(2, West)`

当你看到 `def function():` 时，你真的应该把它看作是这样的一个变量赋值：
`function = create_new_function_object()`
和所有赋值一样，你不能在变量被赋值前使用它！
`def` 语句必须在任何函数调用之前运行。
这段代码会抛出一个 error：

`func()
def func():
	pass`

## 返回值
使用 `return` 关键字让函数返回一个值。
例如，以下函数定义了异或操作。如果一个值为 `True` 而另一个值为 `False`，异或操作将返回 `True`：

`def xor(a, b):
	return a != b

if xor(True, False):
	do_a_flip()`

[Tuple](docs/scripting/tuples.md) 允许返回多个值。

## 默认参数
你还可以分配默认值，如果没有传递参数，将使用这些默认值。

`def f(a = False):
	if a:
		do_a_flip()

f()

f(True)`

有默认值的参数后面不能跟没有默认值的参数。

## 高级函数用法
函数和其他任何值一样都是值，`def` 语句就像一个赋值语句，将函数赋给你给它的任何名称。
这允许做这样的事情：

`def f():
	def d():
		do_a_flip()
	return d

f()()`

这里 `f()` 调用函数 `f`，它定义并返回一个新函数 `d`。第二个 `()` 随后执行返回的函数并执行翻转。
（通常不建议做这类事情，因为很难看懂代码在做什么）

将其他函数作为参数的函数可以让你发挥真正的创造力：

`def f(g, arg):
	for _ in range(10):
		g(arg)

f(move, North)
f(use_item, Items.Fertilizer)`

这段代码将无人机向 `North` 移动10次，然后使用肥料10次。
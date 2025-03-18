# Functions
使用 `def` 关键字来定义一个新函数：
`def f(arg1, arg2 = False):
	#function code`

你可以使用调用运算符 `()` 来调用函数：
`f(42)`

还可以查看 [Scopes](docs/scripting/scopes.md) 以了解函数中的局部和全局变量。

## Introduction
你已经见过像 `harvest()` 这样的内置函数。
你也可以定义自己的函数，这样可以以模块化的方式组织代码。基本上，它允许你给一段代码命名，这样你就可以从任何地方调用它。

## Function Definitions
例如，你可以定义一个让无人机移动多次的函数。

`def move_n_dir(n, dir):
	for i in range(n):
		move(dir)`

`def` 关键字表示这是一个函数定义。
`move_n_dir` 是函数绑定的名字。它可以是任何有效的变量名，并将用于调用函数。
`n` 和 `dir` 是参数。它们是持有传入函数的值（这些值也称作参数）的变量。你可以在函数定义中添加任意数量的参数。
在 `:` 后面是代码块，当函数被调用时将运行它。

有了上面的定义，下面的代码将把无人机移动 `10` 格 `North`，然后移动 `2` 格 `West`。

`move_n_dir(10, North)
move_n_dir(2, West)`

当你看到 `def function():` 时，你应该把它当作一个变量赋值来理解，就像这样：
`function = create_new_function_object()`
像所有赋值一样，在变量被赋值之前，你不能使用它！
`def` 声明必须在任何函数调用之前运行。
这段代码将会抛出错误：

`func()
def func():
	pass`

## Return Values
使用 `return` 关键字让函数返回一个值。
例如，下面的函数定义了异或操作。如果一个值是 `True` 而另一个是 `False`，异或将返回 `True`：

`def xor(a, b):
	return a != b

if xor(True, False):
	do_a_flip()`

[Tuples](docs/scripting/tuples.md) 可以返回多个值。

## Default Arguments
你也可以分配默认值，当没有传入参数时将使用这些默认值。

`def f(a = False):
	if a:
		do_a_flip()

f()

f(True)`

有默认值的参数后不能跟没有默认值的参数。

## Advanced Function Usage
函数和任何其他值一样是值，`def` 声明就像赋值声明一样，将函数分配给你给它的名字。
这允许你做这样的事情：

`def f():
	def d():
		do_a_flip()
	return d

f()()`

这里 `f()` 调用函数 `f`，它定义并返回一个新函数 `d`。第二个 `()` 然后执行返回的函数并进行翻转。
（做这些事情通常不是个好主意，因为很难看懂发生了什么）

接受其他函数作为参数的函数让你可以很有创意：

`def f(g, arg):
	for _ in range(10):
		g(arg)

f(move, North)
f(use_item, Items.Fertilizer)`

这段代码将无人机向 `North` 移动10次，然后用肥料10次。
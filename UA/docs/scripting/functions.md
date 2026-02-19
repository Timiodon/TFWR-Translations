# Functions
Use the `def` keyword to define a new function:
`def f(arg1, arg2 = False):
	#function code`

You can use the call operator `()` to call the function:
`f(42)`

Also see [Scopes](docs/scripting/scopes.md) to learn about local and global variables in functions.

## Introduction
You've already seen built-in functions like `harvest()`.
You can also define your own functions which allows structuring your code in a modular way. It basically allows you to give a name to a block of code so you can call it from anywhere you want.

## Function Definitions
For example, you could define a function that moves the drone several times.

`def move_n_dir(n, dir):
	for i in range(n):
		move(dir)`

The `def` keyword signals that this is a function definition. 
`move_n_dir` is the name that the function gets bound to. This can be any valid variable name and will be used to call the function.
`n` and `dir` are parameters. They are variables that hold the values that are passed into the function (These values are also called arguments). You can add as many parameters to a function definition as you want.
After the `:` comes the code block that will run when the function is called.

With the above definition the following code then moves the drone `10` tiles `North` and `2` tiles `West`.

`move_n_dir(10, North)
move_n_dir(2, West)`

When you see `def function():` you should really think of it as a variable assignment like this:
`function = create_new_function_object()`
Like with all assignments, you can't use the variable before it was assigned!
The `def` statement has to run before any function calls.
This code will throw an error:

`func()
def func():
	pass`

## Return Values
Use the `return` keyword to make a function return a value. 
For example, the following function defines the exclusive or operation. The exclusive or returns `True` if one value is `True` and the other one is `False`:

`def xor(a, b):
	return a != b

if xor(True, False):
	do_a_flip()`

[Tuples](docs/scripting/tuples.md) allow returning multiple values.

## Default Arguments
You can also assign default values that will be used if no arguments are passed.

`def f(a = False):
	if a:
		do_a_flip()

f()

f(True)`

An argument that has a default value cannot be followed by an argument that doesn't have a default value.

## Advanced Function Usage
Functions are values just like any other value, and the `def` statement just acts like an assignment statement, assigning the function to whatever name you give it.
This allows doing things like this:

`def f():
	def d():
		do_a_flip()
	return d

f()()`

Here `f()` calls the function `f` which defines and returns a new function `d`. The second `()` then executes the returned function and performs flip.
(Doing these sort of things is usually not a good idea because it's hard to see what's going on)

Functions that take other functions as arguments let you get really creative:

`def f(g, arg):
	for _ in range(10):
		g(arg)

f(move, North)
f(use_item, Items.Fertilizer)`

This code moves the drone `North` 10 times and then uses fertilizer 10 times.
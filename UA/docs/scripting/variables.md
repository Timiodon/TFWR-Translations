# Variables
Variables can be thought of as named containers that can hold a value.
The `=` operator is used to declare a variable and store a value in it.

`variable_name = value`

The left hand side of the operator is the variable name. You can give it any name you want.
The right hand side is an expression whose resulting value will be stored in the variable.

Declare a variable named `a` and store the value `5` in it:
`a = 5`
Declare a variable named `b` and store the return value of `can_harvest()` in it:
`b = can_harvest()`

Do not confuse the `=` operator with the `==` operator. 
The `==` operator checks whether two values are equal and returns `True` or `False`.
The `=` operator assigns the value on the right to the name on the left.

After a variable has been assigned you can use it in the code to retrieve the value it contains

`a = 5
for i in range(a):
	do_a_flip()`

The above loop is executed 5 times because `a` is set to `5`.
The `i` in the `for` loop is also a variable that is automatically assigned the current value of the sequence at each iteration of the loop. (It doesn't have to be called `i`, you can give it any valid variable name.)

Variables also let you do the same thing with a while loop:

`a = 5
i = 0
while i < a:
	do_a_flip()
	i = i + 1`

This does the same thing as the for loop above. We just have to increment i manually.
Note that to increment i, we set it to be its own value plus `1`. Changing the value of a variable based on its previous value is something very common. 
It can be abbreviated using these operators: `+=, -=, *=, /=, %=`

`i = i + 1` is the same as `i += 1`
`a = a / 3` is the same as `a /= 3`

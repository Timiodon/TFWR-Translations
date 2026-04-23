# Break
`break` allows stopping a loop early. When the `break` statement is reached it will immediately exit the innermost loop and start running the code after the loop.

`for i in range(10):
	break
print(i)`
This prints `0` because `i` is `0` in the first iteration of the loop and then the break statement ends the loop.

It also works on `while` loops.

`while True:
	if can_harvest():
		break`

This code runs the `while` loop until `can_harvest()` is `True`. 
It has the same effect as

`while not can_harvest():
	pass`

In nested loops `break` always exits the innermost loop.

`for i in range(10):
	for j in range(10):
		break
		print("this is never printed")
	print("this is printed 10 times")`
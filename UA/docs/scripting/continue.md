# Continue
continue allows stopping the current iteration of a loop and jumping to the next iteration of the innermost loop.

`for i in range(10):
	continue
    print("this is never printed")`

This runs all `10` iterations of the loop, but the `print` statement after the `continue` is always skipped.

It also works on `while` loops.

`while True:
	if not can_harvest():
		continue
    
    harvest()`

This code only calls `harvest()` when `can_harvest()` is `True`. 
It has the same effect as

`while True:
	if can_harvest():
		harvest()`

In nested loops `continue` always affects the innermost loop.

`for i in range(10):
	for j in range(10):
	    print("this is printed 100 times")
		continue
		print("this is never printed")
	print("this is printed 10 times")`
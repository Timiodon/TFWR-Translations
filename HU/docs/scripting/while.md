# While Loop
You have unlocked the `while` loop and the values `True` and `False`. The `while` loop keeps executing the loop body as long as the condition is `True`.

`while condition:
	#loop body`

Don't worry about creating infinite loops. The delays in the execution will prevent the program from freezing.

## For Beginners
Perhaps you have already tried to put several `harvest()` calls in a row:

`harvest()
harvest()
harvest()`

This allows you to harvest several times in one program run. 
However, it would be nice to harvest more than three times, and writing the same code multiple times is bad practice. 
The solution is a loop. 
A loop allows you to run the same code multiple times.

The while loop takes a condition, which is a logical value that can only be in one of two states: `True` or `False`. 
Such a value is called a Boolean value.

The loop then executes the code inside the loop until the condition is False.
The while loop looks like this:

`while condition:
	#loop body
	#loop body
	#...`
	
Where you have to replace "condition" with a boolean value and `#loop body` with whatever you want to do in the loop.

There are two constant boolean values available. Constants are values that never change during the program.

To create a constant boolean value that is always `True`, you can simply write `True`. Write `False` as a constant boolean value that will always be `False`.
So you could either write


`while False:
	do_a_flip()`

or

`while True:
	do_a_flip()`

The first will never do a flip and the second will do flips forever (an infinite loop). 

Normally creating an infinite loop is a bad idea because it will freeze the program, but in this game there are delays between each iteration of the loop, so it will cause the drone to keep doing a flip until you manually stop it by pressing the execute button again.

Notice how the line after the colon is indented. Indentation like this is used to separate blocks of code.
Just press Tab to add indentation and Shift + Tab (or Backspace) to remove it.

The loop will repeat all indented statements after the colon.
Statements after the indented block will be executed after the loop has finished.

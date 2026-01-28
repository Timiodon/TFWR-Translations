# Timing
If you really want to optimize your methods you need to understand how time is measured in this game. This unlock is all about that.

## New Functions
There are two useful functions to measure how long things take:

`get_time()` returns the time in seconds since the start of the game.

`get_tick_count()` returns the number of ticks performed since the start of execution.

These two functions as well as `quick_print()`, are completely free. Even the call operation is free for them.

## Runtime Details

### Heads-Up
This is not how performance works in the real world. These are just rules made up for this game to have a consistent and understandable timing model.
You will probably only care about this if you want to hyper-optimize your code.


The basic unit of time for code execution is called a "tick". Without speed upgrades and power, the execution proceeds at a rate of `400` ticks per second.

In general, operations that combine two values such as `+, -, *, /, //, %, and, or, ...` take one tick to run.
Single value `-` and `not` are free.
An `if` branch also takes one tick to run (in addition to the time it takes to evaluate the condition expression).
Function calls and variable reads and writes are free but function definitions take 1 tick.
`import` statements are free.
Accessing an imported module with the `.` operator is free.
If a function or module has been passed via arguments or variable assignments, using it will cost 1 tick instead of 0.
`for` and `while` loops take one tick to start, but the iterations are free (not counting the time to evaluate the condition/sequence expressions).
`return`, `break` and `continue` are all free.
`pass` takes one tick so it can be used to create precise delays.
Indexing into a datastructure takes one tick for the index operator and, in the case of a dictionary or set, additional ticks depending on the size of the key.

The number of ticks that builtin functions take to execute is documented in the documentation of each function on an individual basis.
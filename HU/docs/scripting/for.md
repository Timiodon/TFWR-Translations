# For Loop
The `for` loop works like in Python. (Called a foreach loop in some languages, not to be confused with the C-style for loop, which is a different thing).

`for i in sequence:
	#do something with i`

Similar to the `while` loop, the `for` loop also repeatedly calls a block of code. Instead of looping based on a condition, it executes the loop body once for each element in a sequence.

## Syntax
A for loop looks like this:

`for variable_name in sequence:
	#code block`

`variable_name` can be any name you choose. It is a variable that stores the current element in the sequence. `sequence` needs to be some value that can be iterated like a range of numbers. The code block is executed for every element with the loop variable assigned to that element.

## Sequences
[Ranges](functions/range)      <unlock=lists>[Lists](docs/scripting/lists.md)      </unlock><unlock=functions>[Tuples](docs/scripting/tuples.md)      </unlock><unlock=dicts>[Dictionaries](docs/scripting/dicts.md)      </unlock><unlock=sets>[Sets](docs/scripting/sets.md)</unlock>

## Example
`for i in range(5):
    harvest()`

This loop executes the body a fixed number of times. It is essentially the same as writing

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

So it calls `harvest()` 5 times.

See also [Break](docs/scripting/break.md) and [Continue](docs/scripting/continue.md)
# Expand 2
Your farm has expanded again! Now the tiles are no longer in a nice row, so you need to find a way to traverse a square grid.

With the `while` loop this is not possible until you unlock senses and operators.
It is time to introduce the `for` loop.

You can read all about the `for` loop on the [For Loop](docs/scripting/for.md) page, but for now you will only need it to repeat code a fixed number of times.

`#do n flips
for i in range(5):
	do_a_flip()`

`range(n)` creates a range of numbers from `0` to `n-1` which has `n` elements in it. The `for` loop runs it's loop body once for every element in the sequence. In this example `do_a_flip()` will be called `5` times.

The function `get_world_size()` is also available now. It returns the side length of your farm. This way you can write code that won't break with the next expand upgrade.

`for i in range(get_world_size()):
	harvest()
	move(North)`

This example harvests one column of the farm for any farm size.

If you're stuck on trying to figure out how to move the drone around the farm see the hint below.
<spoiler=show hint>There are, of course, several ways to move around the farm.
What we're looking for is a way to traverse it in a systematic way that won't break when the farm grows again.
A systematic way to get to every place on the farm would be to repeat the following 2 steps forever:

1.Move `North` until it wraps back.
2.Move `East`

`for i in range(get_world_size()):` may be helpful to turn this idea into code.
</spoiler>
<spoiler=show possible solution> The basic traversal might look like this:

`for i in range(get_world_size()):
	for j in range(get_world_size()):
		#do a flip on every tile
		do_a_flip()
		move(North)
	move(East)`
</spoiler>
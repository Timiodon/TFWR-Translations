# Mazes
`Items.Weird_Substance`, which is obtained by [fertilizing](docs/unlocks/fertilizer.md) plants, has a strange effect on bushes. If the drone is over a bush and you call `use_item(Items.Weird_Substance, amount)` the bush will grow into a maze of hedges.
The size of the maze depends on the amount of `Items.Weird_Substance` used (the second argument of the `use_item()` call).
Without maze upgrades, using `n` `Items.Weird_Substance` will result in a `n`x`n` maze. Each maze upgrade level doubles the treasure, but it also doubles the amount of `Items.Weird_Substance` needed. 
So to make a full field maze:

`plant(Entities.Bush)
n_substance = get_world_size() * 2**(num_unlocked(Unlocks.Mazes) - 1)
use_item(Items.Weird_Substance, n_substance)`


For some reason the drone can't fly over the hedges, even though they don't look that high.

There is a treasure hidden somewhere in the hedge. Use `harvest()` on the treasure to receive gold equal to the area of the maze. (For example, a 5x5 maze will yield 25 gold.)

If you use `harvest()` anywhere else the maze will simply disappear.

`get_entity_type()` is equal to `Entities.Treasure` if the drone is over the treasure and `Entities.Hedge` everywhere else in the maze.

Mazes do not contain any loops unless you reuse the maze (see below how to reuse a maze). So there is no way for the drone to end up in the same position again without going back.

You can check if there is a wall by trying to move through it. 
`move()` returns `True` if it succeeded and `False` otherwise.

If you have no idea how to get to the treasure, take a look at Hint 1. It shows you how to approach a problem like this.


For an extra challenge you can also reuse the maze by using the same amount of `Items.Weird_Substance` on the treasure again. 
This will increase the amount of gold in the treasure by one full maze and move it to a random position in the maze.

Using `measure()` on a treasure returns the position, that it will move to, as a tuple.
`next_x, next_y = measure()`

Each time the treasure is moved, a random wall may be removed from the maze. So reused mazes can contain loops.

Note that loops in the maze make it much more difficult because it means that you can get to the same location again without moving back.
Reusing a maze doesn't give you more gold than just harvesting and spawning a new maze.
This is 100% an extra challenge that you can just skip.
It's only worth it if the extra information and the shortcuts help you solve the maze faster.

The same maze can be solved a maximum of 300 times. This corresponds to 299 relocations. After that, using weird substance on the treasure won't increase the gold in it anymore and `measure()` will return `None`.

<spoiler=show hint 1>Here's a general approach to solving the problem:

Create a maze and imagine that you are the drone.

Think about how you would try to find the treasure if you were in the maze.

Write down your strategy step by step so that someone else could follow it without thinking.

Now try translating your steps into code.
</spoiler>
<spoiler=show hint 2>As long as there are no loops: All the walls are really just one large connected wall. If you follow the wall, it will lead you through the whole maze.
This approach requires very little code and you do not need to keep track of where you have already been. Around 10 lines of code is all you need.</spoiler>
<spoiler=show hint 3>Instead of moving the drone in absolute directions like east or west it can be very useful to move the drone in relative directions like "turn right" or "turn left". To do this you need to keep track of which way the drone is currently moving. The drone never actually rotates, but you can still keep a "virtual" rotation in code.
The following index trick is helpful for this:

`directions = [North, East, South, West]
index = 0`

Use `% 4` to allow it to rotate "around the circle", so that after `West` it wraps back to `North`.
`# turn right
index = (index + 1) % 4`

`# turn left
index = (index - 1) % 4

move(directions[index])`</spoiler>
<spoiler=show hint 4>If you can't solve it, you can always make your life easy and do it less efficiently. 
Solvig a `1`x`1` maze is trivial.</spoiler>
# Senses
The drone can see now! 

The functions `get_pos_x()` and `get_pos_y()` return the current x and y position of the drone. At the start position they are both `0`. The x position increases by `1` every tile towards `East` and the y position increases by `1` every tile towards `North`.

`num_items(item)` returns how many of an item you have.
For example `num_items(Items.Hay)` returns how much hay you have.

`get_entity_type()` and `get_ground_type()` return the type of entity or ground that is under the drone.

Do a flip if you are over a bush:
`if get_entity_type() == Entities.Bush:
	do_a_flip()`

The `None` keyword is also unlocked now! `None` is a value that represents that there is no value.
For example, a function that has no `return` statement will actually return `None`.

`get_entity_type()` returns `None` if there is no entity under the drone.


If you want to find out how many of a particular unlock you have, use the `num_unlocked(unlock)` function.

For example, `num_unlocked(Unlocks.Speed)` will return the number of speed upgrades you have.

`num_unlocked(Unlocks.Senses)` will return `1` if senses are unlocked and `0` if they are not.

You can also use `num_unlocked()` on Items, Entities or Grounds. This will return `1` if it's unlocked otherwise `0`.

Be careful `num_unlocked(Unlocks.Carrots)` will return the number of times it was unlocked/upgraded.
`num_unlocked(Items.Carrot)` will only return `0` or `1`. (Same for other plants)
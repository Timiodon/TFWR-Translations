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

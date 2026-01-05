# Dictionaries
Dictionaries are a datastructure that allows you to map keys to values in the same way that a real dictionary maps words to their definitions and you can look them up very quickly.

A dictionary can be created like this:
`right_of = {North:East, East:South, South:West, West:North}`

The expression before the colon is the key and the expression after the colon is the value to which the key maps.
The above dictionary maps each direction to the direction to it's right.

Here's another one that maps the drone's position to the entity it's over.
`x, y = get_pos_x(), get_pos_y()
entity_dict = {(x,y):get_entity_type()}`

Accessing the value mapped to a key is similar to accessing an element in a list:
`value = dict[key]`

Example:
`orientation = right_of[South]`
This sets `orientation` to `West`.

You can add a new key-value pair to a dictionary like this:
`dict[key] = value`

Example:
`entity_dict[(get_pos_x(), get_pos_y())] = get_entity_type()`
This updates the entity stored for the current position.

Keys are unique, so adding a key that already exists in the dictionary will overwrite the previous value.

Use `dict.pop(key)` to remove a key-value pair from `dict`.

`key in dict` evaluates to `True` if `key` is a key in the `dict` and `False` otherwise.
So you can use `if key in dict:` to check if `dict` contains the key.

Putting a dictionary in a for loop allows you to iterate through all keys:
`for key in dict:
	value = dict[key]`

There are no guarantees about the order in which the keys are iterated.

See also [Sets](docs/scripting/sets.md)
# In Statement
You can use an `in` statement to check if a value is available within a `sequence` or a string of characters. A `sequence` needs to be some value that can be iterated over like a range of numbers. If the value is in the `sequence` then then the statement will return `True` and if it is not then it will return `False`.

Note: When used in a `for` loop the `in` keyword functions differently. Please see [For Loop](docs/scripting/for.md) to learn about how to use the `in` keyword for those.

## Syntax
An `in` statement looks like this:

`variable_name = variable_name_or_value in sequence`

`variable_name` can be any name you choose and will be given the value of `True` or `False`

Or:

`if variable_name_or_value in sequence:
    # code block`

Or:

`while variable_name_or_value in sequence:
    # code block`

`variable_name_or_value` can be any variable you want or any value you want. `sequence` must be one of the things listed below, or a string of characters. An `if` or `while` code block will run if the value is in the provided sequence.

## 存储序列
[范围](functions/range)      <unlock=variables>[元组](docs/scripting/tuples.md)      </unlock><unlock=lists>[列表](docs/scripting/lists.md)      </unlock><unlock=dicts>[字典](docs/scripting/dicts.md)      </unlock><unlock=sets>[集合](docs/scripting/sets.md)</unlock>

## Example - 2x2 Square of Bushes
`clear()
for x in range(get_world_size()):
    for y in range(get_world_size()):

        if x in (0, 1) and y in (0, 1):
            plant(Entities.Bush)

        move(North)
    move(East)`

This will plant a square of `Entities.Bush` in a 2x2 square starting at the origin (0, 0) of the world leaving the rest untouched.
<unlock=senses>
## Example - Tilling
`desired_entity = Entities.Carrot
entities_needing_soil = (Entities.Pumpkin, Entities.Carrot)

if desired_entity in entities_needing_soil:
    if get_ground_type() != Grounds.Soil:
        till()`

This will check if the `desired_entity` is in the `tuple` `entities_needing_soil` so that the drone can know if it needs to check if the current ground type is `Grounds.Soil`. If it is not then it will call the `till` function to change the ground type.</unlock>
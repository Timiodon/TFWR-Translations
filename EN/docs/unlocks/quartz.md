[<- Iron](docs/unlocks/iron.md) <right>[Mushroom ->](docs/unlocks/mushroom.md)
---
# Quartz
Continuing from the iron veins in `Grounds.Rock`, you find quartz in the lower part of the rock layer and into the hard `Grounds.Dirt` below (check the hardness using `get_hardness()` from the [underground senses](docs/unlocks/underground_senses.md) unlock).

The following code snippet digs past the dirt and into the rock layer. There it continuously prospects for quartz while digging, until the distance is smaller than 2. Finally, it prints the prospect distance it arrived at.
{{codeexample 
{
    "camera_position": {"x": -1, "y": 0, "z": 8},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [{"item": "block", "n": 1}, {"item": "iron", "n": 100}],
    "world_size": {"x": 3, "y": 3},
    "execution_speed": 8,
    "digging_speed": 16,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 9,
    "exclude_unlocks": ["watering", "fertilizer", "mushrooms", "dynamite"]
}
#SETUP
move(East)
move(North)
#CODE
# Dig down to the rock layer
while get_ground_type() != Grounds.Rock:
    dig()

# Continue digging until a quartz vein is close
while prospect_quartz() == None or prospect_quartz() >= 2:
    for i in range(10):
        dig()

# Print the final distance to the vein
print(prospect_quartz())
}}

## Vein Structure
Quartz grows in needle-shaped veins that form vertical columns, making them quite difficult to find through trial and error.

## Prospecting Quartz
Luckily, we can use our iron and mangle it into something similar to a dowsing rod that allows us to locate these quartz veins more easily. The command for this is `prospect_quartz()`.

`prospect_quartz()` works differently from `prospect_iron()`. Instead of returning the direction for the drone to move towards the closest iron ore, it returns the exact 3D distance between the closest Quartz block and the drone (Euclidean distance).

Executing `prospect_quartz()` costs 1 iron, so it might be a good idea to use the command sparingly.

If `prospect_quartz()` can't find any nearby quartz, or if you don't have enough iron to perform the search, it returns `None`.

## Strategy
<spoiler=show hint>You can repeatedly prospect and move to see how the distance changes. On a flat surface, trying to minimize the distance can place you above a quartz vein. You can use a strategy similar to binary search to minimize the number of `prospect_quartz()` calls and the amount of iron they consume.

More involved strategies can use 2D geometry to find the intersection between two or more circles or you can go the hard route and do full triliteration, to intersect three spheres and find the exact 3D position of the vein.

Note that to do a square root, you can use the exponent operator, e.g. to get the square root of 16, use `16**0.5`. There aren't any built-in math functions for trigonometry or vectors, you'll have to implement them yourself. 

Also note that there can be multiple veins in the vicinity, so if you take multiple nearby measurements, they might not point to the same vein.</spoiler>

---

[Stats](docs/stats.md)      [Mining](docs/unlocks/mining.md)      [Underground Senses](docs/unlocks/underground_senses.md)      [Variables](docs/scripting/variables.md)      [Operators](docs/scripting/operators.md)

[move()](functions/move)      [dig()](functions/dig)      [get_ground_type()](functions/get_ground_type)      [prospect_quartz()](functions/prospect_quartz)

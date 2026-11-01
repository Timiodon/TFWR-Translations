[<- Mushroom](docs/unlocks/mushroom.md) <right>[Explosive Drill ->](docs/unlocks/explosive_drill.md)
---
# Dynamite
The revolutionary explosive, left behind by previous mining expeditions. Unfortunately, your drill is perfect to make dynamite explode, blasting away all the blocks around you. Collected dynamite can be used with `use_item(Items.Dynamite)` and explodes immediately below the drone.

To safely mine dynamite, find a layer of `Grounds.Dynamite`, directly followed by a layer of `Grounds.Soot` below it. The dynamite layer above has gotten a bit old, and some of its blocks are safe to dig into. However, some of the dynamite blocks are still live and will explode when you dig into them.

This example digs into dynamite and all around the initial dig point, revealing the soot layer with numbers on it, printing the measurement:
{{codeexample 
{
    "camera_position": {"x": -3, "y": 0, "z": 15},
    "show_image": true,
    "image_size": {"x": 800, "y": 500},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 7, "y": 7},
    "execution_speed": 2,
    "digging_speed": 2,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 6,
    "exclude_unlocks": ["watering", "fertilizer", "mushrooms", "coal", "quartz", "petrified_pumpkins"]
}
#SETUP
jump(Unlocks.Dynamite)
for _ in range(3):
    move(East)
    move(North)
#CODE
# Dig down to the soot layer, through the dynamite layer above
while get_ground_type() != Grounds.Soot:
    dig()

# List of directions that make the drone move in a circle
circle_directions = [
    East, South, West, West, 
    North, North, East, East
]
for dir in circle_directions:
    move(dir)
    dig()
    print(measure()) # The number on the soot block
}}

## Dynamite Sweeper
Can you find and dig all the dud dynamite blocks, leaving only live blocks behind? Every live block that's surrounded only by other live blocks or soot blocks will yield you extra dynamite once the dynamite stratum disappears.

Luckily, the soot blocks below will help you: they can detect the number of neighboring dynamite blocks that contain live dynamite. They won't tell you exactly which blocks are live, only the total number, so you need to combine the readings from multiple soot blocks and work it out yourself.

Calling `measure()` on a soot block returns the number of mines in the eight neighboring tiles on the dynamite stratum above. The number can range from `0` (no live mines) to `8` (every neighbor contains a live mine).

The first dig into the dynamite stratum is always a dud. Every mined block of dynamite yields a bit of dynamite. When the dynamite stratum is destroyed, either through successfully digging up all the duds or by inadvertently digging into live dynamite, you also gain dynamite equal to the number of fully uncovered live blocks, squared.

## Strata Structure
The number of live mines in the dynamite stratum, and therefore the difficulty of finding them, increases with depth. The number of total mines increases with the farm size, therefore also the possible maximum yield for clearing a dynamite stratum.

Upgrade dynamite to increase the yield of digging into dynamite blocks and fully uncovering live blocks. The upgrade also increases the energy of dynamite explosions by 30%.

## Detect Success and Failure
If you dig into live dynamite, the two strata explode. You can check for this using `get_ground_type()` after digging into `Grounds.Dynamite`. If the ground is not `Grounds.Soot`, you failed solving the puzzle. On the other hand, if the last non-live dynamite block is dug up, all dynamite blocks disappear and you earn the max amount of yield for the puzzle. The soot stratum remains but `measure()` returns `None`, indicating the puzzle was solved successfully.

`# Dig into a dynamite block and check the puzzle state
def dig_dynamite():
    dig()
    if get_ground_type() != Grounds.Soot:
        # Dug into live dynamite, puzzle failed
        return False
    elif measure() == None:
        # Dug up final dud block, puzzle solved
        return True
    else:
        # Got a count from measuring, puzzle still ongoing
        return None
`

## Strategy
<spoiler=hint>
The code below digs into the dynamite stratum and looks for soot blocks that measure `0`. For every such block it finds, it digs away all the dynamite blocks that surround it:
{{codeexample 
{
    "camera_position": {"x": -5, "y": 0, "z": 15},
    "show_image": true,
    "image_size": {"x": 800, "y": 500},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 7, "y": 7},
    "execution_speed": 4,
    "digging_speed": 8,
    "action_ticks": 200,
    "operation_ticks": 20,
    "seed": 6,
    "exclude_unlocks": ["watering", "fertilizer", "mushrooms", "coal", "quartz", "petrified_pumpkins"]
}
#SETUP
jump(Unlocks.Dynamite)
for _ in range(3):
    move(East)
    move(North)
#CODE
while get_ground_type() != Grounds.Soot:
    dig()

circle_directions = [
    East, South, West, West, North,
    North, East, East, South, West
]
# Go around the block we initially dug into
for dir in circle_directions:
    # If the soot measures 0,
    # we know all surrounding dynamite blocks are duds
    if get_ground_type() == Grounds.Soot and measure() == 0:
        # Do another circle through the surrounding blocks
        for dir2 in circle_directions:
            move(dir2)
            # Dig up the dynamite dud block
            while get_ground_type() != Grounds.Soot:
                dig()
    move(dir)
}}
</spoiler>

---

[Stats](docs/stats.md)      [Underground Senses](docs/unlocks/underground_senses.md)      [Dictionaries](docs/scripting/dicts.md)      [Sets](docs/scripting/sets.md)

[move()](functions/move)      [dig()](functions/dig)      [measure()](functions/measure)      [use_item()](functions/use_item)

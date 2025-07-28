# Patch Notes

Multiple Drones Have been added to the game. Check out the new "Megafarm" unlock!
Also a large part of the tech tree has been experimentally reworked to be more exponential.

Gameplay:
-Pumpkins now scale up to 6x6 instead of 5x5.
-The ground drying behavior has slightly changed. Instead of drying by 1% every 0.8 to 1.2 seconds, each ground tile now has a 10% chance of drying every 0.1 seconds.
-The cactus grow time is now always exactly 1 second.

Visuals:
-The visuals of the tech tree have been completely reworked.
-Pumpkins now leave behind a dead pumpkin to indicate that they have died.
-Cacti are now brown when they aren't sorted to make it more visible.

Code Editor:
-Double clicking identifiers with underscores in them now selects the whole identifier.
-If the "tabs to spaces" option is turned off, indentation spaces are now converted to tabs.
-Zooming is now much smoother.

Other:
-You can now chain comparison operators like in Python.
-`get_cost(Entities.Hedge)` and `get_cost(Entities.Treasure)` now return the cost of a 1x1 maze.

Fixes:
-Some of the most common cases of code highlights being visible through other windows have been fixed.
-Actions like tilling can no longer affect the water drying behavior.

Breaking Changes from older Patches that you might have missed:
-Functions defined in other files (windows in the game) are no longer imported implicitly. You now have to unlock and use explicit import statements like in Python (See the import unlock).
-`Items.Bones` has been renamed to `Items.Bone` so all items are singular.
-`Entities.Carrots` has been renamed to `Entities.Carrot` so all entities are singular.
-`Grounds.Turf` has been renamed to `Grounds.Grassland` to make it easier to understand.
-`Items.Water_Tank` has been renamed to `Items.Water` because the tank refill feature has been removed.
-`Unlocks.Benchmark` has been replaced with `Unlocks.Timing`.
-`get_op_count()` has been renamed to `get_tick_count()`.
-`set_farm_size()` has been renamed to `set_world_size()` to be consistent with `get_world_size()`.
-`get_companion()` now returns a tuple of the form (entity, (x, y)) instead of a list.
-`trade()` has been removed from the game.
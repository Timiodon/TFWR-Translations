# Patch Notes

This patch brings many optimizations on both the GPU and CPU side. 
Particularly on the GPU side there have been some very significant optimizations that finally make the game less GPU intensive.
Unfortunately the items in the inventory are no longer 3D because it turned out this was using a lot of GPU resources.

Some things that were changed alongside the optimizations are:
-The call stack limit is now 1000 function calls.
-Items in the inventory are now in a fixed order.
-When the camera moves to the position of an error or a search term it now moves to it's exact location instead of the center of the window. Also, the camera no longer moves to errors that are already on screen.
-Fixed various UI bugs.

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
# 1.0 is finally here!
After over three and a half years of steady development, over 20 updates, and your amazing feedback, Early Access has finally come to an end.

## What’s new in 1.0?
- Multiple drones to maximize your farming
- A reworked unlock tree with a more exponential progression
- 60 achievements to test your skills
- Unlocking certain achievements will give your drone special hats
- A complete sound overhaul
- One new music track
- Quality of life improvements and various fixes
- Breaking Changes: Upgrades will be partially reset. Reusing mazes works slightly differently.

Thank you all so much for supporting The Farmer Was Replaced from Early Access to full release. 
I can’t wait to see how you use the multiple drones in creative and clever ways!
-Timon

Also make sure to join us on Discord: 
[Discord](https://discord.com/invite/kj33cJkeJn)

## Full Patch Notes
Breaking Changes:
-Due to the rework of the tech tree, the upgrade numbers of old savegames will no longer be valid. The game will reset all upgrades to a reasonable level when you open an old save.
-If you are reusing mazes you now have to first reposition the treasure and then measure the position instead of first measuring and then repositioning.

Gameplay:
-Added tooltips with helpful information when hovering tiles in the farm.
-Using `measure()` anywhere in the maze now always returns the position of the current treasure. You no longer have to measure the treasure specifically.
-There is now a `can_move()` function for the maze.
-Pumpkins now scale up to 6x6 instead of 5x5.
-The ground drying behavior has slightly changed. Instead of drying by 1% every 0.8 to 1.2 seconds, each ground tile now has a 10% chance of drying every 0.1 seconds.
-The cactus grow time is now always exactly 1 second.
-Pumpkins now leave behind a dead pumpkin to indicate that they have died.
-Added `pet_the_piggy()`.
-`num_unlocked()` now already gets unlocked with Senses.

Audio:
-The audio has been completely remade.
-There is music when you start the game now!

Visuals:
-The visuals of the tech tree have been completely reworked.
-The inventory panel in the top left corner of the screen now has a nice item pickup visual effect.
-Cacti are now brown when they aren't correctly sorted to make it more visible.
-Plants are now visible immediately after planting, even if they haven't grown yet.

Code Editor:
-Double clicking identifiers with underscores in them now selects the whole identifier.
-If the "tabs to spaces" option is turned off, indentation spaces are now converted to tabs.
-Zooming is now much smoother.
-The code completer is now properly import aware and can give suggestions from other files.
-Added different cursors for editing text and resizing windows.
-Debugger steps are now based on the code line instead of simulation ticks.

Other:
-You can now chain comparison operators like in Python.
-`get_cost(Entities.Hedge)` and `get_cost(Entities.Treasure)` now return the cost of a 1x1 maze.
-Added a resolution setting.
-Added a setting to turn off the flashing highlights when the code is running.
-The code execution has been optimized further, allowing the game to run smoother while code is running.
-Added a "Toggle HUD" keybind.

Fixes:
-Some of the most common cases of code highlights being visible through other windows have been fixed.
-Actions like tilling can no longer affect the water drying behavior.
-Fixed keybinding problems on non US keyboards.
-Fixed the piggy bank moving really far away from the farm sometimes.
-Fixed fertilizer not infecting fully grown plants.
-Fixed `set_world_size(get_world_size())` resetting the drone position.
-Fixed a simulation + dinosaur interaction that caused lots of apples to be left behind.
-Fixed the bug that caused error messages to move around when you clicked minimize and then opened the menu.
-Fixed error messages popping up while you are still typing.

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
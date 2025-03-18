# Patch Notes

-Code windows are now scrollable.
-Added code highlights to visualize the call stack.
-You can now search all windows with ctrl + F.
-If an error happens in a window that is completely off screen the camera will move to it.
-The code autocomplete is now more fuzzy and inserting autocomplete words with Enter works better.
-There is now a warning icon that pops up when a warning is emitted to make it more visible.
-To better support external editors that don't automatically pick up on the `__builtins__.py` file, importing from that file can now already be done before unlocking the import feature.
-The Undo and Redo history is now per window instead of global.
-Autocomplete suggestions work better with imports now.
-Green is back in the syntax color.

-Fixed a bug that mixed leaderboard runs with the main simulation.
-Fixed growtimes not being updated when watering grassland.
-Fixed the UI issue that was caused by trailing spaces in file names.
-Fixed unindent problems with the "tabs to spaces" option.
-Infecting bushes by using 1 weird substance after upgrading the maze now works.
-Fixed item numbers rounding wrong in some cases.
-Typing in values in slider options in the menu has been fixed.
-Fixed the broken "error_not_a_function" error.
-Fixed a bunch of error messages that showed up in the wrong place.

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
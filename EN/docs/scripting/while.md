[<- First Program](docs/first_program.md) <right>[Speed Upgrade ->](docs/unlocks/speed.md)
---
# While Loop
You have unlocked the `while` loop and the values `True` and `False`. The `while` loop keeps executing the loop body as long as the condition is `True`.

`while condition:
	#loop body`

Don't worry about creating infinite loops. The delays in the execution will prevent the program from freezing.

## For Beginners
Perhaps you have already tried to put several `harvest()` calls in a row:

{{codeexample 
{
    "camera_position": {"x": 0, "y": 1.5, "z": 4},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 1, "y": 1},
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
do_a_flip()
#CODE
harvest()
harvest()
harvest()
}}
This allows you to harvest several times in one program run.
However, it would be nice to harvest more than three times, and writing the same code multiple times is bad practice.
The solution is a loop.
A loop allows you to run the same code multiple times.

The while loop takes a condition, which is a logical value that can only be in one of two states: `True` or `False`. 
Such a value is called a Boolean value.

The loop then executes the code inside the loop until the condition is False.
The while loop looks like this:

`while condition:
	#loop body
	#loop body
	#...`

Where you have to replace "condition" with a boolean value and `#loop body` with whatever you want to do in the loop.

There are two constant boolean values available. Constants are values that never change during the program.

To create a constant Boolean value, simply write `True` or `False`.
So you could either write

{{codeexample 
{
    "camera_position": {"x": 0, "y": 1.5, "z": 4},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 1, "y": 1},
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
while False:
	do_a_flip()
}}
or

{{codeexample 
{
    "camera_position": {"x": 0, "y": 1.5, "z": 4},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 1, "y": 1},
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
while True:
	do_a_flip()
}}
The first will never perform a flip, and the second will perform flips forever (an infinite loop).

Normally, creating an infinite loop is a bad idea because it will freeze the program. In this game, however, there are delays between iterations, so the drone will keep performing flips until you stop it manually by pressing the Execute button again.

Notice how the line after the colon is indented. Indentation like this is used to separate blocks of code.
Just press Tab to add indentation and Shift + Tab (or Backspace) to remove it. If several lines are selected, Tab and Shift + Tab will apply to all of them.

Note: if you are playing the game through steam, pressing Shift + Tab will open the steam overlay instead. You can rebind the unindent shortcut in the game options, or the steam overlay shortcut in the steam overlay options.

Here, `do_a_flip()` and `pet_the_piggy()` are called repeatedly because they are inside the indented `while` block. However, `harvest()` never runs because it comes after that block.
{{codeexample 
{
    "camera_position": {"x": 0, "y": 1.5, "z": 4},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 1, "y": 1},
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
while True:
	do_a_flip()
	pet_the_piggy()
harvest()
}}

---

[For Loop](docs/scripting/for.md)      [If](docs/scripting/if.md)      [Break](docs/scripting/break.md)      [Continue](docs/scripting/continue.md)      [External Editor](docs/external_editor.md)

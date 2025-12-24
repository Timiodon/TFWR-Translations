# Debug
Sometimes your code just doesn't work and you need to find out why. There are a couple of tools to help you do that.

The first is to execute the program step by step. 
You can go into step-by-step mode with the button next to the Execute button or by setting a breakpoint.

Breakpoints can be added by clicking on the breakpoint panel to the left of the code.
![](Breakpoints227)
When execution reaches the line where the breakpoint is, it will automatically switch to step-by-step mode.

When you move your mouse over a variable, its current value is displayed.

The `print()` function can also be very useful. It will write any value passed to it directly into the air.

Examples:

Print "0.24".
`print(0.24)`

Print "True" or "False".
`print(can_harvest())`

Print the current position.
`print(get_pos_x(), get_pos_y())`

The print function prints the value directly into the air and to the [Output](docs/output.md) page.

Writing into the air can sometimes be a bit slow if you want to print a lot of values.
In this case you can use the `quick_print()` function which prints only to the output window.

The output window also logs warnings and errors, so if something doesn't work as expected it can be useful to check that.

When the execution stops, the output is also written to the output.txt file in the game folder. [output.txt](persistent_data_path/output.txt).
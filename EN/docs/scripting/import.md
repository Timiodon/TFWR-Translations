# Import
Putting all your code in a single file quickly becomes unmanageable. 
`import` statements allow you to import functions and global variables from another file.

`import filename`

This is the simplest form of import statement. It will give you access to everything defined in the file named `filename`. Each window in the game is a file, and the filename is the name displayed at the top of the window.

Here's an example with two files:
File named helper:
`x = 0

def say_hello():
    print("hello from helper")`

Some other file:
`import helper
helper.say_hello()
helper.x += 1`

Here `import helper` runs the file named `helper` and gives you access to all it's globals.
You can then access variables and functions within the imported module using the `.` operator.
So in this example, `helper.say_hello()` calls `say_hello()` inside helper and the last line increments the global variable x.

You can also move the globals from the imported module into the current scope where the import statement is executed using the `from` syntax.

`from helper import *`
Imports all globals from helper.

or

`from helper import say_hello`
Imports only the specified globals from helper.

This also imports the helper file, but instead of accessing it through a variable named `helper`, it unpacks globals from `helper` and assigns them directly in the local scope.

`from helper import say_hello
say_hello()`

This form of import is usually not recommended because it doesn't work well when two files import each other, and you may accidentally overwrite variables in the importing file due to name collisions.

# How it really works

## TLDR
Imports can be quite unintuitive, but most problems can be avoided by sticking to the `import file` syntax instead of `from file import`, and wrapping everything that isn't a global definition in
`if __name__ == "__main__":`

## Import Side Effects
The first time you import a file, it will execute the entire file and then give you access to all variables that have been defined during the execution.
If you import the same file again, it will just return the cached module from the first time again.

This means that import statements can have side effects. If you import a file that calls `harvest()`, it will actually harvest during the import. But when you import it again, it won't harvest again because the file is only run once.

There is a way to avoid such side effects using the `__name__` variable. This is a variable that is automatically set to `"__main__"` when a file is run directly, and to the name of the file when a file is run through `import`.
It is considered good practice to put any code that you don't want to run when the file is imported inside of a `if __name__ == "__main__":` block.

A common file structure in Python is to put the code that should be executed when the file is run into a `main()` function. This way you have a clear distinction between local variables (defined inside `main()`) and global variables that can be imported (defined outside `main()`).

`a_global_variable = "global"

def main():
    a_local_variable = "local"
    # do things

if __name__ == "__main__":
    main()`

## Import Cycles
What happens if file `a` imports file `b` and file `b` imports file `a`?

file `a`:
`import b
x = 0`

file `b`:
`import a
def f():
    print(a.x)`

This will work fine. Let's say neither of the two files are loaded yet, and someone else executes `import a`.

-`a` runs until the `import b` line.
-`b` runs until the `import a` line.
-The module `a` already exists, but doesn't contain `x` because it has only reached the `import b` line.
-`b` stores a reference to the half-loaded module `a` in a variable called `a`.
-`b` runs the `def` statement and stores the function `f()`.
-`a` continues to run and initializes `x`.

When someone calls `b.f()` it will correctly print `0` because the module `a` that `b` has a reference to is now fully loaded.

Now consider the same code using the `from` syntax.

file `a`:
`from b import *
x = 0`

file `b`:
`from a import *
def f():
    print(x)`

-`a` runs until the `from b import *` line.
-`b` runs until the `from a import *` line.
-The module `a` already exists, but hasn't been fully executed yet.
-`b` unpacks everything that is currently in `a` into it's own global scope. At this point, `a` contains nothing because it hasn't reached the `x = 0` line yet, so nothing is imported.
-`b` runs the `def` statement and stores the function `f()`.
-`a` continues to run and initializes `x`.

If someone now calls `b.f()`, they will get an error that `x` doesn't exist in the current scope. This is because this time `b` does not have a reference to the still-loading `a` and does not see definitions that were added after the import.
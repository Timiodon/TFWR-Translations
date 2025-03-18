# Operators
arithmetic operators: `+, -, *, /, //, %, **`
comparison operators: `==, !=, <=, >=, <, >`
boolean operators: `not, and, or`

Note: All numbers in the game are floating point numbers. So all arithmetic operators are floating point operators.
`//` is defined to just floor the number after the division.

For assignment operators you need to unlock the "Variables" unlock.

## Introduction
Operators allow you to compare, modify and combine values. 
The arithmetic operators `+, -, *, /, //, %, **` are used to perform common mathematical operations on numbers. 
The comparison operators `==, !=, <=, >=, <, >` are used to compare values. The result is always either `True` or `False`.
The logic operators (also called boolean operators) `not, and, or` are used to combine truth values.

## Arithmetic Operators
`+` and `-` are used for addition and subtraction.

`2 + 3` evaluates to `5`
`3 - 2` evaluates to `1`

`*`, `/` and `//` are used for multiplication and division.

`2 * 3` evaluates to `6`
`5 / 2` evaluates to `2.5`

`//` does the same thing as `/` but the result is floored (rounded down to the next integer).

`5 // 2` evaluates to `2`

`%` is the modulo operator, also known as the remainder operator. It essentially divides the two numbers and then returns the remainder. You can also think of it as repeatedly subtracting the right number from the left number until the remainder is less than the right number.

`4 % 2` evaluates to `0`
`5 % 2` evaluates to `1`
`6 % 2` evaluates to `0`
`2 % 6` evaluates to `2`
`1.5 % 1` evaluates to `0.5`

`**` is the power operator.

`2**2` evaluates to `4`
`(-5)**3` evaluates to `-125`

## Comparison Operators
`==` and `!=` are used to check of two values are "equal"(`==`) or "not equal"(`!=`). They can be used on all types of values.

`2 == 2` evaluates to `True`
`Entities.Bush != Entities.Bush` evaluates to `False`
`3 != 3 + 1` evaluates to `True`

`<=, >=, <, >` can only be used on numbers. They check if the left number is "smaller or equal"(`<=`), "bigger or equal"(`>=`), "smaller" (`<`) or "bigger" (`>`) than the right number.

`1 <= 1` evaluates to `True`
`2 >= 3` evaluates to `False`
`-2 < -1` evaluates to `True`
`6 > 6` evaluates to `False`

## Logic Operators
`not` simply inverts the value:

`not False` evaluates to `True`
`not True` evaluates to `False`

`and` evaluates to `True` only if both values are `True`

`True and True` evaluates to `True`
`True and False` evaluates to `False`
`False and False` evaluates to `False`

`or` evaluates to `True` if at least one of the values is `True`

`True or True` evaluates to `True`
`True or False` evaluates to `True`
`False or False` evaluates to `False`
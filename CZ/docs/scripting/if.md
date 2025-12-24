# Podmínky (`if`)
Konstrukce `if`, `elif` a `else` umožňují podmíněné provádění kódu.

`if condition1:
    do_a_flip()
elif condition2:
    harvest()
else:
    do_a_flip()
    harvest()`

## Syntaxe
`if` provede blok kódu pouze, pokud podmínka vyhodnotí na `True`. Je podobný `while`, akorát se neopakuje.
`if` přijímá podmínku stejně jako smyčka `while` a provede blok kódu if, pokud je podmínka vyhodnocena jako `True`:

`#do a flip if condition is True
if condition:
	do_a_flip()`

Po `if` můžete přidat `else`, který se vykoná, pokud je podmínka `False`.

`elif` je zkratka pro `else if` a umožňuje řetězit více podmínek:

`if condition1:
    #a
elif condition2:
    #b
else:
    #c`
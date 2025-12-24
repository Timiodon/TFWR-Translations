# Continue
`continue` umožňuje přeskočit aktuální iteraci smyčky a pokračovat další iterací nejvnitřnější smyčky.

`for i in range(10):
    continue
    print("this is never printed")`

Tento příklad projde všech 10 iterací smyčky, ale `print` za `continue` se nikdy nevykoná.

`continue` funguje i v `while` smyčkách.

`while True:
    if not can_harvest():
        continue

    harvest()`

Tento kód zavolá `harvest()` jen tehdy, když je `can_harvest()` `True`.
Má stejný efekt jako:

`while True:
    if can_harvest():
        harvest()`

Ve vnořených smyčkách `continue` ovlivní vždy nejvnitřnější smyčku.

`for i in range(10):
    for j in range(10):
        print("this is printed 100 times")
        continue
        print("this is never printed")
    print("this is printed 10 times")`
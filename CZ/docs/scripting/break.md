# Break
Příkaz `break` umožňuje předčasné ukončení smyčky. Když program narazí na `break`, okamžitě opustí nejvnitřnější smyčku a pokračuje prováděním kódu za ní.

`for i in range(10):
    break
print(i)`

Tento příklad vytiskne `0`, protože `i` má v první iteraci hodnotu `0` a `break` smyčku ukončí.

`break` funguje i v `while` smyčkách.

`while True:
    if can_harvest():
        break`

Tento kód poběží, dokud `can_harvest()` není `True`.
Má stejný efekt jako:

`while not can_harvest():
    pass`

V případě vnořených smyček `break` vždy opustí tu nejvnitřnější.

`for i in range(10):
    for j in range(10):
        break
        print("this is never printed")
    print("this is printed 10 times")`
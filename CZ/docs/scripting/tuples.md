# Tuples
N-tice (tuples) jsou skvělý způsob, jak zkombinovat více hodnot do jedné proměnné.  
Pro vytvoření n-tice stačí oddělit hodnoty čárkami:

`tuple = 1, 2`

N-tici můžeš také rozbalit zpět do několika proměnných. V následujícím kódu je n-tice `(1,2)` rozbalena do proměnných `a` a `b`.

`a, b = 1, 2`

N-tice lze indexovat stejně jako seznamy, ale jsou neměnné – po vytvoření je nelze měnit.

`tuple = 1, 2`

`print(tuple[1])`
vypíše `2`

`tuple[0] = 3`
vyvolá chybu
<unlock=dicts>
Na rozdíl od seznamů mohou být n-tice použity jako klíče ve slovnících.

`d = {(1,2):(4,5)}

print(d[(1,2)])`
vypíše `(4,5)`</unlock>

Mohou být také užitečné pro vracení více hodnot z funkce.

`def f():
    return 1, 2

a, b = f()`
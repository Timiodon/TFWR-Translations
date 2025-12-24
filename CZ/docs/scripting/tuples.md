# N-tice (Tuples)
N-tice jsou skvělý způsob, jak zkombinovat více hodnot do jedné hodnoty.
K vytvoření n-tice stačí oddělit hodnoty čárkami:

`tuple = 1, 2`

Můžete je také znovu rozbalit do několika proměnných. V kódu níže je n-tice `(1,2)` rozbalena do dvou proměnných `a` a `b`.

`a, b = 1, 2`

N-tice lze indexovat jako seznamy, ale jsou neměnné a po vytvoření je nelze změnit.

`tuple = 1, 2`

`print(tuple[1])`
vypíše `2`

`tuple[0] = 3`
vyvolá chybu
<unlock=dicts>
Na rozdíl od seznamů lze n-tice použít jako klíče ve slovnících.

`d = {(1,2):(4,5)}

print(d[(1,2)])`
`vypíše` (4,5)</unlock>

Mohou být také užitečné pro vrácení více hodnot z funkce.

`def f():
    return 1, 2

a, b = f()`
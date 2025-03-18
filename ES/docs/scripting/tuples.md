# Tuplas
Las tuplas son una excelente forma de combinar múltiples valores en un solo valor. 
Para crear una tupla, solo separa los valores con comas:

`tuple = 1, 2`

También puedes desempaquetarlas en varias variables nuevamente. En el código a continuación, la tupla `(1,2)` se desempaqueta en dos variables `a` y `b`.

`a, b = 1, 2`

Las tuplas se pueden indexar como listas, pero son inmutables y no se pueden cambiar después de su creación.

`tuple = 1, 2`

`print(tuple[1])`
imprime `2`

`tuple[0] = 3`
lanza un error
<unlock=dicts>
A diferencia de las listas, las tuplas se pueden usar como claves en dictionaries.

`d = {(1,2):(4,5)}

print(d[(1,2)])`
`imprime` (4,5)</unlock>

También pueden ser útiles para devolver múltiples valores en una función.

`def f():
    return 1, 2

a, b = f()`
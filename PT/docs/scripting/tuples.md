# Tuples
Os tuples são uma ótima maneira de combinar múltiplos valores num único valor.
Para criar um tuple, basta separar os valores com vírgulas:

`tuple = 1, 2`

Podes também desempacotá-los novamente em várias variáveis. No código abaixo, o tuple `(1,2)` é desempacotado em duas variáveis `a` e `b`.

`a, b = 1, 2`

Os tuples podem ser indexados como listas, mas são imutáveis e não podem ser alterados após a criação.

`tuple = 1, 2`

`print(tuple[1])`
imprime `2`

`tuple[0] = 3`
lança um erro
<unlock=dicts>
Ao contrário das listas, os tuples podem ser usados como chaves em dictionaries.

`d = {(1,2):(4,5)}

print(d[(1,2)])`
`imprime` (4,5)</unlock>

Também podem ser úteis para retornar múltiplos valores numa função.

`def f():
    return 1, 2

a, b = f()`
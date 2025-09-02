# Operadores
operadores aritméticos: `+, -, *, /, //, %, **`
operadores de comparação: `==, !=, <=, >=, <, >`
operadores booleanos: `not, and, or`

Nota: Todos os números no jogo são números de ponto flutuante. Portanto, todos os operadores aritméticos são operadores de ponto flutuante.
`//` é definido para apenas arredondar o número para baixo após a divisão.

Para operadores de atribuição, você precisa desbloquear o desbloqueio "Variáveis".

## Introdução
Operadores permitem que você compare, modifique e combine valores. 
Os operadores aritméticos `+, -, *, /, //, %, **` são usados para realizar operações matemáticas comuns em números. 
Os operadores de comparação `==, !=, <=, >=, <, >` são usados para comparar valores. O resultado é sempre `True` ou `False`.
Os operadores lógicos (também chamados de operadores booleanos) `not, and, or` são usados para combinar valores de verdade.

## Operadores Aritméticos
`+` e `-` são usados para adição e subtração.

`2 + 3` avalia para `5`
`3 - 2` avalia para `1`

`*`, `/` e `//` são usados para multiplicação e divisão.

`2 * 3` avalia para `6`
`5 / 2` avalia para `2.5`

`//` faz a mesma coisa que `/`, mas o resultado é arredondado para baixo (para o próximo inteiro).

`5 // 2` avalia para `2`

`%` é o operador de módulo, também conhecido como operador de resto. Ele essencialmente divide os dois números e depois retorna o resto. Você também pode pensar nele como subtrair repetidamente o número da direita do número da esquerda até que o resto seja menor que o número da direita.

`4 % 2` avalia para `0`
`5 % 2` avalia para `1`
`6 % 2` avalia para `0`
`2 % 6` avalia para `2`
`1.5 % 1` avalia para `0.5`

`**` é o operador de potência.

`2**2` avalia para `4`
`(-5)**3` avalia para `-125`

## Operadores de Comparação
`==` e `!=` são usados para verificar se dois valores são "iguais"(`==`) ou "diferentes"(`!=`). Eles podem ser usados em todos os tipos de valores.

`2 == 2` avalia para `True`
`Entities.Bush != Entities.Bush` avalia para `False`
`3 != 3 + 1` avalia para `True`

`<=, >=, <, >` só podem ser usados em números. Eles verificam se o número da esquerda é "menor ou igual"(`<=`), "maior ou igual"(`>=`), "menor" (`<`) ou "maior" (`>`) que o número da direita.

`1 <= 1` avalia para `True`
`2 >= 3` avalia para `False`
`-2 < -1` avalia para `True`
`6 > 6` avalia para `False`

## Operadores Lógicos
`not` simplesmente inverte o valor:

`not False` avalia para `True`
`not True` avalia para `False`

`and` avalia para `True` somente se ambos os valores forem `True`

`True and True` avalia para `True`
`True and False` avalia para `False`
`False and False` avalia para `False`

`or` avalia para `True` se pelo menos um dos valores for `True`

`True or True` avalia para `True`
`True or False` avalia para `True`
`False or False` avalia para `False`
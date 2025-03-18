# Operadores
operadores aritméticos: `+, -, *, /, //, %, **`
operadores de comparação: `==, !=, <=, >=, <, >`
operadores booleanos: `not, and, or`

Nota: Todos os números no jogo são números de ponto flutuante. Então, todos os operadores aritméticos são operadores de ponto flutuante.
`//` é definido para apenas arredondar o número para baixo após a divisão.

Para operadores de atribuição, você precisa desbloquear a seção "Variáveis".

## Introdução
Operadores permitem que você compare, modifique e combine valores. 
Os operadores aritméticos `+, -, *, /, //, %, **` são usados para realizar operações matemáticas comuns em números. 
Os operadores de comparação `==, !=, <=, >=, <, >` são usados para comparar valores. O resultado é sempre `True` ou `False`.
Os operadores lógicos (também chamados de operadores booleanos) `not, and, or` são usados para combinar valores verdadeiros.

## Operadores Aritméticos
`+` e `-` são usados para adição e subtração.

`2 + 3` resulta em `5`
`3 - 2` resulta em `1`

`*`, `/` e `//` são usados para multiplicação e divisão.

`2 * 3` resulta em `6`
`5 / 2` resulta em `2.5`

`//` faz o mesmo que `/` mas o resultado é arredondado para baixo (próximo inteiro inferior).

`5 // 2` resulta em `2`

`%` é o operador de módulo, também conhecido como operador de resto. Ele essencialmente divide os dois números e devolve o resto. Você também pode pensar nele como subtrair repetidamente o número da direita do número da esquerda até que o resto seja menor que o número da direita.

`4 % 2` resulta em `0`
`5 % 2` resulta em `1`
`6 % 2` resulta em `0`
`2 % 6` resulta em `2`
`1.5 % 1` resulta em `0.5`

`**` é o operador de potência.

`2**2` resulta em `4`
`(-5)**3` resulta em `-125`

## Operadores de Comparação
`==` e `!=` são usados para verificar se dois valores são "iguais"(`==`) ou "diferentes"(`!=`). Eles podem ser usados em todos os tipos de valores.

`2 == 2` resulta em `True`
`Entities.Bush != Entities.Bush` resulta em `False`
`3 != 3 + 1` resulta em `True`

`<=, >=, <, >` só podem ser usados em números. Eles verificam se o número da esquerda é "menor ou igual"(`<=`), "maior ou igual"(`>=`), "menor" (`<`) ou "maior" (`>`) que o número da direita.

`1 <= 1` resulta em `True`
`2 >= 3` resulta em `False`
`-2 < -1` resulta em `True`
`6 > 6` resulta em `False`

## Operadores Lógicos
`not` simplesmente inverte o valor:

`not False` resulta em `True`
`not True` resulta em `False`

`and` resulta em `True` apenas se ambos os valores forem `True`

`True and True` resulta em `True`
`True and False` resulta em `False`
`False and False` resulta em `False`

`or` resulta em `True` se pelo menos um dos valores for `True`

`True or True` resulta em `True`
`True or False` resulta em `True`
`False or False` resulta em `False`
# Variáveis
Variáveis podem ser vistas como recipientes nomeados que podem guardar um valor. O operador `=` é usado para declarar uma variável e armazenar um valor nela.

`nome_variavel = valor`

O lado esquerdo do operador é o nome da variável. Você pode nomeá-la como quiser. O lado direito é uma expressão cujo valor resultante será armazenado na variável.

Declare uma variável chamada `a` e armazene o valor `5` nela:
`a = 5`
Declare uma variável chamada `b` e armazene o valor de retorno de `can_harvest()` nela:
`b = can_harvest()`

Não confunda o operador `=` com o operador `==`. O operador `==` verifica se dois valores são iguais e retorna `True` ou `False`. O operador `=` atribui o valor à direita ao nome à esquerda.

Depois que uma variável foi atribuída, você pode usá-la no código para recuperar o valor que ela contém.

`a = 5
for i in range(a):
	do_a_flip()`

O loop acima é executado 5 vezes porque `a` está definido como `5`. O `i` no loop `for` também é uma variável que recebe automaticamente o valor atual da sequência em cada iteração do loop. (Não tem que ser chamado `i`, você pode usar qualquer nome de variável válido.)

As variáveis também permitem que você faça a mesma coisa com um loop while:

`a = 5
i = 0
while i < a:
	do_a_flip()
	i = i + 1`

Isso faz a mesma coisa que o loop for acima. Apenas temos que incrementar i manualmente. Note que para incrementar i, definimos que ele será igual ao seu próprio valor mais `1`. Alterar o valor de uma variável com base em seu valor anterior é algo muito comum. 
Isso pode ser abreviado usando esses operadores: `+=, -=, *=, /=, %=`

`i = i + 1` é o mesmo que `i += 1`
`a = a / 3` é o mesmo que `a /= 3`
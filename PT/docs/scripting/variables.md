# Variáveis
As variáveis podem ser vistas como contentores com nome que podem guardar um valor.
O operador `=` é usado para declarar uma variável e guardar um valor nela.

`nome_da_variavel = valor`

O lado esquerdo do operador é o nome da variável. Podes dar-lhe o nome que quiseres.
O lado direito é uma expressão cujo valor resultante será guardado na variável.

Declara uma variável chamada `a` e guarda o valor `5` nela:
`a = 5`
Declara uma variável chamada `b` e guarda o valor de retorno de `can_harvest()` nela:
`b = can_harvest()`

Não confundas o operador `=` com o operador `==`.
O operador `==` verifica se dois valores são iguais e retorna `True` ou `False`.
O operador `=` atribui o valor à direita ao nome à esquerda.

Depois de uma variável ter sido atribuída, podes usá-la no código para obter o valor que ela contém.

`a = 5
for i in range(a):
	do_a_flip()`

O loop acima é executado 5 vezes porque `a` está definido como `5`.
O `i` no loop `for` também é uma variável à qual é automaticamente atribuído o valor atual da sequência em cada iteração do loop. (Não tem de se chamar `i`, podes dar-lhe qualquer nome de variável válido.)

As variáveis também te permitem fazer a mesma coisa com um loop while:

`a = 5
i = 0
while i < a:
	do_a_flip()
	i = i + 1`

Isto faz a mesma coisa que o loop for acima. Apenas temos de incrementar i manualmente.
Nota que para incrementar i, definimo-lo como o seu próprio valor mais `1`. Mudar o valor de uma variável com base no seu valor anterior é algo muito comum.
Pode ser abreviado usando estes operadores: `+=, -=, *=, /=, %=`

`i = i + 1` é o mesmo que `i += 1`
`a = a / 3` é o mesmo que `a /= 3`

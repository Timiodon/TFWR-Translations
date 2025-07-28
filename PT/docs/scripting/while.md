# Loop While
Desbloqueaste o loop `while` e os valores `True` e `False`. O loop `while` continua a executar o corpo do loop enquanto a condição for `True`.

`while condition:
	#corpo do loop`

Não te preocupes em criar loops infinitos. Os atrasos na execução impedirão o programa de congelar.

## Para Iniciantes
Talvez já tenhas tentado colocar várias chamadas de `harvest()` seguidas:

`harvest()
harvest()
harvest()`

Isto permite-te colher várias vezes numa única execução do programa.
No entanto, seria bom colher mais de três vezes, e escrever o mesmo código várias vezes é uma má prática.
A solução é um loop.
Um loop permite-te executar o mesmo código várias vezes.

O loop while recebe uma condição, que é um valor lógico que só pode estar num de dois estados: `True` ou `False`.
Tal valor é chamado de valor Booleano.

O loop então executa o código dentro do loop até que a condição seja False.
O loop while tem esta aparência:

`while condition:
	#corpo do loop
	#corpo do loop
	#...`
	
Onde tens de substituir "condition" por um valor booleano e `#corpo do loop` com o que quer que queiras fazer no loop.

Existem dois valores booleanos constantes disponíveis. Constantes são valores que nunca mudam durante o programa.

Para criar um valor booleano constante que é sempre `True`, podes simplesmente escrever `True`. Escreve `False` como um valor booleano constante que será sempre `False`.
Então poderias escrever ou


`while False:
	do_a_flip()`

ou

`while True:
	do_a_flip()`

O primeiro nunca fará um pino e o segundo fará pinos para sempre (um loop infinito).

Normalmente, criar um loop infinito é uma má ideia porque congela o programa, mas neste jogo há atrasos entre cada iteração do loop, então fará com que o drone continue a fazer um pino até que o pares manualmente, premindo novamente o botão de execução.

Repara como a linha a seguir aos dois pontos está indentada. A indentação como esta é usada para separar blocos de código.
Basta pressionar Tab para adicionar indentação e Shift + Tab (ou Backspace) para a remover.

O loop repetirá todas as instruções indentadas após os dois pontos.
As instruções após o bloco indentado serão executadas depois de o loop terminar.

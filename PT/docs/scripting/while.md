# Loop While
Você desbloqueou o loop `while` e os valores `True` e `False`. O loop `while` continua executando o corpo do loop enquanto a condição for `True`.

`while condition:
	#corpo do loop`

Não se preocupe em criar loops infinitos. Os atrasos na execução impedirão que o programa congele.

## Para Iniciantes
Talvez você já tenha tentado colocar várias chamadas `harvest()` em sequência:

`harvest()
harvest()
harvest()`

Isso permite que você colha várias vezes em uma única execução do programa. 
No entanto, seria bom colher mais de três vezes, e escrever o mesmo código várias vezes é uma má prática. 
A solução é um loop. 
Um loop permite que você execute o mesmo código várias vezes.

O loop while recebe uma condição, que é um valor lógico que só pode estar em um de dois estados: `True` ou `False`. 
Tal valor é chamado de valor Booleano.

O loop então executa o código dentro do loop até que a condição seja False.
O loop while se parece com isto:

`while condition:
	#corpo do loop
	#corpo do loop
	#...`
	
Onde você tem que substituir "condition" por um valor booleano e `#corpo do loop` com o que você quiser fazer no loop.

Existem dois valores booleanos constantes disponíveis. Constantes são valores que nunca mudam durante o programa.

Para criar um valor booleano constante que é sempre `True`, você pode simplesmente escrever `True`. Escreva `False` para um valor booleano constante que sempre será `False`.
Então você poderia escrever


`while False:
	do_a_flip()`

ou

`while True:
	do_a_flip()`

O primeiro nunca dará uma pirueta e o segundo dará piruetas para sempre (um loop infinito). 

Normalmente, criar um loop infinito é uma má ideia porque irá congelar o programa, mas neste jogo existem atrasos entre cada iteração do loop, então fará com que o drone continue a dar uma pirueta até que você o pare manualmente pressionando o botão de execução novamente.

Note como a linha após os dois pontos está indentada. Indentação como esta é usada para separar blocos de código.
Basta pressionar Tab para adicionar indentação e Shift + Tab (ou Backspace) para removê-la.

O loop repetirá todas as declarações indentadas após os dois pontos.
Declarações após o bloco indentado serão executadas depois que o loop terminar.

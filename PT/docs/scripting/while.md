# While Loop
Você desbloqueou o loop `while` e os valores `True` e `False`. O loop `while` continua executando o corpo do loop enquanto a condição for `True`.

`while condição:
	#corpo do loop`

Não se preocupe em criar loops infinitos. Os atrasos na execução impedirão que o programa congele.

## Para Iniciantes
Talvez você já tenha tentado colocar várias chamadas de `harvest()` em sequência:

`harvest()
harvest()
harvest()`

Isso permite que você colha várias vezes em uma execução do programa. 
No entanto, seria bom colher mais do que três vezes, e escrever o mesmo código várias vezes é uma prática ruim. 
A solução é um loop. 
Um loop permite executar o mesmo código várias vezes.

O loop while aceita uma condição, que é um valor lógico que só pode estar em um de dois estados: `True` ou `False`. 
Um valor assim é chamado de valor booleano.

O loop então executa o código dentro do loop até que a condição seja `False`.
O loop while se parece com isto:

`while condição:
	#corpo do loop
	#corpo do loop
	#...`

Onde você deve substituir "condição" por um valor booleano e `#corpo do loop` pelo que você quiser fazer no loop.

Existem dois valores booleanos constantes disponíveis. Constantes são valores que nunca mudam durante o programa.

Para criar um valor booleano constante que é sempre `True`, você pode simplesmente escrever `True`. Escreva `False` como um valor booleano constante que será sempre `False`.
Então você poderia escrever

`while False:
	do_a_flip()`

ou

`while True:
	do_a_flip()`

O primeiro nunca fará uma cambalhota e o segundo fará cambalhotas para sempre (um loop infinito).

Normalmente, criar um loop infinito é uma má ideia porque ele congela o programa, mas neste jogo há atrasos entre cada iteração do loop, então isso fará com que o drone continue fazendo uma cambalhota até que você o pare manualmente pressionando o botão de execução novamente.

Perceba como a linha após os dois pontos está indentada. A indentação assim é usada para separar blocos de código.
Basta pressionar Tab para adicionar indentação e Shift + Tab (ou Backspace) para removê-la.

O loop repetirá todas as instruções indentadas após os dois pontos.
As instruções após o bloco indentado serão executadas após o loop terminar.
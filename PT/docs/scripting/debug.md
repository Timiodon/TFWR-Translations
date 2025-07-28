# Debug
Às vezes, o teu código simplesmente não funciona e precisas de descobrir porquê. Existem algumas ferramentas para te ajudar a fazer isso.

A primeira é executar o programa passo a passo.
Podes entrar no modo passo a passo com o botão ao lado do botão Executar ou definindo um breakpoint.

Os breakpoints podem ser adicionados clicando no painel de breakpoints à esquerda do código.
![](Breakpoints227)
Quando a execução chega à linha onde o breakpoint está, ela mudará automaticamente para o modo passo a passo.

Quando passas o rato sobre uma variável, o seu valor atual é exibido.

A função `print()` também pode ser muito útil. Ela escreverá qualquer valor passado para ela diretamente no ar.

Exemplos:

Imprimir "0.24".
`print(0.24)`

Imprimir "True" ou "False".
`print(can_harvest())`

Imprimir a posição atual.
`print(get_pos_x(), get_pos_y())`

A função print imprime o valor diretamente no ar e na página de [Output](docs/output.md).

Escrever no ar pode por vezes ser um pouco lento se quiseres imprimir muitos valores.
Neste caso, podes usar a função `quick_print()` que imprime apenas na janela de output.

A janela de output também regista avisos e errors, por isso, se algo não funcionar como esperado, pode ser útil verificá-la.

Quando a execução para, o output também é escrito no ficheiro output.txt na pasta do jogo. [output.txt](persistent_data_path/output.txt).
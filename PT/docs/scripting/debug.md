# Debug
Às vezes, seu código simplesmente não funciona e você precisa descobrir o porquê. Existem algumas ferramentas para te ajudar com isso.

A primeira é executar o programa passo a passo. 
Você pode entrar no modo passo a passo com o botão ao lado do botão Executar ou configurando um breakpoint.

Breakpoints podem ser adicionados clicando no painel de breakpoint à esquerda do código.
![](Breakpoints227)
Quando a execução chegar à linha onde está o breakpoint, ele trocará automaticamente para o modo passo a passo.

Quando você move o mouse sobre uma variável, seu valor atual é exibido.

A função `print()` também pode ser muito útil. Ela escreve qualquer valor passado diretamente no ar.

Exemplos:

Imprimir "0.24".
`print(0.24)`

Imprimir "True" ou "False".
`print(can_harvest())`

Imprimir a posição atual.
`print(get_pos_x(), get_pos_y())`

A função print imprime o valor diretamente no ar e na página [Output](docs/output.md).

Escrever no ar pode às vezes ser um pouco lento se você quiser imprimir muitos valores.
Nesse caso, você pode usar a função `quick_print()`, que imprime apenas na janela de output.

A janela de output também registra avisos e erros, então se algo não funcionar como esperado, pode ser útil checar isso.

Quando a execução para, o output também é escrito no arquivo output.txt na pasta do jogo. [output.txt](persistent_data_path/output.txt).
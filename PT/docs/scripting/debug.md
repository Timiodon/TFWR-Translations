# Depuração
Às vezes, seu código simplesmente não funciona e você precisa descobrir o porquê. Existem algumas ferramentas para ajudá-lo com isso.

A primeira é executar o programa passo a passo. 
Você pode entrar no modo passo a passo com o botão ao lado do botão Executar ou definindo um ponto de interrupção.

Pontos de interrupção podem ser adicionados clicando no painel de pontos de interrupção à esquerda do código.
![](Breakpoints227)
Quando a execução chega à linha onde o ponto de interrupção está, ele mudará automaticamente para o modo passo a passo.

Quando você move o mouse sobre uma variável, seu valor atual é exibido.

A função `print()` também pode ser muito útil. Ela escreverá qualquer valor passado para ela diretamente no ar.

Exemplos:

Imprimir "0.24".
`print(0.24)`

Imprimir "True" ou "False".
`print(can_harvest())`

Imprimir a posição atual.
`print(get_pos_x(), get_pos_y())`

A função print imprime o valor diretamente no ar e na página de [Saída](docs/output.md).

Escrever no ar pode ser um pouco lento se você quiser imprimir muitos valores.
Nesse caso, você pode usar a função `quick_print()`, que imprime apenas na janela de saída.

A janela de saída também registra avisos e erros, então, se algo não funcionar como esperado, pode ser útil verificá-la.

Quando a execução para, a saída também é escrita no arquivo output.txt na pasta do jogo. [output.txt](persistent_data_path/output.txt).
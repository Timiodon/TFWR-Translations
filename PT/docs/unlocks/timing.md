# Timing
Se queres mesmo otimizar os teus métodos, precisas de entender como o tempo é medido neste jogo. Este unlock é sobre isso.

## Novas Funções
Existem duas funções úteis para medir quanto tempo as coisas levam:

`get_time()` retorna o tempo em segundos desde o início do jogo.

`get_tick_count()` retorna o número de ticks executados desde o início da execução.

Estas duas funções, bem como `quick_print()`, são completamente gratuitas. Até a operação de chamada é gratuita para elas.

## Detalhes de Execução

### Atenção
Não é assim que o desempenho funciona no mundo real. Estas são apenas regras criadas para este jogo para ter um modelo de tempo consistente e compreensível.
Provavelmente só te vais importar com isto se quiseres hiper-otimizar o teu código.


A unidade básica de tempo para a execução do código é chamada de "tick". Sem melhorias de velocidade e energia, a execução prossegue a uma taxa de `400` ticks por segundo.

Em geral, operações que combinam dois valores como `+, -, *, /, //, %, and, or, ...` levam um tick para serem executadas.
Os operadores de valor único `-` e `not` são gratuitos.
Uma ramificação `if` também leva um tick para ser executada (além do tempo que leva para avaliar a expressão da condição).
Chamadas de função e leituras e escritas de variáveis são gratuitas, mas as definições de função levam 1 tick.
As declarações `import` são gratuitas.
Aceder a um módulo importado com o operador `.` é gratuito.
Se uma função ou módulo foi passado através de argumentos ou atribuições de variáveis, usá-lo custará 1 tick em vez de 0.
Os loops `for` e `while` levam um tick para começar, mas as iterações são gratuitas (não contando o tempo para avaliar as expressões da condição/sequência).
`return`, `break` e `continue` são todos gratuitos.
`pass` leva um tick, por isso pode ser usado para criar atrasos precisos.
Indexar uma estrutura de dados leva um tick para o operador de índice e, no caso de um dictionary ou set, ticks adicionais dependendo do tamanho da chave.

O número de ticks que as funções incorporadas levam para executar está documentado na documentação de cada função individualmente.
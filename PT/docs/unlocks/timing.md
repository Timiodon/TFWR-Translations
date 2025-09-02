# Medição de Tempo
Se você realmente quer otimizar seus métodos, precisa entender como o tempo é medido neste jogo. Este desbloqueio é todo sobre isso.

## Novas Funções
Existem duas funções úteis para medir quanto tempo as coisas levam:

`get_time()` retorna o tempo em segundos desde o início do jogo.

`get_tick_count()` retorna o número de ticks executados desde o início da execução.

Essas duas funções, assim como `quick_print()`, são completamente gratuitas. Até a operação de chamada é gratuita para elas.

## Detalhes de Execução

### Fique Ligado
Não é assim que o desempenho funciona no mundo real. Estas são apenas regras criadas para este jogo ter um modelo de tempo consistente e compreensível.
Você provavelmente só se importará com isso se quiser hiper-otimizar seu código.

A unidade básica de tempo para a execução do código é chamada de "tick". Sem melhorias de velocidade e energia, a execução prossegue a uma taxa de `400` ticks por segundo.

Em geral, operações que combinam dois valores como `+, -, *, /, //, %, and, or, ...` levam um tick para serem executadas.
O `-` unário e o `not` são gratuitos.
Uma estrutura `if` também leva um tick para ser executada (além do tempo que leva para avaliar a expressão da condição).
Chamadas de função e leituras e escritas de variáveis são gratuitas, mas definições de função levam 1 tick.
Instruções `import` são gratuitas.
Acessar um módulo importado com o operador `.` é gratuito.
Se uma função ou módulo foi passado via argumentos ou atribuições de variáveis, usá-lo custará 1 tick em vez de 0.
Os loops `for` e `while` levam um tick para iniciar, mas as iterações são gratuitas (sem contar o tempo para avaliar as expressões da condição/sequência).
`return`, `break` e `continue` são todos gratuitos.
`pass` leva um tick, então pode ser usado para criar atrasos precisos.
Indexar uma estrutura de dados leva um tick para o operador de índice e, no caso de um dicionário ou conjunto, ticks adicionais dependendo do tamanho da chave.

O número de ticks que as funções nativas levam para serem executadas está documentado na documentação de cada função individualmente.
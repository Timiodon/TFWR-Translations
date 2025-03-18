# Tempo
Se você realmente quer otimizar seus métodos, precisa entender como o tempo é medido neste jogo. Este desbloqueio é sobre isso.

## Novas Funções
Existem duas funções úteis para medir quanto tempo as coisas levam:

`get_time()` retorna o tempo em segundos desde o início do jogo.

`get_tick_count()` retorna o número de ticks realizados desde o início da execução.

Essas duas funções, assim como `quick_print()`, são completamente gratuitas. Mesmo a operação de chamada é gratuita para elas.

## Detalhes de Execução

### Aviso
Isso não é como o desempenho funciona no mundo real. Estas são apenas regras inventadas para que este jogo tenha um modelo de tempo consistente e compreensível.
Provavelmente você só vai se importar com isso se quiser hiper-otimizar seu código.

A unidade básica de tempo para a execução do código é chamada de "tick". Sem upgrades de velocidade e energia, a execução procede a uma taxa de `400` ticks por segundo.

Em geral, operações que combinam dois valores, como `+, -, *, /, //, %, and, or, ...`, levam um tick para serem realizadas.
O valor único `-` e `not` são gratuitos.
Um ramo `if` também leva um tick para ser executado (além do tempo necessário para avaliar a expressão condicional).
Chamadas de funções e leituras e escritas de variáveis são gratuitas, mas definições de funções levam 1 tick.
Declarações `import` são gratuitas.
Acessar um módulo importado com o operador `.` é gratuito.
Se uma função ou módulo foi passado por argumentos ou atribuições de variáveis, usá-lo custará 1 tick em vez de 0.
Loops `for` e `while` levam um tick para começar, mas as iterações são gratuitas (sem contar o tempo para avaliar as expressões de condição/sequência).
`return`, `break` e `continue` são todos gratuitos.
`pass` leva um tick, então pode ser usado para criar atrasos precisos.
Indexar em uma estrutura de dados leva um tick para o operador de índice e, no caso de um dictionary ou set, ticks adicionais dependendo do tamanho da chave.

O número de ticks que funções builtin levam para executar está documentado na documentação de cada função individualmente.
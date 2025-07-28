# Simulação

As simulações permitem-te testar código rapidamente sem alterar o estado da quinta real.
O estado inicial da simulação pode ser escolhido livremente, e quando a simulação termina, a quinta real estará no estado exato em que estava antes do início da simulação.

A função `simulate()` é usada para iniciar uma simulação.

o ficheiro onde a execução deve começar
`filename = "f1"`

começar com tudo desbloqueado e totalmente melhorado
`sim_unlocks = Unlocks`

começar com 10000 cenouras e 50 feno
`sim_items = {Items.Carrot : 10000, Items.Hay : 50}`

começar com uma variável global "a" com o valor 13
`sim_globals = {"a" : 13}`

usar uma seed aleatória fixa
`seed = 0`

acelerar a simulação por um fator de 64
`speedup = 64`

executar a simulação
`run_time = simulate(filename, sim_unlocks, sim_items, sim_globals, seed, speedup)`

A função `simulate()` retorna o tempo, em segundos, que demorou a simular o ficheiro inicial dado.

### Nome do Ficheiro
O primeiro argumento da função simulate é o nome do ficheiro. Este é o nome que é exibido no topo da janela de código. A simulação executará o ficheiro especificado como se tivesses clicado no botão Executar nele.

### Unlocks Iniciais
Todas as funcionalidades de programação como loops, declarações if, listas, dicts,... permanecerão sempre desbloqueadas.

O segundo argumento permite-te especificar com que unlocks/melhorias a simulação deve começar, para além das funcionalidades de programação. Isto deve ser uma sequência de unlocks. A simulação começará com todos os unlocks na sequência melhorados para o seu nível máximo.

Se quiseres especificar um nível de melhoria diferente do máximo, podes passar um dictionary que mapeia os unlocks para níveis de unlock. Neste caso, valores negativos correspondem ao nível máximo de unlock.

### Itens Iniciais
O terceiro argumento permite-te passar um dictionary que mapeia itens para números. Especifica os itens com os quais a simulação deve começar.

### Globals Iniciais
Como a simulação inicia uma execução de programa completamente nova, não podes aceder a variáveis do programa que inicia a simulação.
No entanto, é possível passar valores para a simulação usando o quarto argumento. Este é um dict que mapeia nomes de variáveis na forma de strings para valores. Estas variáveis são então adicionadas ao scope global da execução dentro da simulação.

Nota que isto copia todos os valores, por isso, alterá-los dentro da simulação não afetará os valores originais fora da simulação. Não é possível retornar valores da simulação, exceto o tempo que demorou a executar.

### Seed Aleatória
O quinto argumento permite-te especificar a seed aleatória usada na simulação. Isto deve ser um número inteiro positivo. Valores negativos farão com que seja usada uma seed aleatória.

A seed aleatória afeta tudo, desde os tempos de crescimento das plantas até aos layouts dos labirintos e aos tempos de evaporação da água. Se iniciares a mesma simulação várias vezes com a mesma seed aleatória e as mesmas condições iniciais, o resultado deverá ser sempre o mesmo.

### Aceleração
O sexto argumento é a aceleração inicial da simulação. Isto permite-te testar coisas rapidamente. Se o jogo não conseguir acompanhar a velocidade definida, abrandará automaticamente.

A aceleração não afeta o resultado da simulação de forma alguma. Existe apenas para reduzir o tempo de espera.
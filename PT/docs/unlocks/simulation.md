# Simulação

Simulações permitem que você teste código rapidamente sem alterar o estado da fazenda real.
O estado inicial da simulação pode ser escolhido livremente, e quando a simulação termina, a fazenda real estará no estado exato em que estava antes do início da simulação.

A função `simulate()` é usada para iniciar uma simulação.

o arquivo em que a execução deve começar
`filename = "f1"`

comece com tudo desbloqueado e totalmente melhorado
`sim_unlocks = Unlocks`

comece com 10000 cenouras e 50 fenos
`sim_items = {Items.Carrot : 10000, Items.Hay : 50}`

comece com uma variável global "a" com valor 13
`sim_globals = {"a" : 13}`

use uma semente aleatória fixa
`seed = 0`

acelere a simulação por um fator de 64
`speedup = 64`

execute a simulação
`run_time = simulate(filename, sim_unlocks, sim_items, sim_globals, seed, speedup)`

A função `simulate()` retorna o tempo, em segundos, que levou para simular o arquivo inicial fornecido.

### Nome do Arquivo
O primeiro argumento da função simulate é o nome do arquivo. Este é o nome que é exibido no topo da janela de código. A simulação executará o arquivo especificado como se você tivesse clicado no botão Executar nele.

### Desbloqueios Iniciais
Todos os recursos de programação como loops, instruções `if`, listas, dicionários,... sempre permanecerão desbloqueados. 

O segundo argumento permite que você especifique com quais desbloqueios/melhorias a simulação deve começar, além dos recursos de programação. Isso deve ser uma sequência de desbloqueios. A simulação começará com todos os desbloqueios na sequência melhorados para o seu nível máximo.

Se você quiser especificar um nível de melhoria diferente do máximo, pode passar um dicionário que mapeia os desbloqueios para os níveis de desbloqueio. Neste caso, valores negativos correspondem ao nível máximo de desbloqueio.

### Itens Iniciais
O terceiro argumento permite que você passe um dicionário que mapeia itens para números. Ele especifica os itens com os quais a simulação deve começar.

### Globais Iniciais
Como a simulação inicia uma execução de programa completamente nova, você não pode acessar variáveis do programa que inicia a simulação.
No entanto, é possível passar valores para a simulação usando o quarto argumento. Este é um dicionário que mapeia nomes de variáveis na forma de strings para valores. Essas variáveis são então adicionadas ao escopo global da execução dentro da simulação.

Note que isso copia todos os valores, então modificá-los dentro da simulação não afetará os valores originais fora da simulação. Não é possível retornar valores da simulação além do tempo que ela levou para ser executada.

### Semente Aleatória
O quinto argumento permite que você especifique a semente aleatória usada na simulação. Deve ser um inteiro positivo. Valores negativos farão com que uma semente aleatória seja usada.

A semente aleatória afeta tudo, desde os tempos de crescimento das plantas até os layouts dos labirintos e os tempos de decaimento da água. Se você iniciar a mesma simulação várias vezes com a mesma semente aleatória e as mesmas condições iniciais, o resultado deve ser sempre o mesmo.

### Aceleração
O sexto argumento é a aceleração inicial da simulação. Isso permite que você teste as coisas rapidamente. Se o jogo não conseguir acompanhar a velocidade definida, ele diminuirá a velocidade automaticamente.

A aceleração não afeta o resultado da simulação de forma alguma. Ela existe apenas para reduzir o tempo de espera.
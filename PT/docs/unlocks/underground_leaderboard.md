# Placar de Líderes Subterrâneo
O subsolo guarda desafios ainda maiores. Está pronto para otimizar seus programas de mineração e cultivo?
Com este desbloqueio, você pode competir pelos métodos mais eficientes nas profundezas.

Você pode iniciar uma tentativa do placar de líderes subterrâneo chamando `leaderboard_run(leaderboard, filename, speedup)`.
Isso inicia uma [simulação](docs/unlocks/simulation.md) parecida com `simulate()`, mas com condições iniciais fixas. Cada categoria do placar tem condições iniciais e de sucesso diferentes.

A tentativa no placar de líderes é bem-sucedida se a condição de sucesso for `True` quando a simulação terminar. 

A simulação NÃO terminará automaticamente quando o objetivo for alcançado. Você deve garantir que o programa termine.
Se a tentativa for bem-sucedida, seu tempo será adicionado ao placar de líderes.

Para reduzir a variação, todas as tentativas devem abranger pelo menos 2 horas de tempo simulado. Você pode acelerar a simulação, então ela não levará tudo isso em tempo real. Se uma tentativa terminar antes, ela será repetida até o tempo simulado total chegar a 2 horas. A média de tempo de todas as tentativas será enviada como sua pontuação.

Aqui está uma configuração de exemplo para entrar no placar `Leaderboards.Rice_Single`.

![|x400](UndergroundLeaderboardSetup)

## Reinicialização Subterrânea Mais Rápida
A reinicialização subterrânea é a categoria de maior prestígio. Nela você automatiza toda a árvore de mineração, começando com uma casa e terminando ao desbloquear `Unlocks.Underground_Leaderboard` novamente.

Você não precisa desbloquear tudo: tente desbloquear `Unlocks.Underground_Leaderboard` o mais rápido possível.

Lembre-se de que você pode usar `num_unlocked(unlock) > 0` para verificar se algo está desbloqueado. Também pode usar `get_cost()` em desbloqueios para consultar o custo deles e produzir automaticamente os itens certos.

`unlock()` não considera as dependências da árvore de tecnologias. Por exemplo, é possível desbloquear `Unlocks.Fertilizer` antes de `Unlocks.Water`.

Chamada de Função:
`leaderboard_run(Leaderboards.Fastest_Underground_Reset, filename, speedup)`

Simulação Equivalente:
`unlocks = {}
items = {}
globals = {}
#um valor de semente negativo significa uma semente aleatória
seed = -1
simulate(filename, unlocks, items, globals, seed, speedup)`

Condição de Sucesso:
`num_unlocked(Unlocks.Underground_Leaderboard) > 0`

## Minérios
Este placar testa sua habilidade de produzir minérios, especialmente quartzo. Ele modifica a geração do solo para fornecer carvão, ferro e quartzo, nessa ordem.

Comece com tudo desbloqueado e produza `20000` de quartzo o mais rápido possível.

Chamada de Função:
`leaderboard_run(Leaderboards.Ores, filename, speedup)`

Simulação Equivalente:
`unlocks = Unlocks
items = {Items.Power: 1000000000}
globals = {}
seed = -1
simulate(filename, unlocks, items, globals, seed, speedup)`

Condição de Sucesso:
`num_items(Items.Quartz) >= 20000`

## Mapa do Tesouro
Este placar começa com tudo desbloqueado e muita energia. Ele modifica a geração do solo para que existam muitos mapas do tesouro.

Ele acontece em um mundo 8x8 com um único drone. O objetivo é produzir `115000` de ouro o mais rápido possível.

Chamada de Função:
`leaderboard_run(Leaderboards.Treasure_Map, filename, speedup)`

Simulação Equivalente:
`unlocks = Unlocks
items = {Items.Power: 1000000000}
globals = {}
seed = -1
simulate(filename, unlocks, items, globals, seed, speedup)`

Condição de Sucesso:
`num_items(Items.Gold) >= 115000`

## Placares de Recursos
Esses placares se concentram em produzir recursos específicos o mais rápido possível. Você começa com tudo desbloqueado e muita energia. A única exceção é o placar de pirâmides, em que você precisa gerar energia restaurando pirâmides.

O objetivo é produzir uma quantidade definida de recursos.

Como sempre, você precisa garantir que seu programa termine quando atingir o objetivo. Uma corrida não termina até que o programa termine, mesmo que o objetivo seja alcançado.

Esses placares modificam a geração do solo para que o recurso desejado apareça continuamente. Assim, não é preciso usar `clear()`. Por exemplo, o placar de arroz consiste apenas em camadas de argila.

### `Leaderboards.Rice`
`leaderboard_run(Leaderboards.Rice, filename, speedup)`
Condição de Sucesso: `num_items(Items.Rice) >= 2000000`

### `Leaderboards.Bamboo`
O placar de bambu proíbe escavações.

`leaderboard_run(Leaderboards.Bamboo, filename, speedup)`
Condição de Sucesso: `num_items(Items.Bamboo) >= 500000000`

### `Leaderboards.Dynamite`
`leaderboard_run(Leaderboards.Dynamite, filename, speedup)`
Condição de Sucesso: `num_items(Items.Dynamite) >= 10000000`

### `Leaderboards.Mushrooms`
`leaderboard_run(Leaderboards.Mushrooms, filename, speedup)`
Condição de Sucesso: `num_items(Items.Mushroom) >= 240000`

### `Leaderboards.Pyramids`
`leaderboard_run(Leaderboards.Pyramids, filename, speedup)`
Condição de Sucesso: `num_items(Items.Power) >= 150000`

## Placares Subterrâneos com Um Drone
Também há placares para produzir com um único drone. Você recebe apenas um drone e uma fazenda 8x8 e precisa produzir certa quantidade de recursos o mais rápido possível.

### `Leaderboards.Rice_Single`
`leaderboard_run(Leaderboards.Rice_Single, filename, speedup)`
Condição de Sucesso: `num_items(Items.Rice) >= 100000`

### `Leaderboards.Ores_Single`
`leaderboard_run(Leaderboards.Ores_Single, filename, speedup)`
Condição de Sucesso: `num_items(Items.Quartz) >= 4000`

### `Leaderboards.Bamboo_Single`
`leaderboard_run(Leaderboards.Bamboo_Single, filename, speedup)`
Condição de Sucesso: `num_items(Items.Bamboo) >= 25000000`

### `Leaderboards.Dynamite_Single`
`leaderboard_run(Leaderboards.Dynamite_Single, filename, speedup)`
Condição de Sucesso: `num_items(Items.Dynamite) >= 100000`

### `Leaderboards.Mushrooms_Single`
`leaderboard_run(Leaderboards.Mushrooms_Single, filename, speedup)`
Condição de Sucesso: `num_items(Items.Mushroom) >= 30000`

### `Leaderboards.Pyramids_Single`
`leaderboard_run(Leaderboards.Pyramids_Single, filename, speedup)`
Condição de Sucesso: `num_items(Items.Power) >= 30000`


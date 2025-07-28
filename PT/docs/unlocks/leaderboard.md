# Leaderboard
Se chegaste até aqui, superaste muitos desafios. Mas será que os resolveste de forma eficiente?
Podes competir com outros jogadores em várias leaderboards pelos métodos de cultivo mais eficientes.

Podes iniciar uma corrida da leaderboard chamando `leaderboard_run(leaderboard, filename, speedup)`.
Isto inicia uma [simulação](docs/unlocks/simulation.md) semelhante a `simulate()`, exceto que as condições iniciais são fixas. Cada categoria da leaderboard tem condições de início e de sucesso diferentes.

A corrida da leaderboard é bem-sucedida se a condição de sucesso for `True` quando a simulação termina. A simulação não terminará automaticamente quando o objetivo for alcançado. Deves garantir que o programa termina.
Se a corrida for bem-sucedida, o teu tempo será adicionado à leaderboard.

Para reduzir a variância, todas as corridas devem durar pelo menos 2 horas (podes acelerá-la, por isso não demorará tanto tempo). Se uma corrida for concluída mais cedo, será repetida até que um tempo total de 2 horas seja atingido. A média de todas as corridas é então enviada como a tua pontuação.

Aqui está um exemplo de configuração que te colocará na leaderboard de feno.
![](LeaderboardSetup400)

## Reset Mais Rápido
O reset mais rápido é a categoria de maior prestígio. Automatiza completamente o jogo a partir de um único lote de quinta até desbloquear as leaderboards novamente.

Não precisas de desbloquear tudo, apenas tenta desbloquear `Unlocks.Leaderboard` o mais rápido possível.

Lembra-te que podes usar `num_unlocked(unlock) > 0` para verificar se algo está desbloqueado e podes usar `get_cost()` em unlocks para ver o que custam, para que possas cultivar automaticamente os itens certos.

Chamada de Função:
`leaderboard_run(Leaderboards.Fastest_Reset, filename, speedup)`

Simulação Equivalente:
`unlocks = {}
items = {}
globals = {}
#um valor de seed negativo significa uma seed aleatória
seed = -1
simulate(filename, unlocks, items, globals, seed, speedup)`

Condição de Sucesso:
`num_unlocked(Unlocks.Leaderboard) > 0`

## Labirinto
Começa com tudo desbloqueado e cultiva `300000` de ouro o mais rápido que conseguires. Esta é exatamente a quantidade de ouro que ganharás ao resolver um labirinto `300` vezes.

Chamada de Função:
`leaderboard_run(Leaderboards.Maze, filename, speedup)`

Simulação Equivalente:
`unlocks = Unlocks
items = {Items.Weird_Substance : 1000000, Items.Power: 1000000}
globals = {}
seed = -1
simulate(filename, unlocks, items, globals, seed, speedup)`

Condição de Sucesso:
`num_items(Items.Gold) >= 300000`

## Dinossauro
Começa com tudo desbloqueado e cultiva `98010` de ossos o mais rápido que conseguires. Este é exatamente o número de ossos que obterás se preencheres uma área de 10x10 com a cauda de dinossauro.

Chamada de Função:
`leaderboard_run(Leaderboards.Dinosaur, filename, speedup)`

Simulação Equivalente:
`unlocks = Unlocks
items = {Items.Pumpkin : 1000000, Items.Power: 1000000}
globals = {}
seed = -1
simulate(filename, unlocks, items, globals, seed, speedup)`

Condição de Sucesso:
`num_items(Items.Bone) >= 98010`

## Outras Leaderboards de Recursos
Cada planta tem a sua própria leaderboard para cultivar essa planta em particular o mais rápido possível. Começas com todos os unlocks, os recursos de que precisas para cultivar a planta e muita energia. O objetivo é cultivar `100000` do recurso produzido pela planta.

Chamadas de Função:
`leaderboard_run(Leaderboards.Cactus, filename, speedup)`
`leaderboard_run(Leaderboards.Sunflowers, filename, speedup)`
`leaderboard_run(Leaderboards.Pumpkins, filename, speedup)`
`leaderboard_run(Leaderboards.Wood, filename, speedup)`
`leaderboard_run(Leaderboards.Carrots, filename, speedup)`
`leaderboard_run(Leaderboards.Hay, filename, speedup)`
`leaderboard_run(Leaderboards.Polyculture, filename, speedup)`

Condição de Sucesso:
`num_items(resource) >= 100000`

`Leaderboards.Polyculture` requer o cultivo de `100000` de cada um dos três recursos de policultura.
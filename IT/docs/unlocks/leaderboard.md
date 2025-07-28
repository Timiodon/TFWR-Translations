# Leaderboard
Se sei arrivato fin qui, hai superato molte sfide. Ma le hai risolte in modo efficiente?
Puoi competere con altri giocatori su vari leaderboard per i metodi di coltivazione più efficienti.

Puoi iniziare una run del leaderboard chiamando `leaderboard_run(leaderboard, filename, speedup)`.
Questo avvia una [simulazione](docs/unlocks/simulation.md) simile a `simulate()`, ma le condizioni di partenza sono fisse. Ogni categoria di leaderboard ha condizioni di partenza e di successo diverse.

La run del leaderboard ha successo se la condizione di successo è `True` quando la simulazione termina. La simulazione non terminerà automaticamente quando l'obiettivo viene raggiunto. Devi assicurarti che il programma termini.
Se la run ha successo, il tuo tempo sarà aggiunto al leaderboard.

Per ridurre la varianza, tutte le run devono durare almeno 2 ore (puoi accelerarle, quindi non ci vorrà così tanto). Se una run viene completata prima, sarà ripetuta finché non si raggiunge un tempo totale di 2 ore. La media di tutte le run viene quindi caricata come tuo punteggio.

Ecco un esempio di configurazione che ti porterà sul leaderboard del fieno.
![](LeaderboardSetup400)

## Reset Più Veloce
Il reset più veloce è la categoria più prestigiosa. Automatizza completamente il gioco da una singola casella della fattoria fino a sbloccare di nuovo i leaderboard.

Non devi sbloccare tutto, cerca solo di sbloccare `Unlocks.Leaderboard` il più velocemente possibile.

Ricorda che puoi usare `num_unlocked(unlock) > 0` per controllare se qualcosa è sbloccato e puoi usare `get_cost()` sugli sblocchi per vedere quanto costano, così puoi coltivare automaticamente gli item giusti.

Chiamata di Funzione:
`leaderboard_run(Leaderboards.Fastest_Reset, filename, speedup)`

Simulazione Equivalente:
`unlocks = {}
items = {}
globals = {}
#un valore di seed negativo significa un seed casuale
seed = -1
simulate(filename, unlocks, items, globals, seed, speedup)`

Condizione di Successo:
`num_unlocked(Unlocks.Leaderboard) > 0`

## Labirinto
Inizia con tutto sbloccato e coltiva `300000` oro il più velocemente possibile. Questa è esattamente la quantità di oro che guadagnerai risolvendo un labirinto `300` volte.

Chiamata di Funzione:
`leaderboard_run(Leaderboards.Maze, filename, speedup)`

Simulazione Equivalente:
`unlocks = Unlocks
items = {Items.Weird_Substance : 1000000, Items.Power: 1000000}
globals = {}
seed = -1
simulate(filename, unlocks, items, globals, seed, speedup)`

Condizione di Successo:
`num_items(Items.Gold) >= 300000`

## Dinosauro
Inizia con tutto sbloccato e coltiva `98010` ossa il più velocemente possibile. Questo è esattamente il numero di ossa che otterrai se riempi un'area 10x10 con la coda del dinosauro.

Chiamata di Funzione:
`leaderboard_run(Leaderboards.Dinosaur, filename, speedup)`

Simulazione Equivalente:
`unlocks = Unlocks
items = {Items.Pumpkin : 1000000, Items.Power: 1000000}
globals = {}
seed = -1
simulate(filename, unlocks, items, globals, seed, speedup)`

Condizione di Successo:
`num_items(Items.Bone) >= 98010`

## Altri Leaderboard di Risorse
Ogni pianta ha il suo leaderboard per coltivarla il più velocemente possibile. Inizi con tutti gli sblocchi, le risorse necessarie per far crescere la pianta e molta energia. L'obiettivo è coltivare `100000` della risorsa prodotta dalla pianta.

Chiamate di Funzione:
`leaderboard_run(Leaderboards.Cactus, filename, speedup)`
`leaderboard_run(Leaderboards.Sunflowers, filename, speedup)`
`leaderboard_run(Leaderboards.Pumpkins, filename, speedup)`
`leaderboard_run(Leaderboards.Wood, filename, speedup)`
`leaderboard_run(Leaderboards.Carrots, filename, speedup)`
`leaderboard_run(Leaderboards.Hay, filename, speedup)`
`leaderboard_run(Leaderboards.Polyculture, filename, speedup)`

Condizione di Successo:
`num_items(resource) >= 100000`

`Leaderboards.Polyculture` richiede di coltivare `100000` di tutte e tre le risorse della policoltura.
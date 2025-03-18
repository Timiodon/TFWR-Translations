# Classifica
Se sei arrivato fin qui, hai superato molte sfide. Ma le hai risolte in modo efficiente? 
Puoi competere con altri giocatori su varie classifiche per i metodi di coltivazione più efficienti.

Puoi iniziare un tentativo di classifica chiamando `leaderboard_run(leaderboard, filename, speedup)`.
Questo avvia una [simulazione](docs/unlocks/simulation.md) simile a `simulate()` ma con condizioni iniziali fisse. Ogni categoria di classifica ha differenti condizioni di partenza e di successo.

Il tentativo di classifica ha successo se la condizione di successo è `True` quando la simulazione termina. La simulazione non terminerà automaticamente quando l'obiettivo è raggiunto. Devi assicurarti che il programma si chiuda correttamente.
Se il tentativo ha successo, il tuo tempo sarà aggiunto alla classifica.

Per ridurre la varianza, tutti i tentativi devono durare almeno 2 ore (Puoi velocizzarlo, quindi non ci metterà così tanto). Se un tentativo viene completato prima, verrà ripetuto fino a raggiungere un tempo totale di 2 ore. La media di tutti i tentativi viene poi caricata come tuo punteggio.

Ecco un esempio di configurazione che ti porterà nella classifica del fieno.
![](LeaderboardSetup400)

## Reset Più Veloce
Il reset più veloce è la categoria più prestigiosa. Automatizza completamente il gioco da un singolo campo di coltivazione fino allo sblocco delle classifiche di nuovo.

Non devi sbloccare tutto, basta cercare di sbloccare `Unlocks.Leaderboard` il più rapidamente possibile.

Ricorda che puoi usare `num_unlocked(unlock) > 0` per verificare se qualcosa è sbloccato e puoi usare `get_cost()` su sblocchi per vedere quanto costano e così potrai coltivare automaticamente gli oggetti giusti.

Chiamata Funzione:
`leaderboard_run(Leaderboards.Fastest_Reset, filename, speedup)`

Simulazione Equivalente:
`unlocks = {}
items = {}
globals = {}
#a negative seed value means a random seed
seed = -1
simulate(filename, unlocks, items, globals, seed, speedup)`

Condizione di Successo:
`num_unlocked(Unlocks.Leaderboard) > 0`

## Labirinto
Inizia con tutto sbloccato e raccogli `300000` oro il più velocemente possibile. Questa è esattamente la quantità di oro che guadagnerai risolvendo un labirinto `300` volte.

Chiamata Funzione:
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
Inizia con tutto sbloccato e raccogli `98010` ossa il più velocemente possibile. Questo è esattamente il numero di ossa che otterrai riempendo un'area 10x10 con la coda di dinosauro.

Chiamata Funzione:
`leaderboard_run(Leaderboards.Dinosaur, filename, speedup)`

Simulazione Equivalente:
`unlocks = Unlocks
items = {Items.Pumpkin : 1000000, Items.Power: 1000000}
globals = {}
seed = -1
simulate(filename, unlocks, items, globals, seed, speedup)`

Condizione di Successo:
`num_items(Items.Bone) >= 98010`

## Altre Classifiche per Risorse
Ogni pianta ha la propria classifica per coltivare quella determinata pianta il più velocemente possibile. Inizi con tutti gli sblocchi, le risorse necessarie per far crescere la pianta e molta energia. L'obiettivo è coltivare `100000` della risorsa prodotta dalla pianta.

Chiamate Funzione:
`leaderboard_run(Leaderboards.Cactus, filename, speedup)`
`leaderboard_run(Leaderboards.Sunflowers, filename, speedup)`
`leaderboard_run(Leaderboards.Pumpkins, filename, speedup)`
`leaderboard_run(Leaderboards.Wood, filename, speedup)`
`leaderboard_run(Leaderboards.Carrots, filename, speedup)`
`leaderboard_run(Leaderboards.Hay, filename, speedup)`
`leaderboard_run(Leaderboards.Polyculture, filename, speedup)`

Condizione di Successo:
`num_items(resource) >= 100000`

`Leaderboards.Polyculture` richiede la coltivazione di `100000` di tutte e tre le risorse policulture.
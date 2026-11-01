# Classifica Sotterranea
Il sottosuolo nasconde sfide ancora più grandi. Sei pronto a ottimizzare i tuoi programmi minerari e agricoli?
Con questo sblocco puoi competere per i metodi più efficienti nelle profondità.

Puoi avviare una prova della classifica sotterranea chiamando `leaderboard_run(leaderboard, filename, speedup)`.
Questo avvia una [simulazione](docs/unlocks/simulation.md) simile a `simulate()`, ma con condizioni iniziali fisse. Ogni categoria della classifica ha condizioni iniziali e di successo diverse.

La partita per la classifica ha successo se la condizione di successo è `True` quando la simulazione termina. 

La simulazione NON terminerà automaticamente quando l'obiettivo viene raggiunto. Devi assicurarti che il programma termini.
Se la partita ha successo, il tuo tempo verrà aggiunto alla classifica.

Per ridurre la variabilità, tutte le run devono coprire almeno 2 ore di tempo simulato. Puoi accelerare la simulazione, quindi non servirà altrettanto tempo reale. Se una run termina prima, verrà ripetuta finché il tempo simulato totale non raggiunge 2 ore. La media dei tempi di tutte le run viene quindi caricata come punteggio.

Ecco una configurazione di esempio per entrare nella classifica `Leaderboards.Rice_Single`.

![|x400](UndergroundLeaderboardSetup)

## Ripristino Sotterraneo Più Veloce
Il ripristino sotterraneo è la categoria più prestigiosa. In questa categoria automatizzi completamente l'albero minerario, da una sola casella fino a sbloccare di nuovo `Unlocks.Underground_Leaderboard`.

Non devi sbloccare tutto: cerca solo di sbloccare `Unlocks.Underground_Leaderboard` il prima possibile.

Ricorda che puoi usare `num_unlocked(unlock) > 0` per controllare se qualcosa è sbloccato. Puoi anche usare `get_cost()` sugli sblocchi per conoscerne il costo e raccogliere automaticamente gli oggetti giusti.

`unlock()` ignora le dipendenze dell'albero tecnologico. Per esempio, puoi sbloccare `Unlocks.Fertilizer` prima di `Unlocks.Water`.

Chiamata di Funzione:
`leaderboard_run(Leaderboards.Fastest_Underground_Reset, filename, speedup)`

Simulazione Equivalente:
`unlocks = {}
items = {}
globals = {}
#un valore di seed negativo significa un seed casuale
seed = -1
simulate(filename, unlocks, items, globals, seed, speedup)`

Condizione di Successo:
`num_unlocked(Unlocks.Underground_Leaderboard) > 0`

## Minerali
Questa classifica mette alla prova la tua capacità di produrre minerali, in particolare quarzo. Modifica la generazione del terreno per fornire carbone, poi ferro e infine quarzo, in quest'ordine.

Inizia con tutto sbloccato e produci `20000` di quarzo il più rapidamente possibile.

Chiamata di Funzione:
`leaderboard_run(Leaderboards.Ores, filename, speedup)`

Simulazione Equivalente:
`unlocks = Unlocks
items = {Items.Power: 1000000000}
globals = {}
seed = -1
simulate(filename, unlocks, items, globals, seed, speedup)`

Condizione di Successo:
`num_items(Items.Quartz) >= 20000`

## Mappa del Tesoro
Questa classifica inizia con tutto sbloccato e molta energia. Modifica la generazione del terreno in modo che ci siano molte mappe del tesoro.

Si svolge in un mondo di 8x8 con un solo drone. L'obiettivo è produrre `115000` di oro il più rapidamente possibile.

Chiamata di Funzione:
`leaderboard_run(Leaderboards.Treasure_Map, filename, speedup)`

Simulazione Equivalente:
`unlocks = Unlocks
items = {Items.Power: 1000000000}
globals = {}
seed = -1
simulate(filename, unlocks, items, globals, seed, speedup)`

Condizione di Successo:
`num_items(Items.Gold) >= 115000`

## Classifiche delle Risorse
Queste classifiche si concentrano sulla produzione di risorse specifiche il più rapidamente possibile. Inizi con tutto sbloccato e molta energia. L'unica eccezione è la classifica delle piramidi, dove devi produrre energia ripristinando piramidi.

L'obiettivo è produrre una quantità prestabilita di risorse.

Come sempre, devi assicurarti che il tuo programma termini quando raggiungi l'obiettivo. Una partita non è finita finché il programma non termina, anche se l'obiettivo è stato raggiunto.

Queste classifiche modificano la generazione del terreno affinché la risorsa desiderata si trovi continuamente. Non è quindi necessario usare `clear()`. Per esempio, la classifica del riso contiene solo strati di argilla.

### `Leaderboards.Rice`
`leaderboard_run(Leaderboards.Rice, filename, speedup)`
Condizione di Successo: `num_items(Items.Rice) >= 2000000`

### `Leaderboards.Bamboo`
Nella classifica del bambù non è consentito scavare.

`leaderboard_run(Leaderboards.Bamboo, filename, speedup)`
Condizione di Successo: `num_items(Items.Bamboo) >= 500000000`

### `Leaderboards.Dynamite`
`leaderboard_run(Leaderboards.Dynamite, filename, speedup)`
Condizione di Successo: `num_items(Items.Dynamite) >= 10000000`

### `Leaderboards.Mushrooms`
`leaderboard_run(Leaderboards.Mushrooms, filename, speedup)`
Condizione di Successo: `num_items(Items.Mushroom) >= 240000`

### `Leaderboards.Pyramids`
`leaderboard_run(Leaderboards.Pyramids, filename, speedup)`
Condizione di Successo: `num_items(Items.Power) >= 150000`

## Classifiche Sotterranee con un Solo Drone
Esistono anche classifiche per la coltivazione con un solo drone. Hai a disposizione un solo drone e una fattoria 8x8 e devi raccogliere una certa quantità di risorse il più rapidamente possibile.

### `Leaderboards.Rice_Single`
`leaderboard_run(Leaderboards.Rice_Single, filename, speedup)`
Condizione di Successo: `num_items(Items.Rice) >= 100000`

### `Leaderboards.Ores_Single`
`leaderboard_run(Leaderboards.Ores_Single, filename, speedup)`
Condizione di Successo: `num_items(Items.Quartz) >= 4000`

### `Leaderboards.Bamboo_Single`
`leaderboard_run(Leaderboards.Bamboo_Single, filename, speedup)`
Condizione di Successo: `num_items(Items.Bamboo) >= 25000000`

### `Leaderboards.Dynamite_Single`
`leaderboard_run(Leaderboards.Dynamite_Single, filename, speedup)`
Condizione di Successo: `num_items(Items.Dynamite) >= 100000`

### `Leaderboards.Mushrooms_Single`
`leaderboard_run(Leaderboards.Mushrooms_Single, filename, speedup)`
Condizione di Successo: `num_items(Items.Mushroom) >= 30000`

### `Leaderboards.Pyramids_Single`
`leaderboard_run(Leaderboards.Pyramids_Single, filename, speedup)`
Condizione di Successo: `num_items(Items.Power) >= 30000`


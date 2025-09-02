# Timing
Se vuoi davvero ottimizzare i tuoi metodi, devi capire come viene misurato il tempo in questo gioco. Questo sblocco riguarda proprio questo.

## Nuove Funzioni
Ci sono due funzioni utili per misurare quanto tempo impiegano le cose:

`get_time()` restituisce il tempo in secondi dall'inizio del gioco.

`get_tick_count()` restituisce il numero di tick eseguiti dall'inizio dell'esecuzione.

Queste due funzioni, così come `quick_print()`, sono completamente gratuite. Anche l'operazione di chiamata è gratuita per loro.

## Dettagli sul Runtime

### Attenzione
Questo non è il modo in cui le prestazioni funzionano nel mondo reale. Queste sono solo regole create per questo gioco per avere un modello di timing coerente e comprensibile.
Probabilmente ti interesserà solo se vuoi iper-ottimizzare il tuo codice.


L'unità di tempo base per l'esecuzione del codice è chiamata "tick". Senza potenziamenti di velocità ed energia, l'esecuzione procede a una velocità di `400` tick al secondo.

In generale, le operazioni che combinano due valori come `+, -, *, /, //, %, and, or, ...` richiedono un tick per essere eseguite.
`-` e `not` su un singolo valore sono gratuiti.
Un ramo `if` richiede anche un tick per essere eseguito (oltre al tempo necessario per valutare l'espressione della condizione).
Le chiamate di funzione e le letture e scritture di variabili sono gratuite, ma le definizioni di funzione richiedono 1 tick.
Le istruzioni `import` sono gratuite.
L'accesso a un modulo importato con l'operatore `.` è gratuito.
Se una funzione o un modulo è stato passato tramite argomenti o assegnazioni di variabili, il suo utilizzo costerà 1 tick invece di 0.
I cicli `for` e `while` richiedono un tick per iniziare, ma le iterazioni sono gratuite (senza contare il tempo per valutare le espressioni di condizione/sequenza).
`return`, `break` e `continue` sono tutti gratuiti.
`pass` richiede un tick, quindi può essere usato per creare ritardi precisi.
L'indicizzazione in una struttura dati richiede un tick per l'operatore di indice e, nel caso di un dizionario o di un set, tick aggiuntivi a seconda della dimensione della chiave.

Il numero di tick che le funzioni integrate impiegano per essere eseguite è documentato nella documentazione di ciascuna funzione su base individuale.

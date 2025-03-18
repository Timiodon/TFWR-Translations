# Tempo
Se vuoi davvero ottimizzare i tuoi metodi, devi capire come viene misurato il tempo in questo gioco. Questo sblocco è dedicato a questo.

## Nuove Funzioni
Ci sono due funzioni utili per misurare quanto tempo richiedono le cose:

`get_time()` restituisce il tempo in secondi dall'inizio del gioco.

`get_tick_count()` restituisce il numero di tick eseguiti dall'inizio dell'esecuzione.

Queste due funzioni, così come `quick_print()`, sono completamente gratuite. Anche l'operazione di chiamata è gratuita per loro.

## Dettagli di Esecuzione

### Attenzione
Questo non è come funziona la performance nel mondo reale. Queste sono solo regole inventate per questo gioco per avere un modello di temporizzazione coerente e comprensibile.
Probabilmente ti interesserà solo se vuoi ottimizzare il tuo codice al massimo.

L'unità di base del tempo per l'esecuzione del codice è chiamata "tick". Senza aggiornamenti di velocità e potenza, l'esecuzione procede a un ritmo di `400` tick al secondo.

In generale, le operazioni che combinano due valori come `+, -, *, /, //, %, and, or, ...` richiedono un tick per essere eseguite.
I valori singoli come `-` e `not` sono gratuiti.
Un ramo `if` richiede anche un tick per essere eseguito (oltre al tempo necessario per valutare l'espressione della condizione).
Le chiamate a funzione e le letture e scritture di variabili sono gratuite, ma le definizioni di funzione richiedono 1 tick.
Le istruzioni `import` sono gratuite.
Accedere a un modulo importato con l'operatore `.` è gratuito.
Se una funzione o un modulo è stato passato tramite argomenti o assegnazioni di variabili, utilizzarlo costerà 1 tick invece di 0.
I loop `for` e `while` richiedono un tick per iniziare, ma le iterazioni sono gratuite (escludendo il tempo per valutare le espressioni della condizione/sequenza).
`return`, `break` e `continue` sono tutti gratuiti.
`pass` richiede un tick, quindi può essere usato per creare ritardi precisi.
Indicizzare una struttura dati richiede un tick per l'operatore di indice e, nel caso di un dictionary o set, tick aggiuntivi a seconda della dimensione della chiave.

Il numero di tick che le funzioni integrate richiedono per essere eseguite è documentato nella documentazione di ciascuna funzione individualmente.
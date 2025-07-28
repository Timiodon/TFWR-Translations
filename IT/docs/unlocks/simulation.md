# Simulazione

Le simulazioni ti permettono di testare rapidamente il codice senza modificare lo stato della fattoria reale.
Lo stato iniziale della simulazione può essere scelto liberamente e, al termine della simulazione, la fattoria reale sarà nello stato esatto in cui si trovava prima dell'inizio della simulazione.

La funzione `simulate()` è usata per avviare una simulazione.

il file da cui dovrebbe iniziare l'esecuzione
`filename = "f1"`

inizia con tutto sbloccato e completamente potenziato
`sim_unlocks = Unlocks`

inizia con 10000 carote e 50 fieno
`sim_items = {Items.Carrot : 10000, Items.Hay : 50}`

inizia con una variabile globale "a" con un valore di 13
`sim_globals = {"a" : 13}`

usa un seed casuale fisso
`seed = 0`

accelera la simulazione di un fattore 64
`speedup = 64`

esegui la simulazione
`run_time = simulate(filename, sim_unlocks, sim_items, sim_globals, seed, speedup)`

La funzione `simulate()` restituisce il tempo, in secondi, impiegato per simulare il file di partenza dato.

### Nome del File
Il primo argomento della funzione di simulazione è il nome del file. Questo è il nome visualizzato in cima alla finestra del codice. La simulazione eseguirà il file specificato come se avessi cliccato il pulsante Esegui su di esso.

### Sblocchi Iniziali
Tutte le funzionalità di programmazione come cicli, istruzioni if, liste, dizionari,... rimarranno sempre sbloccate.

Il secondo argomento ti permette di specificare con quali sblocchi/potenziamenti la simulazione dovrebbe iniziare, oltre alle funzionalità di programmazione. Questa dovrebbe essere una sequenza di sblocchi. La simulazione inizierà con tutti gli sblocchi nella sequenza potenziati al loro livello massimo.

Se vuoi specificare un livello di potenziamento diverso dal massimo, puoi passare un dizionario che mappa gli sblocchi ai livelli di sblocco. In questo caso, i valori negativi corrispondono al livello di sblocco massimo.

### Item Iniziali
Il terzo argomento ti permette di passare un dizionario che mappa item a numeri. Specifica gli item con cui iniziare la simulazione.

### Globali Iniziali
Poiché la simulazione avvia un'esecuzione di programma completamente nuova, non puoi accedere alle variabili del programma che avvia la simulazione.
Tuttavia, è possibile passare valori alla simulazione usando il quarto argomento. Questo è un dict che mappa nomi di variabili sotto forma di stringhe a valori. Queste variabili vengono quindi aggiunte allo scope globale dell'esecuzione all'interno della simulazione.

Nota che questo copia tutti i valori, quindi modificarli all'interno della simulazione non influenzerà i valori originali al di fuori della simulazione. Non è possibile restituire valori dalla simulazione, tranne il tempo impiegato per eseguirla.

### Seed Casuale
Il quinto argomento ti permette di specificare il seed casuale usato nella simulazione. Questo deve essere un intero positivo. Valori negativi causeranno l'uso di un seed casuale.

Il seed casuale influenza tutto, dai tempi di crescita delle piante alla disposizione dei labirinti ai tempi di decadimento dell'acqua. Se avvii la stessa simulazione più volte con lo stesso seed casuale e le stesse condizioni iniziali, il risultato dovrebbe essere sempre lo stesso.

### Accelerazione
Il sesto argomento è l'accelerazione iniziale della simulazione. Questo ti permette di testare le cose rapidamente. Se il gioco non riesce a tenere il passo con la velocità impostata, rallenterà automaticamente.

L'accelerazione non influisce in alcun modo sul risultato della simulazione. Esiste solo per ridurre il tempo di attesa.
# Simulazione

Le simulazioni ti permettono di testare rapidamente il codice senza cambiare lo stato della fattoria reale.
Lo stato iniziale della simulazione può essere scelto liberamente e, quando la simulazione termina, la fattoria reale sarà esattamente nello stato in cui si trovava prima dell'inizio della simulazione.

La funzione `simulate()` è usata per avviare una simulazione.

il file da cui dovrebbe partire l'esecuzione
`filename = "f1"`

inizia con tutto sbloccato e completamente potenziato
`sim_unlocks = Unlocks`

inizia con 10000 carote e 50 fieno
`sim_items = {Items.Carrot : 10000, Items.Hay : 50}`

inizia con una variabile globale "a" con valore 13
`sim_globals = {"a" : 13}`

utilizza un seme casuale fisso
`seed = 0`

accelera la simulazione di un fattore 64
`speedup = 64`

esegui la simulazione
`run_time = simulate(filename, sim_unlocks, sim_items, sim_globals, seed, speedup)`

La funzione `simulate()` restituisce il tempo, in secondi, che ci è voluto per simulare il file di avvio fornito.

### Nome del File
Il primo argomento della funzione simulate è il filename. Questo è il nome che viene mostrato in cima alla finestra del codice. La simulazione eseguirà il file specificato come se avessi cliccato il pulsante Esegui su di esso.

### Sblocchi Iniziali
Tutte le funzionalità di programmazione come cicli, istruzioni if, liste, dict,... rimarranno sempre sbloccate.

Il secondo argomento ti permette di specificare con quali sblocchi/potenziamenti la simulazione dovrebbe iniziare oltre alle funzionalità di programmazione. Questa dovrebbe essere una sequenza di sblocchi. La simulazione inizierà con tutti gli sblocchi nella sequenza potenziati al loro livello massimo.

Se vuoi specificare un livello di potenziamento diverso dal massimo, puoi passare un dictionary che mappa gli sblocchi ai livelli di sblocco. In questo caso, i valori negativi corrispondono al livello massimo di sblocco.

### Oggetti Iniziali
Il terzo argomento ti permette di passare un dictionary che mappa gli oggetti ai numeri. Specifica gli oggetti con cui iniziare la simulazione.

### Variabili Globali Iniziali
Poiché la simulazione avvia una nuova esecuzione del programma, non puoi accedere alle variabili del programma che avvia la simulazione.
Tuttavia, è possibile passare valori alla simulazione usando il quarto argomento. Questo è un dict che mappa nomi di variabili in forma di stringhe ai valori. Queste variabili vengono poi aggiunte allo scope globale dell'esecuzione all'interno della simulazione.

Nota che questo copia tutti i valori, quindi modificarli all'interno della simulazione non influirà sui valori originali al di fuori della simulazione. Non è possibile restituire valori dalla simulazione a parte il tempo impiegato per eseguire.

### Seme Casuale
Il quinto argomento ti permette di specificare il seme casuale usato nella simulazione. Deve essere un numero intero positivo. Valori negativi faranno utilizzare un seme casuale.

Il seme casuale influenza tutto, dai tempi di crescita delle piante ai layout dei labirinti ai tempi di decadimento dell'acqua. Se inizi la stessa simulazione più volte con lo stesso seme casuale e le stesse condizioni iniziali, il risultato dovrebbe essere sempre lo stesso.

### Accelerazione
Il sesto argomento è l'accelerazione iniziale della simulazione. Questo ti permette di testare le cose rapidamente. Se il gioco non riesce a tenere il passo con la velocità impostata, rallenterà automaticamente.

L'accelerazione non influisce in alcun modo sul risultato della simulazione. Esiste solo per ridurre il tempo di attesa.
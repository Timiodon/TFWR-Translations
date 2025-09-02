# Debug
A volte il tuo codice semplicemente non funziona e devi scoprire perché. Ci sono un paio di strumenti per aiutarti a farlo.

Il primo è eseguire il programma passo dopo passo.
Puoi entrare in modalità passo dopo passo con il pulsante accanto al pulsante Esegui o impostando un breakpoint.

I breakpoint possono essere aggiunti cliccando sul pannello dei breakpoint a sinistra del codice.
![](Breakpoints227)
Quando l'esecuzione raggiunge la riga in cui si trova il breakpoint, passerà automaticamente alla modalità passo dopo passo.

Quando sposti il mouse su una variabile, viene visualizzato il suo valore attuale.

Anche la funzione `print()` può essere molto utile. Scriverà qualsiasi valore passato ad essa direttamente in aria.

Esempi:

Stampa "0.24".
`print(0.24)`

Stampa "True" o "False".
`print(can_harvest())`

Stampa la posizione attuale.
`print(get_pos_x(), get_pos_y())`

La funzione print stampa il valore direttamente in aria e sulla pagina di [Output](docs/output.md).

Scrivere in aria a volte può essere un po' lento se vuoi stampare molti valori.
In questo caso puoi usare la funzione `quick_print()` che stampa solo nella finestra di output.

La finestra di output registra anche avvisi ed errori, quindi se qualcosa non funziona come previsto può essere utile controllarla.

Quando l'esecuzione si ferma, l'output viene scritto anche nel file output.txt nella cartella del gioco. [output.txt](persistent_data_path/output.txt).
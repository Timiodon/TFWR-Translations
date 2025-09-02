# Ciclo While
Hai sbloccato il ciclo `while` e i valori `True` e `False`. Il ciclo `while` continua a eseguire il corpo del ciclo finché la condizione è `True`.

`while condition:
	#corpo del ciclo`

Non preoccuparti di creare cicli infiniti. I ritardi nell'esecuzione impediranno al programma di bloccarsi.

## Per Principianti
Forse hai già provato a mettere diverse chiamate `harvest()` di seguito:

`harvest()
harvest()
harvest()`

Questo ti permette di raccogliere più volte in una singola esecuzione del programma. 
Tuttavia, sarebbe bello raccogliere più di tre volte, e scrivere lo stesso codice più volte è una cattiva pratica. 
La soluzione è un ciclo. 
Un ciclo ti permette di eseguire lo stesso codice più volte.

Il ciclo while prende una condizione, che è un valore logico che può trovarsi solo in uno di due stati: `True` o `False`. 
Un valore di questo tipo è chiamato valore Booleano.

Il ciclo quindi esegue il codice al suo interno finché la condizione non è Falsa.
Il ciclo while si presenta così:

`while condition:
	#corpo del ciclo
	#corpo del ciclo
	#...`
	
Dove devi sostituire "condition" con un valore booleano e `#corpo del ciclo` con quello che vuoi fare nel ciclo.

Ci sono due valori booleani costanti disponibili. Le costanti sono valori che non cambiano mai durante il programma.

Per creare un valore booleano costante che sia sempre `True`, puoi semplicemente scrivere `True`. Scrivi `False` per un valore booleano costante che sarà sempre `False`.
Quindi potresti scrivere o


`while False:
	do_a_flip()`

o

`while True:
	do_a_flip()`

Il primo non farà mai una capriola e il secondo farà capriole per sempre (un ciclo infinito). 

Normalmente creare un ciclo infinito è una cattiva idea perché bloccherà il programma, ma in questo gioco ci sono ritardi tra ogni iterazione del ciclo, quindi farà sì che il drone continui a fare capriole finché non lo fermerai manualmente premendo di nuovo il pulsante di esecuzione.

Nota come la riga dopo i due punti sia indentata. L'indentazione come questa viene usata per separare i blocchi di codice.
Basta premere Tab per aggiungere indentazione e Shift + Tab (o Backspace) per rimuoverla.

Il ciclo ripeterà tutte le istruzioni indentate dopo i due punti.
Le istruzioni dopo il blocco indentato saranno eseguite dopo che il ciclo è terminato.

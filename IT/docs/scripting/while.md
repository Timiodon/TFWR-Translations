# Ciclo While
Hai sbloccato il ciclo `while` e i valori `True` e `False`. Il ciclo `while` continua a eseguire il corpo del ciclo finché la condizione è `True`.

`while condizione:
	#corpo del ciclo`

Non preoccuparti di creare cicli infiniti. I ritardi nell'esecuzione impediranno al programma di bloccarsi.

## Per Principianti
Forse hai già provato a mettere diverse chiamate `harvest()` una dopo l'altra:

`harvest()
harvest()
harvest()`

Questo ti permette di raccogliere più volte in un'unica esecuzione del programma. 
Tuttavia, sarebbe bello raccogliere più di tre volte, e scrivere lo stesso codice più volte non è una buona pratica. 
La soluzione è un ciclo. 
Un ciclo ti permette di eseguire lo stesso codice più volte.

Il ciclo while prende una condizione, che è un valore logico che può essere in uno dei due stati: `True` o `False`. 
Un tale valore è chiamato valore booleano.

Il ciclo esegue poi il codice all'interno del ciclo fino a quando la condizione è `False`.
Il ciclo while appare così:

`while condizione:
	#corpo del ciclo
	#corpo del ciclo
	#...`

Dove devi sostituire "condizione" con un valore booleano e `#corpo del ciclo` con quello che vuoi fare nel ciclo.

Ci sono due valori booleani costanti disponibili. Le costanti sono valori che non cambiano mai durante il programma.

Per creare un valore booleano costante che è sempre `True`, puoi semplicemente scrivere `True`. Scrivi `False` come valore booleano costante che sarà sempre `False`.
Quindi potresti scrivere

`while False:
	do_a_flip()`

oppure

`while True:
	do_a_flip()`

Il primo non farà mai un flip e il secondo farà flip per sempre (un ciclo infinito). 

Normalmente creare un ciclo infinito è una cattiva idea perché bloccherà il programma, ma in questo gioco ci sono ritardi tra ogni iterazione del ciclo, quindi farà sì che il drone continui a fare flip finché non lo fermerai manualmente premendo nuovamente il pulsante di esecuzione.

Nota come la riga dopo il due punti è indentata. L'indentazione come questa viene usata per separare blocchi di codice.
Basta premere Tab per aggiungere l'indentazione e Shift + Tab (o Backspace) per rimuoverla.

Il ciclo ripeterà tutte le istruzioni indentate dopo il due punti.
Le istruzioni dopo il blocco indentato verranno eseguite dopo che il ciclo è terminato.
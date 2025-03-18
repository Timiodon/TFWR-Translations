# Espansione 2
La tua fattoria si è espansa ancora! Ora le tessere non sono più in una bella riga, quindi devi trovare un modo per attraversare una griglia quadrata.

Con il ciclo `while` questo non è possibile fino a quando non sblocchi i sensori e gli operatori. È il momento di introdurre il ciclo `for`.

Puoi leggere tutto sul ciclo `for` nella pagina [For Loop](docs/scripting/for.md), ma per ora ti servirà solo per ripetere il codice un numero fisso di volte.

`#fai n flip
for i in range(5):
	do_a_flip()`

`range(n)` crea un intervallo di numeri da `0` a `n-1` e contiene `n` elementi. Il ciclo `for` esegue il corpo del ciclo una volta per ogni elemento nella sequenza. In questo esempio `do_a_flip()` sarà chiamato `5` volte.

La funzione `get_world_size()` è ora disponibile. Restituisce la lunghezza del lato della tua fattoria. In questo modo puoi scrivere codice che non si romperà con il prossimo upgrade di espansione.

`for i in range(get_world_size()):
	harvest()
	move(North)`

Questo esempio raccoglie una colonna della fattoria per qualsiasi dimensione della fattoria.

Se sei bloccato nel cercare di capire come muovere il drone intorno alla fattoria, guarda il suggerimento qui sotto.
<spoiler=mostra suggerimento>Ci sono, ovviamente, diversi modi per muoversi nella fattoria.
Ciò che stiamo cercando è un modo per attraversarla in modo sistematico che non si rompa quando la fattoria crescerà di nuovo.
Un modo sistematico per arrivare ovunque nella fattoria sarebbe ripetere i seguenti 2 passaggi all'infinito:

1.Muoviti a `North` finché non torna indietro.
2.Muoviti a `East`.

`for i in range(get_world_size()):` può essere utile per trasformare questa idea in codice.
</spoiler>
<spoiler=mostra possibile soluzione> Il percorso di base potrebbe essere simile a questo:

`for i in range(get_world_size()):
	for j in range(get_world_size()):
		#fai un flip su ogni tessera
		do_a_flip()
		move(North)
	move(East)`
</spoiler>
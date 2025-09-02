# Espansione 2
La tua fattoria si è espansa di nuovo! Ora le caselle non sono più in una bella fila, quindi devi trovare un modo per attraversare una griglia quadrata.

Con il ciclo `while` questo non è possibile finché non sblocchi i sensori e gli operatori.
È ora di introdurre il ciclo `for`.

Puoi leggere tutto sul ciclo `for` nella pagina [Ciclo For](docs/scripting/for.md), ma per ora ti servirà solo per ripetere del codice un numero fisso di volte.

`#fai n capriole
for i in range(5):
	do_a_flip()`

`range(n)` crea un intervallo di numeri da `0` a `n-1` che contiene `n` elementi. Il ciclo `for` esegue il suo corpo una volta per ogni elemento della sequenza. In questo esempio `do_a_flip()` sarà chiamato `5` volte.

Ora è disponibile anche la funzione `get_world_size()`. Restituisce la lunghezza del lato della tua fattoria. In questo modo puoi scrivere codice che non si romperà con il prossimo potenziamento di espansione.

`for i in range(get_world_size()):
	harvest()
	move(North)`

Questo esempio raccoglie una colonna della fattoria per qualsiasi dimensione della fattoria.

Se sei bloccato nel tentativo di capire come muovere il drone per la fattoria, vedi il suggerimento qui sotto.
<spoiler=mostra suggerimento>Ci sono, ovviamente, diversi modi per muoversi nella fattoria.
Quello che cerchiamo è un modo per attraversarla sistematicamente che non si rompa quando la fattoria crescerà di nuovo.
Un modo sistematico per raggiungere ogni punto della fattoria sarebbe ripetere i seguenti 2 passi all'infinito:

1.Muoviti a `Nord` finché non torni indietro.
2.Muoviti a `Est`

`for i in range(get_world_size()):` potrebbe essere utile per trasformare questa idea in codice.
</spoiler>
<spoiler=mostra possibile soluzione> L'attraversamento di base potrebbe assomigliare a questo:

`for i in range(get_world_size()):
	for j in range(get_world_size()):
		#fai una capriola su ogni casella
		do_a_flip()
		move(North)
	move(East)`
</spoiler>
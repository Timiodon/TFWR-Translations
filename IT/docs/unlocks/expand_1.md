# Espansione 1
<unlock=for>Vedi anche [Expand_2](docs/unlocks/expand_2.md)

</unlock>La tua fattoria è cresciuta! Questo spazio non serve a molto se non puoi muovere il drone, quindi c'è una nuova funzione `move()` che sposta il drone. `move()` richiede che specifichi la direzione in cui vuoi muovere il drone. Ci sono quattro nuove costanti per questo: `North, East, South, West`

Ad esempio, `move(North)` sposterà il drone di un quadrato verso il nord.

Se ti sposti oltre il bordo della fattoria, il drone verrà spostato sull'altro lato della fattoria.
Il seguente esempio di codice continuerà a spostare il drone a nord e tornerà all'inizio quando raggiunge il bordo della fattoria:

`while True:
	move(North)`
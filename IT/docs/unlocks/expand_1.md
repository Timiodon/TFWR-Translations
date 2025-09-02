# Espansione 1
<unlock=for>Vedi anche [Expand_2](docs/unlocks/expand_2.md)

</unlock>La tua fattoria è cresciuta! Questo spazio non è molto utile se non puoi muovere il drone, quindi c'è una nuova funzione `move()` che muove il drone. `move()` richiede che tu specifichi la direzione in cui vuoi che il drone si muova. Ci sono quattro nuove costanti per questo: `North, East, South, West`

Ad esempio, `move(North)` muoverà il drone di una casella a nord.

Se ti muovi oltre il bordo della fattoria, il drone verrà spostato dall'altro lato.
Il seguente codice di esempio continuerà a muovere il drone verso nord e tornerà all'inizio quando raggiungerà il bordo della fattoria:

`while True:
	move(North)`

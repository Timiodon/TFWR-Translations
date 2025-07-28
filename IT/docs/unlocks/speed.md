# Potenziamento Velocità
La velocità di esecuzione è stata raddoppiata. Il problema è che ora il drone raccoglie più velocemente di quanto l'erba possa crescere, risultando in nessun raccolto. Per gestire questo, sono ora sbloccati i costrutti [if](docs/scripting/if.md) e la funzione [can_harvest](functions/can_harvest).

## Controllare Prima di Raccogliere
Finora abbiamo avuto solo `True` e `False` come condizioni, il che ovviamente non è molto utile con `if`.

La nuova funzione can_harvest() fornisce una condizione migliore. `can_harvest()` restituisce `True` se la pianta sotto il drone può essere raccolta e `False` altrimenti.

`if can_harvest():
	#fai qualcosa`

Il motivo per cui puoi usare questa funzione come condizione in questo modo è perché restituisce un valore booleano.

Un valore restituito significa essenzialmente che, dopo l'esecuzione della funzionalità, l'espressione della chiamata di funzione valuta al valore restituito.

Cosa succede quando il codice sopra viene eseguito:
	-l'if viene eseguito
	-`can_harvest()` viene chiamata
	-`can_harvest()` fa il suo lavoro
	-`can_harvest()` restituisce `True` o `False`
	-l'istruzione diventa `if True:` o `if False:`
	-il blocco di codice viene eseguito solo se si può raccogliere

Ora possiamo usare `if` per impedire al drone di raccogliere troppo presto.
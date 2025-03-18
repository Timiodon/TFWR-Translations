# Miglioramento della Velocità
La velocità di esecuzione è stata raddoppiata. Il problema è che ora il drone raccoglie più velocemente di quanto l'erba possa crescere, risultando in un raccolto nullo. Per affrontare questo, i rami [if](docs/scripting/if.md) e la funzione [can_harvest](functions/can_harvest) sono ora sbloccati.

## Controllare Prima di Raccogliere
Finora avevamo solo `True` e `False` come condizioni, il che ovviamente non è molto utile con `if`.

La nuova funzione can_harvest() fornisce una condizione migliore. `can_harvest()` restituisce `True` se la pianta sotto il drone può essere raccolta e `False` altrimenti.

`if can_harvest():
	#do something`

Il motivo per cui puoi usare questa funzione come condizione è perché restituisce un valore booleano.

Un valore di ritorno significa essenzialmente che dopo l'esecuzione della funzionalità, l'espressione della chiamata alla funzione viene valutata come il valore restituito.

Cosa succede quando il codice sopra viene eseguito:
   - l'if viene eseguito
   - `can_harvest()` viene chiamata
   - `can_harvest()` fa il suo lavoro
   - `can_harvest()` restituisce `True` o `False`
   - la dichiarazione diventa ora `if True:` o `if False:`
   - il blocco di codice viene eseguito solo se può raccogliere

Ora possiamo usare `if` per impedire al drone di raccogliere troppo presto.
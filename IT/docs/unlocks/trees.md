# Alberi
Gli [alberi](objects/tree) sono un modo migliore per ottenere legno rispetto ai cespugli. Danno 5 di legno ciascuno. Come i cespugli, possono essere piantati sull'erba o sul terreno.

Agli alberi piace avere un po' di spazio e piantarli uno accanto all'altro rallenterà la loro crescita. Il tempo di crescita è raddoppiato per ogni albero che si trova su una casella direttamente a nord, est, ovest o sud di esso. Quindi se pianti alberi su ogni casella, ci metteranno `2*2*2*2 = 16` volte di più a crescere.

<spoiler=mostra> L'operatore `%` può essere utile qui. Ricorda che l'operatore `%` restituisce il resto della divisione. I numeri pari divisi per `2` hanno un resto di `0` e i numeri dispari divisi per `2` hanno un resto di `1`.
Quindi puoi controllare se un numero è pari in questo modo:

`def is_even(n):
	return n % 2 == 0`

Questo restituisce `True` se n è pari e `False` se non lo è.
</spoiler>
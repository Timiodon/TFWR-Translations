# Policoltura
Potresti aver già notato che a volte le piante producono di più se piantate insieme.
Erba, cespugli, alberi e carote producono di più quando hanno la giusta pianta compagna. La preferenza del compagno è diversa per ogni singola pianta e non può essere prevista. Fortunatamente, la preferenza del compagno della pianta sotto il drone può essere misurata usando `get_companion()`. Restituisce una tupla in cui il primo elemento è il tipo di pianta che desidera come compagno e il secondo elemento è la posizione in cui desidera il suo compagno.

`plant_type, (x, y) = get_companion()`

Ad esempio, se pianti un cespuglio e poi chiami `get_companion()`, restituirà qualcosa come `(Entities.Carrot, (3, 5))`. Ciò significa che questo cespuglio vorrebbe avere delle carote nella posizione `(3,5)`. Quindi, se pianti delle carote in `(3,5)` e poi raccogli il cespuglio, produrrà più legno. Lo stadio di crescita della carota non ha importanza.

La preferenza del compagno di una pianta può essere `Entities.Grass`, `Entities.Bush`, `Entities.Tree` o `Entities.Carrot`. Ogni pianta sceglie questo a caso, ma sceglierà sempre una pianta diversa da sé stessa. La posizione può anche essere qualsiasi posizione entro 3 mosse dalla pianta, tranne la posizione della pianta stessa.

Se non c'è nessuna pianta sotto il drone che ha una preferenza per un compagno, `get_companion()` restituirà `None`.

Prima che la policoltura sia sbloccata, il moltiplicatore di resa è `5`. Raddoppia ogni volta che lo potenzi.
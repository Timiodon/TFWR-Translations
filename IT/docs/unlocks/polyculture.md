# Policultura
Forse hai già notato che a volte le piante rendono di più quando vengono piantate insieme. Erba, cespugli, alberi e carote rendono di più quando hanno il giusto compagno vegetale. La preferenza di compagno è diversa per ogni pianta e non può essere prevista. Fortunatamente, la preferenza di compagno della pianta sotto il drone può essere misurata usando `get_companion()`. Restituisce una tupla dove il primo elemento è il tipo di pianta che desidera come compagno e il secondo elemento è la posizione in cui vuole il suo compagno.

`plant, (x, y) = get_companion()`

Ad esempio, se pianti un cespuglio e poi chiami `get_companion()` restituirà qualcosa del tipo `(Entities.Carrot, (3, 5))`. Questo significa che questo cespuglio vorrebbe avere delle carote nella posizione `(3,5)`. Quindi, se pianti delle carote a `(3,5)` e poi raccogli il cespuglio, otterrai più legno. Lo stadio di crescita della carota non importa.

La preferenza di compagno di una pianta può essere `Entities.Grass`, `Entities.Bush`, `Entities.Tree` o `Entities.Carrot`. Ogni pianta sceglie questo casualmente, ma sceglierà sempre una pianta diversa da sé. La posizione può essere qualsiasi posizione entro 3 mosse dalla pianta, eccetto la posizione della pianta stessa.

Se non c'è nessuna pianta sotto il drone che ha una preferenza di compagno `get_companion()` restituirà `None`.

Il moltiplicatore di resa è `5` più il numero di aggiornamenti della policultura.
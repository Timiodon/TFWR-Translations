# Dinosauri
I dinosauri sono creature antiche e maestose che possono essere allevate per ottenere ossa antiche.

Purtroppo i dinosauri si sono estinti molto tempo fa, quindi il meglio che possiamo fare ora è travestirci da uno di loro.
A questo scopo hai ricevuto il nuovo cappello da dinosauro.

Il cappello può essere equipaggiato con
`change_hat(Hats.Dinosaur_Hat)`

Purtroppo non assomiglia molto a quello della pubblicità...

Se equipaggi il cappello da dinosauro e hai abbastanza zucche, una [mela](objects/apple) verrà automaticamente acquistata e posizionata sotto il drone.
Quando il drone si trova sopra una mela e si muove di nuovo, mangerà la mela e la sua coda si allungherà di uno. Se puoi permettertelo, una nuova mela verrà acquistata e posizionata in un punto casuale.
La mela non può apparire se c'è qualcos'altro piantato dove vorrebbe essere.

La coda del dinosauro verrà trascinata dietro il drone, riempiendo le caselle precedenti su cui si è mosso. Se un drone cerca di muoversi sopra la coda, `move()` fallirà e restituirà `False`.
L'ultimo segmento della coda si sposterà durante il movimento, quindi potrai passarci sopra. Tuttavia, se il serpente riempie l'intera fattoria, non potrai più muoverti. Quindi puoi controllare se il serpente è completamente cresciuto verificando se non puoi più muoverti.

Usare `measure()` su una mela restituirà la posizione della prossima mela come una tupla.

`next_x, next_y = measure()`

Quando il cappello viene rimosso equipaggiandone uno diverso, la coda verrà raccolta.
Riceverai ossa pari alla lunghezza della coda al quadrato. Quindi per una coda di lunghezza `n` riceverai `n**2` `Items.Bone`.
Per Esempio:
lunghezza 1 => 1 osso
lunghezza 2 => 4 ossa
lunghezza 3 => 9 ossa
lunghezza 4 => 16 ossa
lunghezza 16 => 256 ossa
lunghezza 100 => 10000 ossa

Il Cappello da Dinosauro è molto pesante, quindi se lo equipaggi, farà sì che `move()` impieghi 800 tick invece di 200. Tuttavia, ogni volta che raccogli una mela, il numero di tick usati da `move()` si riduce del 3% (arrotondato per difetto), perché una coda più lunga può aiutarti a muoverti.

Il seguente ciclo stampa il numero di tick usati da `move()` dopo un qualsiasi numero di mele:

`ticks = 800
for i in range(100):
    print("tick dopo ", i, " mele: ", ticks)
    ticks -= ticks * 0.03 // 1`

<spoiler=mostra suggerimento 1>Se continui a muoverti lungo lo stesso percorso che copre l'intero campo, puoi facilmente ottenere un serpente che copre ogni volta l'intero campo, perché coprirai ogni punto libero prima di tornare dove si trova la tua coda. Non è molto efficiente, ma funziona.
I campi di dimensioni dispari possono essere più difficili. Se hai sbloccato `Unlocks.Debug2`, puoi cambiare la dimensione del campo in qualcosa di più conveniente.</spoiler>
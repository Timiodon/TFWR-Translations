# Dinosauri
I dinosauri sono creature antiche e maestose che possono essere coltivate per ottenere ossa antiche.

Purtroppo i dinosauri si sono estinti molto tempo fa, quindi la cosa migliore che possiamo fare ora è travestirci da uno di loro.
A tal scopo hai ricevuto il nuovo cappello da dinosauro.

Il cappello può essere equipaggiato con
`change_hat(Hats.Dinosaur_Hat)`

Purtroppo non sembra proprio come nella pubblicità...

Se equipaggi il cappello da dinosauro e hai abbastanza zucche, una [apple](objects/apple) sarà automaticamente acquistata e posizionata sotto il drone.
Quando il drone è sopra una mela e si muove di nuovo, la mangerà e il suo coda crescerà di uno. Se puoi permettertelo, una nuova mela sarà acquistata e posizionata in una posizione casuale.
La mela non può generarsi se c'è qualcosa piantato dove vuole apparire.

La coda del dinosauro verrà trascinata dietro il drone, riempiendo le tile precedenti dove il drone si è mosso. Se un drone cerca di muoversi sopra la coda, `move()` fallirà e restituirà `False`.
L'ultimo segmento della coda si sposterà durante il movimento, così potrai muoverti sopra di esso. Tuttavia, se il serpente riempie tutto il campo, non potrai più muoverti. Quindi puoi controllare se il serpente è completamente cresciuto verificando se non puoi più muoverti.

Usare `measure()` su una mela restituirà la posizione della prossima mela come tupla.

`next_x, next_y = measure()`

Quando il cappello viene nuovamente tolto equipaggiando un altro cappello, la coda verrà raccolta.
Riceverai ossa pari al quadrato della lunghezza della coda. Quindi per una coda di lunghezza `n` riceverai `n**2` `Items.Bone`.
Per esempio:
lunghezza 1 => 1 osso
lunghezza 2 => 4 ossa
lunghezza 3 => 9 ossa
lunghezza 4 => 16 ossa
lunghezza 16 => 256 ossa
lunghezza 100 => 10000 ossa

Il Cappello da Dinosauro è molto pesante, quindi se lo equipaggi, farà in modo che `move()` impieghi 800 tick invece di 200. Tuttavia, ogni volta che raccogli una mela, il numero di tick usati da `move()` è ridotto del 3% (arrotondato verso il basso), perché una coda più lunga può aiutarti a muoverti.

Il seguente ciclo stampa il numero di tick usati da `move()` dopo un qualsiasi numero di mele:

`ticks = 800
for i in range(100):
    print("ticks dopo ", i, " mele: ", ticks)
    ticks -= ticks * 0.03 // 1`

<spoiler=mostra suggerimento 1>Se continui a muoverti lungo lo stesso percorso che copre l'intero campo, puoi facilmente ottenere un serpente che copre tutto il campo ogni volta, perché coprirai ogni spazio libero prima di tornare dov'era la tua coda. Non è molto efficiente, ma funziona.
Campi di dimensioni dispari possono essere più difficili. Se hai sbloccato `Unlocks.Debug2`, puoi cambiare la dimensione del campo in qualcosa di più comodo.</spoiler>
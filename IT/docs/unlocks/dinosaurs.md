# Dinosauri
I dinosauri sono creature antiche e maestose che possono essere allevate per ottenere ossa antiche.

Sfortunatamente i dinosauri si sono estinti molto tempo fa, quindi il meglio che possiamo fare ora è travestirci da uno di loro.
A questo scopo hai ricevuto il nuovo cappello da dinosauro.

Il cappello può essere equipaggiato con
`change_hat(Hats.Dinosaur_Hat)`

Sfortunatamente non ha l'aspetto che aveva nella pubblicità...

Se equipaggi il cappello da dinosauro e hai abbastanza cactus, una [mela](objects/apple) verrà automaticamente acquistata e posizionata sotto il drone.
Quando il drone si trova su una mela e si muove di nuovo, mangerà la mela e la sua coda si allungherà di uno. Se te lo puoi permettere, una nuova mela verrà acquistata e posizionata in un luogo casuale.
La mela non può comparire se c'è qualcos'altro piantato dove vorrebbe essere.

La coda del dinosauro verrà trascinata dietro il drone, riempiendo le caselle precedenti su cui si è mosso. Se un drone cerca di muoversi sopra la coda, `move()` fallirà e restituirà `False`. 
L'ultimo segmento della coda si sposterà durante il movimento, quindi puoi muovertici sopra. Tuttavia, se il serpente riempie tutta la fattoria, non sarai più in grado di muoverti. Quindi puoi controllare se il serpente è completamente cresciuto verificando se non puoi più muoverti.

Usando `measure()` su una mela si ottiene la posizione della mela successiva come una tupla.

`next_x, next_y = measure()`

Quando il cappello viene rimosso equipaggiandone un altro, la coda verrà raccolta.
Riceverai un numero di ossa pari alla lunghezza della coda al quadrato. Quindi per una coda di lunghezza `n` riceverai `n**2` `Items.Bone`. 
Per Esempio:
lunghezza 1 => 1 osso
lunghezza 2 => 4 ossa
lunghezza 3 => 9 ossa
lunghezza 4 => 16 ossa
lunghezza 16 => 256 ossa
lunghezza 100 => 10000 ossa

Il Cappello da Dinosauro è molto pesante, quindi se lo equipaggi, `move()` impiegherà 400 tick invece di 200. Tuttavia, ogni volta che raccogli una mela, il numero di tick usati da `move()` si riduce del 3% (arrotondato per difetto), perché una coda più lunga può aiutarti a muoverti.

Il seguente ciclo stampa il numero di tick usati da `move()` dopo un qualsiasi numero di mele:

`ticks = 400
for i in range(100):
    print("tick dopo ", i, " mele: ", ticks)
    ticks -= ticks * 0.03 // 1`

Hai solo un cappello da dinosauro, quindi solo un drone può indossarlo.

<spoiler=mostra suggerimento 1>Se continui a muoverti lungo lo stesso percorso che copre l'intero campo, puoi facilmente ottenere un serpente che copre l'intero campo ogni volta. Non è molto efficiente, ma funziona.
Attraversare completamente una fattoria molto grande può richiedere molto tempo e potresti non aver bisogno di così tante ossa. Sentiti libero di usare `set_world_size()` per cambiare la dimensione della fattoria in qualcosa di più conveniente.</spoiler>
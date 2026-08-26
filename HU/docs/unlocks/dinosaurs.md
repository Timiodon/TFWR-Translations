# Dinoszauruszok
A dinoszauruszok ősi, fenséges lények, amik ősi csontokért farmolhatók.

Sajnos a dinoszauruszok nagyon régen kihaltak, szóval a legjobb, amit tehetünk, az egy öltözködés egyként.
Ehhez kaptad az új dinoszaurusz kalapot.

A kalapot így оборудования:
`change_hat(Hats.Dinosaur_Hat)`

Sajnos nem úgy néz ki, mint a reklámban...

Ha felveszed a dinoszaurusz kalapot és van elegendő kaktusz, egy [alma](objects/apple) automatikusan megvásárlásra és a drón alá kerül.
Amikor a drón egy alma felett van és újra mozog, megeszi az almát és a farkát egyel meghosszabbítja. Ha meg tudod fizetni, egy új alma kerül megvásárlásra és véletlenszerű helyre kerül.
Az alma nem spawnolhat, ha valami más van ültetve oda, ahova szeretné.

A dinoszaurusz farka a drón mögött húzódik, kitöltve az előző csempéket, amin a drón áthaladt. Ha egy drón megpróbál a farok tetejére mozogni, a `move()` sikertelen lesz és `False`-t ad vissza.
A farok utolsó szegmense elmozdul a mozgás alatt, szóval ráléphetsz. Azonban ha a kígyó az egész farmot kitölti, nem fogsz tudni tovább mozogni. Szóval ellenőrizheted, hogy a kígyó teljesen megnőtt-e azáltal, hogy nem tudsz már mozogni.
A dinoszaurusz kalap viselése közben a drón nem mozoghat a farm szélén át a másik oldalra.

A `measure()` alma használata a következő alma pozícióját adja vissza tuple-ként.

`next_x, next_y = measure()`

Amikor a kalap ismét levehető egy másik kalap felvételével, a farok betakarításra kerül.
Olyan csontokat kapsz, amennyi a farok hosszának négyzete. Tehát `n` hosszú farokhoz `n**2` `Items.Bone`-t kapsz.
Például:
hossz 1 => 1 csont
hossz 2 => 4 csont
hossz 3 => 9 csont
hossz 4 => 16 csont
hossz 16 => 256 csont
hossz 100 => 10000 csont

A Dinoszaurusz Kalap nagyon nehéz, szóval ha felveszed, a `move()` 400 ticket fog igénybe venni 200 helyett. Azonban minden alma felvételekor a `move()` által használt tickek száma 3%-kal csökken (lefelé kerekítve), mert egy hosszabb farok segíthet a mozgásban.

A következő ciklus kiírja a `move()` által használt tickek számát bármennyi alma után:

`ticks = 400
for i in range(100):
    print("tickek ", i, " alma után: ", ticks)
    ticks -= ticks * 0.03 // 1`

Csak egy dinoszaurusz kalapod van, szóval csak egy drón viselheti.

<spoiler=show hint 1>Ha ugyanazon az úton haladsz, ami a teljes mezőt lefedi, könnyen kaphatsz egy kígyót, ami minden alkalommal lefedi a teljes mezőt. Nem túl hatékony, de működik.
Egy nagyon nagy farm teljes bejárása hosszú ideig tarthat és valószínűleg nem is kell annyi csont. Nyugodtan használd a `set_world_size()`-t a farm méretének kényelmesebb értékre állításához.</spoiler>
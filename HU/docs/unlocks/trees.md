# Fák
A [fák](objects/tree) jobb módja a fa megszerzésének, mint a bokrok. 5 fát adnak darabonként. Mint a bokrok, ültethetők fűre vagy talajra.

A fák szeretnek némi helyet és ha egymás mellé ülteted őket, lelassítja a növekedésüket. A növekedési idő megduplázódik minden fáért, ami egy csempén van közvetlenül északra, keletre, nyugatra vagy délre tőle. Szóval ha minden csempére fát ültetsz, `2*2*2*2 = 16` annyi ideig fognak nőni.

<spoiler=show> A `%` operátor hasznos lehet itt. Emlékezz arra, hogy a `%` operátor az osztás maradékát adja vissza. A `2`-vel osztott páros számok maradéka `0` és a páratlan számok maradéka `1`.
Szóval ellenőrizheted, hogy egy szám páros-e így:

`def is_even(n):
	return n % 2 == 0`

Ez `True`-t ad vissza, ha n páros és `False`, ha nem.
</spoiler>
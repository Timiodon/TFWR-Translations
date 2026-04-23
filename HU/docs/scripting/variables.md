# Változók
A változókat úgy képzeld el, mint elnevezett konténereket, amelyek értéket tárolhatnak.
Az `=` operátort változó deklarálására és érték tárolására használjuk.

`variable_name = value`

Az operátor bal oldala a változó neve. Bármilyen nevet adhatsz neki.
A jobb oldal egy kifejezés, amelynek eredmény értéke a változóban tárolódik.

Deklarálj egy `a` nevű változót és tárolj benne `5` értéket:
`a = 5`
Deklarálj egy `b` nevű változót és tárold benne a `can_harvest()` visszatérési értékét:
`b = can_harvest()`

Ne keverd össze az `=` operátort a `==` operátorral.
A `==` operátor ellenőrzi, hogy két érték egyenlő-e, és `True` vagy `False` értéket ad vissza.
Az `=` operátor a jobb oldali értéket rendeli a bal oldali névhez.

Miután egy változónak értéket adtál, használhatod a kódban, hogy lekérd a benne tárolt értéket

`a = 5
for i in range(a):
	do_a_flip()`

A fenti ciklus 5-szer fut le, mert `a` értéke `5`.
A `for` ciklusban lévő `i` is egy változó, amely automatikusan megkapja a szekvencia aktuális értékét a ciklus minden iterációjában. (Nem kell `i`-nek hívni, bármilyen érvényes változónevet adhatsz neki.)

A változók lehetővé teszik ugyanezt while ciklussal is:

`a = 5
i = 0
while i < a:
	do_a_flip()
	i = i + 1`

Ez ugyanazt csinálja, mint a fenti for ciklus. Csak kézzel kell növelni i-t.
Figyelj arra, hogy i növeléséhez önmaga értékét + `1`-et állítjuk be. Egy változó értékének megváltoztatása az előző értéke alapján nagyon gyakori dolog.
Rövidíthető ezekkel az operátorokkal: `+=, -=, *=, /=, %=`

`i = i + 1` ugyanaz, mint `i += 1`
`a = a / 3` ugyanaz, mint `a /= 3`
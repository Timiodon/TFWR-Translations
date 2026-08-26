# Bővítés 2
A farmod ismét bővült! Most a csempék már nem szépen sorban vannak, szóval találnod kell egy módot, hogyan járd be a négyzetrácsot.

A `while` ciklussal ez nem lehetséges, amíg fel nem oldod az érzékeket és az operátorokat.
Itt az ideje bevezetni a `for` ciklust.

A `for` ciklusról mindent elolvashatsz a [For ciklus](docs/scripting/for.md) oldalon, de egyelőre csak arra lesz szükséged, hogy a kódot fix számú alkalommal ismételjed.

`#n flipet csinál
for i in range(5):
	do_a_flip()`

A `range(n)` számok tartományát hozza létre `0`-tól `n-1`-ig, ami `n` elemet tartalmaz. A `for` ciklus a ciklus törzsét minden szekvencia elemhez egyszer futtatja. Ebben a példában a `do_a_flip()` 5-ször kerül meghívásra.

A `get_world_size()` függvény is elérhető most. A farmod oldalhosszát adja vissza. Így írhatsz olyan kódot, ami nem törik el a következő bővítésnél.

`for i in range(get_world_size()):
	harvest()
	move(North)`

Ez a példa a farm egy oszlopát takarítja be bármilyen farm méretre.

Ha elakadtál, hogyan mozogjasd a drónt a farm körül, nézd meg az alábbi tippet.
<spoiler=show hint> Természetesen több módja is van a farm körül mozgásnak.
Amit keresünk, az egy szisztematikus módja, hogy minden helyre eljuss a farmon, ami nem törik el, amikor a farm ismét nő.
Egy szisztematikus módja minden hely eléréséhez a farmon az lenne, hogy örökre ismételd a következő 2 lépést:

1.Mozogj `North` irányba, amíg vissza nem wrapel.
2.Mozogj `East` irányba

A `for i in range(get_world_size()):` hasznos lehet ötlet kóddá alakításához.
</spoiler>
<spoiler=show possible solution> Az alap traversál így nézhet ki:

`for i in range(get_world_size()):
	for j in range(get_world_size()):
		#flipet csinál minden csempén
		do_a_flip()
		move(North)
	move(East)`
</spoiler>
# Bővítés 1
<unlock=for>Lásd még: [Bővítés_2](docs/unlocks/expand_2.md)

</unlock>A farmod megnőtt! Ez a hely nem túl hasznos, ha nem tudod mozgatni a drónt, szóval van egy új `move()` függvény, ami a drónt mozgatja. A `move()` megköveteli, hogy megadd azt az irányt, amelyikbe a drónt mozgatni akarod. Ehhez négy új konstans van: `North, East, South, West`

Például a `move(North)` a drónt egy négyzetnyit észak felé mozgatja.

Ha a farm szélén túl mozogsz, a drón a farm másik oldalára kerül.
A következő példa kód a drónt észak felé mozgatja és vissza wrapel a startra, amikor eléri a farm szélét:

`while True:
	move(North)`
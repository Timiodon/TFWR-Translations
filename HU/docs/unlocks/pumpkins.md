# Tökök
A [tökök](objects/pumpkin) úgy nőnek, mint a répák a felszántott talajon. Ültetésük répába kerül.

Amikor egy négyzet összes tökje teljesen megnőtt, együtt nőnek óriási tökké. Sajnos a tököknek 20% esélyük meghalni, amikor teljesen megnőttek, szóval újra kell ültetned a halottakat, ha egyesülni akarsz őket.

Amikor egy tök meghal, maga után hagy egy halott tököt, ami nem dob semmit betakarításkor. Új növény ültetése a helyére automatikusan eltávolítja a halott tököt, szóval nincs szükség betakarítani. A `can_harvest()` mindig `False`-t ad vissza halott tökökön.

Az óriási tök hozama a tök méretétől függ.

Egy 1x1 tök `1*1*1 = 1` tököt hoz.
Egy 2x2 tök `2*2*2 = 8` tököt hoz `4` helyett.
Egy 3x3 tök `3*3*3 = 27` tököt hoz `9` helyett.
Egy 4x4 tök `4*4*4 = 64` tököt hoz `16` helyett.
Egy 5x5 tök `5*5*5 = 125` tököt hoz `25` helyett.
Egy `n`x`n` tök `n*n*6` tököt hoz `n >= 6` esetén.

Jó ötlet legalább 6x6 méretű tököket szerezni a teljes szorzó eléréséhez.

Ez azt jelenti, hogy még ha tököt ültetsz is minden csempére egy négyzetben, az egyik tök meghalhat és megakadályozhatja az óriási tök növekedését.
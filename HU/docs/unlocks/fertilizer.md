# Műtrágya
Egyszer csak a növények növekedésére várni már nem elég hatékony.
A vízhez hasonlóan minden 10 másodpercben automatikusan kapsz 1 műtrágyát, fejlesztésenként megduplázódva.

A műtrágya azonnali növekedést eredményezhet a növényeken. A `use_item(Items.Fertilizer)` csökkenti a drón alatti növény megmaradt növekedési idejét 2 másodperccel.

Ennek néhány mellékhatása van.
Műtrágyával termesztett növények fertőzöttek lesznek.

Amikor egy növény fertőzött, a hozam fele `Items.Weird_Substance`-vá alakul betakarításkor.
A Weird Substance növényeken is használható, aminek az a hatása, hogy toggle-oli a növény és az összes szomszédos növény fertőzési státuszát.

Tehát ha a `use_item(Items.Weird_Substance)`-t hívod fertőzött növényen, meggyógyítja, de ha egészséges növényen használod, megfertőzi.

Ha fertőzött növényen használod, ami egészséges szomszédokkal rendelkezik, meggyógyítja a növényt, de megfertőzi a szomszédokat és fordítva.
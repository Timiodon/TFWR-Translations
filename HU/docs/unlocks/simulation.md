# Szimuláció

A szimulációk lehetővé teszik a kód gyors tesztelését a valódi farm állapotának megváltoztatása nélkül.
A szimuláció kezdőállapota szabadon választható, és amikor a szimuláció véget ér, a valódi farm pontosan olyan állapotban lesz, mint a szimuláció megkezdése előtt.

A `simulate()` függvény szolgál a szimuláció indítására.

a fájl, amiből a végrehajtás indul
`filename = "f1"`

minden feloldva és teljesen fejlesztve indul
`sim_unlocks = Unlocks`

10000 répával és 50 szénával indul
`sim_items = {Items.Carrot : 10000, Items.Hay : 50}`

egy "a" nevű globális változó 13 értékkel indul
`sim_globals = {"a" : 13}`

rögzített random seed használata
`seed = 0`

a szimuláció 64x gyorsítása
`speedup = 64`

a szimuláció futtatása
`run_time = simulate(filename, sim_unlocks, sim_items, sim_globals, seed, speedup)`

A `simulate()` függvény másodpercben adja vissza az adott indító fájl szimulálásához szükséges időt.

### Fájlnév
A simulate függvény első argumentuma a fájlnév. Ez a név jelenik meg a kódablak tetején. A szimuláció a megadott fájlt futtatja, mintha rákattintottál volna a Végrehajtás gombra rajta.

### Kezdő feloldások
Minden programozási funkció mint ciklusok, if utasítások, listák, dicts,... mindig feloldva maradnak.

A második argumentum lehetővé teszi, hogy megadd, mely feloldások/fejlesztések legyenek a szimulációban a programozási funkciókon felül. Ez feloldások szekvenciája kell legyen. A szimuláció az összes feloldást a maximum szintjére fejlesztve kezdi.

Ha a maximumtól eltérő fejlesztési szintet akarsz megadni, átadhatsz egy szótárat, ami a feloldásokat fejlesztési szintekre képezi le. Ebben az esetben a negatív értékek a maximum feloldási szintnek felelnek meg.

### Kezdő itemek
A harmadik argumentum lehetővé teszi, hogy szótárat adj át, ami itemeket számokra képez le. Megadja az itemeket, amikkel a szimuláció indul.

### Kezdő globálisok
Mivel a szimuláció teljesen új program végrehajtást indít, nem érheted el a szimulációt indító programból a változókat.
Azonban lehetséges értékeket átadni a szimulációnak a negyedik argumentum használatával. Ez egy dict, ami string formájú változóneveket értékekre képez. Ezek a változók aztán hozzáadásra kerülnek a szimuláción belüli végrehajtás globális hatóköréhez.

Figyelj arra, hogy ez minden értéket másol, szóval a szimuláción belüli mutálásuk nem fogja érinteni az eredeti értékeket a szimuláción kívül. Nem lehetséges értékeket visszaadni a szimulációból a futási időn kívül.

### Random Seed
Az ötödik argumentum lehetővé teszi a szimulációban használt random seed megadását. Pozitív egésznek kell lennie. A negatív értékek random seed használatát okozzák.

A random seed mindent érint a növény növekedési időktől a labirintus elrendezésekig a víz csökkenési időkig. Ha ugyanazzal a random seeddel és ugyanazokkal a kezdő feltételekkel többször indítod ugyanazt a szimulációt, az eredmény mindig ugyanaz kell legyen.

### Sebesség felét
A hatodik argumentum a szimuláció kezdő sebesség felét. Ez lehetővé teszi, hogy gyorsan tesztelj dolgokat. Ha a játék nem tud lépést tartani a beállított sebességgel, automatikusan lelassul.

A sebesség felét semmilyen módon nem befolyásolja a szimuláció eredményét. Csak a várakozási idő csökkentésére szolgál.
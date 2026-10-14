# Időzítés
Ha igazán optimalizálni akarod a módszereidet, meg kell értened, hogyan mérjük az időt ebben a játékban. Ez a feloldás erről szól.

## Új függvények
Két hasznos függvény van dolgok időtartamának mérésére:

A `get_time()` a játék kezdete óta eltelt időt adja vissza másodpercben.

A `get_tick_count()` a végrehajtás kezdete óta végrehajtott tickek számát adja vissza.

Ez a két függvény, valamint a `quick_print()` teljesen ingyenesek. Még a hívás művelet is ingyenes ezeknél.

## Futásidegi részletek

### Figyelem
Ez nem így működik a teljesítmény a valóságban. Ezek csak szabályok, amiket ehhez a játékhoz találtak ki, hogy konzisztens és érthető időzítési modellje legyen.
Valószínűleg csak akkor fog érdekelni, ha hyper-optimalizálni akarod a kódot.

A kód végrehajtás alapegysége "tick". Sebességfejlesztések és erő nélkül a végrehajtás `400` tick per másodperc sebességgel halad.

Általában a két értéket kombináló műveletek mint `+, -, *, /, //, %, and, or, ...` egy ticket vesznek igénybe.
Egyetlen értékű `-` és `not` ingyenes.
Egy `if` ág is egy ticket vesz igénybe (a feltétel kifejezés kiértékelésének idejét is beleszámítva).
Függvényhívások és változó olvasások és írások ingyenesek, de függvény definíciók 1 ticket vesznek igénybe.
`import` utasítások ingyenesek.
Importált modul elérése a `.` operátorral ingyenes.
Ha egy függvény vagy modul argumentumokon vagy változó értékadásokon keresztül lett átadva, a használata 1 ticket fog költeni 0 helyett.
`for` és `while` ciklusok egy ticket vesznek igénybe az indításkor, de az iterációk ingyenesek (nem számítva a feltétel/szekvencia kifejezések kiértékelésének idejét).
`return`, `break` és `continue` mind ingyenes.
`pass` egy ticket vesz igénybe, így használható precíz késleltetések létrehozására.
Adatszerkezetbe indexelés egy ticket vesz igénybe az index operátornál, és szótár vagy halmaz esetén további tickek a kulcs méretétől függően.

A beépített függvények végrehajtásához szükséges tickek számát az egyes függvények dokumentációjában találod meg.
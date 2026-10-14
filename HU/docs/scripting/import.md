# Import
Az összes kódot egyetlen fájlba téve gyorsan kezelhetetlenné válik.
Az `import` utasítások lehetővé teszik függvények és globális változók importálását egy másik fájlból.
Egy képen így működik:
![](ImportsInOnePicture400)

Itt az `import module2` lefuttatja a `module2` nevű fájlt és hozzáférést ad az összes globális változójához.
Ezután a `.` operátorral érheted el az importált modulon belüli változókat és függvényeket.
Tehát ebben a példában a `module2.print_x()` meghívja a `print_x()`-et a `module2`-ben.

### Nem kell tovább olvasni

A `from` szintaxist használva az importált modul globális változóit a jelenlegi hatókörbe is mozgathatod, ahol az import utasítás végrehajtódik.

`from module2 import print_x
print_x()`
Csak a megadott globális változókat importálja a `module2`-ből.

vagy

`from module2 import *
print_x()`
Minden globális változót importál a `module2`-ből.

Ez szintén importálja a `module2` fájlt, de ahelyett, hogy egy `module2` nevű változón keresztül érnéd el, kicsomagolja a `module2` globális változóit és közvetlenül a lokális hatókörbe rendeli őket.

Ez az importálási forma általában nem ajánlott, mert nem működik jól, ha két fájl importálja egymást, és véletlenül felülírhatsz változókat az importáló fájlban névütközések miatt. Biztonságosabb elkerülni a `from` szintaxist, ha nem tudod, mit csinálsz.

# Hogyan működik valójában

## TLDR
Az importálás elég intuitív lehet, de a legtöbb probléma elkerülhető, ha ragaszkodsz az `import file` szintaxishoz a `from file import` helyett, és mindent, ami nem globális definíció, becsomagolhatsz
`if __name__ == "__main__":`
 blokkba.

## Import mellékhatások
Amikor először importálsz egy fájlt, az végrehajtja a teljes fájlt, majd hozzáférést ad az összes változóhoz, ami a végrehajtás során definiálva lett.
Ha ugyanazt a fájlt újra importálod, csak az első alkalommal létrehozott cached modult adja vissza.

Ez azt jelenti, hogy az import utasításoknak mellékhatásaik lehetnek. Ha importálsz egy fájlt, ami meghívja a `harvest()`-t, az ténylegesen be fog takarítani az importálás során. De amikor újra importálod, nem takarít be újra, mert a fájl csak egyszer fut le.

Van egy módja az ilyen mellékhatások elkerülésére a `__name__` változó használatával. Ez egy változó, ami automatikusan `"__main__"`-re van állítva, amikor egy fájl közvetlenül fut, és a fájl nevére, amikor egy fájl `import` révén fut.
Jó gyakorlatnak számít minden kódot, amit nem akarsz futtatni, amikor a fájl importálódik, `if __name__ == "__main__":` blokkba tenni.

Egy gyakori fájl struktúra Pythonban, hogy a fájlt, amit futtatni kell, egy `main()` függvénybe teszed. Így világos elkülönítés van a lokális változók (a `main()`-en belül definiálva) és a globális változók között, amik importálhatók (a `main()`-en kívül definiálva).

`a_global_variable = "global"

def main():
    a_local_variable = "local"
    # csinálj valamit

if __name__ == "__main__":
    main()`

## Import ciklusok
Mi történik, ha az `a` fájl importálja a `b` fájlt és a `b` fájl importálja az `a` fájlt?

`a` fájl:
`import b
x = 0`

`b` fájl:
`import a
def f():
    print(a.x)`

Ez jól fog működni. Tegyük fel, hogy egyik fájl sincs még betöltve, és valaki végrehajtja az `import a`-t.

-A `a` fut, amíg az `import b` sorig.
-A `b` fut, amíg az `import a` sorig.
-A `a` modul már létezik, de nem tartalmazza az `x`-et, mert csak az `import b` sorig jutott.
-A `b` egy referencia tárol a félig betöltött `a` modulhoz egy `a` nevű változóban.
-A `b` futtatja a `def` utasítást és eltárolja az `f()` függvényt.
-A `a` folytatja a futást és inicializálja az `x`-et.

Amikor valaki meghívja a `b.f()`-et, helyesen kiírja a `0`-t, mert a `b`-nek a `a`-ra mutató referenciája most már teljesen betöltött.

Most nézd meg ugyanezt a kódot a `from` szintaxissal.

`a` fájl:
`from b import *
x = 0`

`b` fájl:
`from a import *
def f():
    print(x)`

-A `a` fut, amíg a `from b import *` sorig.
-A `b` fut, amíg a `from a import *` sorig.
-A `a` modul már létezik, de még nincs teljesen végrehajtva.
-A `b` kicsomagol mindent, ami jelenleg az `a`-ban van, a saját globális hatókörébe. Ebben a pillanatban az `a` nem tartalmaz semmit, mert még nem jutott el az `x = 0` sorig, így semmi sem importálódik.
-A `b` futtatja a `def` utasítást és eltárolja az `f()` függvényt.
-A `a` folytatja a futást és inicializálja az `x`-et.

Ha valaki most meghívja a `b.f()`-et, hibát kap, hogy az `x` nem létezik az aktuális hatókörben. Ez azért van, mert most a `b`-nek nincs referenciája a még betöltődő `a`-hoz, és nem látja az import után hozzáadott definíciókat.
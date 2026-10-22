# Név hatókörök
A hatókörök határozzák meg, hogy mely változók érhetők el honnan. Egy hatókör alapvetően neveket értékekre képez le.
Lényegében ugyanúgy működnek, mint Pythonban.

Van egy globális hatókör, és minden függvénynek saját lokális hatóköre van.
Amikor definiálsz egy változót, az hozzáadódik az aktuális hatókörhöz.
Bármi, ami egy függvény definícióján kívül van, a globális hatókör részének számít.

`x = 1`
A `1` értéket rendeli az `x` névhez a globális hatókörben.

Ez a `def` utasítás egy függvényt rendel az `f` névhez a globális hatókörben.
`def f():
    `A `1` értéket rendeli az `y` névhez az `f` lokális hatókörében.`
    y = 1

    `Egy függvényt rendel a `g` névhez az `f` lokális hatókörében.`
    def g():
        pass`

`f()`
A `f`-ben tárolt függvényt kéri le a globális hatókörből és meghívja.

`print(y)`
Ez a print utasítás a globális hatókörben hibát dob, mert `y` soha nem volt deklarálva a globális hatókörben, így itt nem olvasható.
Csak az `f` lokális hatókörében létezett.

## A global kulcsszó
Alapértelmezetten a függvényeken belüli összes változó a lokális hatókörhöz kötődik, még akkor is, ha ugyanolyan nevű változó létezik a globális hatókörben.

`x = 0

def f():
    x = 1
f()
print(x)`

Ez a kód `0`-t ír ki, mert az `f` függvényen belüli lokális `x` nem ugyanaz a változó, mint a globális `x`, így a globális `x` változatlan marad. Ez azért fontos, mert különben egy függvényhívás véletlenül felülírhatna egy globális változót, amely történetesen ugyanazt a nevet viseli, mint a függvény lokális változója.

Ha globális változóba akarsz írni, azt explicit módon kell megtenned a `global` kulcsszó használatával.

`x = 0

def f():
    global x
    x = 1
f()
print(x)`

Ebben a példában a `global x` az `x`-et a felette definiált globális `x` változóhoz köti. Ez most kiírja az `1`-et.
Figyelj arra, hogy a globális változók megváltoztatása általában az első lépés a spagetti kód felé, ahol a program minden része a program minden más részét érinti, szóval ne használd túl sokat.

## Ciklusok és elágazások
A ciklusok és elágazások nem hoznak létre saját hatókört, így bármi, ami bennük van deklarálva, kívül is használható.

`for i in range(3):
    pass
print(i)`

Ez kiírja a `2`-t, mert a `for` ciklus utolsó iterációja `2`-t rendelt az `i`-hez.
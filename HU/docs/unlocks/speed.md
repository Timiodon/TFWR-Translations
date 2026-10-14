# Sebességfejlesztés
A végrehajtási sebesség megduplázódott. A probléma az, hogy a drón most gyorsabban takarít be, mint a fű nőni tud, ami eredményez null harvest at all. Ennek kezelésére az [if](docs/scripting/if.md) ágak és a [can_harvest](functions/can_harvest) függvény most feloldásra kerültek.

## Betakarítás előtti ellenőrzés
Ezidáig csak `True` és `False` volt a feltételek, ami persze nem túl hasznos az `if`-fel.

Az új `can_harvest()` függvény jobb feltételt biztosít. A `can_harvest()` `True`-t ad vissza, ha a drón alatti növény betakarítható, és `False` egyébként.

`if can_harvest():
	#csinálj valamit`

Az oka, hogy használhatod ezt a függvényt feltételként, az, hogy boolean értéket ad vissza.

A visszatérési érték lényegében azt jelenti, hogy a funkció végrehajtása után a függvényhívás kifejezés a visszaadott értékre értékelődik.

Mi történik, amikor a fenti kód fut:
	-az `if` fut
	-a `can_harvest()` hívva van
	-a `can_harvest()` csinálja a dolgát
	-a `can_harvest()` `True` vagy `False`-t ad vissza
	-az utasítás most `if True:` vagy `if False:`
	-a kód blokk csak akkor hajtódik végre, ha betakarítható

Most használhatjuk az `if`-et a drón korai betakarításának megakadályozására.
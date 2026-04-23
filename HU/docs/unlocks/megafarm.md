# Mega Farm
Ez az hihetetlenül erős feloldás több drónhoz biztosít hozzáférést.

Mint korábban, továbbra is csak egy drónnal kezdesz. A további drónokat először létre kell hozni, és a program befejeződése után eltűnnek.
Minden drón a saját külön programját futtatja. Új drónokat a `spawn_drone(function)` függvénnyel hozhatsz létre.

`def drone_function():
    move(North)
    do_a_flip()

spawn_drone(drone_function)`

Ez létrehoz egy új drónt ugyanazon a pozíción, mint amelyik a `spawn_drone(function)` parancsot futtatta. Az új drón aztán a megadott függvényt kezdi el végrehajtani. Amikor végzett, automatikusan eltűnik.

A drónok nem ütköznek egymással.

Használd a `max_drones()`-t a maximális egyidejűleg létező drónok számának lekérdezéséhez.
Használd a `num_drones()`-t a már a farmon lévő drónok számának lekérdezéséhez.

## Példa:
`def harvest_column():
    for _ in range(get_world_size()):
        harvest()
        move(North)

while True:
    if spawn_drone(harvest_column):
        move(East)`

Ez azt eredményezi, hogy az első drónod vízszintesen mozog és több drónt hoz létre. A létrehozott drónok aztán függőlegesen mozognak és betakarítanak mindent az útjukban.

Ha az összes elérhető drón már létrehozásra került, a `spawn_drone()` nem csinál semmit és `None`-t ad vissza.

Íme egy másik példa, amely minden drónnak egy különböző irányt ad át.
`for dir in [North, East, South, West]:
    def task():
        move(dir)
        do_a_flip()
    spawn_drone(task)`

## Minden drón egyenlő
Nincs speciális "fő" drón. Minden drón hozhat létre más drónokat, és mind count toward the drone limit. Minden drón eltűnik, amikor befejeződik. Ha az első drón korán befejezi a programját, egy másik drón lesz az, akinek a végrehajtása kód kiemeléssel jelenik meg. Minden drón kiválthat breakpointot, és amikor egy drón kivált egy breakpointot, a kód kiemelés átkapcsol arra a drónra.

<spoiler=show hint> Nézd meg ezt a szuper hasznos párhuzamos `for_all` függvényt, ami bármilyen függvényt minden farm csempén futtat. Az összes elérhető drónt felhasználja ehhez.

`def for_all(f):
	def row():
		for _ in range(get_world_size()-1):
			f()
			move(East)
		f()
	for _ in range(get_world_size()):
		if not spawn_drone(row):
			row()
		move(North)

for_all(harvest)`

Egy különösen hasznos minta drón létrehozása, ha van elérhető, különben csináld magad.

`if not spawn_drone(task):
	task()`
</spoiler>

## Egy másik drónra várva
Használd a `wait_for(drone)` függvényt egy másik drón befejezésére várakozáshoz. A `drone` handle-t kapod, amikor létrehozod a drónt.
A `wait_for(drone)` visszaadja a többi drón által futtatott függvény visszatérési értékét.

`def get_entity_type_in_direction(dir):
    move(dir)
    return get_entity_type()

def zero_arg_wrapper():
    return get_entity_type_in_direction(North)
drone = spawn_drone(zero_arg_wrapper)
print(wait_for(drone))`

Figyelj arra, hogy drónok létrehozása időbe telik, szóval nem jó ötlet minden kis dologhoz új drónt létrehozni.

Használhatod a `has_finished(drone)`-t annak ellenőrzésére, hogy a drón befejeződött-e várakozás nélkül.

## Nincs megosztott memória
Minden drónnak saját memóriája van és nem tud közvetlenül olvasni vagy írni egy másik drón globális változóit.

`x = 0

def increment():
    global x
    x += 1

wait_for(spawn_drone(increment))
print(x)`

Ez kiírja a `0`-t, mert az új drón a saját másolatát növelte meg a globális `x`-ről, ami nem affecteli az első drón `x`-ét.

## Argumentumok átadása

A `spawn_drone` további opcionális argumentumokat fogad el, amik a hívott függvénynek lesznek átadva:

`def harvest_spiral(radius):
    for i in range(0, radius, 2):
        for j in range(i):
            harvest()
            move(West)
        for j in range(i):
            harvest()
            move(South)
        for j in range(i+1):
            harvest()
            move(East)
        for j in range(i+1):
            harvest()
            move(North)

wait_for(spawn_drone(harvest_spiral, 6))`

Figyelj arra, hogy a Nincs megosztott memoria-záradék still applies. Ez means that the called function operates on a copy of the arguments:

`def modify(list):
	move(North)
	list.append('green')
	print(list) # prints ['red', 'green']

l = ['red']
wait_for(spawn_drone(modify, l))
print(l) # prints ['red']`

## Verseny állapotok
Több drón ugyanazzal a farm csempével ugyanabban a pillanatban kölcsönhatásba léphet. Ha két drón ugyanazzal a csempével lép kölcsönhatásba ugyanabban a tickben, mindkét kölcsönhatás végbemegy, de az eredmények eltérhetnek a kölcsönhatások sorrendjétől függően.

Például, képzeld el, hogy a `0` és `1` drónok ugyanazon a fáron vannak, ami szinte teljesen megnőtt.
A `0` drón hívja
`use_item(Items.Fertilizer)`
Az `1` drón hívja
`harvest()`

Ha ezek a műveletek ugyanabban a pillanatban történnek, a fa először trágyázva lesz, aztán betakarítva. Ebben az esetben fát kapsz érte. Ha viszont az `1` drón egy kicsit gyorsabb, a fa trágyázás előtt betakarításra kerül, és nem kapod meg a fát.
Ezt "verseny állapotnak" hívják. Gyakori probléma a párhuzamos programozásban, ahol az eredmény a műveletek végrehajtási sorrendjétől függ.

Íme egy másik problémás helyzet, ami akkor fordulhat elő, amikor több drón ugyanazt a kódot párhuzamosan futtatja ugyanazon a pozíción.
`if get_water() < 0.5:
    use_item(Items.Water)`

Ha több drón futtatja ezt egyszerre, mindegyik futtatja az első sort, ami belépteti őket az `if` blokkba. Aztán mind használnak vizet, rengeteget elpazarolva.
Mire egy drón a második sorhoz ér, a `get_water()` már lehet, hogy nem kisebb `0.5`-nél, mert egy másik drón már megöntözte a csempét azóta.
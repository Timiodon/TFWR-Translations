# Mega Farm
Tento neuvěřitelně silný prvek ti umožní používat více dronů najednou. 🚁  

Stejně jako dříve začínáš pouze s jedním dronem. Další drony musíš nejprve vytvořit („spawnout“) a po ukončení programu zase zmizí.  
Každý dron spouští svůj vlastní, oddělený program. Nové drony můžeš vytvářet pomocí funkce `spawn_drone(function)`.

`def drone_function():
    move(North)
    do_a_flip()

spawn_drone(drone_function)`

Tím se vytvoří nový dron na stejné pozici jako ten, který zavolal `spawn_drone(function)`. Nový dron začne vykonávat zadanou funkci a po dokončení automaticky zmizí.

Drony do sebe nenarážejí.

Pomocí `max_drones()` zjistíš maximální počet dronů, které lze vytvořit.  
Pomocí `num_drones()` zjistíš, kolik jich už na farmě je.

## Příklad:
`def harvest_column():
    for _ in range(get_world_size()):
        harvest()
        move(North)

while True:
    if spawn_drone(harvest_column):
        move(East)`

Tento kód způsobí, že tvůj první dron se bude pohybovat vodorovně a vytvářet další drony.  Vytvořené drony se pak budou pohybovat svisle a po cestě sklízet všechno, co najdou.

Pokud jsou všechny dostupné drony už vytvořené, `spawn_drone()` nic neprovede a vrátí `None`.

Zde je další příklad, který předává každému dronu jiný směr:
`for dir in [North, East, South, West]:
    def task():
        move(dir)
        do_a_flip()
    spawn_drone(task)`

<spoiler=show hint>Podívej se na tuto užitečnou paralelní funkci `for_all`, která vezme libovolnou funkci a spustí ji na každé dlaždici farmy. Využije k tomu všechny dostupné drony.

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

Velmi užitečný vzor je vytvořit nový dron, pokud je volný — a pokud ne, udělat úlohu sám.

`if not spawn_drone(task):
	task()`
</spoiler>

## Čekání na jiný dron
Pomocí `wait_for(drone)` můžeš počkat, až jiný dron dokončí svou práci. Při vytváření dronu získáš jeho identifikátor (handle), který do funkce předáš.  
`wait_for(drone)` vrací návratovou hodnotu funkce, kterou daný dron vykonával.

`def get_entity_type_in_direction(dir):
    move(dir)
    return get_entity_type()

def zero_arg_wrapper():
    return get_entity_type_in_direction(North)
drone = spawn_drone(zero_arg_wrapper)
print(wait_for(drone))`

Všimni si, že vytváření dronů zabírá čas, takže není dobré spawnovat nový dron pro každou drobnost.

Pomocí `has_finished(drone)` můžeš ověřit, zda už dron skončil, aniž bys na něj čekal.

## Žádná sdílená paměť
Každý dron má vlastní paměť a nemůže přímo číst nebo zapisovat globální proměnné jiného dronu.

`x = 0

def increment():
    global x
    x += 1

wait_for(spawn_drone(increment))
print(x)`

Toto vytiskne `0`, protože nový dron upravil svou vlastní kopii globální proměnné `x`, což nijak neovlivní `x` původního dronu.

## Race Conditions
Více dronů může současně interagovat se stejnou dlaždicí farmy. Pokud dva drony provedou akci nad stejnou dlaždicí ve stejném ticku, obě se provedou, ale výsledek může záviset na pořadí.

Příklad: drony `0` a `1` stojí nad stejným stromem, který je téměř dorostlý.  
Dron `0` volá:
`use_item(Items.Fertilizer)`
Dron `1` volá:
`harvest()`

Pokud k těmto akcím dojde zároveň, strom se nejprve pohnojí a poté sklidí — v tom případě dostaneš dřevo. Pokud je ale dron `1` o něco rychlejší, strom se sklidí dřív, než se pohnojí, a dřevo nedostaneš.  
Tento jev se nazývá „race condition“ (datový závod). Je běžný v paralelním programování, kdy výsledek závisí na pořadí vykonání operací.

Další problém může nastat, když více dronů spouští stejný kód ve stejné pozici:
`if get_water() < 0.5:
    use_item(Items.Water)`

Pokud tento kód spustí více dronů najednou, všichni vyhodnotí první řádek stejně, vstoupí do bloku `if` a všichni použijí vodu — čímž ji zbytečně plýtvají.  
Než se dostanou k druhému řádku, `get_water()` už možná nebude menší než `0.5`, protože jiný dron mezitím políčko zalil.

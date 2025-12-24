# Mega Farma
Toto neuvěřitelně silné odemčení vám dává přístup k více dronům.

Stejně jako dříve začínáte pouze s jedním dronem. Další drony musí být nejprve vytvořeny a zmizí po ukončení programu.
Každý dron spouští svůj vlastní samostatný program. Nové drony lze vytvořit pomocí funkce `spawn_drone(function)`.

`def drone_function():
    move(North)
    do_a_flip()

spawn_drone(drone_function)`

Tím se vytvoří nový dron na stejné pozici jako dron, který spustil příkaz `spawn_drone(function)`. Nový dron poté začne provádět zadanou funkci. Jakmile skončí, automaticky zmizí.

Drony do sebe nenarážejí.

Použijte `max_drones()` k získání maximálního počtu dronů, které mohou existovat současně.
Použijte `num_drones()` k získání počtu dronů, které jsou již na farmě.


## Příklad:
`def harvest_column():
    for _ in range(get_world_size()):
        harvest()
        move(North)

while True:
    if spawn_drone(harvest_column):
        move(East)`

To způsobí, že se váš první dron bude pohybovat horizontálně a vytvářet další drony. Vytvořené drony se pak budou pohybovat vertikálně a sklízet vše, co jim stojí v cestě.

Pokud již byly vytvořeny všechny dostupné drony, `spawn_drone()` neudělá nic a vrátí `None`.

Zde je další příklad, který předává každému dronu jiný směr.
`for dir in [North, East, South, West]:
    def task():
        move(dir)
        do_a_flip()
    spawn_drone(task)`

## Všechny drony jsou si rovny
Neexistuje žádný speciální "hlavní" dron. Všechny drony mohou vytvářet další drony a všechny se započítávají do limitu dronů. Všechny drony zmizí, když skončí. Pokud první dron dokončí svůj program dříve, jiný dron se stane tím, jehož provádění je vizualizováno zvýrazněním kódu. Všechny drony mohou spouštět breakpointy, a když dron spustí breakpoint, zvýraznění kódu se přepne na tento dron.

<spoiler=zobrazit nápovědu> Podívejte se na tuto super užitečnou paralelní funkci `for_all`, která vezme jakoukoli funkci a spustí ji na každém políčku farmy. Využívá k tomu všechny dostupné drony.

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

Jeden obzvláště užitečný vzor je vytvořit drona, pokud je k dispozici, a jinak to udělat sám.

`if not spawn_drone(task):
	task()`
</spoiler>

## Čekání na dalšího drona
Použijte funkci `wait_for(drone)` k čekání na dokončení jiného drona. Rukojeť `drone` získáte, když drona vytvoříte.
`wait_for(drone)` vrací návratovou hodnotu funkce, kterou druhý dron prováděl.

`def get_entity_type_in_direction(dir):
    move(dir)
    return get_entity_type()

def zero_arg_wrapper():
    return get_entity_type_in_direction(North)
drone = spawn_drone(zero_arg_wrapper)
print(wait_for(drone))`

Všimněte si, že vytváření dronů zabere čas, takže není dobrý nápad vytvářet nového drona pro každou maličkost.

Můžete použít `has_finished(drone)` ke kontrole, zda dron skončil, aniž byste na něj čekali.

## Žádná sdílená paměť
Každý dron má svou vlastní paměť a nemůže přímo číst ani zapisovat globální proměnné jiného drona.

`x = 0

def increment():
    global x
    x += 1

wait_for(spawn_drone(increment))
print(x)`

Toto vypíše `0`, protože nový dron inkrementoval svou vlastní kopii globální proměnné `x`, což neovlivní `x` prvního drona.

## Souběh (Race Conditions)
Více dronů může interagovat se stejným políčkem farmy současně. Pokud dva drony interagují se stejným políčkem během stejného tiku, obě interakce proběhnou, ale výsledky se mohou lišit v závislosti na pořadí interakcí.

Například si představte, že drony `0` a `1` jsou oba nad stejným stromem, který je téměř plně vzrostlý.
Drone `0` calls
`use_item(Items.Fertilizer)`
Drone `1` calls
`harvest()`

If these actions occur at the same time, the tree will first be fertilized and then harvested. In that case, you will receive wood from it. However, if Drone `1` is slightly faster, the tree will be harvested before it is fertilized, and you will not receive the wood.
This is called a "race condition." It is a common issue in parallel programming, where the result depends on the order in which operations are performed.

Here's another problematic situation that can happen when multiple drones run the same code simultaneously at the same position.
`if get_water() < 0.5:
    use_item(Items.Water)`

If multiple drones run this simultaneously, they will all run the first line, which puts them into the `if` block. Then, they will all use water, wasting a lot of it.
By the time a drone reaches the second line, `get_water()` might no longer be less than `0.5` because another drone has watered the tile in the meantime.
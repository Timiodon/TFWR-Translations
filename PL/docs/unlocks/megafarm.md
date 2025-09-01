# Megafarma
To niezwykle potężne odblokowanie daje ci dostęp do wielu dronów.

Tak jak poprzednio, zaczynasz z jednym dronem. Dodatkowe drony muszą najpierw zostać stworzone i znikną po zakończeniu programu.
Każdy dron uruchamia swój własny, oddzielny program. Nowe drony można tworzyć za pomocą funkcji `spawn_drone(function)`.

`def drone_function():
    move(North)
    do_a_flip()

spawn_drone(drone_function)`

Tworzy to nowego drona w tej samej pozycji co dron, który uruchomił komendę `spawn_drone(function)`. Nowy dron następnie zaczyna wykonywać określoną funkcję. Po jej zakończeniu zniknie automatycznie.

Drony nie kolidują ze sobą.

Użyj `max_drones()`, aby uzyskać maksymalną liczbę dronów, które można stworzyć.
Użyj `num_drones()`, aby uzyskać liczbę dronów, które już znajdują się na farmie.


## Przykład:
`def harvest_column():
    for _ in range(get_world_size()):
        harvest()
        move(North)

while True:
    if spawn_drone(harvest_column):
        move(East)`

Spowoduje to, że twój pierwszy dron będzie poruszał się poziomo i tworzył więcej dronów. Stworzone drony będą następnie poruszać się pionowo i zbierać wszystko na swojej drodze.

Jeśli wszystkie dostępne drony zostały już stworzone, `spawn_drone()` nic не zrobi i zwróci `None`.

<spoiler=pokaż wskazówkę> Sprawdź tę super przydatną, równoległą funkcję `for_all`, która przyjmuje dowolną funkcję i uruchamia ją na każdym polu farmy. Wykorzystuje do tego wszystkie dostępne drony.

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

Jednym ze szczególnie przydatnych wzorców jest stworzenie drona, jeśli jest dostępny, a w przeciwnym razie zrobienie tego samemu.

`if not spawn_drone(task):
	task()`
</spoiler>

## Oczekiwanie na innego drona
Użyj funkcji `wait_for(drone)`, aby poczekać na zakończenie pracy innego drona. Otrzymujesz uchwyt `drone` podczas tworzenia drona.
`wait_for(drone)` zwraca wartość zwróconą przez funkcję, którą uruchamiał inny dron.

`def get_entity_type_in_direction(dir):
    move(dir)
    return get_entity_type()

def zero_arg_wrapper():
    return get_entity_type_in_direction(North)
drone = spawn_drone(zero_arg_wrapper)
print(wait_for(drone))`

Zauważ, że tworzenie dronów zajmuje czas, więc nie jest dobrym pomysłem tworzenie nowego drona dla każdej małej rzeczy.

## Brak współdzielonej pamięci
Każdy dron ma swoją własną pamięć i nie może bezpośrednio odczytywać ani zapisywać zmiennych globalnych innego drona.

`x = 0

def increment():
    global x
    x += 1

wait_for(spawn_drone(increment))
print(x)`

Wydrukuje to `0`, ponieważ nowy dron zwiększył swoją własną kopię globalnej zmiennej `x`, co nie wpływa na `x` pierwszego drona.

## Race Conditions
Wiele dronów może oddziaływać na to samo pole farmy w tym samym czasie. Jeśli dwa drony oddziałują na to samo pole w tym samym ticku, obie interakcje wystąpią, ale wyniki mogą się różnić w zależności od kolejności interakcji.

Na przykład, wyobraź sobie, że drony `0` i `1` znajdują się nad tym samym, prawie w pełni wyrośniętym drzewem.
Dron `0` wywołuje
`use_item(Items.Fertilizer)`
Dron `1` wywołuje
`harvest()`

Jeśli te akcje wystąpią w tym samym czasie, drzewo zostanie najpierw nawiezione, a następnie zebrane. W takim przypadku otrzymasz z niego drewno. Jednakże, jeśli Dron `1` będzie nieco szybszy, drzewo zostanie zebrane przed nawożeniem i nie otrzymasz drewna.
Nazywa się to „race condition”. Jest to częsty problem w programowaniu równoległym, gdzie wynik zależy od kolejności, w jakiej wykonywane są operacje.

Oto kolejna problematyczna sytuacja, która może się zdarzyć, gdy wiele dronów uruchamia ten sam kod jednocześnie w tej samej pozycji.
`if get_water() < 0.5:
    use_item(Items.Water)`

Jeśli wiele dronów uruchomi to jednocześnie, wszystkie uruchomią pierwszą linię, co umieści je w bloku `if`. Następnie wszystkie użyją wody, marnując jej dużo.
Zanim dron dotrze do drugiej linii, `get_water()` może już nie być mniejsze niż `0.5`, ponieważ inny dron w międzyczasie podlał pole.
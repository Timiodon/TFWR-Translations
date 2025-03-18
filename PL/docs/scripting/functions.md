# Funkcje
Użyj słowa kluczowego `def`, aby zdefiniować nową funkcję:
`def f(arg1, arg2 = False):
	#kod funkcji`

Możesz użyć operatora wywołania `()`, aby wywołać funkcję:
`f(42)`

Zobacz także [Zakresy](docs/scripting/scopes.md), aby dowiedzieć się o lokalnych i globalnych zmiennych w funkcjach.

## Wprowadzenie
Widziałaś/widziałeś już wbudowane funkcje, takie jak `harvest()`.
Możesz również definiować własne funkcje, co pozwala na strukturyzację kodu w sposób modułowy. W zasadzie pozwala to na nadanie nazwy blokowi kodu, aby móc go wywołać z dowolnego miejsca.

## Definicje funkcji
Na przykład, możesz zdefiniować funkcję, która przesunie dron kilka razy.

`def move_n_dir(n, dir):
	for i in range(n):
		move(dir)`

Słowo kluczowe `def` oznacza, że to jest definicja funkcji. 
`move_n_dir` to nazwa, pod którą funkcja zostanie przypisana. Może to być dowolna poprawna nazwa zmiennej i będzie używana do wywołania funkcji.
`n` i `dir` to parametry. Są to zmienne, które przechowują wartości przekazane do funkcji (Te wartości nazywane są również argumentami). Możesz dodać tyle parametrów do definicji funkcji, ile chcesz.
Po `:` znajduje się blok kodu, który zostanie wykonany, gdy funkcja zostanie wywołana.

Przy powyższej definicji, poniższy kod przesuwa dron `10` pól `North` i `2` pola `West`.

`move_n_dir(10, North)
move_n_dir(2, West)`

Kiedy widzisz `def function():`, powinnaś/powinieneś myśleć o tym jak o przypisaniu zmiennej w taki sposób:
`function = create_new_function_object()`
Tak jak przy wszystkich przypisaniach, nie możesz użyć zmiennej przed jej przypisaniem!
Instrukcja `def` musi być wykonana przed jakimkolwiek wywołaniem funkcji.
Ten kod spowoduje błąd:

`func()
def func():
	pass`

## Wartości zwracane
Użyj słowa kluczowego `return`, aby funkcja zwróciła wartość. 
Na przykład, poniższa funkcja definiuje operację wyłącznie lub (xor). Wyłącznie lub zwraca `True`, jeśli jedna wartość jest `True`, a druga `False`:

`def xor(a, b):
	return a != b

if xor(True, False):
	do_a_flip()`

[Krotki](docs/scripting/tuples.md) pozwalają na zwracanie wielu wartości.

## Domyślne argumenty
Możesz również przypisać wartości domyślne, które będą używane jeśli nie zostaną przekazane żadne argumenty.

`def f(a = False):
	if a:
		do_a_flip()

f()

f(True)`

Argument, który ma wartość domyślną, nie może być poprzedzony argumentem, który takiej wartości nie ma.

## Zaawansowane użycie funkcji
Funkcje są wartościami takimi samymi, jak każda inna wartość, a instrukcja `def` działa jak przypisanie, przypisując funkcję do dowolnej nazwy, którą jej nadamy.
To pozwala na robienie takich rzeczy jak:

`def f():
	def d():
		do_a_flip()
	return d

f()()`

Tutaj `f()` wywołuje funkcję `f`, która definiuje i zwraca nową funkcję `d`. Drugi `()` następnie wykonuje zwróconą funkcję i wykonuje flip.
(Robienie takich rzeczy zazwyczaj nie jest dobrym pomysłem, ponieważ trudniej zobaczyć, co się dzieje)

Funkcje, które przyjmują inne funkcje jako argumenty, pozwalają ci naprawdę kreatywnie podejść do zadania:

`def f(g, arg):
	for _ in range(10):
		g(arg)

f(move, North)
f(use_item, Items.Fertilizer)`

Ten kod przesuwa dron `North` 10 razy, a następnie używa nawozu 10 razy.
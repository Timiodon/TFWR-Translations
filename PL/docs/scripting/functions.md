# Funkcje
Użyj słowa kluczowego `def`, aby zdefiniować nową funkcję:
`def f(arg1, arg2 = False):
	#kod funkcji`

Możesz użyć operatora wywołania `()`, aby wywołać funkcję:
`f(42)`

Zobacz także [Zasięgi](docs/scripting/scopes.md), aby dowiedzieć się o zmiennych lokalnych i globalnych w funkcjach.

## Wprowadzenie
Widziałeś już wbudowane funkcje, takie jak `harvest()`.
Możesz także definiować własne funkcje, co pozwala na strukturyzowanie kodu w sposób modularny. W zasadzie pozwala to nadać nazwę blokowi kodu, abyś mógł go wywołać z dowolnego miejsca.

## Definicje funkcji
Na przykład, możesz zdefiniować funkcję, która przesuwa drona kilka razy.

`def move_n_dir(n, dir):
	for i in range(n):
		move(dir)`

Słowo kluczowe `def` sygnalizuje, że jest to definicja funkcji. 
`move_n_dir` to nazwa, do której funkcja zostanie przypisana. Może to być dowolna prawidłowa nazwa zmiennej i będzie używana do wywołania funkcji.
`n` i `dir` to parametry. Są to zmienne, które przechowują wartości przekazywane do funkcji (te wartości nazywane są również argumentami). Do definicji funkcji możesz dodać tyle parametrów, ile chcesz.
Po znaku `:` następuje blok kodu, który zostanie wykonany po wywołaniu funkcji.

Z powyższą definicją, poniższy kod przesuwa drona o `10` pól na `North` i `2` pola na `West`.

`move_n_dir(10, North)
move_n_dir(2, West)`

Kiedy widzisz `def function():`, powinieneś myśleć o tym jak o przypisaniu zmiennej, w ten sposób:
`function = create_new_function_object()`
Podobnie jak w przypadku wszystkich przypisań, nie możesz użyć zmiennej przed jej przypisaniem!
Instrukcja `def` musi zostać wykonana przed jakimkolwiek wywołaniem funkcji.
Ten kod zgłosi błąd:

`func()
def func():
	pass`

## Wartości zwracane
Użyj słowa kluczowego `return`, aby funkcja zwracała wartość. 
Na przykład, poniższa funkcja definiuje operację alternatywy wyłączającej (XOR). Alternatywa wyłączająca zwraca `True`, jeśli jedna wartość jest `True`, a druga `False`:

`def xor(a, b):
	return a != b

if xor(True, False):
	do_a_flip()`

[Krotki](docs/scripting/tuples.md) pozwalają na zwracanie wielu wartości.

## Argumenty domyślne
Możesz również przypisać wartości domyślne, które zostaną użyte, jeśli nie zostaną przekazane żadne argumenty.

`def f(a = False):
	if a:
		do_a_flip()

f()

f(True)`

Argument, który ma wartość domyślną, nie może być poprzedzony argumentem, który nie ma wartości domyślnej.

## Zaawansowane użycie funkcji
Funkcje są wartościami, tak jak każda inna wartość, a instrukcja `def` działa jak instrukcja przypisania, przypisując funkcję do dowolnej nazwy, jaką jej nadasz.
Pozwala to na robienie takich rzeczy:

`def f():
	def d():
		do_a_flip()
	return d

f()()`

Tutaj `f()` wywołuje funkcję `f`, która definiuje i zwraca nową funkcję `d`. Drugie `()` następnie wykonuje zwróconą funkcję i wykonuje obrót.
(Robienie tego typu rzeczy zazwyczaj nie jest dobrym pomysłem, ponieważ trudno jest zobaczyć, co się dzieje)

Funkcje, które przyjmują inne funkcje jako argumenty, pozwalają na dużą kreatywność:

`def f(g, arg):
	for _ in range(10):
		g(arg)

f(move, North)
f(use_item, Items.Fertilizer)`

Ten kod przesuwa drona `North` 10 razy, a następnie używa nawozu 10 razy.
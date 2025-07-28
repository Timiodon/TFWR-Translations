# Pętla For
Pętla `for` działa jak w Pythonie. (Nazywana pętlą foreach w niektórych językach, nie mylić z pętlą for w stylu C, która jest czymś innym).

`for i in sequence:
	#zrób coś z i`

Podobnie jak pętla `while`, pętla `for` również wielokrotnie wywołuje blok kodu. Zamiast pętli opartej na warunku, wykonuje ona ciało pętli raz dla każdego elementu w sekwencji.

## Składnia
Pętla for wygląda tak:

`for nazwa_zmiennej in sekwencja:
	#blok kodu`

`nazwa_zmiennej` może być dowolną wybraną przez ciebie nazwą. Jest to zmienna, która przechowuje bieżący element w sekwencji. `sekwencja` musi być jakąś wartością, po której można iterować, jak zakres lub liczby. Blok kodu jest wykonywany dla każdego elementu, z przypisaną do niego zmienną pętli.

## Sekwencje
[Zakresy (Ranges)](functions/range)      <unlock=lists>[Listy (Lists)](docs/scripting/lists.md)      </unlock><unlock=functions>[Krotki (Tuples)](docs/scripting/tuples.md)      </unlock><unlock=dicts>[Słowniki (Dictionaries)](docs/scripting/dicts.md)      </unlock><unlock=sets>[Sety (Sets)](docs/scripting/sets.md)</unlock>

## Przykład
`for i in range(5):
    harvest()`

Ta pętla wykonuje swoje ciało ustaloną liczbę razy. Jest to w zasadzie to samo, co napisanie

`i = 0
harvest()
i = 1
harvest()
i = 2
harvest()
i = 3
harvest()
i = 4
harvest()`

Więc wywołuje `harvest()` 5 razy.

Zobacz także [Break](docs/scripting/break.md) i [Continue](docs/scripting/continue.md)
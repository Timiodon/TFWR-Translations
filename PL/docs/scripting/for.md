# Pętla For
Pętla `for` działa tak jak w Pythonie. (W niektórych językach nazywana pętlą foreach, nie mylić z pętlą for w stylu C, która jest czymś innym).

`for i in sequence:
	#zrób coś z i`

Podobnie jak pętla `while`, pętla `for` również wielokrotnie wywołuje blok kodu. Zamiast pętli opartej na warunku, wykonuje ciało pętli raz dla każdego elementu w sekwencji.

## Składnia
Pętla for wygląda tak:

`for nazwa_zmiennej in sekwencja:
	#blok kodu`

`nazwa_zmiennej` może być dowolną wybraną przez ciebie nazwą. Jest to zmienna, która przechowuje bieżący element w sekwencji. `sekwencja` musi być wartością, po której można iterować, jak zakres liczb. Blok kodu jest wykonywany dla każdego elementu z zmienną pętli przypisaną do tego elementu.

## Sekwencje
[Zakresy](functions/range)      <unlock=lists>[Listy](docs/scripting/lists.md)      </unlock><unlock=functions>[Krotki](docs/scripting/tuples.md)      </unlock><unlock=dicts>[Słowniki](docs/scripting/dicts.md)      </unlock><unlock=sets>[Zbiory](docs/scripting/sets.md)</unlock>

## Przykład
`for i in range(5):
    harvest()`

Ta pętla wykonuje ciało określoną liczbę razy. Jest to w zasadzie to samo, co napisanie

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

Zobacz również [Break](docs/scripting/break.md) i [Continue](docs/scripting/continue.md)
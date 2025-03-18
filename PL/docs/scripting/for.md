# Pętla For
Pętla `for` działa tak samo jak w Pythonie. (W niektórych językach nazywana jest pętlą foreach, nie mylić z pętlą typu C, która działa inaczej).

`for i in sequence:
	#do something with i`

Podobnie jak pętla `while`, pętla `for` również wielokrotnie wykonuje blok kodu. Zamiast pętli opartej na warunku, wykonuje ciało pętli raz dla każdego elementu w sekwencji.

## Składnia
Pętla for wygląda tak:

`for variable_name in sequence:
	#code block`

`variable_name` może być dowolną nazwą, którą wybierzesz. To zmienna, która przechowuje bieżący element z sekwencji. `sequence` musi być wartością, którą można iterować, jak zakresem lub liczbami. Blok kodu jest wykonywany dla każdego elementu, przy czym zmienna pętli jest przypisana do tego elementu.

## Sekwencje
[Zakresy](functions/range)      <unlock=lists>[Listy](docs/scripting/lists.md)      </unlock><unlock=functions>[Krotki](docs/scripting/tuples.md)      </unlock><unlock=dicts>[Słowniki](docs/scripting/dicts.md)      </unlock><unlock=sets>[Zbiory](docs/scripting/sets.md)</unlock>

## Przykład
`for i in range(5):
    harvest()`

Ta pętla wykonuje ciało określoną liczbę razy. To zasadniczo to samo, co napisanie

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

Czyli wywołuje `harvest()` 5 razy.

Zobacz także [Break](docs/scripting/break.md) i [Continue](docs/scripting/continue.md)
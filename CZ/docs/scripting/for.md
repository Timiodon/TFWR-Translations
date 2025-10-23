# For Loop
Příkaz `for` funguje stejně jako v Pythonu. (V některých jazycích se nazývá „foreach“, ale neplést s C-style `for` cyklem, který je odlišný).

`for i in sequence:
	#do something with i`

Podobně jako cyklus `while` i `for` opakovaně volá blok kódu. Místo opakování podle podmínky však provede tělo cyklu jednou pro každý prvek v sekvenci.

## Syntax
Cyklus `for` vypadá takto:

`for variable_name in sequence:
	#code block`

`variable_name` může být libovolný název. Je to proměnná, která uchovává aktuální prvek sekvence. `sequence` musí být hodnota, přes kterou lze iterovat, například rozsah čísel. Blok kódu se vykoná pro každý prvek s přiřazenou proměnnou cyklu.

## Sequences
[Ranges](functions/range)      <unlock=lists>[Lists](docs/scripting/lists.md)      </unlock><unlock=functions>[Tuples](docs/scripting/tuples.md)      </unlock><unlock=dicts>[Dictionaries](docs/scripting/dicts.md)      </unlock><unlock=sets>[Sets](docs/scripting/sets.md)</unlock>

## Example
`for i in range(5):
    harvest()`

Tento cyklus provede tělo pevně daný početkrát. Je to v podstatě totéž jako:

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

Tedy zavolá `harvest()` 5×.

Viz také [Break](docs/scripting/break.md) a [Continue](docs/scripting/continue.md)
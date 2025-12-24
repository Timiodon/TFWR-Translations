# Smyčka `for`
Smyčka `for` funguje podobně jako v Pythonu.

`for i in sequence:
    #něco s i` 

Na rozdíl od `while`, která běží podle podmínky, `for` provede tělo smyčky pro každý prvek v sekvenci.

## Syntaxe
`for variable_name in sequence:
    #blok kódu`

`variable_name` je libovolné jméno, které přijme aktuální prvek ze sekvence. `sequence` musí být něco, přes co lze iterovat (např. `range` nebo `list`).

## Sekvence
[Rozsahy](functions/range)      <unlock=lists>[Seznamy](docs/scripting/lists.md)      </unlock><unlock=functions>[N-tice](docs/scripting/tuples.md)      </unlock><unlock=dicts>[Slovníky](docs/scripting/dicts.md)      </unlock><unlock=sets>[Množiny](docs/scripting/sets.md)</unlock>

## Příklad
`for i in range(5):
    harvest()`

Tato smyčka zavolá `harvest()` pětkrát.

Viz také [Break](docs/scripting/break.md) a [Continue](docs/scripting/continue.md)
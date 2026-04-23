# For ciklus
A `for` ciklus úgy működik, mint Pythonban. (Néhány nyelvben foreach ciklusnak hívják, nem összekeverendő a C-stílusú for ciklussal, ami egy másik dolog).

`for i in sequence:
	#csinálj valamit i-vel`

A `while` ciklushoz hasonlóan a `for` ciklus is ismételten végrehajt egy kód blokkot. Ahelyett, hogy feltétel alapján ciklusokat hajtana végre, a ciklus törzsét minden szekvencia elemnél egyszer hajtja végre.

## Szintaxis
Egy for ciklus így néz ki:

`for variable_name in sequence:
	#kód blokk`

A `variable_name` bármilyen tetszőleges név lehet. Ez egy változó, ami az aktuális elemet tárolja a szekvenciában. A `sequence`-nek olyan értéknek kell lennie, amin lehet iterálni, mint például számok tartománya. A kód blokk minden elemhez végrehajtódik, a ciklus változóhoz rendelve azt az elemet.

## Szekvenciák
[Tartományok](functions/range)      <unlock=lists>[Listák](docs/scripting/lists.md)      </unlock><unlock=functions>[Tuple-ök](docs/scripting/tuples.md)      </unlock><unlock=dicts>[Szótárak](docs/scripting/dicts.md)      </unlock><unlock=sets>[Halmazok](docs/scripting/sets.md)</unlock>

## Példa
`for i in range(5):
    harvest()`

Ez a ciklus a törzset fix számú alkalommal hajtja végre. Lényegében ugyanaz, mintha ezt írnád

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

Tehát 5-ször hívja meg a `harvest()`-t.

Lásd még: [Break](docs/scripting/break.md) és [Continue](docs/scripting/continue.md)
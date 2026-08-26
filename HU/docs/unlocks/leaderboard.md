# Ranglista
Ha idáig eljutottál, sok kihívásnak ellenálltál. De hatékonyan oldottad meg őket?
Versenyezhetsz más játékosokkal különböző ranglistákon a leghatékonyabb gazdálkodási módszerekért.

Indíthatsz ranglista futást a `leaderboard_run(leaderboard, filename, speedup)` meghívásával.
Ez [szimulációt](docs/unlocks/simulation.md) indít, hasonló a `simulate()`-hoz, kivéve hogy a kezdő feltételek rögzítettek. Minden ranglista kategóriának különböző indulási és siker feltételei vannak.

A ranglista futás sikeres, ha a siker feltétel `True`, amikor a szimuláció véget ér.

A szimuláció NEM ér véget automatikusan, amikor a cél elérték. Biztosítanod kell, hogy a program befejeződjön.
Ha a futás sikeres, az időd hozzáadásra kerül a ranglistához.

A variancia csökkentése érdekében minden futásnak legalább 2 óráig kell futnia (Felemelheted a sebességet, szóval nem fog olyan sokáig tartani). Ha egy futás korábban befejeződik, megismétlésre kerül, amíg összesen 2 óra el nem ér. Az összes futás átlaga kerül feltöltésre pontszámként.

Íme egy példa beállítás, ami a széna ranglistára juttat.
![](LeaderboardSetup400)

## Leggyorsabb visszaállítás
A leggyorsabb visszaállítás a legrangosabb kategória. Teljesen automatizáld a játékot egyetlen farm parcellától a ranglisták újbóli feloldásáig.

Nem kell mindent feloldanod, csak próbáld a lehető leggyorsabban feloldani az `Unlocks.Leaderboard`-ot.

Ne feledd, hogy használhatod a `num_unlocked(unlock) > 0`-t annak ellenőrzésére, hogy valami fel van-e oldva, és használhatod a `get_cost()`-ot a feloldásokon a költségek megtekintéséhez, így automatikusan farmolhatod a megfelelő itemeket.

Függvényhívás:
`leaderboard_run(Leaderboards.Fastest_Reset, filename, speedup)`

Egyenértékű szimuláció:
`unlocks = {}
items = {}
globals = {}
#negatív seed érték véletlen seedet jelent
seed = -1
simulate(filename, unlocks, items, globals, seed, speedup)`

Siker feltétel:
`num_unlocked(Unlocks.Leaderboard) > 0`

## Labirintus
Minden feloldva indulj és farmolj `9863168` aranyat amilyen gyorsan csak tudsz. Ez pontosan az arany mennyiség, amit egy 32x32 labirintus `300` alkalommal újrafelhasználásával keresel.

Függvényhívás:
`leaderboard_run(Leaderboards.Maze, filename, speedup)`

Egyenértékű szimuláció:
`unlocks = Unlocks
items = {Items.Weird_Substance : 1000000000, Items.Power: 1000000000}
globals = {}
seed = -1
simulate(filename, unlocks, items, globals, seed, speedup)`

Siker feltétel:
`num_items(Items.Gold) >= 9863168`

## Dinoszaurusz
Minden feloldva indulj és farmolj `33488928` csontot amilyen gyorsan csak tudsz. Ez pontosan a csontok száma, amit egy 32x32 terület dinoszaurusz farokkal való feltöltésével kapsz.

Függvényhívás:
`leaderboard_run(Leaderboards.Dinosaur, filename, speedup)`

Egyenértékű szimuláció:
`unlocks = Unlocks
items = {Items.Cactus : 1000000000, Items.Power: 1000000000}
globals = {}
seed = -1
simulate(filename, unlocks, items, globals, seed, speedup)`

Siker feltétel:
`num_items(Items.Bone) >= 33488928`

## Egyéb erőforrás ranglisták
Minden növénynek saját ranglistája van az adott növény lehető leggyorsabb farmolásához. Minden feloldással, a növény termesztéséhez szükséges erőforrásokkal és rengeteg erővel indulsz. A cél egy meghatározott mennyiségű erőforrás farmolása a növény által termelt erőforrásból.

Mint mindig, meg kell győződnöd, hogy a programod befejeződik, amikor eléri a célt. A futás nem kész, amíg a program véget nem ér, még ha a cél el is érődött.

### `Leaderboards.Cactus`
`leaderboard_run(Leaderboards.Cactus, filename, speedup)`
Siker feltétel: `num_items(Items.Cactus) >= 33554432`

### `Leaderboards.Sunflowers`
`leaderboard_run(Leaderboards.Sunflowers, filename, speedup)`
Siker feltétel: `num_items(Items.Power) >= 100000`

### `Leaderboards.Pumpkins`
`leaderboard_run(Leaderboards.Pumpkins, filename, speedup)`
Siker feltétel: `num_items(Items.Pumpkin) >= 200000000`

### `Leaderboards.Wood`
`leaderboard_run(Leaderboards.Wood, filename, speedup)`
Siker feltétel: `num_items(Items.Wood) >= 10000000000`

### `Leaderboards.Carrots`
`leaderboard_run(Leaderboards.Carrots, filename, speedup)`
Siker feltétel: `num_items(Items.Carrot) >= 2000000000`

### `Leaderboards.Hay`
`leaderboard_run(Leaderboards.Hay, filename, speedup)`
Siker feltétel: `num_items(Items.Hay) >= 2000000000`

## Egyetlen drón ranglisták
Vannak ranglisták egyetlen drónnal gazdálkodáshoz is. Csak egy drónt és egy 8x8 farmot kapsz, és a lehető leggyorsabban meghatározott mennyiségű erőforrást kell farmolnod.

### `Leaderboards.Maze_Single`
`leaderboard_run(Leaderboards.Maze_Single, filename, speedup)`
Siker feltétel: `num_items(Items.Gold) >= 616448`

### `Leaderboards.Cactus_Single`
`leaderboard_run(Leaderboards.Cactus_Single, filename, speedup)`
Siker feltétel: `num_items(Items.Cactus) >= 131072`

### `Leaderboards.Sunflowers_Single`
`leaderboard_run(Leaderboards.Sunflowers_Single, filename, speedup)`
Siker feltétel: `num_items(Items.Power) >= 10000`

### `Leaderboards.Pumpkins_Single`
`leaderboard_run(Leaderboards.Pumpkins_Single, filename, speedup)`
Siker feltétel: `num_items(Items.Pumpkin) >= 10000000`

### `Leaderboards.Wood_Single`
`leaderboard_run(Leaderboards.Wood_Single, filename, speedup)`
Siker feltétel: `num_items(Items.Wood) >= 500000000`

### `Leaderboards.Carrots_Single`
`leaderboard_run(Leaderboards.Carrots_Single, filename, speedup)`
Siker feltétel: `num_items(Items.Carrot) >= 100000000`

### `Leaderboards.Hay_Single`
`leaderboard_run(Leaderboards.Hay_Single, filename, speedup)`
Siker feltétel: `num_items(Items.Hay) >= 100000000`
# Leaderboard
Pokud ses dostal až sem, překonal jsi spoustu výzev. Ale vyřešil jsi je efektivně?  
Můžeš soutěžit s ostatními hráči v různých kategoriích žebříčku o nejefektivnější metody farmaření.

Běh pro žebříček můžeš spustit voláním `leaderboard_run(leaderboard, filename, speedup)`.  
To spustí [simulaci](docs/unlocks/simulation.md) podobnou `simulate()`, ale s pevně danými počátečními podmínkami. Každá kategorie žebříčku má odlišné startovní a úspěšné podmínky.

Běh pro žebříček je úspěšný, pokud je po skončení simulace splněna úspěšná podmínka (`True`). 

Simulace se NEUKONČÍ automaticky ve chvíli, kdy dosáhneš cíle. Musíš zajistit, aby se program ukončil.  
Pokud je běh úspěšný, tvůj čas se přidá do žebříčku.

Aby se snížila náhodnost, všechny běhy musí běžet alespoň 2 hodiny (můžeš je zrychlit, takže to reálně netrvá tak dlouho). Pokud je běh dokončen dřív, opakuje se, dokud součet časů nedosáhne 2 hodin. Do žebříčku se pak nahraje průměr všech běhů jako tvé skóre.

Tady je ukázkové nastavení, které tě dostane do žebříčku sena.  
![](LeaderboardSetup400)

## Fastest Reset
„Fastest Reset“ je nejprestižnější kategorie. Úplně zautomatizuj hru od jediné dlaždice farmy až po opětovné odemknutí žebříčků.

Nemusíš odemknout úplně vše — cílem je co nejrychleji odemknout `Unlocks.Leaderboard`.

Pamatuj, že můžeš použít `num_unlocked(unlock) > 0` ke zjištění, zda je něco odemčeno, a také `get_cost()` na odemykatelné prvky, abys viděl jejich cenu a mohl automaticky farmařit správné předměty.

Function Call:
`leaderboard_run(Leaderboards.Fastest_Reset, filename, speedup)`

Equivalent Simulation:
`unlocks = {}
items = {}
globals = {}
#a negative seed value means a random seed
seed = -1
simulate(filename, unlocks, items, globals, seed, speedup)`

Success Condition:
`num_unlocked(Unlocks.Leaderboard) > 0`

## Maze
Začni se vším odemčeným a nafarm `9863168` zlata co nejrychleji. To je přesně množství zlata, které získáš opětovným použitím jednoho bludiště 32×32 přesně `300`krát.

Function Call:
`leaderboard_run(Leaderboards.Maze, filename, speedup)`

Equivalent Simulation:
`unlocks = Unlocks
items = {Items.Weird_Substance : 1000000000, Items.Power: 1000000000}
globals = {}
seed = -1
simulate(filename, unlocks, items, globals, seed, speedup)`

Success Condition:
`num_items(Items.Gold) >= 9863168`

## Dinosaur
Začni se vším odemčeným a nafarm `33488928` kostí co nejrychleji. To je přesně počet kostí, které dostaneš, pokud ocas dinosaura zaplní plochu 32×32.

Function Call:
`leaderboard_run(Leaderboards.Dinosaur, filename, speedup)`

Equivalent Simulation:
`unlocks = Unlocks
items = {Items.Cactus : 1000000000, Items.Power: 1000000000}
globals = {}
seed = -1
simulate(filename, unlocks, items, globals, seed, speedup)`

Success Condition:
`num_items(Items.Bone) >= 33488928`

## Other Resource Leaderboards
Každá rostlina má vlastní žebříček pro co nejrychlejší farmaření dané suroviny. Začínáš se všemi odemknutími, se zdroji potřebnými k pěstování dané rostliny a s velkým množstvím „Power“. Cílem je nafarmit stanovené množství suroviny, kterou rostlina produkuje.

Jako vždy, i zde se ujisti, že se program po dosažení cíle opravdu ukončí. Běh není dokončen, dokud program neskončí, i když už jsi cíle dosáhl.

### `Leaderboards.Cactus`
`leaderboard_run(Leaderboards.Cactus, filename, speedup)`
Success Condition: `num_items(Items.Cactus) >= 33554432`

### `Leaderboards.Sunflowers`
`leaderboard_run(Leaderboards.Sunflowers, filename, speedup)`
Success Condition: `num_items(Items.Power) >= 100000`

### `Leaderboards.Pumpkins`
`leaderboard_run(Leaderboards.Pumpkins, filename, speedup)`
Success Condition: `num_items(Items.Pumpkin) >= 200000000`

### `Leaderboards.Wood`
`leaderboard_run(Leaderboards.Wood, filename, speedup)`
Success Condition: `num_items(Items.Wood) >= 10000000000`

### `Leaderboards.Carrots`
`leaderboard_run(Leaderboards.Carrots, filename, speedup)`
Success Condition: `num_items(Items.Carrot) >= 2000000000`

### `Leaderboards.Hay`
`leaderboard_run(Leaderboards.Hay, filename, speedup)`
Success Condition: `num_items(Items.Hay) >= 2000000000`

## Single Drone Leaderboards
Existují také žebříčky pro farmaření s jediným dronem. Dostaneš jen jeden dron a farmu 8×8 a musíš co nejrychleji nafarmit stanovené množství surovin.

### `Leaderboards.Maze_Single`
`leaderboard_run(Leaderboards.Maze_Single, filename, speedup)`
Success Condition: `num_items(Items.Gold) >= 616448`

### `Leaderboards.Cactus_Single`
`leaderboard_run(Leaderboards.Cactus_Single, filename, speedup)`
Success Condition: `num_items(Items.Cactus) >= 131072`

### `Leaderboards.Sunflowers_Single`
`leaderboard_run(Leaderboards.Sunflowers_Single, filename, speedup)`
Success Condition: `num_items(Items.Power) >= 10000`

### `Leaderboards.Pumpkins_Single`
`leaderboard_run(Leaderboards.Pumpkins_Single, filename, speedup)`
Success Condition: `num_items(Items.Pumpkin) >= 10000000`

### `Leaderboards.Wood_Single`
`leaderboard_run(Leaderboards.Wood_Single, filename, speedup)`
Success Condition: `num_items(Items.Wood) >= 500000000`

### `Leaderboards.Carrots_Single`
`leaderboard_run(Leaderboards.Carrots_Single, filename, speedup)`
Success Condition: `num_items(Items.Carrot) >= 100000000`

### `Leaderboards.Hay_Single`
`leaderboard_run(Leaderboards.Hay_Single, filename, speedup)`
Success Condition: `num_items(Items.Hay) >= 100000000`
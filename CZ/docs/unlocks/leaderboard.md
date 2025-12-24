# Žebříček
Pokud jste se dostali až sem, překonali jste mnoho výzev. Ale vyřešili jste je efektivně?
Můžete soutěžit s ostatními hráči v různých žebříčcích o nejefektivnější metody farmaření.

Běh žebříčku můžete spustit zavoláním `leaderboard_run(leaderboard, filename, speedup)`.
Tím se spustí [simulace](docs/unlocks/simulation.md) podobná `simulate()`, s tím rozdílem, že počáteční podmínky jsou pevně dané. Každá kategorie žebříčku má jiné počáteční a úspěšné podmínky.

Běh žebříčku je úspěšný, pokud je podmínka úspěchu `True` (pravda), když simulace skončí.

Simulace se NEUKONČÍ automaticky, když je dosaženo cíle. Musíte zajistit, aby se program ukončil.
Pokud je běh úspěšný, váš čas bude přidán do žebříčku.

Pro snížení rozptylu je vyžadováno, aby všechny běhy trvaly alespoň 2 hodiny (můžete to zrychlit, takže to nebude trvat tak dlouho). Pokud je běh dokončen dříve, bude se opakovat, dokud nebude dosaženo celkového času 2 hodin. Průměr všech běhů je poté nahrán jako vaše skóre.

Zde je příklad nastavení, které vás dostane do žebříčku sena.
![](LeaderboardSetup400)

## Nejrychlejší reset
Nejrychlejší reset je nejprestižnější kategorie. Zcela zautomatizujte hru od jediného políčka farmy až po opětovné odemčení žebříčků.

Nemusíte odemykat vše, stačí se pokusit odemknout `Unlocks.Leaderboard` co nejrychleji.

Pamatujte, že můžete použít `num_unlocked(unlock) > 0` ke kontrole, zda je něco odemčeno, a můžete použít `get_cost()` na odemčení, abyste viděli, co stojí, takže můžete automaticky farmit správné předměty.

Volání funkce:
`leaderboard_run(Leaderboards.Fastest_Reset, filename, speedup)`

Ekvivalentní simulace:
`unlocks = {}
items = {}
globals = {}
#záporná hodnota seed znamená náhodný seed
seed = -1
simulate(filename, unlocks, items, globals, seed, speedup)`

Podmínka úspěchu:
`num_unlocked(Unlocks.Leaderboard) > 0`

## Bludiště
Začněte se vším odemčeným a nafarměte `9863168` zlata co nejrychleji. To je přesně množství zlata, které získáte opětovným použitím jednoho bludiště 32x32 `300` krát.

Volání funkce:
`leaderboard_run(Leaderboards.Maze, filename, speedup)`

Ekvivalentní simulace:
`unlocks = Unlocks
items = {Items.Weird_Substance : 1000000000, Items.Power: 1000000000}
globals = {}
seed = -1
simulate(filename, unlocks, items, globals, seed, speedup)`

Podmínka úspěchu:
`num_items(Items.Gold) >= 9863168`

## Dinosaurus
Začněte se vším odemčeným a nafarměte `33488928` kostí co nejrychleji. To je přesně počet kostí, které získáte, pokud zaplníte oblast 32x32 dinosauřím ocasem.

Volání funkce:
`leaderboard_run(Leaderboards.Dinosaur, filename, speedup)`

Ekvivalentní simulace:
`unlocks = Unlocks
items = {Items.Cactus : 1000000000, Items.Power: 1000000000}
globals = {}
seed = -1
simulate(filename, unlocks, items, globals, seed, speedup)`

Podmínka úspěchu:
`num_items(Items.Bone) >= 33488928`

## Žebříčky ostatních zdrojů
Každá rostlina má svůj vlastní žebříček pro farmaření této konkrétní rostliny co nejrychleji. Začínáte se všemi odemčeními, zdroji, které potřebujete k pěstování rostliny, a spoustou energie. Cílem je nafarmit stanovené množství zdroje produkovaného rostlinou.

Jako vždy musíte zajistit, aby se váš program ukončil, když dosáhnete cíle. Běh není dokončen, dokud program neskončí, i když je cíle dosaženo.

### `Leaderboards.Cactus`
`leaderboard_run(Leaderboards.Cactus, filename, speedup)`
Podmínka úspěchu: `num_items(Items.Cactus) >= 33554432`

### `Leaderboards.Sunflowers`
`leaderboard_run(Leaderboards.Sunflowers, filename, speedup)`
Podmínka úspěchu: `num_items(Items.Power) >= 100000`

### `Leaderboards.Pumpkins`
`leaderboard_run(Leaderboards.Pumpkins, filename, speedup)`
Podmínka úspěchu: `num_items(Items.Pumpkin) >= 200000000`

### `Leaderboards.Wood`
`leaderboard_run(Leaderboards.Wood, filename, speedup)`
Podmínka úspěchu: `num_items(Items.Wood) >= 10000000000`

### `Leaderboards.Carrots`
`leaderboard_run(Leaderboards.Carrots, filename, speedup)`
Podmínka úspěchu: `num_items(Items.Carrot) >= 2000000000`

### `Leaderboards.Hay`
`leaderboard_run(Leaderboards.Hay, filename, speedup)`
Podmínka úspěchu: `num_items(Items.Hay) >= 2000000000`

## Žebříčky pro jednoho drona
There are also Leaderboards for farming with a single drone. You only get one drone and an 8x8 farm and have to farm a certain amount of resources as quickly as possible.

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
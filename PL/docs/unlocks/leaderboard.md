# Tabela wyników
Jeśli dotarłeś tak daleko, pokonałeś wiele wyzwań. Ale czy rozwiązałeś je wydajnie? 
Możesz konkurować z innymi graczami w różnych tabelach wyników o najbardziej wydajne metody uprawy.

Możesz rozpocząć próbę w tabeli wyników, wywołując `leaderboard_run(leaderboard, filename, speedup)`.
Rozpoczyna to [symulację](docs/unlocks/simulation.md) podobną do `simulate()`, z tym wyjątkiem, że warunki początkowe są stałe. Każda kategoria tabeli wyników ma inne warunki początkowe i warunki powodzenia.

Próba w tabeli wyników kończy się sukcesem, jeśli warunek powodzenia jest `True`, gdy symulacja się kończy. 

Symulacja NIE zakończy się automatycznie po osiągnięciu celu. Musisz upewnić się, że program zakończy działanie.
Jeśli próba się powiedzie, twój czas zostanie dodany do tabeli wyników.

Aby zmniejszyć wariancję, wszystkie próby muszą trwać co najmniej 2 godziny (możesz to przyspieszyć, więc nie potrwa to tak długo). Jeśli próba zostanie ukończona wcześniej, będzie powtarzana, aż do osiągnięcia łącznego czasu 2 godzin. Średnia ze wszystkich prób jest następnie przesyłana jako twój wynik.

Oto przykładowa konfiguracja, która pozwoli ci znaleźć się w tabeli wyników siana.
![](LeaderboardSetup400)

## Najszybszy reset
Najszybszy reset to najbardziej prestiżowa kategoria. Całkowicie zautomatyzuj grę od jednego poletka do ponownego odblokowania tabel wyników.

Nie musisz wszystkiego odblokowywać, po prostu spróbuj jak najszybciej odblokować `Unlocks.Leaderboard`.

Pamiętaj, że możesz użyć `num_unlocked(unlock) > 0`, aby sprawdzić, czy coś jest odblokowane, i możesz użyć `get_cost()` na odblokowaniach, aby zobaczyć, ile kosztują, dzięki czemu możesz automatycznie uprawiać odpowiednie przedmioty.

Wywołanie funkcji:
`leaderboard_run(Leaderboards.Fastest_Reset, filename, speedup)`

Równoważna symulacja:
`unlocks = {}
items = {}
globals = {}
#ujemna wartość seed oznacza losowy seed
seed = -1
simulate(filename, unlocks, items, globals, seed, speedup)`

Warunek powodzenia:
`num_unlocked(Unlocks.Leaderboard) > 0`

## Labirynt
Zacznij z wszystkim odblokowanym i zbierz `9863168` złota tak szybko, jak potrafisz. To dokładnie tyle złota, ile zarobisz, używając ponownie jednego labiryntu 32x32 `300` razy.

Wywołanie funkcji:
`leaderboard_run(Leaderboards.Maze, filename, speedup)`

Równoważna symulacja:
`unlocks = Unlocks
items = {Items.Weird_Substance : 1000000000, Items.Power: 1000000000}
globals = {}
seed = -1
simulate(filename, unlocks, items, globals, seed, speedup)`

Warunek powodzenia:
`num_items(Items.Gold) >= 9863168`

## Dinozaur
Zacznij z wszystkim odblokowanym i zbierz `33488928` kości tak szybko, jak potrafisz. To dokładnie tyle kości, ile zdobędziesz, jeśli wypełnisz obszar 32x32 ogonem dinozaura.

Wywołanie funkcji:
`leaderboard_run(Leaderboards.Dinosaur, filename, speedup)`

Równoważna symulacja:
`unlocks = Unlocks
items = {Items.Cactus : 1000000000, Items.Power: 1000000000}
globals = {}
seed = -1
simulate(filename, unlocks, items, globals, seed, speedup)`

Warunek powodzenia:
`num_items(Items.Bone) >= 33488928`

## Inne tabele wyników zasobów
Każda roślina ma swoją własną tabelę wyników za jak najszybsze uprawianie tej konkretnej rośliny. Zaczynasz z wszystkimi odblokowaniami, zasobami potrzebnymi do uprawy rośliny i dużą ilością energii. Celem jest zebranie określonej ilości zasobu produkowanego przez roślinę.

Jak zawsze, musisz upewnić się, że twój program zakończy działanie po osiągnięciu celu. Próba nie jest zakończona, dopóki program nie zakończy swojego działania, nawet jeśli cel został osiągnięty.

### `Leaderboards.Cactus`
`leaderboard_run(Leaderboards.Cactus, filename, speedup)`
Warunek powodzenia: `num_items(Items.Cactus) >= 33554432`

### `Leaderboards.Sunflowers`
`leaderboard_run(Leaderboards.Sunflowers, filename, speedup)`
Warunek powodzenia: `num_items(Items.Sunflower) >= 100000`

### `Leaderboards.Pumpkins`
`leaderboard_run(Leaderboards.Pumpkins, filename, speedup)`
Warunek powodzenia: `num_items(Items.Pumpkin) >= 200000000`

### `Leaderboards.Wood`
`leaderboard_run(Leaderboards.Wood, filename, speedup)`
Warunek powodzenia: `num_items(Items.Wood) >= 10000000000`

### `Leaderboards.Carrots`
`leaderboard_run(Leaderboards.Carrots, filename, speedup)`
Warunek powodzenia: `num_items(Items.Carrot) >= 2000000000`

### `Leaderboards.Hay`
`leaderboard_run(Leaderboards.Hay, filename, speedup)`
Warunek powodzenia: `num_items(Items.Hay) >= 2000000000`

## Tabele wyników dla jednego drona
Istnieją również tabele wyników dla uprawy przy użyciu jednego drona. Otrzymujesz tylko jednego drona i farmę 8x8, i musisz jak najszybciej zebrać określoną ilość zasobów.

### `Leaderboards.Maze_Single`
`leaderboard_run(Leaderboards.Maze_Single, filename, speedup)`
Warunek powodzenia: `num_items(Items.Gold) >= 616448`

### `Leaderboards.Cactus_Single`
`leaderboard_run(Leaderboards.Cactus_Single, filename, speedup)`
Warunek powodzenia: `num_items(Items.Cactus) >= 131072`

### `Leaderboards.Sunflowers_Single`
`leaderboard_run(Leaderboards.Sunflowers_Single, filename, speedup)`
Warunek powodzenia: `num_items(Items.Sunflower) >= 10000`

### `Leaderboards.Pumpkins_Single`
`leaderboard_run(Leaderboards.Pumpkins_Single, filename, speedup)`
Warunek powodzenia: `num_items(Items.Pumpkin) >= 10000000`

### `Leaderboards.Wood_Single`
`leaderboard_run(Leaderboards.Wood_Single, filename, speedup)`
Warunek powodzenia: `num_items(Items.Wood) >= 500000000`

### `Leaderboards.Carrots_Single`
`leaderboard_run(Leaderboards.Carrots_Single, filename, speedup)`
Warunek powodzenia: `num_items(Items.Carrot) >= 100000000`

### `Leaderboards.Hay_Single`
`leaderboard_run(Leaderboards.Hay_Single, filename, speedup)`
Warunek powodzenia: `num_items(Items.Hay) >= 100000000`
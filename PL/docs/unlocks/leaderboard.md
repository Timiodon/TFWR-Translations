# Tabela wyników
Jeśli dotarłeś tak daleko, pokonałeś wiele wyzwań. Ale czy rozwiązałeś je wydajnie? 
Możesz konkurować z innymi graczami w różnych tabelach wyników o najbardziej wydajne metody uprawy.

Możesz rozpocząć próbę w tabeli wyników, wywołując `leaderboard_run(leaderboard, filename, speedup)`.
Rozpoczyna to [symulację](docs/unlocks/simulation.md) podobną do `simulate()`, z tym wyjątkiem, że warunki początkowe są stałe. Każda kategoria tabeli wyników ma inne warunki początkowe i warunki powodzenia.

Próba w tabeli wyników kończy się sukcesem, jeśli warunek powodzenia jest `True`, gdy symulacja się kończy. Symulacja nie zakończy się automatycznie po osiągnięciu celu. Musisz upewnić się, że program zakończy działanie.
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
Zacznij z wszystkim odblokowanym i zbierz `300000` złota tak szybko, jak potrafisz. To dokładnie tyle złota, ile zarobisz, rozwiązując jeden labirynt `300` razy.

Wywołanie funkcji:
`leaderboard_run(Leaderboards.Maze, filename, speedup)`

Równoważna symulacja:
`unlocks = Unlocks
items = {Items.Weird_Substance : 1000000, Items.Power: 1000000}
globals = {}
seed = -1
simulate(filename, unlocks, items, globals, seed, speedup)`

Warunek powodzenia:
`num_items(Items.Gold) >= 300000`

## Dinozaur
Zacznij z wszystkim odblokowanym i zbierz `98010` kości tak szybko, jak potrafisz. To dokładnie tyle kości, ile zdobędziesz, jeśli wypełnisz obszar 10x10 ogonem dinozaura.

Wywołanie funkcji:
`leaderboard_run(Leaderboards.Dinosaur, filename, speedup)`

Równoważna symulacja:
`unlocks = Unlocks
items = {Items.Pumpkin : 1000000, Items.Power: 1000000}
globals = {}
seed = -1
simulate(filename, unlocks, items, globals, seed, speedup)`

Warunek powodzenia:
`num_items(Items.Bone) >= 98010`

## Inne tabele wyników zasobów
Każda roślina ma swoją własną tabelę wyników za jak najszybsze uprawianie tej konkretnej rośliny. Zaczynasz z wszystkimi odblokowaniami, zasobami potrzebnymi do uprawy rośliny i dużą ilością energii. Celem jest zebranie `100000` jednostek zasobu produkowanego przez roślinę.

Wywołania funkcji:
`leaderboard_run(Leaderboards.Cactus, filename, speedup)`
`leaderboard_run(Leaderboards.Sunflowers, filename, speedup)`
`leaderboard_run(Leaderboards.Pumpkins, filename, speedup)`
`leaderboard_run(Leaderboards.Wood, filename, speedup)`
`leaderboard_run(Leaderboards.Carrots, filename, speedup)`
`leaderboard_run(Leaderboards.Hay, filename, speedup)`
`leaderboard_run(Leaderboards.Polyculture, filename, speedup)`

Warunek powodzenia:
`num_items(resource) >= 100000`

`Leaderboards.Polyculture` wymaga zebrania `100000` jednostek wszystkich trzech zasobów uprawy współrzędnej.
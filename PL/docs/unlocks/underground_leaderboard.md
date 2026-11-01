# Ranking podziemny
Podziemia kryją jeszcze większe wyzwania. Czy jesteś gotów zoptymalizować swoje programy górnicze i rolnicze?
To odblokowanie pozwala rywalizować o najwydajniejsze metody w głębinach.

Możesz rozpocząć podziemną próbę rankingową przez `leaderboard_run(leaderboard, filename, speedup)`.
Rozpoczyna to [symulację](docs/unlocks/simulation.md) podobną do `simulate()`, z tym wyjątkiem, że warunki początkowe są stałe. Każda kategoria tabeli wyników ma inne warunki początkowe i warunki powodzenia.

Próba w tabeli wyników kończy się sukcesem, jeśli warunek powodzenia jest `True`, gdy symulacja się kończy.

Symulacja NIE zakończy się automatycznie po osiągnięciu celu. Musisz upewnić się, że program zakończy działanie.
Jeśli próba się powiedzie, twój czas zostanie dodany do tabeli wyników.

Aby zmniejszyć wariancję, wszystkie próby muszą obejmować co najmniej 2 godziny symulowanego czasu. Symulację można przyspieszyć, więc w rzeczywistości nie potrwa to tak długo. Jeśli próba zakończy się wcześniej, będzie powtarzana, aż łączny symulowany czas osiągnie 2 godziny. Jako twój wynik zostanie przesłany średni czas ze wszystkich prób.

Oto przykładowy układ, który pozwoli wejść do rankingu `Leaderboards.Rice_Single`.

![|x400](UndergroundLeaderboardSetup)

## Najszybszy podziemny reset
Podziemny reset jest najbardziej prestiżową kategorią. W pełni automatyzujesz drzewko górnictwa, zaczynając od jednego pola i kończąc na ponownym odblokowaniu `Unlocks.Underground_Leaderboard`.

Nie musisz odblokowywać wszystkiego — po prostu odblokuj `Unlocks.Underground_Leaderboard` jak najszybciej.

Pamiętaj, że za pomocą `num_unlocked(unlock) > 0` możesz sprawdzić, czy coś jest odblokowane. Możesz też użyć `get_cost()` na odblokowaniach, aby poznać ich koszt i automatycznie zdobywać odpowiednie przedmioty.

`unlock()` nie uwzględnia zależności w drzewku technologii. Można na przykład odblokować `Unlocks.Fertilizer` przed `Unlocks.Water`.

Wywołanie funkcji:
`leaderboard_run(Leaderboards.Fastest_Underground_Reset, filename, speedup)`

Równoważna symulacja:
`unlocks = {}
items = {}
globals = {}
#ujemna wartość zmiennej seed oznacza losowe ziarno
seed = -1
simulate(filename, unlocks, items, globals, seed, speedup)`

Warunek powodzenia:
`num_unlocked(Unlocks.Underground_Leaderboard) > 0`

## Rudy
Ten ranking sprawdza umiejętność zbierania rud, zwłaszcza kwarcu. Zmienia generowanie podłoża, by warstwy dostarczały kolejno węgla, żelaza i kwarcu.

Zacznij ze wszystkim odblokowanym i zbierz `20000` kwarcu jak najszybciej.

Wywołanie funkcji:
`leaderboard_run(Leaderboards.Ores, filename, speedup)`

Równoważna symulacja:
`unlocks = Unlocks
items = {Items.Power: 1000000000}
globals = {}
seed = -1
simulate(filename, unlocks, items, globals, seed, speedup)`

Warunek powodzenia:
`num_items(Items.Quartz) >= 20000`

## Mapa skarbów
Ten ranking zaczyna się ze wszystkim odblokowanym i dużą ilością energii. Zmienia generowanie podłoża tak, by było wiele map skarbów.

Rozgrywa się w świecie 8x8 z jednym dronem. Celem jest zebranie `115000` złota jak najszybciej.

Wywołanie funkcji:
`leaderboard_run(Leaderboards.Treasure_Map, filename, speedup)`

Równoważna symulacja:
`unlocks = Unlocks
items = {Items.Power: 1000000000}
globals = {}
seed = -1
simulate(filename, unlocks, items, globals, seed, speedup)`

Warunek powodzenia:
`num_items(Items.Gold) >= 115000`

## Rankingi zasobów
Te rankingi skupiają się na jak najszybszym zbieraniu konkretnych zasobów. Zaczynasz ze wszystkim odblokowanym i dużą ilością energii. Wyjątkiem jest ranking piramid, w którym musisz samodzielnie wytwarzać energię przez ich odbudowę.

Celem jest zebranie określonej liczby zasobów.

Jak zawsze musisz upewnić się, że program zakończy działanie po osiągnięciu celu. Próba nie kończy się, dopóki program nie przestanie działać, nawet jeśli cel został już osiągnięty.

Te rankingi zmieniają generowanie podłoża, aby żądany zasób pojawiał się bez końca. Nie musisz więc używać `clear()`. Na przykład ranking ryżu zawiera wyłącznie warstwy gliny.

### `Leaderboards.Rice`
`leaderboard_run(Leaderboards.Rice, filename, speedup)`
Warunek powodzenia: `num_items(Items.Rice) >= 2000000`

### `Leaderboards.Bamboo`
Ranking bambusa zabrania kopania.

`leaderboard_run(Leaderboards.Bamboo, filename, speedup)`
Warunek powodzenia: `num_items(Items.Bamboo) >= 500000000`

### `Leaderboards.Dynamite`
`leaderboard_run(Leaderboards.Dynamite, filename, speedup)`
Warunek powodzenia: `num_items(Items.Dynamite) >= 10000000`

### `Leaderboards.Mushrooms`
`leaderboard_run(Leaderboards.Mushrooms, filename, speedup)`
Warunek powodzenia: `num_items(Items.Mushroom) >= 240000`

### `Leaderboards.Pyramids`
`leaderboard_run(Leaderboards.Pyramids, filename, speedup)`
Warunek powodzenia: `num_items(Items.Power) >= 150000`

## Podziemne rankingi jednego drona
Istnieją również tabele wyników dla uprawy jednym dronem. Otrzymujesz tylko jednego drona i farmę 8x8, a twoim zadaniem jest jak najszybsze zebranie określonej ilości zasobów.

### `Leaderboards.Rice_Single`
`leaderboard_run(Leaderboards.Rice_Single, filename, speedup)`
Warunek powodzenia: `num_items(Items.Rice) >= 100000`

### `Leaderboards.Ores_Single`
`leaderboard_run(Leaderboards.Ores_Single, filename, speedup)`
Warunek powodzenia: `num_items(Items.Quartz) >= 4000`

### `Leaderboards.Bamboo_Single`
`leaderboard_run(Leaderboards.Bamboo_Single, filename, speedup)`
Warunek powodzenia: `num_items(Items.Bamboo) >= 25000000`

### `Leaderboards.Dynamite_Single`
`leaderboard_run(Leaderboards.Dynamite_Single, filename, speedup)`
Warunek powodzenia: `num_items(Items.Dynamite) >= 100000`

### `Leaderboards.Mushrooms_Single`
`leaderboard_run(Leaderboards.Mushrooms_Single, filename, speedup)`
Warunek powodzenia: `num_items(Items.Mushroom) >= 30000`

### `Leaderboards.Pyramids_Single`
`leaderboard_run(Leaderboards.Pyramids_Single, filename, speedup)`
Warunek powodzenia: `num_items(Items.Power) >= 30000`


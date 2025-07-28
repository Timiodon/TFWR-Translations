# Leaderboard
Jeśli dotarłeś tak daleko, pokonałeś wiele wyzwań. Ale czy rozwiązałeś je wydajnie?
Możesz rywalizować z innymi graczami na różnych leaderboardach o najbardziej wydajne metody uprawy.

Możesz rozpocząć próbę na leaderboardzie, wywołując `leaderboard_run(leaderboard, filename, speedup)`.
Rozpoczyna to [symulację](docs/unlocks/simulation.md) podobną do `simulate()`, z tą różnicą, że warunki początkowe są ustalone. Każda kategoria leaderboarda ma inne warunki startowe i warunki sukcesu.

Próba na leaderboardzie kończy się sukcesem, jeśli warunek sukcesu jest `True`, gdy symulacja się kończy. Symulacja nie zakończy się automatycznie po osiągnięciu celu. Musisz upewnić się, że program się zakończy.
Jeśli próba zakończy się sukcesem, Twój czas zostanie dodany do leaderboarda.

Aby zmniejszyć wariancję, wszystkie próby muszą trwać co najmniej 2 godziny (możesz to przyspieszyć, więc nie potrwa to tak długo). Jeśli próba zostanie ukończona wcześniej, będzie powtarzana, aż osiągnie łączny czas 2 godzin. Średnia ze wszystkich prób jest następnie przesyłana jako Twój wynik.

Oto przykładowa konfiguracja, która pozwoli Ci znaleźć się na leaderboardzie siana.
![](LeaderboardSetup400)

## Fastest Reset
Najszybszy reset to najbardziej prestiżowa kategoria. Całkowicie zautomatyzuj grę od pojedynczej działki rolnej do ponownego odblokowania leaderboardów.

Nie musisz odblokowywać wszystkiego, po prostu postaraj się jak najszybciej odblokować `Unlocks.Leaderboard`.

Pamiętaj, że możesz użyć `num_unlocked(unlock) > 0`, aby sprawdzić, czy coś jest odblokowane, a także `get_cost()` na odblokowaniach, aby zobaczyć, ile kosztują, dzięki czemu możesz automatycznie uprawiać odpowiednie przedmioty.

Wywołanie funkcji:
`leaderboard_run(Leaderboards.Fastest_Reset, filename, speedup)`

Równoważna symulacja:
`unlocks = {}
items = {}
globals = {}
#ujemna wartość seed oznacza losowy seed
seed = -1
simulate(filename, unlocks, items, globals, seed, speedup)`

Warunek sukcesu:
`num_unlocked(Unlocks.Leaderboard) > 0`

## Labirynt
Zacznij z wszystkim odblokowanym i zdobądź `300000` złota tak szybko, jak potrafisz. To dokładnie tyle złota, ile zarobisz, rozwiązując jeden labirynt `300` razy.

Wywołanie funkcji:
`leaderboard_run(Leaderboards.Maze, filename, speedup)`

Równoważna symulacja:
`unlocks = Unlocks
items = {Items.Weird_Substance : 1000000, Items.Power: 1000000}
globals = {}
seed = -1
simulate(filename, unlocks, items, globals, seed, speedup)`

Warunek sukcesu:
`num_items(Items.Gold) >= 300000`

## Dinozaur
Zacznij z wszystkim odblokowanym i zdobądź `98010` kości tak szybko, jak potrafisz. To dokładnie tyle kości, ile zdobędziesz, wypełniając obszar 10x10 ogonem dinozaura.

Wywołanie funkcji:
`leaderboard_run(Leaderboards.Dinosaur, filename, speedup)`

Równoważna symulacja:
`unlocks = Unlocks
items = {Items.Pumpkin : 1000000, Items.Power: 1000000}
globals = {}
seed = -1
simulate(filename, unlocks, items, globals, seed, speedup)`

Warunek sukcesu:
`num_items(Items.Bone) >= 98010`

## Inne Leaderboardy zasobów
Każda roślina ma swój własny leaderboard do jak najszybszego zbierania tej konkretnej rośliny. Zaczynasz z wszystkimi odblokowaniami, zasobami potrzebnymi do uprawy rośliny i dużą ilością mocy. Celem jest zebranie `100000` zasobu produkowanego przez roślinę.

Wywołania funkcji:
`leaderboard_run(Leaderboards.Cactus, filename, speedup)`
`leaderboard_run(Leaderboards.Sunflowers, filename, speedup)`
`leaderboard_run(Leaderboards.Pumpkins, filename, speedup)`
`leaderboard_run(Leaderboards.Wood, filename, speedup)`
`leaderboard_run(Leaderboards.Carrots, filename, speedup)`
`leaderboard_run(Leaderboards.Hay, filename, speedup)`
`leaderboard_run(Leaderboards.Polyculture, filename, speedup)`

Warunek sukcesu:
`num_items(resource) >= 100000`

`Leaderboards.Polyculture` wymaga zebrania `100000` wszystkich trzech zasobów polikultury.
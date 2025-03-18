# Leaderboard
Jeśli dotarłeś tak daleko, pokonałeś wiele wyzwań. Ale czy rozwiązałeś je efektywnie?
Możesz rywalizować z innymi graczami na różnych leaderboardach, aby wypracować najwydajniejsze metody uprawy.

Możesz rozpocząć próbę na leaderboardzie, wywołując `leaderboard_run(leaderboard, filename, speedup)`.
To rozpoczyna [symulację](docs/unlocks/simulation.md) podobną do `simulate()`, z tym że warunki początkowe są ustalone. Każda kategoria leaderboardu ma różne warunki startowe i sukcesu.

Próba na leaderboardzie zakończy się sukcesem, jeśli warunek sukcesu będzie `True`, gdy symulacja się skończy. Symulacja nie zakończy się automatycznie, gdy cel zostanie osiągnięty. Musisz upewnić się, że program się zakończy.
Jeśli próba zakończy się sukcesem, Twój czas zostanie dodany do leaderboardu.

Aby zmniejszyć zmienność, wszystkie próby muszą trwać co najmniej 2 godziny (możesz je przyspieszyć, więc nie potrwa to tak długo). Jeśli próba zostanie zakończona wcześniej, zostanie powtórzona aż do osiągnięcia łącznego czasu 2 godzin. Średnia z wszystkich prób zostanie wtedy przesłana jako Twój wynik.

Oto przykład ustawienia, które wprowadzi Cię na tablicę wyników dla siana.
![](LeaderboardSetup400)

## Najszybszy Reset
Najszybszy reset to najbardziej prestiżowa kategoria. Całkowicie zautomatyzuj grę, zaczynając od jednej działki roli do ponownego odblokowania leaderboardów.

Nie musisz odblokowywać wszystkiego, po prostu spróbuj jak najszybciej odblokować `Unlocks.Leaderboard`.

Pamiętaj, że możesz użyć `num_unlocked(unlock) > 0`, by sprawdzić, czy coś jest odblokowane, i możesz użyć `get_cost()` na odblokowaniach, aby zobaczyć, ile kosztują, dzięki czemu możesz automatycznie zdobyć odpowiednie przedmioty.

Wywołanie funkcji:
`leaderboard_run(Leaderboards.Fastest_Reset, filename, speedup)`

Równoważna Symulacja:
`unlocks = {}
items = {}
globals = {}
#wartość ujemna seed oznacza losowy seed
seed = -1
simulate(filename, unlocks, items, globals, seed, speedup)`

Warunek Sukcesu:
`num_unlocked(Unlocks.Leaderboard) > 0`

## Labirynt
Zacznij, mając wszystko odblokowane, i zdobądź `300000` złota tak szybko, jak potrafisz. Jest to dokładnie taka ilość złota, jaką zdobędziesz, rozwiązując jeden labirynt `300` razy.

Wywołanie funkcji:
`leaderboard_run(Leaderboards.Maze, filename, speedup)`

Równoważna Symulacja:
`unlocks = Unlocks
items = {Items.Weird_Substance : 1000000, Items.Power: 1000000}
globals = {}
seed = -1
simulate(filename, unlocks, items, globals, seed, speedup)`

Warunek Sukcesu:
`num_items(Items.Gold) >= 300000`

## Dinozaur
Zacznij, mając wszystko odblokowane, i zdobądź `98010` kości tak szybko, jak potrafisz. Jest to dokładnie liczba kości, którą otrzymasz, wypełniając obszar 10x10 ogonem dinozaura.

Wywołanie funkcji:
`leaderboard_run(Leaderboards.Dinosaur, filename, speedup)`

Równoważna Symulacja:
`unlocks = Unlocks
items = {Items.Pumpkin : 1000000, Items.Power: 1000000}
globals = {}
seed = -1
simulate(filename, unlocks, items, globals, seed, speedup)`

Warunek Sukcesu:
`num_items(Items.Bone) >= 98010`

## Inne leaderboardy zasobów
Każda roślina ma swój leaderboard do jak najszybszego uprawiania tej konkretnej rośliny. Zaczynasz ze wszystkimi odblokowaniami, zasobami potrzebnymi do wzrostu rośliny i dużą ilością energii. Celem jest zdobycie `100000` zasobów wyprodukowanych przez roślinę.

Wywołania funkcji:
`leaderboard_run(Leaderboards.Cactus, filename, speedup)`
`leaderboard_run(Leaderboards.Sunflowers, filename, speedup)`
`leaderboard_run(Leaderboards.Pumpkins, filename, speedup)`
`leaderboard_run(Leaderboards.Wood, filename, speedup)`
`leaderboard_run(Leaderboards.Carrots, filename, speedup)`
`leaderboard_run(Leaderboards.Hay, filename, speedup)`
`leaderboard_run(Leaderboards.Polyculture, filename, speedup)`

Warunek Sukcesu:
`num_items(resource) >= 100000`

`Leaderboards.Polyculture` wymaga zdobycia `100000` trzech różnych zasobów.
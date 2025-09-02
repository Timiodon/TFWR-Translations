# Symulacja

Symulacje pozwalają na szybkie testowanie kodu bez zmiany stanu prawdziwej farmy.
Stan początkowy symulacji można wybrać dowolnie, a po jej zakończeniu prawdziwa farma będzie w dokładnie takim samym stanie, w jakim była przed rozpoczęciem symulacji.

Funkcja `simulate()` służy do rozpoczęcia symulacji.

plik, w którym ma się rozpocząć wykonywanie
`filename = "f1"`

rozpocznij z wszystkim odblokowanym i w pełni ulepszonym
`sim_unlocks = Unlocks`

rozpocznij z 10000 marchewek i 50 sianem
`sim_items = {Items.Carrot : 10000, Items.Hay : 50}`

rozpocznij z globalną zmienną "a" o wartości 13
`sim_globals = {"a" : 13}`

użyj stałego ziarna losowości (seed)
`seed = 0`

przyspiesz symulację 64 razy
`speedup = 64`

uruchom symulację
`run_time = simulate(filename, sim_unlocks, sim_items, sim_globals, seed, speedup)`

Funkcja `simulate()` zwraca czas w sekundach, jaki zajęła symulacja danego pliku startowego.

### Nazwa pliku
Pierwszym argumentem funkcji symulacji jest nazwa pliku. Jest to nazwa wyświetlana na górze okna kodu. Symulacja uruchomi określony plik tak, jakbyś kliknął na nim przycisk Uruchom.

### Początkowe odblokowania
Wszystkie funkcje programistyczne, takie jak pętle, instrukcje if, listy, słowniki,... zawsze pozostaną odblokowane. 

Drugi argument pozwala określić, z jakimi odblokowaniami/ulepszeniami symulacja ma się rozpocząć, oprócz funkcji programistycznych. Powinna to być sekwencja odblokowań. Symulacja rozpocznie się z wszystkimi odblokowaniami w sekwencji ulepszonymi do maksymalnego poziomu.

Jeśli chcesz określić poziom ulepszenia inny niż maksymalny, możesz przekazać słownik, który mapuje odblokowania na poziomy odblokowań. W tym przypadku wartości ujemne odpowiadają maksymalnemu poziomowi odblokowania.

### Początkowe przedmioty
Trzeci argument pozwala przekazać słownik, który mapuje przedmioty na liczby. Określa on przedmioty, z którymi ma się rozpocząć symulacja.

### Początkowe zmienne globalne
Ponieważ symulacja rozpoczyna całkowicie nowe wykonanie programu, nie masz dostępu do zmiennych z programu, który rozpoczyna symulację.
Jednak możliwe jest przekazanie wartości do symulacji za pomocą czwartego argumentu. Jest to słownik (dict), który mapuje nazwy zmiennych w postaci ciągów znaków na wartości. Zmienne te są następnie dodawane do globalnego zasięgu wykonywania wewnątrz symulacji.

Zauważ, że kopiuje to wszystkie wartości, więc ich zmiana wewnątrz symulacji nie wpłynie na oryginalne wartości poza symulacją. Nie jest możliwe zwracanie wartości z symulacji innych niż czas jej trwania.

### Ziarno losowości (Random Seed)
Piąty argument pozwala określić ziarno losowości używane w symulacji. Musi to być dodatnia liczba całkowita. Wartości ujemne spowodują użycie losowego ziarna.

Ziarno losowości wpływa na wszystko, od czasów wzrostu roślin, przez układy labiryntów, po czasy ubywania wody. Jeśli uruchomisz tę samą symulację wielokrotnie z tym samym ziarnem losowości i tymi samymi warunkami początkowymi, wynik powinien być zawsze taki sam.

### Przyspieszenie (Speedup)
Szósty argument to początkowe przyspieszenie symulacji. Pozwala to na szybkie testowanie. Jeśli gra nie jest w stanie nadążyć z ustawioną prędkością, automatycznie zwolni.

Przyspieszenie nie wpływa w żaden sposób na wynik symulacji. Służy jedynie do skrócenia czasu oczekiwania.
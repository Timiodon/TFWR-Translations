# Symulacja

Symulacje pozwalają szybko testować kod bez zmiany stanu prawdziwej farmy.
Stan początkowy symulacji można dowolnie wybrać, a po zakończeniu symulacji prawdziwa farma będzie w dokładnie takim samym stanie, w jakim była przed rozpoczęciem symulacji.

Funkcja `simulate()` służy do uruchamiania symulacji.

plik, w którym ma się rozpocząć wykonanie
`filename = "f1"`

zacznij ze wszystkim odblokowanym i w pełni ulepszonym
`sim_unlocks = Unlocks`

zacznij z 10000 marchewek i 50 siana
`sim_items = {Items.Carrot : 10000, Items.Hay : 50}`

zacznij ze zmienną globalną "a" o wartości 13
`sim_globals = {"a" : 13}`

użyj stałego ziarna losowości (seed)
`seed = 0`

przyspiesz symulację 64 razy
`speedup = 64`

uruchom symulację
`run_time = simulate(filename, sim_unlocks, sim_items, sim_globals, seed, speedup)`

Funkcja `simulate()` zwraca czas w sekundach, jaki zajęło zasymulowanie danego pliku startowego.

### Nazwa pliku
Pierwszym argumentem funkcji symulacji jest nazwa pliku. Jest to nazwa wyświetlana na górze okna kodu. Symulacja uruchomi określony plik tak, jakbyś kliknął na nim przycisk Wykonaj.

### Odblokowania początkowe
Wszystkie funkcje programistyczne, takie jak pętle, instrukcje if, listy, dicts,... zawsze pozostaną odblokowane.

Drugi argument pozwala określić, z jakimi odblokowaniami/ulepszeniami ma rozpocząć się symulacja, oprócz funkcji programistycznych. Powinna to być sekwencja odblokowań. Symulacja rozpocznie się ze wszystkimi odblokowaniami w sekwencji ulepszonymi do maksymalnego poziomu.

Jeśli chcesz określić poziom ulepszenia inny niż maksymalny, możesz przekazać słownik (dictionary), który mapuje odblokowania na poziomy odblokowań. W tym przypadku wartości ujemne odpowiadają maksymalnemu poziomowi odblokowania.

### Przedmioty początkowe
Trzeci argument pozwala przekazać słownik (dictionary), który mapuje przedmioty na liczby. Określa on przedmioty, z którymi ma rozpocząć się symulacja.

### Zmienne globalne na start
Ponieważ symulacja rozpoczyna całkowicie nowe wykonanie programu, nie masz dostępu do zmiennych z programu, który uruchamia symulację.
Możliwe jest jednak przekazanie wartości do symulacji za pomocą czwartego argumentu. Jest to dict, który mapuje nazwy zmiennych w postaci stringów na wartości. Zmienne te są następnie dodawane do globalnego scope wykonania wewnątrz symulacji.

Pamiętaj, że kopiuje to wszystkie wartości, więc ich zmiana wewnątrz symulacji nie wpłynie na oryginalne wartości poza symulacją. Nie jest możliwe zwracanie wartości z symulacji innych niż czas jej trwania.

### Ziarno losowości (Seed)
Piąty argument pozwala określić ziarno losowości (random seed) używane w symulacji. Musi to być dodatnia liczba całkowita. Wartości ujemne spowodują użycie losowego ziarna.

Ziarno losowości wpływa na wszystko, od czasów wzrostu roślin, przez układy labiryntów, po czasy wysychania wody. Jeśli uruchomisz tę samą symulację wielokrotnie z tym samym ziarnem losowości i tymi samymi warunkami początkowymi, wynik powinien być zawsze taki sam.

### Przyspieszenie
Szósty argument to początkowe przyspieszenie symulacji. Pozwala to na szybkie testowanie. Jeśli gra nie jest w stanie utrzymać ustawionej prędkości, automatycznie zwolni.

Przyspieszenie nie wpływa w żaden sposób na wynik symulacji. Istnieje tylko po to, by skrócić czas oczekiwania.
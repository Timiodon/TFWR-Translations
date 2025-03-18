# Symulacja

Symulacje pozwalają szybko przetestować kod bez zmieniania stanu rzeczywistej farmy. Stan początkowy symulacji można wybrać dowolnie, a gdy symulacja się kończy, prawdziwa farma będzie w takim samym stanie, jak przed rozpoczęciem symulacji.

Funkcja `simulate()` jest używana do rozpoczęcia symulacji.

plik, w którym powinna się rozpocząć wykonanie
`filename = "f1"`

rozpocznij z wszystkim odblokowanym i w pełni ulepszonym
`sim_unlocks = Unlocks`

rozpocznij mając 10000 marchewek i 50 siana
`sim_items = {Items.Carrot : 10000, Items.Hay : 50}`

rozpocznij z globalną zmienną "a" o wartości 13
`sim_globals = {"a" : 13}`

użyj stałego ziarna losowości
`seed = 0`

przyspiesz symulację 64-krotnie
`speedup = 64`

uruchom symulację
`run_time = simulate(filename, sim_unlocks, sim_items, sim_globals, seed, speedup)`

Funkcja `simulate()` zwraca czas, w sekundach, jaki zajęło zasymulowanie podanego pliku startowego.

### Nazwa Pliku
Pierwszym argumentem funkcji simulate jest nazwa pliku. To nazwa, która jest wyświetlana na górze okna kodu. Symulacja uruchomi wskazany plik jakbyś kliknął na nim przycisk Wykonaj.

### Początkowe Odblokowania
Wszystkie funkcje programistyczne takie jak pętle, instrukcje if, listy, dicts,... zawsze pozostaną odblokowane.

Drugi argument pozwala określić, z jakimi odblokowaniami/ulepszeniami symulacja powinna wystartować oprócz funkcji programistycznych. Powinna to być sekwencja odblokowań. Symulacja rozpocznie się z wszystkimi odblokowaniami w sekwencji na maksymalnym poziomie.

Jeśli chcesz określić poziom ulepszenia inny niż maksymalny, możesz przekazać słownik mapujący odblokowania na poziomy odblokowania. W tym przypadku wartości ujemne odpowiadają maksymalnemu poziomowi odblokowania.

### Początkowe Przedmioty
Trzeci argument pozwala przekazać słownik, który mapuje przedmioty na liczby. Określa on przedmioty, z którymi symulacja powinna się rozpocząć.

### Początkowe Zmienne Globalne
Ponieważ symulacja zaczyna zupełnie nowe wykonanie programu, nie można uzyskać dostępu do zmiennych z programu, który rozpoczyna symulację. Jednakże, możliwe jest przekazanie wartości do symulacji za pomocą czwartego argumentu. Jest to dict mapujący nazwy zmiennych w postaci ciągów znaków na wartości. Te zmienne są następnie dodawane do globalnego zakresu wykonania wewnątrz symulacji.

Zauważ, że to kopiuje wszystkie wartości, więc ich zmiana wewnątrz symulacji nie wpłynie na oryginalne wartości poza symulacją. Nie ma możliwości zwrócenia wartości z symulacji poza czasem trwania symulacji.

### Random Seed
Piąty argument pozwala określić ziarno losowości używane w symulacji. Musi to być liczba całkowita dodatnia. Wartości ujemne spowodują użycie losowego ziarna.

Ziarno losowości wpływa na wszystko, od czasu wzrostu roślin po układy labiryntów i czasu rozkładu wody. Jeśli uruchomisz tę samą symulację kilka razy z tym samym ziarnem losowości i tymi samymi warunkami początkowymi, wynik powinien być zawsze taki sam.

### Przyspieszenie
Szósty argument to początkowe przyspieszenie symulacji. Pozwala to na szybkie testowanie. Jeśli gra nie nadąża za ustawioną prędkością, automatycznie zwalnia.

Przyspieszenie w żaden sposób nie wpływa na wynik symulacji. Istnieje tylko po to, by skrócić czas oczekiwania.
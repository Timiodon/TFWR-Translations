# Debugowanie
Czasami twój kod po prostu nie działa i musisz zrozumieć, dlaczego. Istnieje kilka narzędzi, które ci w tym pomogą.

Pierwsze z nich to wykonanie programu krok po kroku. 
Możesz przejść do trybu krokowego za pomocą przycisku obok przycisku Wykonaj albo ustawiając breakpoint.

Breakpoints można dodać, klikając na panelu breakpoint po lewej stronie kodu. 
![](Breakpoints227)
Gdy wykonanie programu dotrze do linii z breakpointem, automatycznie przełączy się w tryb krokowy.

Kiedy najedziesz myszką na zmienną, zostanie wyświetlona jej aktualna wartość.

Funkcja `print()` również może być bardzo przydatna. Zapisuje ona dowolną wartość przekazaną do niej bezpośrednio w powietrze.

Przykłady:

Wypisz "0.24".
`print(0.24)`

Wypisz "True" albo "False".
`print(can_harvest())`

Wypisz aktualną pozycję.
`print(get_pos_x(), get_pos_y())`

Funkcja print wypisuje wartość bezpośrednio w powietrze oraz na stronę [Output](docs/output.md).

Pisanie w powietrze może czasami być trochę wolne, jeśli chcesz wydrukować dużo wartości.
W takim przypadku możesz użyć funkcji `quick_print()`, która drukuje tylko do okna wyjścia.

Okno wyjścia również zapisuje ostrzeżenia i błędy, więc jeśli coś nie działa zgodnie z oczekiwaniami, może być przydatne sprawdzenie tego.

Gdy wykonanie zatrzymuje się, dane wyjściowe są również zapisywane do pliku output.txt w folderze gry. [output.txt](persistent_data_path/output.txt).
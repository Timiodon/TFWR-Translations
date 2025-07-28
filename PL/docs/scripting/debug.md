# Debug
Czasami twój kod po prostu nie działa i musisz dowiedzieć się, dlaczego. Istnieje kilka narzędzi, które ci w tym pomogą.

Pierwszym z nich jest wykonanie programu krok po kroku.
Możesz przejść w tryb krok po kroku za pomocą przycisku obok przycisku Wykonaj lub ustawiając breakpoint.

Breakpoints można dodać, klikając panel breakpointów po lewej stronie kodu.
![](Breakpoints227)
Gdy wykonanie dotrze do linii, w której znajduje się breakpoint, automatycznie przełączy się w tryb krok po kroku.

Gdy najedziesz myszką na zmienną, wyświetli się jej aktualna wartość.

Funkcja `print()` również może być bardzo przydatna. Wypisze ona każdą przekazaną jej wartość bezpośrednio w powietrzu.

Przykłady:

Wydrukuj "0.24".
`print(0.24)`

Wydrukuj "True" lub "False".
`print(can_harvest())`

Wydrukuj aktualną pozycję.
`print(get_pos_x(), get_pos_y())`

Funkcja print drukuje wartość bezpośrednio w powietrzu oraz na stronie [Wyjście](docs/output.md).

Pisanie w powietrzu może być czasem trochę wolne, jeśli chcesz wydrukować wiele wartości.
W takim przypadku możesz użyć funkcji `quick_print()`, która drukuje tylko do okna wyjścia.

Okno wyjścia rejestruje również ostrzeżenia i błędy, więc jeśli coś nie działa zgodnie z oczekiwaniami, warto to sprawdzić.

Gdy wykonanie się zatrzyma, wynik jest również zapisywany do pliku output.txt w folderze gry. [output.txt](persistent_data_path/output.txt).
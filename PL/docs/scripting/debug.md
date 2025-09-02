# Debugowanie
Czasami twój kod po prostu nie działa i musisz dowiedzieć się, dlaczego. Jest kilka narzędzi, które mogą ci w tym pomóc.

Pierwszym z nich jest wykonywanie programu krok po kroku. 
Możesz przejść do trybu krok po kroku za pomocą przycisku obok przycisku Wykonaj lub ustawiając punkt przerwania (breakpoint).

Punkty przerwania można dodawać, klikając w panel punktów przerwania po lewej stronie kodu.
![](Breakpoints227)
Gdy wykonanie dotrze do linii, w której znajduje się punkt przerwania, automatycznie przełączy się w tryb krok po kroku.

Gdy najedziesz myszą na zmienną, wyświetli się jej aktualna wartość.

Funkcja `print()` również może być bardzo przydatna. Wypisze każdą przekazaną jej wartość bezpośrednio w powietrzu.

Przykłady:

Wyświetl "0.24".
`print(0.24)`

Wyświetl "True" lub "False".
`print(can_harvest())`

Wyświetl aktualną pozycję.
`print(get_pos_x(), get_pos_y())`

Funkcja print wyświetla wartość bezpośrednio w powietrzu i na stronie [Wyjście](docs/output.md).

Wypisywanie w powietrzu może być czasami trochę wolne, jeśli chcesz wyświetlić wiele wartości.
W takim przypadku możesz użyć funkcji `quick_print()`, która wyświetla dane tylko w oknie wyjściowym.

Okno wyjściowe rejestruje również ostrzeżenia i błędy, więc jeśli coś nie działa zgodnie z oczekiwaniami, warto je sprawdzić.

Gdy wykonanie się zatrzyma, dane wyjściowe są również zapisywane do pliku output.txt w folderze gry. [output.txt](persistent_data_path/output.txt).
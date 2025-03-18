# Czas
Jeśli naprawdę chcesz zoptymalizować swoje metody, musisz zrozumieć, jak czas jest mierzony w tej grze. To odblokowanie dotyczy właśnie tego.

## Nowe Funkcje
Istnieją dwie przydatne funkcje do mierzenia czasu wykonania:

`get_time()` zwraca czas w sekundach od rozpoczęcia gry.

`get_tick_count()` zwraca liczbę ticków wykonanych od początku wykonania.

Te dwie funkcje, podobnie jak `quick_print()`, są całkowicie darmowe. Nawet operacja wywołania jest dla nich darmowa.

## Szczegóły Wykonania

### Ostrzeżenie
To nie jest sposób, w jaki wydajność działa w rzeczywistości. To są tylko zasady wymyślone dla tej gry, aby miała spójny i zrozumiały model czasu.
Prawdopodobnie zainteresujesz się tym tylko, jeśli chcesz hiper-optymalizować swój kod.

Podstawową jednostką czasu wykonania kodu jest "tick". Bez ulepszeń szybkości i mocy, wykonanie postępuje w tempie `400` ticków na sekundę.

Ogólnie, operacje, które łączą dwie wartości, takie jak `+, -, *, /, //, %, and, or, ...`, wykonują się w jednym ticku.
Pojedyncze wartości `-` i `not` są darmowe.
Gałąź `if` również wykonuje się w jednym ticku (dodatkowo do czasu potrzebnego na ocenę wyrażenia warunkowego).
Wywołania funkcji oraz odczyty i zapisy zmiennych są darmowe, ale definicje funkcji zajmują 1 tick.
Instrukcje `import` są darmowe.
Dostęp do zaimportowanego modułu z użyciem operatora `.` jest darmowy.
Jeśli funkcja lub moduł zostały przekazane przez argumenty lub przypisania zmiennych, ich użycie kosztuje 1 tick zamiast 0.
Pętle `for` i `while` zaczynają się od jednego ticka, ale ich iteracje są darmowe (nie licząc czasu na ocenę wyrażeń warunkowych/sekwencyjnych).
`return`, `break` i `continue` są wszystkie darmowe.
`pass` zajmuje jeden tick, więc można go używać do tworzenia precyzyjnych opóźnień.
Indeksowanie w strukturze danych zajmuje jeden tick dla operatora indeksu, a w przypadku dictionary lub set dodatkowe ticki zależą od rozmiaru klucza.

Liczba ticków potrzebna na wykonanie wbudowanych funkcji jest udokumentowana indywidualnie w dokumentacji każdej funkcji.
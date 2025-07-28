# Taktowanie
Jeśli naprawdę chcesz zoptymalizować swoje metody, musisz zrozumieć, jak mierzony jest czas w tej grze. To odblokowanie właśnie o tym jest.

## Nowe funkcje
Są dwie przydatne funkcje do mierzenia, ile czasu coś zajmuje:

`get_time()` zwraca czas w sekundach od początku gry.

`get_tick_count()` zwraca liczbę ticków wykonanych od początku wykonania.

Te dwie funkcje, jak również `quick_print()`, są całkowicie darmowe. Nawet operacja wywołania jest dla nich darmowa.

## Szczegóły wykonania

### Uwaga
Tak nie działa wydajność w prawdziwym świecie. To są tylko zasady wymyślone na potrzeby tej gry, aby mieć spójny i zrozumiały model czasu.
Prawdopodobnie będzie cię to obchodzić tylko wtedy, gdy będziesz chciał hiperoptymalizować swój kod.


Podstawową jednostką czasu wykonania kodu jest "tick". Bez ulepszeń prędkości i mocy, wykonanie postępuje z szybkością `400` ticks na sekundę.

Ogólnie rzecz biorąc, operacje, które łączą dwie wartości, takie jak `+, -, *, /, //, %, and, or, ...` zajmują jeden tick.
Pojedyncze `-` i `not` są darmowe.
Instrukcja `if` również zajmuje jeden tick (oprócz czasu potrzebnego na ocenę wyrażenia warunkowego).
Wywołania funkcji oraz odczyty i zapisy zmiennych są darmowe, ale definicje funkcji zajmują 1 tick.
Instrukcje `import` są darmowe.
Dostęp do zaimportowanego modułu za pomocą operatora `.` jest darmowy.
Jeśli funkcja lub moduł zostały przekazane przez argumenty lub przypisania zmiennych, ich użycie będzie kosztować 1 tick zamiast 0.
Pętle `for` i `while` zajmują jeden tick na start, ale iteracje są darmowe (nie licząc czasu na ocenę wyrażeń warunku/sekwencji).
`return`, `break` i `continue` są darmowe.
`pass` zajmuje jeden tick, więc można go używać do tworzenia precyzyjnych opóźnień.
Indeksowanie struktury danych zajmuje jeden tick dla operatora indeksu, a w przypadku słownika (dictionary) lub setu, dodatkowe ticki w zależności od rozmiaru klucza.

Liczba ticków, jaką zajmują wbudowane funkcje, jest udokumentowana indywidualnie w dokumentacji każdej funkcji.
# Import
Umieszczanie całego kodu w jednym pliku szybko staje się nie do opanowania. 
Instrukcje `import` pozwalają na importowanie funkcji i zmiennych globalnych z innego pliku.
Jak to działa w jednym zrzucie ekranu:
![](ImportsInOnePicture400)

Tutaj `import module2` uruchamia plik o nazwie `module2` i daje ci dostęp do wszystkich jego zmiennych globalnych.
Następnie możesz uzyskać dostęp do zmiennych i funkcji w zaimportowanym module za pomocą operatora `. `.
Więc w tym przykładzie `module2.print_x()` wywołuje `print_x()` z `module2`.

### Nie musisz czytać dalej

Możesz również przenieść zmienne globalne z zaimportowanego modułu do bieżącego zasięgu, w którym wykonywana jest instrukcja importu, używając składni `from`.

`from module2 import print_x
print_x()`
Importuje tylko określone zmienne globalne z `module2`.

lub

`from module2 import *
print_x()`
Importuje wszystkie zmienne globalne z `module2`.

To również importuje plik `module2`, ale zamiast uzyskiwać do niego dostęp przez zmienną o nazwie `module2`, rozpakowuje zmienne globalne z `module2` i przypisuje je bezpośrednio w zasięgu lokalnym.

Ta forma importu zazwyczaj nie jest zalecana, ponieważ nie działa dobrze, gdy dwa pliki importują się nawzajem, i możesz przypadkowo nadpisać zmienne w pliku importującym z powodu kolizji nazw. Bezpieczniej jest unikać składni `from`, jeśli nie wiesz, co robisz.

# Jak to naprawdę działa

## TLDR
Importy mogą być dość nieintuicyjne, ale większości problemów można uniknąć, trzymając się składni `import file` zamiast `from file import` i opakowując wszystko, co nie jest definicją globalną, w
`if __name__ == "__main__":`

## Efekty uboczne importu
Gdy importujesz plik po raz pierwszy, cały plik zostanie wykonany, a następnie uzyskasz dostęp do wszystkich zmiennych, które zostały zdefiniowane podczas jego wykonania.
Jeśli zaimportujesz ten sam plik ponownie, zwróci on po prostu moduł z pamięci podręcznej z pierwszego importu.

Oznacza to, że instrukcje importu mogą mieć efekty uboczne. Jeśli zaimportujesz plik, który wywołuje `harvest()`, faktycznie zbierze on plony podczas importu. Ale gdy zaimportujesz go ponownie, nie zbierze plonów, ponieważ plik jest uruchamiany tylko raz.

Jest sposób na uniknięcie takich efektów ubocznych za pomocą zmiennej `__name__`. Jest to zmienna, która jest automatycznie ustawiana na `"__main__"`, gdy plik jest uruchamiany bezpośrednio, i na nazwę pliku, gdy plik jest uruchamiany przez `import`.
Uznaje się za dobrą praktykę umieszczanie każdego kodu, który nie powinien być uruchamiany podczas importowania pliku, wewnątrz bloku `if __name__ == "__main__":`.

Powszechną strukturą plików w Pythonie jest umieszczanie kodu, który ma być wykonany po uruchomieniu pliku, w funkcji `main()`. W ten sposób masz wyraźne rozróżnienie między zmiennymi lokalnymi (zdefiniowanymi wewnątrz `main()`) a zmiennymi globalnymi, które można importować (zdefiniowanymi poza `main()`).

`a_global_variable = "global"

def main():
    a_local_variable = "local"
    # do things

if __name__ == "__main__":
    main()`

## Cykle importu
Co się stanie, jeśli plik `a` importuje plik `b`, a plik `b` importuje plik `a`?

plik `a`:
`import b
x = 0`

plik `b`:
`import a
def f():
    print(a.x)`

To zadziała bez problemu. Załóżmy, że żaden z dwóch plików nie jest jeszcze załadowany, a ktoś inny wykonuje `import a`.

-`a` wykonuje się do linii `import b`.
-`b` wykonuje się do linii `import a`.
-Moduł `a` już istnieje, ale nie zawiera `x`, ponieważ doszedł tylko do linii `import b`.
-`b` przechowuje odniesienie do w połowie załadowanego modułu `a` w zmiennej o nazwie `a`.
-`b` wykonuje instrukcję `def` i przechowuje funkcję `f()`.
-`a` kontynuuje działanie i inicjalizuje `x`.

Gdy ktoś wywoła `b.f()`, poprawnie wyświetli się `0`, ponieważ moduł `a`, do którego `b` ma odniesienie, jest już w pełni załadowany.

Teraz rozważ ten sam kod używający składni `from`.

plik `a`:
`from b import *
x = 0`

plik `b`:
`from a import *
def f():
    print(x)`

-`a` wykonuje się do linii `from b import *`.
-`b` wykonuje się do linii `from a import *`.
-Moduł `a` już istnieje, ale nie został jeszcze w pełni wykonany.
-`b` rozpakowuje wszystko, co aktualnie znajduje się w `a`, do swojego własnego zasięgu globalnego. W tym momencie `a` nie zawiera nic, ponieważ nie doszło jeszcze do linii `x = 0`, więc nic nie jest importowane.
-`b` wykonuje instrukcję `def` i przechowuje funkcję `f()`.
-`a` kontynuuje działanie i inicjalizuje `x`.

Jeśli ktoś teraz wywoła `b.f()`, otrzyma błąd, że `x` nie istnieje w bieżącym zasięgu. Dzieje się tak, ponieważ tym razem `b` nie ma odniesienia do wciąż ładującego się `a` i nie widzi definicji, które zostały dodane po imporcie.
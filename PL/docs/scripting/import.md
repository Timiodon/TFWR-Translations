# Import
Umieszczanie całego kodu w jednym pliku szybko staje się niewygodne.
Instrukcje `import` pozwalają na importowanie funkcji i zmiennych globalnych z innego pliku.

`import nazwa_pliku`

To najprostsza forma instrukcji importu. Daje ona dostęp do wszystkiego, co zdefiniowano w pliku o nazwie `nazwa_pliku`. Każde okno w grze to plik, a nazwa pliku to nazwa wyświetlana na górze okna.

Oto przykład z dwoma plikami:
Plik o nazwie helper:
`x = 0

def say_hello():
    print("cześć z helpera")`

Inny plik:
`import helper
helper.say_hello()
helper.x += 1`

Tutaj `import helper` uruchamia plik o nazwie `helper` i daje dostęp do wszystkich jego zmiennych globalnych.
Następnie można uzyskać dostęp do zmiennych i funkcji w zaimportowanym module za pomocą operatora `.`. 
Tak więc w tym przykładzie, `helper.say_hello()` wywołuje `say_hello()` wewnątrz pliku helper, a ostatnia linia inkrementuje globalną zmienną x.

Można również przenieść zmienne globalne z zaimportowanego modułu do bieżącego scope, w którym wykonana jest instrukcja importu, używając składni `from`.

`from helper import *`
Importuje wszystkie zmienne globalne z helpera.

lub

`from helper import say_hello`
Importuje tylko określone zmienne globalne z helpera.

To również importuje plik helper, ale zamiast uzyskiwać do niego dostęp przez zmienną o nazwie `helper`, rozpakowuje zmienne globalne z `helper` i przypisuje je bezpośrednio w lokalnym scope.

`from helper import say_hello
say_hello()`

Ta forma importu zazwyczaj nie jest zalecana, ponieważ nie działa dobrze, gdy dwa pliki importują się nawzajem, i można przypadkowo nadpisać zmienne w pliku importującym z powodu kolizji nazw.

# Jak to naprawdę działa

## TLDR
Importy mogą być dość nieintuicyjne, ale większości problemów można uniknąć, trzymając się składni `import plik` zamiast `from plik import` i opakowując wszystko, co nie jest definicją globalną, w
`if __name__ == "__main__":`

## Efekty uboczne importu
Gdy importujesz plik po raz pierwszy, cały plik zostanie wykonany, a następnie uzyskasz dostęp do wszystkich zmiennych, które zostały zdefiniowane podczas jego wykonania.
Jeśli zaimportujesz ten sam plik ponownie, zwróci on tylko moduł z pamięci podręcznej z pierwszego importu.

Oznacza to, że instrukcje importu mogą mieć efekty uboczne. Jeśli zaimportujesz plik, który wywołuje `harvest()`, faktycznie zbierze on plony podczas importu. Ale gdy zaimportujesz go ponownie, nie zbierze plonów ponownie, ponieważ plik jest uruchamiany tylko raz.

Istnieje sposób na uniknięcie takich efektów ubocznych za pomocą zmiennej `__name__`. Jest to zmienna, która jest automatycznie ustawiana na `"__main__"`, gdy plik jest uruchamiany bezpośrednio, i na nazwę pliku, gdy plik jest uruchamiany przez `import`.
Uważa się za dobrą praktykę umieszczanie kodu, którego nie chcesz uruchamiać, gdy plik jest importowany, wewnątrz bloku `if __name__ == "__main__":`.

Powszechną strukturą plików w Pythonie jest umieszczanie kodu, który powinien być wykonany po uruchomieniu pliku, w funkcji `main()`. W ten sposób masz wyraźne rozróżnienie między zmiennymi lokalnymi (zdefiniowanymi wewnątrz `main()`) a zmiennymi globalnymi, które można importować (zdefiniowanymi poza `main()`).

`a_global_variable = "globalna"

def main():
    a_local_variable = "lokalna"
    # rób rzeczy

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

To zadziała poprawnie. Powiedzmy, że żaden z dwóch plików nie jest jeszcze załadowany, a ktoś inny wykonuje `import a`.

-`a` działa do linii `import b`.
-`b` działa do linii `import a`.
-Moduł `a` już istnieje, ale nie zawiera `x`, ponieważ dotarł tylko do linii `import b`.
-`b` przechowuje odniesienie do w połowie załadowanego modułu `a` w zmiennej o nazwie `a`.
-`b` wykonuje instrukcję `def` i przechowuje funkcję `f()`.
-`a` kontynuuje działanie i inicjalizuje `x`.

Gdy ktoś wywoła `b.f()`, poprawnie wydrukuje `0`, ponieważ moduł `a`, do którego `b` ma odniesienie, jest teraz w pełni załadowany.

Teraz rozważmy ten sam kod z użyciem składni `from`.

plik `a`:
`from b import *
x = 0`

plik `b`:
`from a import *
def f():
    print(x)`

-`a` działa do linii `from b import *`.
-`b` działa do linii `from a import *`.
-Moduł `a` już istnieje, ale nie został jeszcze w pełni wykonany.
-`b` rozpakowuje wszystko, co aktualnie znajduje się w `a`, do swojego własnego globalnego scope. W tym momencie `a` nie zawiera nic, ponieważ nie dotarł jeszcze do linii `x = 0`, więc nic nie jest importowane.
-`b` wykonuje instrukcję `def` i przechowuje funkcję `f()`.
-`a` kontynuuje działanie i inicjalizuje `x`.

Jeśli ktoś teraz wywoła `b.f()`, otrzyma error, że `x` nie istnieje w bieżącym scope. Dzieje się tak, ponieważ tym razem `b` nie ma odniesienia do wciąż ładującego się `a` i nie widzi definicji, które zostały dodane po imporcie.
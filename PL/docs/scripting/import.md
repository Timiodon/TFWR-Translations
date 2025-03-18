# Import

Umieszczanie całego kodu w jednym pliku szybko staje się nie do opanowania.
`import` pozwala na importowanie funkcji i globalnych zmiennych z innego pliku.

`import filename`

To najprostsza forma polecenia importu. Daje ci dostęp do wszystkiego, co jest zdefiniowane w pliku o nazwie `filename`. Każde okno w grze to plik, a nazwa pliku to nazwa wyświetlana na górze okna.

Oto przykład z dwoma plikami:
Plik o nazwie helper:
`x = 0

def say_hello():
    print("hello from helper")`

Jakiś inny plik:
`import helper
helper.say_hello()
helper.x += 1`

Tutaj `import helper` uruchamia plik o nazwie `helper` i daje ci dostęp do wszystkich jego globalnych zmiennych.
Możesz wtedy uzyskać dostęp do zmiennych i funkcji wewnątrz importowanego modułu, używając operatora `.`.
Więc w tym przykładzie `helper.say_hello()` wywołuje `say_hello()` wewnątrz helper, a ostatnia linia zwiększa globalną zmienną x.

Możesz także przenieść globalne zmienne z importowanego modułu do aktualnego scope, w którym wykonywane jest polecenie importu, używając składni `from`.

`from helper import *`
Importuje wszystkie globalne zmienne z helper.

lub

`from helper import say_hello`
Importuje tylko określone globalne zmienne z helper.

To także importuje plik helper, ale zamiast uzyskiwać do niego dostęp przez zmienną o nazwie `helper`, rozpakowuje globalne zmienne z `helper` i przypisuje je bezpośrednio w lokalnym scope.

`from helper import say_hello
say_hello()`

Ta forma importu zwykle nie jest zalecana, ponieważ nie działa dobrze, gdy dwa pliki importują nawzajem, a także można przypadkowo nadpisać zmienne w pliku importującym z powodu konfliktu nazw.

# Jak to naprawdę działa

## TLDR
Importy mogą być dość nieintuicyjne, ale większości problemów można uniknąć, trzymając się składni `import file` zamiast `from file import` i zawijając wszystko, co nie jest globalną definicją, w
`if __name__ == "__main__":`

## Skutki uboczne importu
Za pierwszym razem, gdy importujesz plik, wykona on cały plik, a następnie daje ci dostęp do wszystkich zmiennych, które zostały zdefiniowane podczas jego wykonania.
Jeśli importujesz ten sam plik ponownie, po prostu zwróci on uprzednio załadowany moduł z pierwszego importu.

Oznacza to, że instrukcje importu mogą mieć skutki uboczne. Jeśli importujesz plik, który wywołuje `harvest()`, to naprawdę zostanie wykonane zbieranie podczas importowania. Ale gdy zaimportujesz go ponownie, nie wykona ona ponownie zbioru, ponieważ plik jest uruchamiany tylko raz.

Istnieje sposób, aby uniknąć takich skutków ubocznych za pomocą zmiennej `__name__`. Jest to zmienna, która automatycznie ustawia się na `"__main__"`, gdy plik jest uruchamiany bezpośrednio, oraz na nazwę pliku, gdy plik jest uruchamiany za pośrednictwem `import`.
Jest to uważane za dobrą praktykę, aby umieścić kod, który nie ma być wykonany, gdy plik jest importowany, wewnątrz bloku `if __name__ == "__main__":`.

Typowa struktura pliku w Pythonie polega na umieszczeniu kodu, który powinien być wykonany, gdy plik jest uruchamiany, w funkcji `main()`. Dzięki temu masz wyraźne rozgraniczenie między zmiennymi lokalnymi (zdefiniowanymi wewnątrz `main()`) a globalnymi, które można zaimportować (zdefiniowanymi poza `main()`).

`a_global_variable = "global"

def main():
    a_local_variable = "local"
    # wykonaj rzeczy

if __name__ == "__main__":
    main()`

## Cykl importu
Co się dzieje, gdy plik `a` importuje plik `b`, a plik `b` importuje plik `a`?

Plik `a`:
`import b
x = 0`

Plik `b`:
`import a
def f():
    print(a.x)`

To będzie działać poprawnie. Załóżmy, że żaden z dwóch plików nie jest jeszcze załadowany, a ktoś inny wykonuje `import a`.

-`a` wykonuje się do linii `import b`.
-`b` wykonuje się do linii `import a`.
-Moduł `a` już istnieje, ale nie zawiera jeszcze `x`, ponieważ osiągnięto tylko linię `import b`.
-`b` przechowuje referencję do częściowo załadowanego modułu `a` w zmiennej o nazwie `a`.
-`b` wykonuje instrukcję `def` i przechowuje funkcję `f()`.
-`a` kontynuuje działanie i inicjalizuje `x`.

Kiedy ktoś zadzwoni `b.f()`, poprawnie wydrukuje `0`, ponieważ moduł `a`, do którego `b` ma referencję, jest już w pełni załadowany.

Teraz rozważ ten sam kod za pomocą składni `from`.

Plik `a`:
`from b import *
x = 0`

Plik `b`:
`from a import *
def f():
    print(x)`

-`a` wykonuje się do linii `from b import *`.
-`b` wykonuje się do linii `from a import *`.
-Moduł `a` już istnieje, ale jeszcze nie został w pełni wykonany.
-`b` rozpakowuje wszystko, co jest obecnie w `a`, do swojej własnej globalnej przestrzeni. W tym momencie, `a` nie zawiera niczego, ponieważ jeszcze nie osiągnięto linii `x = 0`, więc nic nie zostaje zaimportowane.
-`b` wykonuje instrukcję `def` i przechowuje funkcję `f()`.
-`a` kontynuuje działanie i inicjalizuje `x`.

Jeśli ktoś teraz zadzwoni `b.f()`, otrzyma błąd mówiący, że `x` nie istnieje w bieżącym scope. To dlatego, że tym razem `b` nie ma referencji do wciąż ładowanego `a` i nie widzi definicji, które zostały dodane po imporcie.
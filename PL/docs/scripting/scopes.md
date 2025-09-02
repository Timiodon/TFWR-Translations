# Zasięgi nazw
Zasięgi określają, do których zmiennych można uzyskać dostęp i skąd. Zasięg to w zasadzie mapowanie nazw na wartości.
Działają one w zasadzie tak samo jak w Pythonie.

Istnieje zasięg globalny, a każda funkcja ma zasięg lokalny.
Gdy definiujesz zmienną, zostaje ona dodana do bieżącego zasięgu.
Wszystko poza definicją funkcji jest uważane za część zasięgu globalnego.

`x = 1`
Przypisuje wartość `1` do nazwy `x` w zasięgu globalnym.

Ta instrukcja `def` przypisuje funkcję do nazwy `f` w zasięgu globalnym.
`def f():
    `Przypisuje wartość `1` do nazwy `y` w lokalnym zasięgu `f`.`
    y = 1

    `Przypisuje funkcję do nazwy `g` w lokalnym zasięgu `f`.`
    def g():
        pass`

`f()`
Pobiera funkcję przechowywaną w `f` z zasięgu globalnego i ją wywołuje.

`print(y)`
Ta instrukcja `print` w zasięgu globalnym zgłasza błąd, ponieważ `y` nigdy nie zostało zadeklarowane w zasięgu globalnym, więc nie możemy go tutaj odczytać.
Istniało ono tylko w lokalnym zasięgu `f`.

## Słowo kluczowe `global`
Domyślnie wszystkie zmienne w funkcjach wiążą się z zasięgiem lokalnym, nawet jeśli zmienna o tej samej nazwie istnieje w zasięgu globalnym.

`x = 0

def f():
    x = 1
f()
print(x)`

Ten kod wyświetla `0`, ponieważ lokalna zmienna `x` wewnątrz `f` nie jest tą samą zmienną co globalna zmienna `x`, więc globalna zmienna `x` pozostaje niezmieniona. Jest to ważne, ponieważ w przeciwnym razie wywołanie funkcji mogłoby przypadkowo nadpisać zmienną globalną, która akurat ma taką samą nazwę jak zmienna lokalna tej funkcji.

Jeśli chcesz pisać do zmiennej globalnej, musisz to zrobić jawnie za pomocą słowa kluczowego `global`.

`x = 0

def f():
    global x
    x = 1
f()
print(x)`

W tym przykładzie `global x` wiąże `x` z globalną zmienną `x` zdefiniowaną powyżej. Teraz wyświetli się `1`.
Zauważ, że zmiana zmiennych globalnych jest zwykle pierwszym krokiem w kierunku kodu spaghetti, gdzie każda część programu wpływa na każdą inną część programu, więc nie nadużywaj tego.

## Pętle i instrukcje warunkowe
Pętle i instrukcje warunkowe nie tworzą własnych zasięgów, więc wszystko, co w nich zadeklarowano, może być nadal używane na zewnątrz.

`for i in range(3):
    pass
print(i)`

To wyświetli `2`, ponieważ ostatnia iteracja pętli `for` przypisała `2` do `i`.
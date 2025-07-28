# Zakresy nazw (Scopes)
Zakresy (scopes) określają, do których zmiennych można uzyskać dostęp z danego miejsca. Scope to w zasadzie mapowanie nazw na wartości.
Działają one zasadniczo tak samo jak w Pythonie.

Istnieje globalny scope, a każda funkcja ma swój lokalny scope.
Kiedy definiujesz zmienną, jest ona dodawana do bieżącego scope.
Wszystko poza definicją funkcji jest uważane za część globalnego scope.

`x = 1`
Przypisuje wartość `1` do nazwy `x` w globalnym scope.

Ta instrukcja `def` przypisuje funkcję do nazwy `f` w globalnym scope.
`def f():
    `Przypisuje wartość `1` do nazwy `y` w lokalnym scope funkcji `f`.`
    y = 1

    `Przypisuje funkcję do nazwy `g` w lokalnym scope funkcji `f`.`
    def g():
        pass`

`f()`
Pobiera funkcję przechowywaną w `f` z globalnego scope i ją wywołuje.

`print(y)`
Ta instrukcja print w globalnym scope zgłasza error, ponieważ `y` nigdy nie zostało zadeklarowane w globalnym scope, więc nie możemy go tutaj odczytać.
Istniało ono tylko w lokalnym scope funkcji `f`.

## Słowo kluczowe global
Domyślnie wszystkie zmienne w funkcjach są przypisywane do lokalnego scope, nawet jeśli zmienna o tej samej nazwie istnieje w globalnym scope.

`x = 0

def f():
    x = 1
f()
print(x)`

Ten kod drukuje `0`, ponieważ lokalne `x` wewnątrz `f` nie jest tą samą zmienną co globalne `x`, więc globalne `x` pozostaje niezmienione. Jest to ważne, ponieważ w przeciwnym razie wywołanie funkcji mogłoby przypadkowo nadpisać zmienną globalną, która akurat ma taką samą nazwę jak zmienna lokalna tej funkcji.

Jeśli chcesz pisać do zmiennej globalnej, musisz to zrobić jawnie, używając słowa kluczowego `global`.

`x = 0

def f():
    global x
    x = 1
f()
print(x)`

W tym przykładzie `global x` wiąże `x` z globalną zmienną `x` zdefiniowaną powyżej. Teraz kod wydrukuje `1`.
Zauważ, że zmiana zmiennych globalnych jest zazwyczaj pierwszym krokiem w kierunku kodu spaghetti, gdzie każda część programu wpływa na każdą inną część programu, więc nie nadużywaj go.

## Pętle i instrukcje warunkowe
Pętle i instrukcje warunkowe nie tworzą własnych scopes, więc wszystko, co w nich zadeklarowano, może być nadal używane na zewnątrz.

`for i in range(3):
    pass
print(i)`

To wydrukuje `2`, ponieważ ostatnia iteracja pętli `for` przypisała `2` do `i`.
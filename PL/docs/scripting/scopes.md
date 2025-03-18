# Zakresy Nazw
Zakresy określają, które zmienne mogą być dostępne z danego miejsca. Zakres to w zasadzie mapa od nazw do wartości.
Działają praktycznie tak samo jak w Pythonie.

Istnieje zakres globalny, a każda funkcja ma swój lokalny zakres.
Kiedy definiujesz zmienną, jest ona dodawana do aktualnego zakresu.
Wszystko, co znajduje się poza definicją funkcji, jest uznawane za część zakresu globalnego.

`x = 1`
Przypisuje wartość `1` do nazwy `x` w zakresie globalnym.

To stwierdzenie `def` przypisuje funkcję do nazwy `f` w zakresie globalnym.
`def f():
    `Przypisz wartość `1` do nazwy `y` w lokalnym zakresie `f`.`
    y = 1

    `Przypisz funkcję do nazwy `g` w lokalnym zakresie `f`.`
    def g():
        pass`

`f()`
Pobiera funkcję zapisaną w `f` z zakresu globalnego i wywołuje ją.

`print(y)`
To polecenie drukowania w zakresie globalnym wyrzuca błąd, ponieważ `y` nigdy nie zostało zadeklarowane w zakresie globalnym, więc nie możemy go tutaj odczytać.
Istniało ono tylko w lokalnym zakresie `f`.

## Słowo kluczowe global
Domyślnie wszystkie zmienne w funkcjach są powiązane z lokalnym zakresem, nawet jeśli zmienna o tej samej nazwie istnieje w zakresie globalnym.

`x == 0

def f():
    x = 1
f()
print(x)`

Ten kod drukuje `0`, ponieważ lokalne `x` wewnątrz `f` nie jest tą samą zmienną co globalne `x`, więc globalne `x` pozostaje niezmienione. To jest ważne, ponieważ w przeciwnym razie wywołanie funkcji mogłoby przypadkowo nadpisać globalną zmienną, która przypadkowo ma tę samą nazwę, co lokalna zmienna tej funkcji.

Jeśli chcesz pisać do zmiennej globalnej, musisz to zrobić jawnie, używając słowa kluczowego `global`.

`x == 0

def f():
    global x
    x = 1
f()
print(x)`

W tym przykładzie, `global x` wiąże `x` z globalną zmienną `x` zdefiniowaną powyżej. Teraz zostanie wydrukowane `1`.
Zwróć uwagę, że zmiana zmiennych globalnych to zazwyczaj pierwszy krok do "spaghetti code", gdzie każda część programu wpływa na każdą inną, więc nie nadużywaj tego.

## Pętle i rozgałęzienia
Pętle i rozgałęzienia nie tworzą własnych zakresów, więc wszystko zadeklarowane wewnątrz nich można nadal używać na zewnątrz.

`for i in range(3):
    pass
print(i)`

To wydrukuje `2`, ponieważ ostatnia iteracja pętli `for` przypisała `2` do `i`.
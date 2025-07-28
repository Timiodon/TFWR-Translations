# Zmienne
Zmienne można traktować jako nazwane pojemniki, które mogą przechowywać wartość.
Operator `=` służy do deklarowania zmiennej i przechowywania w niej wartości.

`nazwa_zmiennej = wartość`

Lewa strona operatora to nazwa zmiennej. Możesz nadać jej dowolną nazwę.
Prawa strona to wyrażenie, którego wynikowa wartość zostanie zapisana w zmiennej.

Zadeklaruj zmienną o nazwie `a` i zapisz w niej wartość `5`:
`a = 5`
Zadeklaruj zmienną o nazwie `b` i zapisz w niej wartość zwracaną przez `can_harvest()`:
`b = can_harvest()`

Nie myl operatora `=` z operatorem `==`.
Operator `==` sprawdza, czy dwie wartości są równe i zwraca `True` lub `False`.
Operator `=` przypisuje wartość po prawej stronie do nazwy po lewej stronie.

Po przypisaniu zmiennej możesz jej użyć w kodzie, aby pobrać wartość, którą przechowuje

`a = 5
for i in range(a):
	do_a_flip()`

Powyższa pętla jest wykonywana 5 razy, ponieważ `a` jest ustawione na `5`.
`i` w pętli `for` to także zmienna, której automatycznie przypisywana jest bieżąca wartość z sekwencji w każdej iteracji pętli. (Nie musi nazywać się `i`, możesz nadać jej dowolną prawidłową nazwę zmiennej.)

Zmienne pozwalają również zrobić to samo za pomocą pętli while:

`a = 5
i = 0
while i < a:
	do_a_flip()
	i = i + 1`

To robi to samo co pętla for powyżej. Musimy tylko ręcznie inkrementować i.
Zauważ, że aby inkrementować i, ustawiamy je na jego własną wartość plus `1`. Zmiana wartości zmiennej na podstawie jej poprzedniej wartości jest czymś bardzo powszechnym.
Można to skrócić za pomocą tych operatorów: `+=, -=, *=, /=, %=`

`i = i + 1` to to samo co `i += 1`
`a = a / 3` to to samo co `a /= 3`

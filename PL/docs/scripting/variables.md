# Zmienne
Zmienne można traktować jako nazwane pojemniki, które mogą przechowywać wartości.
Operator `=` jest używany do deklarowania zmiennej i przechowywania w niej wartości.

`variable_name = value`

Lewą stroną operatora jest nazwa zmiennej. Możesz nadać jej dowolną nazwę.
Po prawej stronie znajduje się wyrażenie, którego wynikowa wartość zostanie przechowana w zmiennej.

Zadeklaruj zmienną o nazwie `a` i przechowaj w niej wartość `5`:
`a = 5`
Zadeklaruj zmienną o nazwie `b` i przechowaj w niej wartość zwróconą przez `can_harvest()`:
`b = can_harvest()`

Nie myl operatora `=` z operatorem `==`. 
Operator `==` sprawdza, czy dwie wartości są równe i zwraca `True` lub `False`.
Operator `=` przypisuje wartość po prawej stronie do nazwy po lewej.

Po przypisaniu wartości do zmiennej można jej używać w kodzie, aby uzyskać wartość, którą zawiera.

`a = 5
for i in range(a):
	do_a_flip()`

Powyższa pętla jest wykonywana 5 razy, ponieważ `a` jest ustawione na `5`.
Zmienna `i` w pętli `for` jest również zmienną, której automatycznie przypisana jest aktualna wartość sekwencji podczas każdej iteracji pętli. (Nie musi być nazwana `i`, możesz nadać jej dowolną poprawną nazwę zmiennej.)

Zmienne pozwalają także robić to samo z pętlą while:

`a = 5
i = 0
while i < a:
	do_a_flip()
	i = i + 1`

To robi to samo, co pętla for powyżej. Musimy tylko ręcznie zwiększać wartość i.
Zauważ, że aby zwiększyć wartość i, ustawiamy ją jako jej własną wartość plus `1`. Zmiana wartości zmiennej na podstawie jej poprzedniej wartości jest czymś bardzo powszechnym. 
Można to skrócić za pomocą tych operatorów: `+=, -=, *=, /=, %=`

`i = i + 1` to to samo co `i += 1`
`a = a / 3` to to samo co `a /= 3`
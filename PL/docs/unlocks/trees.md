# Drzewa
[Drzewa](objects/tree) są lepszym sposobem na zdobycie drewna niż krzaki. Dają 5 drewna każde. Podobnie jak krzaki, można je sadzić na trawie lub ziemi.

Drzewa lubią mieć trochę przestrzeni, a sadzenie ich tuż obok siebie spowolni ich wzrost. Czas wzrostu jest podwajany dla każdego drzewa, które znajduje się na polu bezpośrednio na północ, wschód, zachód lub południe od niego. Więc jeśli posadzisz drzewa na każdym polu, będą rosły `2*2*2*2 = 16` razy dłużej.

<spoiler=pokaż> Operator `%` może być tu przydatny. Pamiętaj, że operator `%` zwraca resztę z dzielenia. Liczby parzyste podzielone przez `2` dają resztę `0`, a liczby nieparzyste podzielone przez `2` dają resztę `1`.
Więc możesz sprawdzić, czy liczba jest parzysta w ten sposób:

`def is_even(n):
	return n % 2 == 0`

Zwraca to `True`, jeśli n jest parzyste, i `False`, jeśli nie jest.
</spoiler>
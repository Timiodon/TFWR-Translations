# Drzewa
[Drzewa](objects/tree) to lepszy sposób na zdobycie drewna niż krzaki. Dają po 5 drewna. Podobnie jak krzaki, można je sadzić na trawie lub glebie.

Drzewa lubią mieć trochę przestrzeni, a sadzenie ich tuż obok siebie spowolni ich wzrost. Czas wzrostu jest podwajany za każde drzewo znajdujące się na polu bezpośrednio na północ, wschód, zachód lub południe od niego. Więc jeśli posadzisz drzewa na każdym polu, będą rosły `2*2*2*2 = 16` razy dłużej.

<spoiler=pokaż> Operator `%` może być tutaj przydatny. Pamiętaj, że operator `%` zwraca resztę z dzielenia. Liczby parzyste podzielone przez `2` dają resztę `0`, a liczby nieparzyste podzielone przez `2` dają resztę `1`.
Więc możesz sprawdzić, czy liczba jest parzysta w ten sposób:

`def is_even(n):
	return n % 2 == 0`

To zwraca `True`, jeśli n jest parzyste, i `False`, jeśli nie jest.
</spoiler>
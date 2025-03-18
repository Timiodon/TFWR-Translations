# Drzewa
[Drzewa](objects/tree) są lepszym sposobem na zdobycie drewna niż krzaki. Dają 5 drewna każde. Podobnie jak krzaki, można je sadzić na trawie lub glebie.

Drzewa lubią mieć trochę przestrzeni, a sadzenie ich tuż obok siebie spowalnia ich wzrost. Czas wzrostu podwaja się dla każdego drzewa znajdującego się na płytce bezpośrednio na północ, wschód, zachód lub południe od niego. Więc jeśli posadzisz drzewa na każdej płytce, będą rosły `2*2*2*2 = 16` razy dłużej.

<spoiler=show> Operator `%` może być tutaj przydatny. Pamiętaj, że operator `%` zwraca resztę z dzielenia. Liczby parzyste dzielone przez `2` mają resztę `0`, a liczby nieparzyste dzielone przez `2` mają resztę `1`.
Więc można sprawdzić, czy liczba jest parzysta w ten sposób:

`def is_even(n):
	return n % 2 == 0`

To zwraca `True`, jeśli n jest parzysta, i `False`, jeśli nie jest.
</spoiler>
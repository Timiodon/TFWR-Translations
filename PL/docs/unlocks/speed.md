# Ulepszenie prędkości
Prędkość wykonywania została podwojona. Problem polega na tym, że dron zbiera plony szybciej, niż trawa może rosnąć, co skutkuje brakiem zbiorów. Aby temu zaradzić, odblokowane zostały teraz gałęzie [if](docs/scripting/if.md) i funkcja [can_harvest](functions/can_harvest).

## Sprawdzanie przed zbiorem
Dotychczas mieliśmy tylko `True` i `False` jako warunki, co oczywiście nie jest zbyt użyteczne z `if`.

Nowa funkcja can_harvest() zapewnia lepszy warunek. `can_harvest()` zwraca `True`, jeśli roślina pod dronem może być zebrana, i `False` w przeciwnym wypadku.

`if can_harvest():
	#do something`

Powodem, dla którego można używać tej funkcji jako warunku, jest to, że zwraca ona wartość logiczną.

Wartość zwrotna zasadniczo oznacza, że po wykonaniu funkcjonalności wyrażenie wywołania funkcji ocenia się do zwróconej wartości.

Co się dzieje, gdy kod powyżej zostaje uruchomiony:
	- if zostaje uruchomiony
	- wywoływana jest `can_harvest()`
	- `can_harvest()` wykonuje swoje zadanie
	- `can_harvest()` zwraca `True` lub `False`
	- teraz ten zapis to `if True:` lub `if False:`
	- blok kodu jest wykonywany tylko, jeśli może zebrać plony

Teraz możemy użyć `if`, aby zapobiec zbyt wczesnemu zbieraniu przez drona.
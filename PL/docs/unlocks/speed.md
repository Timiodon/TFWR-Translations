# Ulepszenie prędkości
Prędkość wykonywania została podwojona. Problem w tym, że dron zbiera teraz plony szybciej, niż trawa może rosnąć, co skutkuje brakiem zbiorów. Aby sobie z tym poradzić, odblokowane zostały teraz instrukcje warunkowe [if](docs/scripting/if.md) oraz funkcja [can_harvest](functions/can_harvest).

## Sprawdzanie przed zbiorem
Do tej pory jako warunki mieliśmy tylko `True` i `False`, co oczywiście nie jest zbyt użyteczne z `if`. 

Nowa funkcja `can_harvest()` zapewnia lepszy warunek. `can_harvest()` zwraca `True`, jeśli roślina pod dronem może być zebrana, i `False` w przeciwnym razie.

`if can_harvest():
	#zrób coś`

Powodem, dla którego możesz używać tej funkcji jako warunku w ten sposób, jest to, że zwraca ona wartość logiczną (boolean).

Wartość zwracana zasadniczo oznacza, że po wykonaniu funkcjonalności, wyrażenie wywołania funkcji przyjmuje zwróconą wartość.

Co się dzieje, gdy powyższy kod jest uruchamiany:
	-uruchamiany jest if
	-wywoływana jest funkcja `can_harvest()`
	-`can_harvest()` robi swoje
	-`can_harvest()` zwraca `True` lub `False`
	-instrukcja wygląda teraz tak: `if True:` lub `if False:`
	-blok kodu jest wykonywany tylko wtedy, gdy można zebrać plon

Teraz możemy użyć `if`, aby zapobiec zbyt wczesnemu zbieraniu przez drona.
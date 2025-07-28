# Ulepszenie prędkości
Prędkość wykonywania została podwojona. Problem polega na tym, że dron zbiera teraz plony szybciej, niż trawa może rosnąć, co skutkuje brakiem zbiorów. Aby sobie z tym poradzić, odblokowano teraz instrukcje [if](docs/scripting/if.md) oraz funkcję [can_harvest](functions/can_harvest).

## Sprawdzanie przed zbiorem
Do tej pory jako warunki mieliśmy tylko `True` i `False`, co oczywiście nie jest zbyt przydatne z `if`.

Nowa funkcja `can_harvest()` zapewnia lepszy warunek. `can_harvest()` zwraca `True`, jeśli roślina pod dronem może być zebrana, a w przeciwnym razie `False`.

`if can_harvest():
	#zrób coś`

Powodem, dla którego można używać tej funkcji jako warunku, jest to, że zwraca ona wartość logiczną (boolean).

Wartość zwrotna w zasadzie oznacza, że po wykonaniu funkcjonalności, wyrażenie wywołania funkcji jest oceniane na zwróconą wartość.

Co się dzieje, gdy powyższy kod jest uruchamiany:
	-uruchamia się if
	-wywoływana jest funkcja `can_harvest()`
	-`can_harvest()` robi swoje
	-`can_harvest()` zwraca `True` lub `False`
	-instrukcja to teraz `if True:` lub `if False:`
	-blok kodu jest wykonywany tylko wtedy, gdy można zbierać plony

Teraz możemy użyć `if`, aby zapobiec zbyt wczesnemu zbieraniu plonów przez drona.
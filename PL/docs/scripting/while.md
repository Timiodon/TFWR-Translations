# Pętla While
Odblokowałeś pętlę `while` oraz wartości `True` i `False`. Pętla `while` wykonuje swoje ciało tak długo, jak warunek jest `True`.

`while warunek:
	#ciało pętli`

Nie martw się o tworzenie nieskończonych pętli. Opóźnienia w wykonaniu zapobiegną zawieszeniu się programu.

## Dla początkujących
Być może próbowałeś już umieścić kilka wywołań `harvest()` pod rząd:

`harvest()
harvest()
harvest()`

Pozwala to na zbieranie plonów kilka razy w jednym uruchomieniu programu.
Jednak fajnie byłoby zbierać plony więcej niż trzy razy, a pisanie tego samego kodu wielokrotnie jest złą praktyką.
Rozwiązaniem jest pętla.
Pętla pozwala na wielokrotne uruchamianie tego samego kodu.

Pętla while przyjmuje warunek, który jest wartością logiczną, która może być tylko w jednym z dwóch stanów: `True` lub `False`.
Taka wartość nazywana jest wartością logiczną (Boolean).

Pętla następnie wykonuje kod wewnątrz pętli, dopóki warunek nie jest Fałszywy.
Pętla while wygląda tak:

`while warunek:
	#ciało pętli
	#ciało pętli
	#...`
	
Gdzie musisz zastąpić „warunek” wartością logiczną, a `#ciało pętli` tym, co chcesz robić w pętli.

Dostępne są dwie stałe wartości logiczne. Stałe to wartości, które nigdy się nie zmieniają podczas działania programu.

Aby utworzyć stałą wartość logiczną, która jest zawsze `True`, możesz po prostu napisać `True`. Napisz `False` jako stałą wartość logiczną, która zawsze będzie `False`.
Więc możesz napisać


`while False:
	do_a_flip()`

lub

`while True:
	do_a_flip()`

Pierwszy przykład nigdy nie zrobi fikołka, a drugi będzie robił fikołki w nieskończoność (nieskończona pętla).

Normalnie tworzenie nieskończonej pętli jest złym pomysłem, ponieważ zawiesza program, ale w tej grze są opóźnienia między każdą iteracją pętli, więc dron będzie robił fikołki, dopóki ręcznie go nie zatrzymasz, naciskając ponownie przycisk wykonania.

Zauważ, jak linia po dwukropku jest wcięta. Wcięcia takie jak to służą do oddzielania bloków kodu.
Wystarczy nacisnąć Tab, aby dodać wcięcie, i Shift + Tab (lub Backspace), aby je usunąć.

Pętla będzie powtarzać wszystkie instrukcje z wcięciem po dwukropku.
Instrukcje po bloku z wcięciem zostaną wykonane po zakończeniu pętli.

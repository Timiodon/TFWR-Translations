# Pętla While
Odblokowałeś pętlę `while` oraz wartości `True` i `False`. Pętla `while` wykonuje swoje ciało tak długo, jak warunek jest `True`.

`while warunek:
	#ciało pętli`

Nie martw się o tworzenie pętli nieskończonych. Opóźnienia w wykonywaniu programu zapobiegną jego zawieszeniu.

## Dla początkujących
Być może próbowałeś już umieścić kilka wywołań `harvest()` pod rząd:

`harvest()
harvest()
harvest()`

Pozwala to na zebranie plonów kilka razy w jednym uruchomieniu programu. 
Jednakże, dobrze byłoby zebrać więcej niż trzy razy, a pisanie tego samego kodu wielokrotnie jest złą praktyką. 
Rozwiązaniem jest pętla. 
Pętla pozwala na wielokrotne uruchamianie tego samego kodu.

Pętla while przyjmuje warunek, który jest wartością logiczną mogącą przyjąć tylko jeden z dwóch stanów: `True` lub `False`. 
Taka wartość nazywana jest wartością boolowską.

Pętla wykonuje kod wewnątrz pętli, dopóki warunek nie stanie się `False`.
Pętla while wygląda tak:

`while warunek:
	#ciało pętli
	#ciało pętli
	#...`
	
Gdzie musisz zastąpić „warunek” wartością boolowską, a „#ciało pętli” tym, co chcesz robić w pętli.

Dostępne są dwie stałe wartości boolowskie. Stałe to wartości, które nigdy się nie zmieniają w trakcie programu.

Aby stworzyć stałą wartość boolowską, która jest zawsze `True`, możesz po prostu napisać `True`. Napisz `False` dla stałej wartości boolowskiej, która zawsze będzie `False`.
Więc możesz napisać albo


`while False:
	do_a_flip()`

albo

`while True:
	do_a_flip()`

Pierwsza nigdy nie wykona obrotu, a druga będzie je wykonywać w nieskończoność (pętla nieskończona). 

Zwykle tworzenie pętli nieskończonej jest złym pomysłem, ponieważ zawiesi program, ale w tej grze są opóźnienia między każdą iteracją pętli, więc dron będzie wykonywał obroty, dopóki ręcznie go nie zatrzymasz, ponownie naciskając przycisk wykonania.

Zauważ, że linia po dwukropku ma wcięcie. Wcięcia takie jak to są używane do oddzielania bloków kodu.
Po prostu naciśnij Tab, aby dodać wcięcie, i Shift + Tab (lub Backspace), aby je usunąć.

Pętla będzie powtarzać wszystkie instrukcje z wcięciem po dwukropku.
Instrukcje po bloku z wcięciem zostaną wykonane po zakończeniu pętli.
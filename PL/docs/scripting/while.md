[<- Pierwszy program](docs/first_program.md) <right>[Ulepszenie prędkości ->](docs/unlocks/speed.md)
---
# Pętla While
Odblokowałeś pętlę `while` oraz wartości `True` i `False`. Pętla `while` wykonuje swoje ciało tak długo, jak warunek jest `True`.

`while warunek:
	#ciało pętli`

Nie martw się o tworzenie pętli nieskończonych. Dron może utknąć, ale cała gra się nie zawiesi. Możesz po prostu zatrzymać program i spróbować ponownie.

## Dla początkujących
Być może próbowałeś już umieścić kilka wywołań `harvest()` pod rząd:

{{codeexample 
{
    "camera_position": {"x": 0, "y": 1.5, "z": 4},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 1, "y": 1},
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
do_a_flip()
#CODE
harvest()
harvest()
harvest()
}}
Pozwala to na zebranie plonów kilka razy w jednym uruchomieniu programu. 
Jednakże, dobrze byłoby zebrać więcej niż trzy razy, a pisanie tego samego kodu wielokrotnie szybko robi w programie bałagan.
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
	
Gdzie musisz zastąpić „warunek” wartością boolowską, a `#ciało pętli` tym, co chcesz robić w pętli.

Dostępne są dwie stałe wartości boolowskie. Stałe to wartości, które nigdy się nie zmieniają w trakcie programu.

Aby utworzyć stałą wartość logiczną, po prostu wpisz `True` lub `False`.
Możesz więc napisać:

{{codeexample 
{
    "camera_position": {"x": 0, "y": 1.5, "z": 4},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 1, "y": 1},
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
while False:
	do_a_flip()
}}
albo

{{codeexample 
{
    "camera_position": {"x": 0, "y": 1.5, "z": 4},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 1, "y": 1},
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
while True:
	do_a_flip()
}}
Pierwsza pętla nigdy nie wykona obrotu, a druga będzie wykonywać obroty bez końca (pętla nieskończona).

Zwykle tworzenie pętli nieskończonej jest złym pomysłem, ponieważ zawiesza program. W tej grze występują jednak opóźnienia między iteracjami, więc dron będzie wykonywał obroty, dopóki nie zatrzymasz go ręcznie, ponownie naciskając przycisk Wykonaj.

Zauważ, że wiersz po dwukropku ma wcięcie. Takie wcięcia służą do oddzielania bloków kodu.
Naciśnij Tab, aby dodać wcięcie, i Shift + Tab (lub Backspace), aby je usunąć. Jeśli zaznaczonych jest kilka wierszy, Tab i Shift + Tab zastosują zmianę do wszystkich.

Uwaga: jeśli grasz przez Steam, naciśnięcie Shift + Tab otworzy nakładkę Steam. Skrót do zmniejszania wcięcia możesz zmienić w opcjach gry, a skrót nakładki — w jej ustawieniach.

Tutaj `do_a_flip()` i `pet_the_piggy()` są wywoływane wielokrotnie, ponieważ znajdują się wewnątrz bloku `while` z wcięciem. `harvest()` nigdy się jednak nie uruchomi, ponieważ znajduje się po tym bloku.
{{codeexample 
{
    "camera_position": {"x": 0, "y": 1.5, "z": 4},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 1, "y": 1},
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
while True:
	do_a_flip()
	pet_the_piggy()
harvest()
}}

---

[Pętla For](docs/scripting/for.md)      [If](docs/scripting/if.md)      [Break](docs/scripting/break.md)      [Continue](docs/scripting/continue.md)      [Zewnętrzny edytor](docs/external_editor.md)

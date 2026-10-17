[<- Nawóz](docs/unlocks/fertilizer.md) <right>[Megafarma ->](docs/unlocks/megafarm.md)
---
# Labirynty
`Items.Weird_Substance` ma dziwny wpływ na krzaki. Jeśli dron znajduje się nad krzakiem i wywołasz `use_item(Items.Weird_Substance, amount)`, krzak wyrośnie w labirynt żywopłotów.
Rozmiar labiryntu zależy od ilości użytej `Items.Weird_Substance` (drugiego argumentu wywołania `use_item()`).
Bez ulepszeń labiryntu użycie `n` `Items.Weird_Substance` utworzy labirynt `n`x`n`. Każdy poziom ulepszenia labiryntu podwaja skarb, ale także ilość potrzebnej `Items.Weird_Substance`.
Aby więc utworzyć labirynt na całe pole:

{{codeexample 
{
    "camera_position": {"x": -1, "y": 2.4, "z": 5},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [{"item": "weird_substance", "n": 10}],
    "world_size": {"x": 4, "y": 4},
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 1,
    "seed": -1,
    "exclude_unlocks": ["watering"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
plant(Entities.Bush)
size = get_world_size()
substance = size * 2**(num_unlocked(Unlocks.Mazes) - 1)
use_item(Items.Weird_Substance, substance)
}}


Z jakiegoś powodu dron nie może przelatywać nad żywopłotami, chociaż nie wyglądają na takie wysokie.

Gdzieś w labiryncie ukryty jest skarb. Użyj `harvest()` na skarbie, aby otrzymać ilość złota równą powierzchni labiryntu. Na przykład labirynt 5x5 da 25 złota.

Jeśli użyjesz `harvest()` gdziekolwiek indziej, labirynt po prostu zniknie.

`get_entity_type()` jest równe `Entities.Treasure`, jeśli dron znajduje się nad skarbem, i `Entities.Hedge` wszędzie indziej w labiryncie.

Labirynty nie zawierają pętli, chyba że użyjesz ich ponownie (patrz niżej). Dron nie może więc wrócić do tej samej pozycji bez cofnięcia się tą samą drogą.

Możesz sprawdzić, czy jest ściana, próbując przez nią przejść. 
`move()` zwraca `True`, jeśli się udało, i `False` w przeciwnym razie.

`can_move()` można użyć do sprawdzenia, czy jest ściana, bez poruszania się.

{{codeexample 
{
    "camera_position": {"x": -1, "y": 2.4, "z": 5},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "items": [{"item": "weird_substance", "n": 10}],
    "world_size": {"x": 4, "y": 4},
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 100,
    "seed": 1,
    "exclude_unlocks": ["watering"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
move(East)
plant(Entities.Bush)
size = get_world_size()
substance = size * 2**(num_unlocked(Unlocks.Mazes) - 1)
use_item(Items.Weird_Substance, substance)
#CODE
quick_print(
    can_move(North), 
    can_move(East), 
    can_move(South), 
    can_move(West)
)
if move(North) and get_entity_type() == Entities.Treasure:
    harvest()
}}

Jeśli nie masz pojęcia, jak dotrzeć do skarbu, spójrz na Podpowiedź 1. Pokazuje ona, jak podejść do takiego problemu.

Użycie `measure()` w dowolnym miejscu labiryntu zwraca pozycję skarbu.
`x, y = measure()`

Dla dodatkowego wyzwania możesz użyć labiryntu ponownie, używając na skarbie tej samej ilości `Items.Weird_Substance`.
Spowoduje to zebranie skarbu i utworzenie nowego w losowym miejscu labiryntu.

Za każdym razem, gdy skarb jest przenoszony, niektóre ściany labiryntu mogą zostać losowo usunięte. Więc ponownie używane labirynty mogą zawierać pętle.

Zauważ, że pętle w labiryncie znacznie go utrudniają, ponieważ oznaczają, że możesz ponownie dotrzeć do tej samej lokalizacji bez cofania się.
Ponowne użycie labiryntu nie daje więcej złota niż zebranie i stworzenie nowego labiryntu.
To jest w 100% dodatkowe wyzwanie, które możesz po prostu pominąć.
Opłaca się to tylko wtedy, gdy dodatkowe informacje i skróty pomagają szybciej rozwiązać labirynt.

Skarb można przenieść do 300 razy. Późniejsze użycie na nim Dziwnej Substancji nie da ci już złota ani nie przeniesie skarbu.

<spoiler=pokaż podpowiedź 1>
Oto ogólne podejście do rozwiązania problemu:

Stwórz labirynt i wyobraź sobie, że jesteś dronem.

Pomyśl, jak próbowałbyś znaleźć skarb, gdybyś był w labiryncie.

Zapisz swoją strategię krok po kroku, aby ktoś inny mógł ją wykonać bez myślenia.

Teraz spróbuj przełożyć swoje kroki na kod.
</spoiler>
<spoiler=pokaż podpowiedź 2>
Dopóki nie ma pętli, wszystkie ściany tworzą jedną dużą połączoną ścianę. Jeśli położysz lewą rękę na ścianie i będziesz za nią podążać, poprowadzi cię przez cały labirynt.
To podejście wymaga bardzo mało kodu i nie musisz śledzić odwiedzonych miejsc. Wystarczy około 10 wierszy kodu.
{{codeexample 
{
    "camera_position": {"x": -1, "y": 2.4, "z": 5},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": false,
    "show_inventory": true,
    "show_output": true,
    "collapsing": false,
    "autoplay": true,
    "items": [{"item": "weird_substance", "n": 10}],
    "world_size": {"x": 4, "y": 4},
    "execution_speed": 2,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 1,
    "seed": -1,
    "exclude_unlocks": ["watering"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
plant(Entities.Bush)
size = get_world_size()
substance = size * 2**(num_unlocked(Unlocks.Mazes) - 1)
use_item(Items.Weird_Substance, substance)
#CODE
directions = [North, East, South, West]
index = 0
while get_entity_type() != Entities.Treasure:
    index = (index - 1) % 4
    for _ in range(4):
        if move(directions[index]):
            break
        index = (index + 1) % 4
do_a_flip()
harvest()
}}
</spoiler>
<spoiler=pokaż podpowiedź 3>
Zamiast poruszać dronem w bezwzględnych kierunkach, takich jak wschód czy zachód, przydatne może być poruszanie nim w kierunkach względnych, takich jak „skręć w prawo” lub „skręć w lewo”. W tym celu musisz śledzić kierunek, w którym dron się obecnie porusza. Dron tak naprawdę nigdy się nie obraca, ale w kodzie możesz utrzymywać jego „wirtualny” obrót.
Pomocna jest następująca sztuczka z indeksem:

{{codeexample 
{
    "camera_position": {"x": -1, "y": 1.8, "z": 5},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "items": [{"item": "weird_substance", "n": 10}],
    "world_size": {"x": 3, "y": 3},
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 1,
    "exclude_unlocks": ["watering"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
directions = [North, East, South, West]
index = 0
move(directions[index])

#skręć w prawo
index = (index + 1) % 4
move(directions[index])

#skręć w lewo
index = (index - 1) % 4
move(directions[index])
}}


Operator `% 4` pozwala obracać się „po okręgu”, dzięki czemu `3 (West) + 1` znów daje `0 (North)`, ponieważ `4 % 4 == 0`, a `-1 % 4 == 3`.</spoiler>
<spoiler=pokaż podpowiedź 4>
Jeśli nie potrafisz tego rozwiązać, zawsze możesz uprościć problem, stosując mniej wydajne podejście.
Rozwiązanie labiryntu `1`x`1` jest banalne.</spoiler>

---

[Statystyki](docs/stats.md)      [Listy](docs/scripting/lists.md)      [Słowniki](docs/scripting/dicts.md)      [Krotki](docs/scripting/tuples.md)

[harvest()](functions/harvest)      [plant()](functions/plant)      [can_move()](functions/can_move)      [move()](functions/move)      [use_item()](functions/use_item)

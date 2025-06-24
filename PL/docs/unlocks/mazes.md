# Labirynty
`Items.Weird_Substance`, która jest pozyskiwana przez [nawóz](docs/unlocks/fertilizer.md) rośliny, ma dziwny efekt na krzaki. Jeśli dron znajduje się nad krzakiem i wywołasz `use_item(Items.Weird_Substance, amount)`, krzak przemieni się w labirynt z żywopłotów. 
Wielkość labiryntu zależy od ilości użytej `Items.Weird_Substance` (drugi argument wywołania `use_item()`).
Bez ulepszeń labiryntów, użycie `n` `Items.Weird_Substance` spowoduje powstanie labiryntu `n`x`n`. Każdy poziom ulepszenia labiryntu podwaja ilość skarbu, ale także podwaja ilość potrzebnej `Items.Weird_Substance`. 
Tak więc, aby stworzyć pełny labirynt na polu:

`plant(Entities.Bush)
n_substance = get_world_size() * 2**(num_unlocked(Unlocks.Mazes) - 1)
use_item(Items.Weird_Substance, n_substance)`

Z jakiegoś powodu dron nie może latać nad żywopłotami, mimo że nie wyglądają one tak wysoko.

W żywopłocie ukryty jest skarb. Użyj `harvest()` na skarbie, aby otrzymać złoto równe powierzchni labiryntu. (Na przykład, labirynt 5x5 przyniesie 25 złota.)

Jeśli użyjesz `harvest()` w jakimkolwiek innym miejscu, labirynt po prostu zniknie.

`get_entity_type()` jest równe `Entities.Treasure` jeśli dron znajduje się nad skarbem, a `Entities.Hedge` w pozostałych miejscach labiryntu.

Labirynty nie zawierają żadnych pętli, chyba że ponownie wykorzystasz labirynt (zobacz poniżej, jak ponownie wykorzystać labirynt). Tak więc nie ma sposobu, aby dron wrócił do tej samej pozycji bez cofnięcia się.

Możesz sprawdzić, czy jest ściana, próbując przez nią przejść.
`move()` zwraca `True` jeśli się udało i `False` w przeciwnym razie.

Jeśli nie masz pojęcia, jak dotrzeć do skarbu, spójrz na Wskazówkę 1. Pokazuje, jak podejść do tego problemu.

Dla dodatkowego wyzwania możesz również ponownie użyć labiryntu, używając tej samej ilości `Items.Weird_Substance` na skarb ponownie. 
To zwiększy ilość złota w skarbie o jeden pełny labirynt i przeniesie go w losowe miejsce w labiryncie.

Użycie `measure()` na skarbie zwraca pozycję, na którą się przemieści, jako krotkę.
`next_x, next_y = measure()`

Za każdym razem, gdy skarb jest przemieszczany, może zostać usunięta losowa ściana z labiryntu. Więc ponownie wykorzystane labirynty mogą zawierać pętle.

Zauważ, że pętle w labiryncie znacząco zwiększają trudność, ponieważ oznacza to, że możesz dotrzeć do tej samej lokalizacji bez cofania się.
Ponowne użycie labiryntu nie da ci więcej złota niż po prostu zbieranie i tworzenie nowego labiryntu.
To w 100% dodatkowe wyzwanie, które możesz po prostu ominąć.
To jest warte tylko wtedy, gdy dodatkowe informacje i skróty pomogą ci szybciej rozwiązać labirynt.

Ten sam labirynt można rozwiązać maksymalnie 300 razy. To odpowiada 299 przemieszczeniom. Po tym użycie dziwnej substancji na skarbie nie zwiększy już ilości złota, a `measure()` zwróci `None`.

<spoiler=show hint 1>Oto ogólne podejście do rozwiązania problemu:

Stwórz labirynt i wyobraź sobie, że jesteś dronem.

Pomyśl o tym, jak spróbowałbyś znaleźć skarb będąc w labiryncie.

Zapisz swoją strategię krok po kroku, tak aby ktoś inny mógł ją wykonać bez zastanawiania się.

Teraz spróbuj przetłumaczyć swoje kroki na kod.
</spoiler>
<spoiler=show hint 2>Dopóki nie ma pętli: Wszystkie ściany są jedną dużą połączoną ścianą. Jeśli podążysz za ścianą, poprowadzi cię przez cały labirynt.
To podejście wymaga bardzo mało kodu i nie musisz śledzić miejsc, w których już byłeś. Potrzebujesz tylko około 10 linii kodu.</spoiler>
<spoiler=show hint 3>Zamiast poruszać dronem w absolutnych kierunkach jak wschód czy zachód, może być bardzo przydatne poruszać dronem w kierunkach względnych, takich jak "skręć w prawo" lub "skręć w lewo". Aby to zrobić, musisz śledzić, w którą stronę dron aktualnie się porusza. Dron nigdy się faktycznie nie obraca, ale możesz nadal utrzymać "wirtualną" rotację w kodzie.
Następująca sztuczka z indeksami jest tutaj pomocna:

`directions = [North, East, South, West]
index = 0`

Użyj `% 4` aby umożliwić obroty "wokół koła", tak że po `West` wraca do `North`.
`# skręć w prawo
index = (index + 1) % 4`

`# skręć w lewo
index = (index - 1) % 4

move(directions[index])`</spoiler>
<spoiler=show hint 4>Jeśli nie możesz tego rozwiązać, zawsze możesz zrobić to mniej efektywnie. 
Rozwiązanie labiryntu `1`x`1` jest trywialne.</spoiler>
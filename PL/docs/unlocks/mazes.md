# Labirynty
`Items.Weird_Substance`, którą uzyskuje się poprzez [nawożenie](docs/unlocks/fertilizer.md) roślin, ma dziwny wpływ na krzaki. Jeśli dron znajduje się nad krzakiem i wywołasz `use_item(Items.Weird_Substance, ilość)`, krzak wyrośnie w labirynt żywopłotów.
Rozmiar labiryntu zależy od ilości użytej `Items.Weird_Substance` (drugi argument wywołania `use_item()`).
Bez ulepszeń labiryntu, użycie `n` `Items.Weird_Substance` spowoduje powstanie labiryntu `n`x`n`. Każdy poziom ulepszenia labiryntu podwaja skarb, ale także podwaja ilość potrzebnej `Items.Weird_Substance`. 
Więc, aby stworzyć labirynt na całe pole:

`plant(Entities.Bush)
substance = get_world_size() * 2**(num_unlocked(Unlocks.Mazes) - 1)
use_item(Items.Weird_Substance, substance)`


Z jakiegoś powodu dron nie może przelatywać nad żywopłotami, chociaż nie wyglądają na takie wysokie.

Gdzieś w żywopłocie ukryty jest skarb. Użyj `harvest()` na skarbie, aby otrzymać złoto równe powierzchni labiryntu. (Na przykład, labirynt 5x5 da 25 złota.)

Jeśli użyjesz `harvest()` gdziekolwiek indziej, labirynt po prostu zniknie.

`get_entity_type()` jest równe `Entities.Treasure`, jeśli dron znajduje się nad skarbem, i `Entities.Hedge` wszędzie indziej w labiryncie.

Labirynty nie zawierają pętli, chyba że ponownie użyjesz labiryntu (zobacz poniżej, jak ponownie użyć labiryntu). Więc dron nie może ponownie znaleźć się w tej samej pozycji bez cofania się.

Możesz sprawdzić, czy jest ściana, próbując przez nią przejść. 
`move()` zwraca `True`, jeśli się udało, i `False` w przeciwnym razie.

`can_move()` można użyć do sprawdzenia, czy jest ściana, bez poruszania się.

Jeśli nie masz pojęcia, jak dotrzeć do skarbu, spójrz na Podpowiedź 1. Pokazuje ona, jak podejść do takiego problemu.

Użycie `measure()` w dowolnym miejscu labiryntu zwraca pozycję skarbu.
`x, y = measure()`

Dla dodatkowego wyzwania możesz również ponownie użyć labiryntu, używając tej samej ilości `Items.Weird_Substance` na skarbie ponownie. 
To zbierze skarb i stworzy nowy w losowej pozycji w labiryncie.

Za każdym razem, gdy skarb jest przenoszony, niektóre ściany labiryntu mogą zostać losowo usunięte. Więc ponownie używane labirynty mogą zawierać pętle.

Zauważ, że pętle w labiryncie znacznie go utrudniają, ponieważ oznaczają, że możesz ponownie dotrzeć do tej samej lokalizacji bez cofania się.
Ponowne użycie labiryntu nie daje więcej złota niż zebranie i stworzenie nowego labiryntu.
To jest w 100% dodatkowe wyzwanie, które możesz po prostu pominąć.
Opłaca się to tylko wtedy, gdy dodatkowe informacje i skróty pomagają szybciej rozwiązać labirynt.

Skarb może być przenoszony do 300 razy. Po tym czasie użycie dziwnej substancji na skarbie nie będzie już ani zwiększać w nim złota, ani go przemieszczać.

<spoiler=pokaż podpowiedź 1>Oto ogólne podejście do rozwiązania problemu:

Stwórz labirynt i wyobraź sobie, że jesteś dronem.

Pomyśl, jak próbowałbyś znaleźć skarb, gdybyś był w labiryncie.

Zapisz swoją strategię krok po kroku, aby ktoś inny mógł ją wykonać bez myślenia.

Teraz spróbuj przetłumaczyć swoje kroki na kod.
</spoiler>
<spoiler=pokaż podpowiedź 2>Dopóki nie ma pętli: wszystkie ściany to tak naprawdę jedna duża połączona ściana. Jeśli będziesz podążać wzdłuż ściany, poprowadzi cię ona przez cały labirynt.
To podejście wymaga bardzo mało kodu i nie musisz śledzić, gdzie już byłeś. Wystarczy około 10 linii kodu.</spoiler>
<spoiler=pokaż podpowiedź 3>Zamiast poruszać dronem w absolutnych kierunkach, takich jak wschód czy zachód, może być bardzo przydatne poruszanie dronem we względnych kierunkach, takich jak „skręć w prawo” lub „skręć w lewo”. Aby to zrobić, musisz śledzić, w którym kierunku dron się aktualnie porusza. Dron tak naprawdę nigdy się nie obraca, ale nadal możesz utrzymywać „wirtualny” obrót w kodzie.
Pomocna w tym jest następująca sztuczka z indeksem:

`directions = [North, East, South, West]
index = 0`

Użyj `% 4`, aby umożliwić obrót „wokół koła”, tak aby po `West` zawijał się z powrotem do `North`.
`# skręć w prawo
index = (index + 1) % 4`

`# skręć w lewo
index = (index - 1) % 4

move(directions[index])`</spoiler>
<spoiler=pokaż podpowiedź 4>Jeśli nie możesz tego rozwiązać, zawsze możesz ułatwić sobie życie i zrobić to mniej wydajnie. 
Rozwiązanie labiryntu `1`x`1` jest banalne.</spoiler>
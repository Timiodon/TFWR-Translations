# Labirynty
`Items.Weird_Substance`, zdobywana poprzez [nawożenie](docs/unlocks/fertilizer.md) roślin, ma dziwny wpływ na krzaki. Jeśli dron jest nad krzakiem i wywołasz `use_item(Items.Weird_Substance, amount)`, krzak wyrośnie w labirynt z żywopłotów.
Rozmiar labiryntu zależy od ilości użytego `Items.Weird_Substance` (drugi argument wywołania `use_item()`).
Bez ulepszeń labiryntu, użycie `n` `Items.Weird_Substance` stworzy labirynt o wymiarach `n`x`n`. Każdy poziom ulepszenia labiryntu podwaja skarb, ale podwaja też wymaganą ilość `Items.Weird_Substance`. 
Więc, aby stworzyć labirynt na całe pole:

`plant(Entities.Bush)
substance = get_world_size() * 2**(num_unlocked(Unlocks.Mazes) - 1)
use_item(Items.Weird_Substance, substance)`


Z jakiegoś powodu dron nie potrafi latać nad żywopłotami, chociaż nie wyglądają na takie wysokie.

Gdzieś w żywopłocie ukryty jest skarb. Użyj `harvest()` na skarbie, aby otrzymać złoto równe powierzchni labiryntu. (Na przykład, labirynt 5x5 da 25 złota.)

Jeśli użyjesz `harvest()` w dowolnym innym miejscu, labirynt po prostu zniknie.

`get_entity_type()` jest równe `Entities.Treasure`, jeśli dron jest nad skarbem, i `Entities.Hedge` w każdym innym miejscu labiryntu.

Labirynty nie zawierają pętli, chyba że użyjesz labiryntu ponownie (zobacz niżej, jak to zrobić). Więc nie ma możliwości, aby dron znalazł się ponownie w tej samej pozycji bez cofania się.

Możesz sprawdzić, czy jest ściana, próbując przez nią przejść. 
`move()` zwraca `True`, jeśli się udało, i `False` w przeciwnym razie.

Jeśli nie masz pomysłu, jak dotrzeć do skarbu, spójrz na Podpowiedź 1. Pokazuje, jak podejść do tego typu problemu.


Dla dodatkowego wyzwania możesz również ponownie użyć labiryntu, używając tej samej ilości `Items.Weird_Substance` na skarbie.
Zwiększy to ilość złota w skarbie o wartość jednego pełnego labiryntu i przeniesie go w losowe miejsce w labiryncie.

Użycie `measure()` na skarbie zwraca pozycję, na którą się przeniesie, jako krotkę (tuple).
`next_x, next_y = measure()`

Za każdym razem, gdy skarb jest przenoszony, losowa ściana może zostać usunięta z labiryntu. Więc ponownie użyte labirynty mogą zawierać pętle.

Zauważ, że pętle w labiryncie znacznie go utrudniają, ponieważ oznaczają, że możesz dotrzeć do tej samej lokalizacji ponownie bez cofania się.
Ponowne użycie labiryntu nie daje więcej złota niż zebranie skarbu i stworzenie nowego labiryntu.
To jest w 100% dodatkowe wyzwanie, które możesz po prostu pominąć.
Opłaca się to tylko wtedy, gdy dodatkowe informacje i skróty pomogą ci szybciej rozwiązać labirynt.

Ten sam labirynt można rozwiązać maksymalnie 300 razy. Odpowiada to 299 przeniesieniom. Po tym czasie użycie Weird Substance na skarbie nie zwiększy już ilości złota, a `measure()` zwróci `None`.

<spoiler=show hint 1>Oto ogólne podejście do rozwiązania problemu:

Stwórz labirynt i wyobraź sobie, że jesteś dronem.

Pomyśl, jak próbowałbyś znaleźć skarb, będąc w labiryncie.

Zapisz swoją strategię krok po kroku, aby ktoś inny mógł ją wykonać bez myślenia.

Teraz spróbuj przetłumaczyć swoje kroki na kod.
</spoiler>
<spoiler=show hint 2>Dopóki nie ma pętli: wszystkie ściany są tak naprawdę jedną dużą, połączoną ścianą. Jeśli będziesz podążać wzdłuż ściany, poprowadzi cię ona przez cały labirynt.
To podejście wymaga bardzo mało kodu i nie musisz śledzić, gdzie już byłeś. Wystarczy około 10 linijek kodu.</spoiler>
<spoiler=show hint 3>Zamiast poruszać dronem w kierunkach bezwzględnych, jak wschód czy zachód, bardzo przydatne może być poruszanie nim w kierunkach względnych, jak „skręć w prawo” czy „skręć w lewo”. Aby to zrobić, musisz śledzić, w którą stronę dron się aktualnie porusza. Dron tak naprawdę nigdy się nie obraca, ale w kodzie możesz zachować „wirtualny” obrót.
Pomocna w tym jest następująca sztuczka z indeksem:

`directions = [North, East, South, West]
index = 0`

Użyj `% 4`, aby umożliwić obrót „w kółko”, tak aby po `West` wracało do `North`.
`# skręć w prawo
index = (index + 1) % 4`

`# skręć w lewo
index = (index - 1) % 4

move(directions[index])`</spoiler>
<spoiler=show hint 4>Jeśli nie potrafisz tego rozwiązać, zawsze możesz ułatwić sobie życie i zrobić to mniej wydajnie. 
Rozwiązanie labiryntu `1`x`1` jest trywialne.</spoiler>
# Labirynty
`Items.Weird_Substance`, którą uzyskuje się poprzez [nawożenie](docs/unlocks/fertilizer.md) roślin, ma dziwny wpływ na krzaki. Jeśli dron znajduje się nad krzakiem i wywołasz `use_item(Items.Weird_Substance, amount)`, krzak wyrośnie na labirynt z żywopłotów.
Rozmiar labiryntu zależy od ilości użytej `Items.Weird_Substance` (drugi argument wywołania `use_item()`).
Bez ulepszeń labiryntu, użycie `n` `Items.Weird_Substance` da w wyniku labirynt `n`x`n`. Każdy poziom ulepszenia labiryntu podwaja skarb, ale podwaja też ilość potrzebnej `Items.Weird_Substance`. 
Więc, aby stworzyć labirynt na całe pole:

`plant(Entities.Bush)
substance = get_world_size() * 2**(num_unlocked(Unlocks.Mazes) - 1)
use_item(Items.Weird_Substance, substance)`


Z jakiegoś powodu dron nie potrafi latać nad żywopłotami, chociaż nie wyglądają na takie wysokie.

Gdzieś w żywopłocie ukryty jest skarb. Użyj `harvest()` na skarbie, aby otrzymać złoto równe powierzchni labiryntu. (Na przykład, labirynt 5x5 da 25 złota.)

Jeśli użyjesz `harvest()` w dowolnym innym miejscu, labirynt po prostu zniknie.

`get_entity_type()` jest równe `Entities.Treasure`, jeśli dron jest nad skarbem, i `Entities.Hedge` w każdym innym miejscu labiryntu.

Labirynty nie zawierają pętli, chyba że ponownie użyjesz labiryntu (zobacz poniżej, jak to zrobić). Więc nie ma możliwości, aby dron ponownie znalazł się w tej samej pozycji bez cofania się.

Możesz sprawdzić, czy jest tam ściana, próbując się przez nią poruszyć. 
`move()` zwraca `True`, jeśli się udało, a w przeciwnym razie `False`.

`can_move()` można użyć do sprawdzenia, czy jest ściana, bez poruszania się.

Jeśli nie masz pomysłu, jak dotrzeć do skarbu, spójrz na Wskazówkę 1. Pokazuje ona, jak podejść do takiego problemu.

Użycie `measure()` w dowolnym miejscu labiryntu zwraca pozycję skarbu.
`x, y = measure()`

Dla dodatkowego wyzwania możesz również ponownie użyć labiryntu, używając tej samej ilości `Items.Weird_Substance` na skarbie. 
Zwiększy to ilość złota w skarbie o wartość całego labiryntu i przeniesie go w losowe miejsce w labiryncie.

Za każdym razem, gdy skarb jest przenoszony, losowa ściana może zostać usunięta z labiryntu. Dlatego ponownie użyte labirynty mogą zawierać pętle.

Zauważ, że pętle w labiryncie znacznie go utrudniają, ponieważ oznacza to, że możesz ponownie dotrzeć do tej samej lokalizacji bez cofania się.
Ponowne użycie labiryntu nie daje więcej złota niż zebranie i stworzenie nowego labiryntu.
To jest w 100% dodatkowe wyzwanie, które możesz po prostu pominąć.
Opłaca się to tylko wtedy, gdy dodatkowe informacje i skróty pomogą ci szybciej rozwiązać labirynt.

Ten sam labirynt można rozwiązać maksymalnie 300 razy. Odpowiada to 299 przeniesieniom. Po tym czasie użycie weird substance na skarbie nie zwiększy już w nim ilości złota, a `measure()` zwróci `None`.

<spoiler=pokaż wskazówkę 1>Oto ogólne podejście do rozwiązania tego problemu:

Stwórz labirynt i wyobraź sobie, że jesteś dronem.

Pomyśl, jak próbowałbyś znaleźć skarb, gdybyś był w labiryncie.

Zapisz swoją strategię krok po kroku, aby ktoś inny mógł ją wykonać bez zastanawiania się.

Teraz spróbuj przetłumaczyć swoje kroki na kod.
</spoiler>
<spoiler=pokaż wskazówkę 2>Dopóki nie ma pętli: wszystkie ściany to tak naprawdę jedna duża, połączona ściana. Jeśli będziesz podążać wzdłuż ściany, poprowadzi cię ona przez cały labirynt.
To podejście wymaga bardzo mało kodu i nie musisz śledzić, gdzie już byłeś. Wystarczy około 10 linii kodu.</spoiler>
<spoiler=pokaż wskazówkę 3>Zamiast poruszać dronem w absolutnych kierunkach, takich jak wschód czy zachód, bardzo przydatne może być poruszanie dronem w kierunkach względnych, takich jak „skręć w prawo” lub „skręć w lewo”. Aby to zrobić, musisz śledzić, w którą stronę dron się aktualnie porusza. Dron tak naprawdę nigdy się nie obraca, ale nadal możesz utrzymywać „wirtualny” obrót w kodzie.
Poniższa sztuczka z indeksem jest do tego pomocna:

`directions = [North, East, South, West]
index = 0`

Użyj `% 4`, aby umożliwić obrót „w kółko”, tak aby po `West` zawijał z powrotem do `North`.
`# skręć w prawo
index = (index + 1) % 4`

`# skręć w lewo
index = (index - 1) % 4

move(directions[index])`</spoiler>
<spoiler=pokaż wskazówkę 4>Jeśli nie możesz go rozwiązać, zawsze możesz ułatwić sobie życie i zrobić to mniej wydajnie. 
Rozwiązanie labiryntu `1`x`1` jest banalne.</spoiler>
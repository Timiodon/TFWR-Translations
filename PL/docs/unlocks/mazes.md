# Labirynty
`Items.Weird_Substance`, które zdobywa się poprzez [nawożenie](docs/unlocks/fertilizer.md) roślin, ma dziwny wpływ na krzaki. Jeśli dron jest nad krzakiem i wywołasz `use_item(Items.Weird_Substance, amount)`, krzak wyrośnie w labirynt żywopłotów.
Rozmiar labiryntu zależy od ilości użytej `Items.Weird_Substance` (drugi argument wywołania `use_item()`).
Bez ulepszeń labiryntu, użycie `n` `Items.Weird_Substance` spowoduje powstanie labiryntu `n`x`n`. Każdy poziom ulepszenia labiryntu podwaja skarb, ale także podwaja ilość potrzebnej `Items.Weird_Substance`.
Więc aby stworzyć labirynt na całe pole:

`plant(Entities.Bush)
n_substance = get_world_size() * 2**(num_unlocked(Unlocks.Mazes) - 1)
use_item(Items.Weird_Substance, n_substance)`


Z jakiegoś powodu dron nie może przelatywać nad żywopłotami, chociaż nie wyglądają na takie wysokie.

Gdzieś w żywopłocie ukryty jest skarb. Użyj `harvest()` na skarbie, aby otrzymać złoto równe powierzchni labiryntu. (Na przykład, labirynt 5x5 da 25 złota.)

Jeśli użyjesz `harvest()` gdziekolwiek indziej, labirynt po prostu zniknie.

`get_entity_type()` jest równe `Entities.Treasure`, jeśli dron jest nad skarbem, i `Entities.Hedge` wszędzie indziej w labiryncie.

Labirynty nie zawierają żadnych pętli, chyba że ponownie użyjesz labiryntu (zobacz poniżej, jak ponownie użyć labiryntu). Więc nie ma możliwości, aby dron znalazł się ponownie w tej samej pozycji bez cofania się.

Możesz sprawdzić, czy jest ściana, próbując przez nią przejść.
`move()` zwraca `True`, jeśli się powiodło, i `False` w przeciwnym razie.

Jeśli nie masz pojęcia, jak dostać się do skarbu, spójrz na Wskazówkę 1. Pokazuje ona, jak podejść do takiego problemu.


Dla dodatkowego wyzwania możesz również ponownie użyć labiryntu, używając tej samej ilości `Items.Weird_Substance` na skarbie ponownie.
Zwiększy to ilość złota w skarbie o jeden pełny labirynt i przeniesie go w losowe miejsce w labiryncie.

Użycie `measure()` na skarbie zwraca pozycję, do której się przeniesie, jako krotkę.
`next_x, next_y = measure()`

Za każdym razem, gdy skarb jest przenoszony, losowa ściana może zostać usunięta z labiryntu. Więc ponownie użyte labirynty mogą zawierać pętle.

Zauważ, że pętle w labiryncie sprawiają, że jest on znacznie trudniejszy, ponieważ oznacza to, że możesz dostać się do tej samej lokalizacji ponownie bez cofania się.
Ponowne użycie labiryntu nie daje więcej złota niż po prostu zebranie go i stworzenie nowego.
To jest w 100% dodatkowe wyzwanie, które możesz po prostu pominąć.
Opłaca się to tylko wtedy, gdy dodatkowe informacje i skróty pomogą ci szybciej rozwiązać labirynt.

Ten sam labirynt można rozwiązać maksymalnie 300 razy. Odpowiada to 299 relokacjom. Po tym czasie użycie dziwnej substancji na skarbie nie zwiększy już w nim złota, a `measure()` zwróci `None`.

<spoiler=pokaż wskazówkę 1>Oto ogólne podejście do rozwiązania problemu:

Stwórz labirynt i wyobraź sobie, że jesteś dronem.

Pomyśl, jak próbowałbyś znaleźć skarb, gdybyś był w labiryncie.

Zapisz swoją strategię krok po kroku, aby ktoś inny mógł ją wykonać bez myślenia.

Teraz spróbuj przetłumaczyć swoje kroki na kod.
</spoiler>
<spoiler=pokaż wskazówkę 2>Dopóki nie ma pętli: Wszystkie ściany są tak naprawdę jedną dużą połączoną ścianą. Jeśli będziesz podążać wzdłuż ściany, poprowadzi cię ona przez cały labirynt.
To podejście wymaga bardzo mało kodu i nie musisz śledzić, gdzie już byłeś. Około 10 linii kodu to wszystko, czego potrzebujesz.</spoiler>
<spoiler=pokaż wskazówkę 3>Zamiast poruszać dronem w absolutnych kierunkach, takich jak wschód czy zachód, bardzo przydatne może być poruszanie dronem we względnych kierunkach, takich jak „skręć w prawo” lub „skręć w lewo”. Aby to zrobić, musisz śledzić, w którą stronę dron się aktualnie porusza. Dron tak naprawdę nigdy się nie obraca, ale nadal możesz utrzymywać „wirtualny” obrót w kodzie.
Pomocny w tym jest następujący trik z indeksem:

`directions = [North, East, South, West]
index = 0`

Użyj `% 4`, aby umożliwić mu obracanie się „wokół koła”, tak aby po `West` zawijał z powrotem do `North`.
`# skręć w prawo
index = (index + 1) % 4`

`# skręć w lewo
index = (index - 1) % 4

move(directions[index])`</spoiler>
<spoiler=pokaż wskazówkę 4>Jeśli nie możesz tego rozwiązać, zawsze możesz ułatwić sobie życie i zrobić to mniej wydajnie.
Rozwiązanie labiryntu `1`x`1` jest banalne.</spoiler>
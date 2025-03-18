# Labirynty
`Items.Weird_Substance`, która jest pozyskiwana przez [nawóz](docs/unlocks/fertilizer.md) roślin, ma dziwny wpływ na krzewy. Jeśli dron znajduje się nad krzewem i użyjesz `use_item(Items.Weird_Substance, amount)`, krzew zamieni się w labirynt z żywopłotów.
Wielkość labiryntu zależy od ilości użytej `Items.Weird_Substance` (drugiego argumentu w wywołaniu `use_item()`).
Bez ulepszeń labiryntu, używając `n` `Items.Weird_Substance`, otrzymasz labirynt o wymiarach `n`x`n`. Na każdym poziomie ulepszenia labiryntu musisz użyć dodatkowego `n` `Items.Weird_Substance`, aby uzyskać ten sam efekt.
Aby stworzyć pełny labirynt na polu:

`plant(Entities.Bush)
n_substance = get_world_size() * num_unlocked(Unlocks.Mazes)
use_item(Items.Weird_Substance, n_substance)`

Z jakiegoś powodu dron nie może przelecieć nad żywopłotami, chociaż nie wyglądają na zbyt wysokie.

W żywopłocie ukryty jest skarb. Użyj `harvest()` na skarbie, aby otrzymać złoto równe powierzchni labiryntu. (Na przykład labirynt 5x5 przyniesie 25 złota.)

Jeśli użyjesz `harvest()` gdziekolwiek indziej, labirynt po prostu zniknie.

`get_entity_type()` jest równe `Entities.Treasure`, jeśli dron jest nad skarbem, a `Entities.Hedge` w każdym innym miejscu w labiryncie.

Labirynty nie zawierają żadnych pętli, chyba że użyjesz ponownie labiryntu (zobacz poniżej, jak to zrobić). Więc nie ma możliwości, aby dron znalazł się ponownie w tej samej pozycji bez cofania się.

Możesz sprawdzić, czy jest ściana, próbując przez nią przejść.
`move()` zwraca `True`, jeśli się udało, i `False` w przeciwnym razie.

Jeśli nie masz pomysłu, jak dostać się do skarbu, spojrzyj na Wskazówkę 1. Pokazuje ona, jak podejść do takiego problemu.


Dla dodatkowego wyzwania możesz ponownie użyć labiryntu, używając tej samej ilości `Items.Weird_Substance` na skarbie. 
To zwiększy ilość złota w skarbie o pełen labirynt i przeniesie go na losową pozycję w labiryncie.

Używając `measure()` na skarbie, zwraca pozycję, do której się przeniesie, jako krotkę.
`next_x, next_y = measure()`

Za każdym razem, gdy skarb jest przenoszony, z labiryntu może zostać usunięta losowa ściana. Więc używane ponownie labirynty mogą zawierać pętle.

Pamiętaj, że pętle w labiryncie znacznie utrudniają sytuację, ponieważ oznacza to, że możesz wrócić do tego samego miejsca bez cofania się.
Ponowne użycie labiryntu nie daje więcej złota niż po prostu zebranie i stworzenie nowego labiryntu.
To w 100% dodatkowe wyzwanie, które można po prostu pominąć.
Warto tylko wtedy, gdy dodatkowe informacje i skróty pomagają szybciej rozwiązać labirynt.

Ten sam labirynt można rozwiązać maksymalnie 300 razy. Odpowiada to 299 przeniesieniom. Po tym, użycie dziwnej substancji na skarbie nie zwiększy już w nim złota i `measure()` zwróci `None`.

<spoiler=pokaż wskazówkę 1>Oto ogólne podejście do rozwiązania problemu:

Stwórz labirynt i wyobraź sobie, że jesteś dronem.

Pomyśl, jak próbowałbyś znaleźć skarb, gdybyś był w labiryncie.

Zapisz swoją strategię krok po kroku, aby ktoś inny mógł ją śledzić bez zastanowienia.

Teraz spróbuj przekształcić swoje kroki w kod.
</spoiler>
<spoiler=pokaż wskazówkę 2>Dopóki nie ma pętli: Wszystkie ściany to w rzeczywistości jedna duża połączona ściana. Jeśli pójdziesz za ścianą, przeprowadzi cię przez cały labirynt. To podejście wymaga bardzo mało kodu i nie musisz śledzić miejsc, w których już byłeś. Wystarczy około 10 linijek kodu.</spoiler>
<spoiler=pokaż wskazówkę 3>Zamiast poruszać dronem w absolutnych kierunkach jak wschód czy zachód, może być bardzo przydatne poruszanie się w relatywnych kierunkach, takich jak "skręć w prawo" lub "skręć w lewo". Aby to zrobić, musisz śledzić, w którą stronę dron się porusza. Dron nigdy faktycznie się nie obraca, ale nadal możesz utrzymywać "wirtualny" obrót w kodzie.
Poniższa sztuczka z indeksem jest pomocna w tym:

`directions = [North, East, South, West]
index = 0`

Użyj `% 4`, aby pozwolić na obrót "wokół koła", tak aby po `West` wracało do `North`.
`# skręć w prawo
index = (index + 1) % 4`

`# skręć w lewo
index = (index - 1) % 4

move(directions[index])`</spoiler>
<spoiler=pokaż wskazówkę 4>Jeśli nie możesz tego rozwiązać, zawsze możesz ułatwić sobie życie i zrobić to mniej efektywnie. 
Rozwiązanie labiryntu `1`x`1` jest trywialne.</spoiler>
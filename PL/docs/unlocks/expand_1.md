# Rozszerzenie 1
<unlock=for>Zobacz także [Rozszerzenie_2](docs/unlocks/expand_2.md)

</unlock>Twoja farma urosła! Ta przestrzeń jest mało użyteczna, jeśli nie możesz poruszać dronem, więc jest nowa funkcja `move()`, która porusza dronem. `move()` wymaga, abyś określił kierunek, w którym chcesz poruszyć drona. Są do tego cztery nowe stałe: `North, East, South, West`

Na przykład, `move(North)` przesunie drona o jedno pole na północ.

Jeśli wyjdziesz poza krawędź farmy, dron zostanie przeniesiony na drugą stronę farmy.
Poniższy przykładowy kod będzie kontynuował poruszanie drona na północ i zawijał go z powrotem na początek, gdy dotrze do krawędzi farmy:

`while True:
	move(North)`

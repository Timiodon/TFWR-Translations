# Ekspansja 1
<unlock=for>Zobacz także [Ekspansja_2](docs/unlocks/expand_2.md)

</unlock>Twoja farma urosła! Ta przestrzeń nie jest zbyt użyteczna, jeśli nie możesz poruszać dronem, więc jest nowa funkcja `move()`, która przesuwa drona. `move()` wymaga, abyś określił kierunek, w którym chcesz poruszyć drona. Są na to cztery nowe stałe: `North, East, South, West`

Na przykład, `move(North)` przesunie drona o jedno pole na północ.

Jeśli wyjdziesz poza krawędź farmy, dron zostanie przeniesiony na drugą stronę farmy.
Poniższy przykładowy kod będzie kontynuował przesuwanie drona na północ i zawijał się z powrotem na początek, gdy dotrze do krawędzi farmy:

`while True:
	move(North)`
# Expand 1
<unlock=for>Also see [Expand_2](docs/unlocks/expand_2.md)

</unlock>Twoja farma się powiększyła! To miejsce nie jest zbyt użyteczne, jeśli nie możesz poruszać drona, więc jest nowa funkcja `move()`, która rusza dronem. `move()` wymaga, abyś określił kierunek, w którym chcesz przesunąć drona. Są cztery nowe stałe do tego: `North, East, South, West`.

Na przykład, `move(North)` przesunie drona o jedną kratkę na północ.

Jeśli przejdziesz poza krawędź farmy, dron zostanie przeniesiony na drugą stronę farmy.
Poniższy przykład kodu będzie przesuwał drona na północ i zacznie od nowa, gdy dotrze do krawędzi farmy:

`while True:
	move(North)`
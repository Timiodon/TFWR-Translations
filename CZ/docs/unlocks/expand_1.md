# Rozšíření 1
<unlock=for>Viz také [Rozšíření 2](docs/unlocks/expand_2.md)

</unlock>Vaše farma se rozrostla! Tento prostor není moc užitečný, pokud nemůžete pohybovat dronem, takže je tu nová funkce `move()`, která pohybuje dronem. `move()` vyžaduje, abyste specifikovali směr, kterým chcete, aby se dron pohyboval. Pro tento účel existují čtyři nové konstanty: `North, East, South, West` (Sever, Východ, Jih, Západ).

Například `move(North)` posune drona o jedno políčko na sever.

Pokud se přesunete přes okraj farmy, dron se přesune na druhou stranu farmy.
Následující ukázkový kód bude neustále posouvat drona na sever a vrátí se na začátek, když dosáhne okraje farmy:

`while True:
	move(North)`

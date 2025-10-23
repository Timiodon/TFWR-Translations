# Rozšíření 1
<unlock=for>Viz také [Expand_2](docs/unlocks/expand_2.md)

</unlock>Tvoje farma se rozrostla! Tento nový prostor ale není moc užitečný, pokud se nemůžeš s dronem pohybovat. Proto je tu nová funkce `move()`, která dron přesune. `move()` vyžaduje, aby bylo uvedeno, kterým směrem se má dron pohnout. K tomu slouží čtyři nové konstanty: `North, East, South, West`

Například `move(North)` posune dron o jedno pole na sever.

Pokud se pohneš přes okraj farmy, dron se objeví na opačné straně.  
Následující ukázkový kód posouvá dron stále na sever a po dosažení okraje farmy ho vrátí zpět na začátek:

`while True:
	move(North)`

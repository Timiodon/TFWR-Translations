# Polikultura
Być może zauważyłeś już, że czasami rośliny dają większe plony, gdy są sadzone razem.
Trawa, krzewy, drzewa i marchewki dają większe plony, gdy mają odpowiedniego towarzysza. Preferencje towarzysza są różne dla każdej pojedynczej rośliny i nie można ich przewidzieć. Na szczęście preferencje towarzysza rośliny pod dronem można zmierzyć za pomocą `get_companion()`. Zwraca ona krotkę, w której pierwszy element to typ rośliny, którą chce mieć za towarzysza, a drugi to pozycja, w której chce mieć swojego towarzysza.

`plant_type, (x, y) = get_companion()`

Na przykład, jeśli posadzisz krzak, a następnie wywołasz `get_companion()`, zwróci coś w rodzaju `(Entities.Carrot, (3, 5))`. Oznacza to, że ten krzak chciałby mieć marchewki na pozycji `(3,5)`. Więc jeśli posadzisz marchewki na `(3,5)`, a następnie zbierzesz krzak, da on więcej drewna. Faza wzrostu marchewki nie ma znaczenia.

Preferencje towarzysza rośliny mogą być `Entities.Grass`, `Entities.Bush`, `Entities.Tree` lub `Entities.Carrot`. Każda roślina wybiera to losowo, ale zawsze wybierze inną roślinę niż ona sama. Pozycja może być również dowolną pozycją w promieniu 3 ruchów od rośliny, z wyjątkiem pozycji samej rośliny.

Jeśli pod dronem nie ma rośliny, która ma preferencje towarzysza, `get_companion()` zwróci `None`.

Przed odblokowaniem polikultury mnożnik plonu wynosi `5`. Podwaja się za każdym razem, gdy go ulepszysz.
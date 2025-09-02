# Uprawa współrzędna
Być może już zauważyłeś, że czasami rośliny dają większy plon, gdy są sadzone razem.
Trawa, krzaki, drzewa i marchewki dają większy plon, gdy mają odpowiedniego towarzysza. Preferencje towarzysza są różne dla każdej pojedynczej rośliny i nie można ich przewidzieć. Na szczęście preferencje towarzysza rośliny pod dronem można zmierzyć za pomocą `get_companion()`. Zwraca ona krotkę, gdzie pierwszy element to typ rośliny, którą chce jako towarzysza, a drugi element to pozycja, w której chce swojego towarzysza.

`plant_type, (x, y) = get_companion()`

Na przykład, jeśli posadzisz krzak, a następnie wywołasz `get_companion()`, zwróci coś w stylu `(Entities.Carrot, (3, 5))`. Oznacza to, że ten krzak chciałby mieć marchewki na pozycji `(3,5)`. Więc jeśli posadzisz marchewki na `(3,5)`, a następnie zbierzesz krzak, da on więcej drewna. Etap wzrostu marchewki nie ma znaczenia.

Preferencje towarzysza rośliny mogą być `Entities.Grass`, `Entities.Bush`, `Entities.Tree` lub `Entities.Carrot`. Każda roślina wybiera to losowo, ale zawsze wybierze inną roślinę niż ona sama. Pozycja może być również dowolną pozycją w odległości do 3 ruchów od rośliny, z wyjątkiem pozycji samej rośliny.

Jeśli pod dronem nie ma rośliny, która ma preferencje towarzysza, `get_companion()` zwróci `None`.

Zanim uprawa współrzędna zostanie odblokowana, mnożnik plonu wynosi `5`. Podwaja się za każdym razem, gdy go ulepszysz.
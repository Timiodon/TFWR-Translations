# Polikultura
Może już zauważyłeś, że czasami rośliny dają lepszy plon, gdy są sadzone razem.
Trawa, krzewy, drzewa i marchewki dają więcej plonów, gdy mają odpowiedniego towarzysza. Preferencje towarzysza są różne dla każdej rośliny i nie można ich przewidzieć. Na szczęście, preferencje towarzysza rośliny pod dronem można zmierzyć za pomocą `get_companion()`. Zwraca to krotkę, w której pierwszy element to typ rośliny, jaką chce mieć jako towarzysza, a drugi to pozycja, na której chce mieć swojego towarzysza.

`plant, (x, y) = get_companion()`

Na przykład, jeśli zasadzisz krzew i potem wywołasz `get_companion()`, zwróci coś w stylu `(Entities.Carrot, (3, 5))`. Oznacza to, że ten krzew chciałby mieć marchewki na pozycji `(3,5)`. Więc jeśli zasadzisz marchewki na `(3,5)` i następnie zbierzesz krzew, da on więcej drewna. Etap wzrostu marchwi nie ma znaczenia.

Preferencje towarzysza rośliny mogą być `Entities.Grass`, `Entities.Bush`, `Entities.Tree` lub `Entities.Carrot`. Każda roślina wybiera to losowo, ale zawsze wybierze inną roślinę niż sama. Pozycja może być również dowolnym miejscem w promieniu 3 ruchów od rośliny, z wyjątkiem pozycji samej rośliny.

Jeśli pod dronem nie ma rośliny, która ma preferencje towarzysza, `get_companion()` zwróci `None`.

Mnożnik plonów to `5` plus liczba ulepszeń polikultury.
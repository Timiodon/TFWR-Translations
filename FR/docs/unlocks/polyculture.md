# Polyculture
Tu as peut-être déjà remarqué que parfois les plantes produisent plus lorsqu'elles sont plantées ensemble. 
L'herbe, les buissons, les arbres, et les carottes produisent plus lorsqu'ils ont le bon compagnon végétal. La préférence de compagnon est différente pour chaque plante et ne peut pas être prédite. Heureusement, la préférence de compagnon de la plante sous le drone peut être mesurée en utilisant `get_companion()`. Cela retourne un tuple où le premier élément est le type de plante qu'elle veut comme compagnon et le second élément est la position où elle veut son compagnon.

`plant, (x, y) = get_companion()`

Par exemple, si tu plantes un buisson et que tu appelles ensuite `get_companion()`, cela retournera quelque chose comme `(Entities.Carrot, (3, 5))`. Cela signifie que ce buisson aimerait avoir des carottes à la position `(3,5)`. Donc, si tu plantes des carottes à `(3,5)` et que tu récoltes ensuite le buisson, il produira plus de bois. Le stade de croissance de la carotte n'a pas d'importance.

La préférence de compagnon d'une plante peut être soit `Entities.Grass`, `Entities.Bush`, `Entities.Tree` ou `Entities.Carrot`. Chaque plante choisit cela de manière aléatoire, mais choisira toujours une plante différente d'elle-même. La position peut également être n'importe quelle position dans un rayon de 3 mouvements de la plante, sauf la position de la plante elle-même.

S'il n'y a pas de plante sous le drone qui a une préférence de compagnon, `get_companion()` retournera `None`.

Le multiplicateur de rendement est `5` plus le nombre d'améliorations de polyculture.
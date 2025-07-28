# Polyculture
Vous avez peut-être déjà remarqué que parfois les plantes rapportent plus lorsqu'elles sont plantées ensemble.
L'herbe, les buissons, les arbres et les carottes rapportent plus lorsqu'ils ont le bon compagnon végétal. La préférence de compagnon est différente pour chaque plante individuelle et ne peut pas être prédite. Heureusement, la préférence de compagnon de la plante sous le drone peut être mesurée en utilisant `get_companion()`. Elle retourne un tuple où le premier élément est le type de plante qu'elle veut comme compagnon et le second est la position où elle veut son compagnon.

`plant_type, (x, y) = get_companion()`

Par exemple, si vous plantez un buisson puis appelez `get_companion()`, cela retournera quelque chose comme `(Entities.Carrot, (3, 5))`. Cela signifie que ce buisson aimerait avoir des carottes à la position `(3,5)`. Donc si vous plantez des carottes à `(3,5)` puis récoltez le buisson, il rapportera plus de bois. Le stade de croissance de la carotte n'a pas d'importance.

La préférence de compagnon d'une plante peut être soit `Entities.Grass`, `Entities.Bush`, `Entities.Tree` ou `Entities.Carrot`. Chaque plante choisit cela au hasard, mais elle choisira toujours une plante différente d'elle-même. La position peut également être n'importe quelle position à moins de 3 déplacements de la plante, sauf la position de la plante elle-même.

S'il n'y a pas de plante sous le drone qui a une préférence de compagnon, `get_companion()` retournera `None`.

Avant que la polyculture ne soit débloquée, le multiplicateur de rendement est de `5`. Il double à chaque fois que vous l'améliorez.
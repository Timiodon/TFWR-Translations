# Riego
Las plantas crecen más rápido cuando se riegan. El suelo tiene un nivel de agua que va de `0` a `1`.
La función `get_water()` devuelve el nivel de agua del suelo sobre el que se encuentra.

La velocidad de crecimiento de una planta escala linealmente desde una velocidad de 1x con un nivel de agua de 0 hasta una velocidad de 5x con un nivel de agua de 1.

El suelo se seca con el tiempo: de media, pierde el 1% de su agua actual por segundo, pero hay cierta variación aleatoria en esto.
Mantener un nivel de agua alto consumirá mucha más agua que mantener un nivel de agua bajo.

Puedes usar agua en tus plantas. Se añade automáticamente un tanque de agua a tu inventario cada 10 segundos.
Mejorar `Unlocks.Watering` te dará un tanque de agua adicional cada 10 segundos.

Un tanque contiene `0.25` de agua.

Llama a `use_item(Items.Water)` sobre cualquier suelo para regar el terreno.
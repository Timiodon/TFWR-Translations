# Riego
Las plantas crecen más rápido cuando se riegan. El suelo tiene un nivel de agua que varía entre `0` y `1`.
La función `get_water()` devuelve el nivel de agua del suelo sobre el que se encuentra.

La velocidad de crecimiento de una planta se escala linealmente desde una velocidad de 1x al nivel de agua 0 hasta una velocidad de 5x al nivel de agua 1.

El suelo se seca con el tiempo: en promedio, pierde un 1% de su agua actual por segundo, pero esto puede variar un poco aleatoriamente. Mantener un nivel de agua alto consumirá mucho más agua que mantenerlo bajo.

Puedes usar agua en tus plantas. Un tanque de agua se añade automáticamente a tu inventario cada 10 segundos.
Mejorar `Unlocks.Watering` te dará un tanque adicional de agua cada 10 segundos.

Un tanque contiene `0.25` de agua.

Llama a `use_item(Items.Water)` sobre cualquier suelo para regarlo.
# Policultivo
Es posible que ya hayas notado que a veces las plantas rinden más cuando se plantan juntas.
La hierba, los arbustos, los árboles y las zanahorias rinden más cuando tienen la planta compañera adecuada. La preferencia de compañía es diferente para cada planta individual y no se puede predecir. Afortunadamente, la preferencia de compañía de la planta bajo el dron se puede medir usando `get_companion()`. Devuelve una tupla donde el primer elemento es el tipo de planta que quiere como compañera y el segundo elemento es la posición donde quiere a su compañera.

`plant_type, (x, y) = get_companion()`

Por ejemplo, si plantas un arbusto y luego llamas a `get_companion()`, devolverá algo como `(Entities.Carrot, (3, 5))`. Esto significa que a este arbusto le gustaría tener zanahorias en la posición `(3,5)`. Así que si plantas zanahorias en `(3,5)` y luego cosechas el arbusto, producirá más madera. La etapa de crecimiento de la zanahoria no importa.

La preferencia de compañía de una planta puede ser `Entities.Grass`, `Entities.Bush`, `Entities.Tree` o `Entities.Carrot`. Cada planta elige esto al azar, pero siempre elegirá una planta diferente a sí misma. La posición también puede ser cualquier posición a 3 movimientos de la planta, excepto la posición de la propia planta.

Si no hay ninguna planta bajo el dron que tenga una preferencia de compañía, `get_companion()` devolverá `None`.

Antes de que se desbloquee el policultivo, el multiplicador de rendimiento es `5`. Se duplica cada vez que lo mejoras.
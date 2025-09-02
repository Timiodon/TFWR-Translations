# Policultivo
Puede que ya hayas notado que a veces las plantas rinden más cuando se plantan juntas.
La hierba, los arbustos, los árboles y las zanahorias rinden más cuando tienen el compañero de planta adecuado. La preferencia de compañero es diferente para cada planta individual y no se puede predecir. Afortunadamente, la preferencia de compañero de la planta debajo del dron se puede medir usando `get_companion()`. Devuelve una tupla donde el primer elemento es el tipo de planta que quiere como compañero y el segundo elemento es la posición donde quiere a su compañero.

`plant_type, (x, y) = get_companion()`

Por ejemplo, si plantas un arbusto y luego llamas a `get_companion()`, devolverá algo como `(Entities.Carrot, (3, 5))`. Esto significa que a este arbusto le gustaría tener zanahorias en la posición `(3,5)`. Así que si plantas zanahorias en `(3,5)` y luego cosechas el arbusto, rendirá más madera. La etapa de crecimiento de la zanahoria no importa.

La preferencia de compañero de una planta puede ser `Entities.Grass`, `Entities.Bush`, `Entities.Tree` o `Entities.Carrot`. Cada planta elige esto al azar, pero siempre elegirá una planta diferente a sí misma. La posición también puede ser cualquier posición dentro de 3 movimientos de la planta, excepto la posición de la planta misma.

Si no hay una planta debajo del dron que tenga una preferencia de compañero, `get_companion()` devolverá `None`.

Antes de que se desbloquee el policultivo, el multiplicador de rendimiento es `5`. Se duplica cada vez que lo mejoras.
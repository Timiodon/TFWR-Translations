# Policultura
Tal vez ya te hayas dado cuenta de que a veces las plantas producen más cuando se plantan juntas. 
La hierba, los arbustos, los árboles y las zanahorias rinden más cuando tienen la planta compañera adecuada. La preferencia de compañero es diferente para cada planta individual y no se puede predecir. Afortunadamente, la preferencia de compañero de la planta bajo el drone puede medirse usando `get_companion()`. Esto devuelve una tupla donde el primer elemento es el tipo de planta que quiere como compañero y el segundo elemento es la posición donde quiere a su compañero.

`plant, (x, y) = get_companion()`

Por ejemplo, si plantas un arbusto y luego llamas a `get_companion()`, devolverá algo como `(Entities.Carrot, (3, 5))`. Esto significa que a este arbusto le gustaría tener zanahorias en la posición `(3,5)`. Así que si plantas zanahorias en `(3,5)` y luego cosechas el arbusto, producirá más madera. La etapa de crecimiento de la zanahoria no importa.

La preferencia de compañero de una planta puede ser `Entities.Grass`, `Entities.Bush`, `Entities.Tree` o `Entities.Carrot`. Cada planta elige esto al azar, pero siempre elegirá una planta diferente a sí misma. La posición también puede ser cualquier posición dentro de 3 movimientos de la planta, excepto la propia posición de la planta.

Si no hay planta bajo el drone que tenga una preferencia de compañero, `get_companion()` devolverá `None`.

El multiplicador de rendimiento es `5` más el número de mejoras de policultura.
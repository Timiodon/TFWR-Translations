# Girasoles
[Girasoles](objects/sunflower) recolectan la energía del sol. Puedes cosechar esa energía.

Plantarlos funciona exactamente igual que plantar zanahorias o calabazas.

Cosechar un girasol crecido produce energía.
Si hay al menos 10 girasoles en la granja y cosechas el que tiene mayor número de pétalos, obtienes `5` veces más energía.

`measure()` devuelve el número de pétalos del girasol bajo el dron.
Los girasoles tienen al menos `7` y como máximo `15` pétalos.
Se pueden medir antes de que estén completamente crecidos.

Varios girasoles pueden tener el mismo número de pétalos, por lo que puede haber varios girasoles con el mayor número de pétalos. En este caso, no importa cuál de ellos coseches.

Mientras tengas energía, el dron la usará para correr el doble de rápido.
Consume 1 de energía cada 30 acciones (como moverse, cosechar, plantar...)
Ejecutar otras declaraciones de código también puede usar energía, pero mucho menos que las acciones del dron.

En general, todo lo que se acelera con las mejoras de velocidad también se acelera con la energía.
Cualquier cosa acelerada por la energía también usa energía proporcional al tiempo que lleva ejecutarla, ignorando las mejoras de velocidad.
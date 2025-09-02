# Calabazas
Las [calabazas](objects/pumpkin) crecen como las zanahorias en suelo arado. Plantarlas cuesta zanahorias.

Cuando todas las calabazas en un cuadrado están completamente crecidas, crecerán juntas para formar una calabaza gigante. Desafortunadamente, las calabazas tienen un 20% de probabilidad de morir una vez que están completamente crecidas, por lo que necesitarás replantar las muertas si quieres que se fusionen. 

Cuando una calabaza muere, deja atrás una calabaza muerta que no soltará nada al ser cosechada. Plantar una nueva planta en su lugar elimina automáticamente la calabaza muerta, por lo que no es necesario cosecharla. `can_harvest()` siempre devuelve `False` en calabazas muertas.

El rendimiento de una calabaza gigante depende del tamaño de la calabaza.

Una calabaza de 1x1 rinde `1*1*1 = 1` calabazas.
Una calabaza de 2x2 rinde `2*2*2 = 8` calabazas en lugar de `4`.
Una calabaza de 3x3 rinde `3*3*3 = 27` calabazas en lugar de `9`.
Una calabaza de 4x4 rinde `4*4*4 = 64` calabazas en lugar de `16`.
Una calabaza de 5x5 rinde `5*5*5 = 125` calabazas en lugar de `25`.
Una calabaza de `n`x`n` rinde `n*n*6` calabazas para `n >= 6`.

Es una buena idea obtener calabazas de tamaño al menos 6x6 para obtener el multiplicador completo. 

Esto significa que incluso si plantas una calabaza en cada casilla de un cuadrado, una de las calabazas puede morir e impedir que crezca la mega calabaza.
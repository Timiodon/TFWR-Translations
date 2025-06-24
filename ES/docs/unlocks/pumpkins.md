# Calabazas
[Calabazas](objects/pumpkin) crecen como zanahorias en suelo cultivado. Plantarlas cuesta zanahorias.

Cuando todas las calabazas en un cuadrado están completamente maduras, crecerán juntas para formar una calabaza gigante. Desafortunadamente, las calabazas tienen un 20% de probabilidad de morir una vez que están completamente maduras, por lo que necesitarás replantar las que mueren si quieres que se fusionen.

El rendimiento de una calabaza gigante depende del tamaño de la calabaza.

Una calabaza de 1x1 da `1*1*1 = 1` calabazas.
Una calabaza de 2x2 da `2*2*2 = 8` calabazas en lugar de `4`.
Una calabaza de 3x3 da `3*3*3 = 27` calabazas en lugar de `9`.
Una calabaza de 4x4 da `4*4*4 = 64` calabazas en lugar de `16`.
Una calabaza de 5x5 da `5*5*5 = 125` calabazas en lugar de `25`.
Una calabaza de `n`x`n` da `n*n*6` calabazas para `n >= 6`.

Es una buena idea obtener calabazas de al menos 6x6 de tamaño para conseguir el multiplicador completo.

Esto significa que incluso si plantas una calabaza en cada baldosa de un cuadrado, una de las calabazas puede morir y evitar que crezca la mega calabaza.
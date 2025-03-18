# Calabazas
[Calabazas](objects/pumpkin) crecen como zanahorias en suelo labrado. Plantarlas cuesta zanahorias.

Cuando todas las calabazas en un cuadrado están completamente crecidas, se unirán para formar una calabaza gigante. Desafortunadamente, las calabazas tienen un 20% de probabilidad de morir una vez que están completamente crecidas, por lo que necesitarás replantar las que mueran si quieres que se fusionen.

El rendimiento de una calabaza gigante depende del tamaño de la calabaza.

Una calabaza de 1x1 produce `1*1*1 = 1` calabaza.
Una calabaza de 2x2 produce `2*2*2 = 8` calabazas en lugar de `4`.
Una calabaza de 3x3 produce `3*3*3 = 27` calabazas en lugar de `9`.
Una calabaza de 4x4 produce `4*4*4 = 64` calabazas en lugar de `16`.
Una calabaza `n`x`n` produce `n*n*5` calabazas para `n >= 5`.

Es una buena idea conseguir al menos calabazas de tamaño 5x5 para obtener el multiplicador completo.

Esto significa que incluso si plantas una calabaza en cada azulejo de un cuadrado, una de las calabazas puede morir e impedir que la mega calabaza crezca.
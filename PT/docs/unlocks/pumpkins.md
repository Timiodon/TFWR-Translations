# Abóboras
As [abóboras](objects/pumpkin) crescem como as cenouras em solo lavrado. Plantá-las custa cenouras.

Quando todas as abóboras num quadrado estão totalmente crescidas, elas crescem juntas para formar uma abóbora gigante. Infelizmente, as abóboras têm uma probabilidade de 20% de morrer quando estão totalmente crescidas, por isso terás de replantar as mortas se quiseres que elas se fundam.

Quando uma abóbora morre, deixa para trás uma abóbora morta que não dá nada quando colhida. Plantar uma nova planta no seu lugar remove automaticamente a abóbora morta, por isso não há necessidade de a colher. `can_harvest()` retorna sempre `False` em abóboras mortas.

O rendimento de uma abóbora gigante depende do tamanho da abóbora.

Uma abóbora 1x1 rende `1*1*1 = 1` abóboras.
Uma abóbora 2x2 rende `2*2*2 = 8` abóboras em vez de `4`.
Uma abóbora 3x3 rende `3*3*3 = 27` abóboras em vez de `9`.
Uma abóbora 4x4 rende `4*4*4 = 64` abóboras em vez de `16`.
Uma abóbora 5x5 rende `5*5*5 = 125` abóboras em vez de `25`.
Uma abóbora `n`x`n` rende `n*n*6` abóboras para `n >= 6`.

É uma boa ideia obter pelo menos abóboras de tamanho 6x6 para obter o multiplicador completo.

Isto significa que mesmo que plantes uma abóbora em cada quadrado, uma das abóboras pode morrer e impedir que a mega abóbora cresça.

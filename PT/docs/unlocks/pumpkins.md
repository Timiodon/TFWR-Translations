# Abóboras
[Abóboras](objects/pumpkin) crescem como cenouras em solo arado. Plantá-las custa cenouras.

Quando todas as abóboras em um quadrado estão completamente crescidas, elas se juntam para formar uma abóbora gigante. Infelizmente, abóboras têm uma chance de 20% de morrer quando estão completamente crescidas, então você precisará replantar as que morreram se quiser que elas se juntem.

A produção de uma abóbora gigante depende do tamanho da abóbora.

Uma abóbora 1x1 gera `1*1*1 = 1` abóboras.
Uma abóbora 2x2 gera `2*2*2 = 8` abóboras ao invés de `4`.
Uma abóbora 3x3 gera `3*3*3 = 27` abóboras ao invés de `9`.
Uma abóbora 4x4 gera `4*4*4 = 64` abóboras ao invés de `16`.
Uma abóbora 5x5 gera `5*5*5 = 125` abóboras ao invés de `25`.
Uma abóbora `n`x`n` gera `n*n*6` abóboras para `n >= 6`.

É uma boa ideia conseguir abóboras de pelo menos tamanho 6x6 para obter o multiplicador completo.

Isso significa que mesmo que você plante uma abóbora em cada tile de um quadrado, uma das abóboras pode morrer e impedir que a mega abóbora cresça.
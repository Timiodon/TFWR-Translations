# Irrigação
As plantas crescem mais rápido quando são regadas. O solo tem um nível de água que varia de `0` a `1`.
A função `get_water()` retorna o nível de água do solo sobre o qual está.

A velocidade de crescimento de uma planta escala linearmente de velocidade 1x no nível de água 0 para velocidade 5x no nível de água 1.

O solo seca com o tempo: em média, ele perde 1% de sua água atual por segundo, mas há alguma variação aleatória nisso. Manter um nível de água alto consumirá muito mais água do que manter um nível de água baixo.

Você pode usar água em suas plantas. Um tanque de água é adicionado automaticamente ao seu inventário a cada 10 segundos.
Melhorar `Unlocks.Watering` lhe dará um tanque de água adicional a cada 10 segundos.

Um tanque comporta `0.25` de água.

Chame `use_item(Items.Water)` sobre qualquer solo para regar o solo.
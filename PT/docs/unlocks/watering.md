# Regar
As plantas crescem mais rápido quando são regadas. O solo tem um nível de água que varia de `0` a `1`.  
A função `get_water()` retorna o nível de água do solo embaixo dele.

A velocidade de crescimento de uma planta aumenta linearmente de 1x na água nível 0 até 5x na água nível 1.

O solo seca com o tempo: Em média, perde 1% da água atual por segundo, mas há alguma variação aleatória nisso. Manter um nível de água alto consome muito mais água do que manter um nível baixo.

Você pode usar água nas suas plantas. Um tanque de água é adicionado automaticamente ao seu inventário a cada 10 segundos.
Atualizar `Unlocks.Watering` te dará um tanque adicional de água a cada 10 segundos.

Um tanque comporta `0.25` de água.

Use `use_item(Items.Water)` sobre qualquer solo para regá-lo.
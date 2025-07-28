# Rega
As plantas crescem mais rápido quando são regadas. O solo tem um nível de água que varia de `0` a `1`.
A função `get_water()` retorna o nível de água do solo sobre o qual se encontra.

A velocidade de crescimento de uma planta escala linearmente de 1x de velocidade ao nível de água 0 para 5x de velocidade ao nível de água 1.

O solo seca com o tempo: Em média, perde 1% da sua água atual por segundo, mas há alguma variação aleatória nisto. Manter um nível de água alto consumirá muito mais água do que manter um nível de água baixo.

Podes usar água nas tuas plantas. Um tanque de água é adicionado automaticamente ao teu inventário a cada 10 segundos.
Melhorar `Unlocks.Watering` dar-te-á um tanque de água adicional a cada 10 segundos.

Um tanque contém `0.25` de água.

Chama `use_item(Items.Water)` sobre qualquer solo para regar o solo.
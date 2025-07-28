# Fertilizante
A certa altura, esperar que as plantas cresçam já não é suficientemente eficiente.
Tal como a água, receberás automaticamente 1 fertilizante a cada 10 segundos, mais um extra por cada melhoria.

O fertilizante pode fazer as plantas crescerem instantaneamente. `use_item(Items.Fertilizer)` reduz o tempo de crescimento restante da planta debaixo do drone em 2 segundos.

Isto tem alguns efeitos secundários.
As plantas cultivadas com fertilizante ficarão infetadas.

Quando uma planta está infetada, metade do seu rendimento é transformado em `Items.Weird_Substance` quando é colhida.
A Substância Estranha também pode ser usada em plantas, o que tem o efeito de alternar o estado de infeção da planta e de todas as plantas adjacentes.

Por isso, se chamares `use_item(Items.Weird_Substance)` numa planta infetada, ela será curada, mas se a usares numa planta saudável, ela será infetada.

Se a usares numa planta infetada que tem vizinhos saudáveis, ela curará a planta, mas infetará os vizinhos e vice-versa.
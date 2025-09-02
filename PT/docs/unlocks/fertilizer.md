# Fertilizante
Em algum momento, esperar as plantas crescerem simplesmente não é mais eficiente o suficiente. 
Semelhante à água, você receberá automaticamente 1 fertilizante a cada 10 segundos, mais um extra para cada melhoria.

O fertilizante pode fazer as plantas crescerem instantaneamente. `use_item(Items.Fertilizer)` reduz o tempo de crescimento restante da planta sob o drone em 2 segundos.

Isso tem alguns efeitos colaterais.
Plantas cultivadas com fertilizante ficarão infectadas.

Quando uma planta está infectada, metade de seu rendimento é transformado em `Items.Weird_Substance` quando é colhida.
A Substância Estranha também pode ser usada em plantas, o que tem o efeito de alternar o status de infecção da planta e de todas as plantas adjacentes.

Então, se você chamar `use_item(Items.Weird_Substance)` em uma planta infectada, irá curá-la, mas se usar em uma planta saudável, irá infectá-la.

Se você usar em uma planta infectada que tem vizinhos saudáveis, irá curar a planta, mas infectar os vizinhos e vice-versa.
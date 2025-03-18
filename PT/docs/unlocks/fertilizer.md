# Fertilizante
Em algum momento, esperar as plantas crescerem já não é mais eficiente o suficiente. 
Semelhante à água, você receberá automaticamente 1 fertilizante a cada 10 segundos, além de um extra para cada upgrade.

O fertilizante pode fazer as plantas crescerem instantaneamente. `use_item(Items.Fertilizer)` reduz o tempo restante de crescimento da planta sob o drone em 2 segundos.

Isso tem alguns efeitos colaterais.
Plantas cultivadas com fertilizante ficarão infectadas.

Quando uma planta está infectada, metade de sua colheita é transformada em `Items.Weird_Substance` quando é colhida.
Weird Substance também pode ser usado em plantas, tendo o efeito de alternar o status de infecção da planta e de todas as plantas adjacentes.

Então, se você chamar `use_item(Items.Weird_Substance)` em uma planta infectada, ela será curada, mas se você usá-la em uma planta saudável, ela será infectada.

Se você usá-la em uma planta infectada que tem vizinhos saudáveis, ela curará a planta, mas infectará os vizinhos e vice-versa.
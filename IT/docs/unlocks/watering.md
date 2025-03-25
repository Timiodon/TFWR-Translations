# Irrigazione
Le piante crescono più velocemente quando sono annaffiate. Il terreno ha un livello d'acqua che varia da `0` a `1`.  
La funzione `get_water()` restituisce il livello d'acqua del terreno su cui si trova.

La velocità di crescita di una pianta aumenta linearmente da una velocità di 1x con livello d'acqua 0 a una velocità di 5x con livello d'acqua 1.

Il terreno si asciuga col tempo: in media, perde l'1% dell'acqua corrente al secondo, ma c'è una certa variabilità casuale in questo. Mantenere un livello d'acqua alto consumerà molta più acqua rispetto a mantenere un livello d'acqua basso.

Puoi usare l'acqua sulle tue piante. Un serbatoio d'acqua viene automaticamente aggiunto al tuo inventario ogni 10 secondi.  
L'aggiornamento `Unlocks.Watering` ti darà un serbatoio d'acqua aggiuntivo ogni 10 secondi.

Un serbatoio contiene `0.25` d'acqua.

Chiama `use_item(Items.Water)` su qualsiasi terreno per annaffiarlo.
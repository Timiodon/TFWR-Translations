# Annaffiatura
Le piante crescono più velocemente quando vengono annaffiate. Il terreno ha un livello d'acqua che va da `0` a `1`.
La funzione `get_water()` restituisce il livello d'acqua del terreno su cui si trova.

La velocità di crescita di una pianta scala linearmente da una velocità 1x a livello d'acqua 0 a una velocità 5x a livello d'acqua 1.

Il terreno si asciuga nel tempo: in media, perde l'1% della sua acqua attuale al secondo, ma c'è una certa varianza casuale in questo. Mantenere un alto livello d'acqua consumerà molta più acqua che mantenere un basso livello d'acqua.

Puoi usare l'acqua sulle tue piante. Un serbatoio d'acqua viene aggiunto automaticamente al tuo inventario ogni 10 secondi.
Potenziare `Unlocks.Watering` ti darà un serbatoio d'acqua aggiuntivo ogni 10 secondi.

Un serbatoio contiene `0.25` di acqua.

Chiama `use_item(Items.Water)` su qualsiasi terreno per annaffiarlo.

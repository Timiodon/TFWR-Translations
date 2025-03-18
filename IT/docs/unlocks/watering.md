# Irrigazione
Le piante crescono più velocemente quando sono annaffiate. Il terreno ha un livello d'acqua che varia da `0` a `1`.  
La funzione `get_water()` restituisce il livello d'acqua del terreno su cui si trova.

La velocità di crescita di una pianta aumenta linearmente da 1x alla velocità con un livello d'acqua di 0 a 5x alla velocità con un livello d'acqua di 1.

Il terreno si asciuga col tempo: in media, perde l'1% della sua acqua corrente al secondo, ma ci può essere una variazione casuale. Mantenere un livello d'acqua alto consumerà molta più acqua rispetto a mantenere un livello d'acqua basso.

Puoi usare i serbatoi d'acqua per annaffiare le tue piante. Un serbatoio d'acqua viene automaticamente aggiunto al tuo inventario ogni 10 secondi. 
Aggiornando `Unlocks.Watering` otterrai un serbatoio d'acqua aggiuntivo ogni 10 secondi.

Un serbatoio contiene `0.25` di acqua.

Chiama `use_item(Items.Water)` su qualsiasi terreno per annaffiarlo.
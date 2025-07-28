# Sblocchi Automatici
Per automatizzare completamente il gioco, puoi usare la funzione `unlock()` per sbloccare automaticamente le funzionalità.
Ad esempio, puoi usare `unlock(Unlocks.Speed)` e `unlock(Unlocks.Expand)` per sbloccare le funzionalità di velocità ed espansione.

Per determinare il costo di uno sblocco, usa semplicemente la funzione `get_cost()` come faresti per una pianta o un item.
Esempio:
`get_cost(Unlocks.Loops)`
restituisce `{Items.Hay:5}`

Se vuoi scoprire quanti sblocchi di un tipo particolare hai, usa la funzione `num_unlocked(unlock)`.

Ad esempio, `num_unlocked(Unlocks.Speed)` restituirà il numero di potenziamenti di velocità che hai.

`num_unlocked(Unlocks.Senses)` restituirà `1` se i sensori sono sbloccati e `0` se non lo sono.

Puoi anche usare `num_unlocked()` su Item, Entity o Terreni. Questo restituirà `1` se è sbloccato, altrimenti `0`.

Fai attenzione, `num_unlocked(Unlocks.Carrots)` restituirà il numero di volte che è stato sbloccato/potenziato.
`num_unlocked(Items.Carrot)` restituirà solo `0` o `1`. (Lo stesso per le altre piante)

# Sblocchi Automatici
Per automatizzare completamente il gioco, puoi usare la funzione `unlock()` per sbloccare automaticamente le funzionalità.
Ad esempio, puoi usare `unlock(Unlocks.Speed)` e `unlock(Unlocks.Expand)` per sbloccare le funzionalità di velocità ed espansione.

Per determinare il costo di uno sblocco, usa semplicemente la funzione `get_cost()` come faresti per una pianta o un item.
Esempio:
`get_cost(Unlocks.Loops)`
restituisce `{Items.Hay:5}`

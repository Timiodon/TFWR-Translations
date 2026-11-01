[<- Ferro](docs/unlocks/iron.md)
---
# Prospezione del Ferro
Avrai notato che a volte è difficile trovare le vene di ferro. Potresti scavare a caso sperando di incontrarle, ma c'è un modo migliore: dato che il ferro è magnetico, possiamo rilevarlo da lontano.

Il comando `prospect_iron()` serve proprio a questo. `prospect_iron()` restituisce la direzione (`North`, `East`, `South` o `West`) in cui il drone deve muoversi per compiere un passo verso il minerale di ferro più vicino.

Eseguire il comando costa 1 carbone.

`prospect_iron()` restituisce `None` se il drone si trova già direttamente sopra il minerale di ferro più vicino, se non hai abbastanza carbone per eseguire il comando o se non c'è ferro nel raggio d'azione.

Puoi usare il codice seguente per avvicinarti di un passo al prossimo minerale di ferro:

{{codeexample 
{
    "camera_position": {"x": -1, "y": 0, "z": 8},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [{"item": "coal", "n": 100}],
    "world_size": {"x": 5, "y": 5},
    "execution_speed": 1,
    "digging_speed": 10,
    "action_ticks": 200,
    "operation_ticks": 50,
    "seed": 8,
    "exclude_unlocks": ["watering", "fertilizer", "mushrooms", "quartz"]
}
#SETUP
jump(Unlocks.Iron)
#CODE
# Controlla che la prospezione restituisca una direzione
if prospect_iron() != None:
    move(prospect_iron()) # Avvicinati alla vena di ferro
}}

Potresti ottimizzare questo codice con una variabile, perché al momento chiama `prospect_iron()` due volte e costa 2 unità di carbone.

## Calcolo della Distanza
Il minerale di ferro più vicino viene calcolato in base al numero di passi che il drone deve compiere. Se un minerale si trova 2 blocchi a est e 3 blocchi a nord del drone, la distanza è 5, perché servono cinque passi per raggiungerlo.

Anche scavare conta come un passo. Quindi, se il ferro è inoltre sepolto 7 blocchi più in profondità, la distanza è 12: servono cinque passi per portarsi sopra il ferro e poi sette scavi per raggiungerlo.

---

[Ferro](docs/unlocks/iron.md)      [Sensi Sotterranei](docs/unlocks/underground_senses.md)

[move()](functions/move)      [dig()](functions/dig)      [prospect_iron()](functions/prospect_iron)

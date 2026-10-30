[<- Espansione 1](docs/unlocks/expand_1.md) <right>[Sensi Sotterranei ->](docs/unlocks/underground_senses.md)
<right>[Riso ->](docs/unlocks/rice.md)
<right>[Carbone ->](docs/unlocks/coal.md)
---
# Estrazione

Il tuo drone ha ottenuto una trivella rudimentale, che gli permette di cercare tesori nel sottosuolo.

Puoi usare il comando `dig()` per scavare nel blocco sotto di te.

Per ora, raccogliamo qualche blocco:

{{codeexample 
{
    "camera_position": {"x": -1, "y": 0, "z": 8},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": false,
    "autoplay": true,
    "items": [{"item": "hay", "n": 100}, {"item": "wood", "n": 100}],
    "world_size": {"x": 4, "y": 4},
    "execution_speed": 2,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer", "mushrooms", "coal", "special_soils"]
}
#SETUP
move(North)
move(East)
#CODE
dig()
do_a_flip()
dig()
do_a_flip()
dig()
do_a_flip()
clear()
}}

Se vuoi tornare in superficie, puoi usare `clear()` in qualsiasi momento. Questo ripristina anche la fattoria.

Passando il mouse su un blocco vedrai il suo nome, la stabilità e la durezza.

# Trivella

Scavando più in profondità noterai che i blocchi diventano più duri e richiedono più tempo per essere scavati. Per fortuna possiamo potenziare la trivella!

Puoi usare `get_hardness()` per controllare la durezza del blocco sotto di te. Se incontri una zona di blocchi particolarmente duri, potrebbe essere meglio aggirarli per avanzare più velocemente:

`while True:
    if get_hardness() < 5:
        dig()
    else:
        move(East)`

Naturalmente i blocchi diventano sempre più duri scendendo, quindi questa strategia è utile solo fino a un certo punto.

## Crolli

Scavare verso il basso provoca il crollo dei blocchi circostanti. I quattro blocchi accanto al drone vengono sempre distrutti. Poi il crollo si propaga in base alla stabilità del terreno. Un blocco con stabilità 1, come il prato, può sopportare una differenza di altezza pari a 1. In altre parole, se il prato ha un vicino verticale o orizzontale con una coordinata z più profonda di almeno 2 blocchi, viene distrutto.

La stabilità di un blocco è indicata nel tooltip visualizzato al passaggio del mouse.

Quando un blocco crolla, rimuove anche tutti i blocchi sopra di esso. Ricevi risorse solo dai blocchi scavati direttamente dal drone, quindi quelli persi in un crollo vengono distrutti senza produrre risorse.

---

[Sensi Sotterranei](docs/unlocks/underground_senses.md)      [Ciclo While](docs/scripting/while.md)

[move()](functions/move)      [dig()](functions/dig)

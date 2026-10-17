[<- Fertilizzante](docs/unlocks/fertilizer.md) <right>[Mega Fattoria ->](docs/unlocks/megafarm.md)
---
# Labirinti
`Items.Weird_Substance` ha uno strano effetto sui cespugli. Se il drone si trova sopra un cespuglio e chiami `use_item(Items.Weird_Substance, amount)`, il cespuglio si trasformerà in un labirinto di siepi.
La dimensione del labirinto dipende dalla quantità di `Items.Weird_Substance` utilizzata (il secondo argomento della chiamata `use_item()`).
Senza potenziamenti del labirinto, usare `n` `Items.Weird_Substance` crea un labirinto `n`x`n`. Ogni livello di potenziamento raddoppia il tesoro, ma anche la quantità di `Items.Weird_Substance` necessaria.
Quindi per creare un labirinto a campo intero:

{{codeexample 
{
    "camera_position": {"x": -1, "y": 2.4, "z": 5},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [{"item": "weird_substance", "n": 10}],
    "world_size": {"x": 4, "y": 4},
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 1,
    "seed": -1,
    "exclude_unlocks": ["watering"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
plant(Entities.Bush)
size = get_world_size()
substance = size * 2**(num_unlocked(Unlocks.Mazes) - 1)
use_item(Items.Weird_Substance, substance)
}}


Per qualche motivo il drone non può volare sopra le siepi, anche se non sembrano così alte.

Da qualche parte nel labirinto è nascosto un tesoro. Usa `harvest()` sul tesoro per ricevere una quantità d'oro pari all'area del labirinto. Per esempio, un labirinto 5x5 produce 25 unità d'oro.

Se usi `harvest()` in qualsiasi altro punto, il labirinto scomparirà.

`get_entity_type()` è uguale a `Entities.Treasure` se il drone si trova sopra il tesoro e `Entities.Hedge` in ogni altro punto del labirinto.

I labirinti non contengono anelli, a meno che non vengano riutilizzati (vedi sotto). Il drone non può quindi tornare nella stessa posizione senza ripercorrere i propri passi.

Puoi controllare se c'è un muro provando a passarci attraverso. 
`move()` restituisce `True` se ha avuto successo e `False` altrimenti.

`can_move()` può essere usato per controllare se c'è un muro senza muoversi.

{{codeexample 
{
    "camera_position": {"x": -1, "y": 2.4, "z": 5},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "items": [{"item": "weird_substance", "n": 10}],
    "world_size": {"x": 4, "y": 4},
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 100,
    "seed": 1,
    "exclude_unlocks": ["watering"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
move(East)
plant(Entities.Bush)
size = get_world_size()
substance = size * 2**(num_unlocked(Unlocks.Mazes) - 1)
use_item(Items.Weird_Substance, substance)
#CODE
quick_print(
    can_move(North), 
    can_move(East), 
    can_move(South), 
    can_move(West)
)
if move(North) and get_entity_type() == Entities.Treasure:
    harvest()
}}

Se non hai idea di come arrivare al tesoro, dai un'occhiata al Suggerimento 1. Ti mostra come affrontare un problema del genere.

Usare `measure()` in qualsiasi punto del labirinto restituisce la posizione del tesoro.
`x, y = measure()`

Per una sfida ulteriore, puoi riutilizzare il labirinto usando di nuovo sul tesoro la stessa quantità di `Items.Weird_Substance`.
Questo raccoglierà il tesoro e genererà un nuovo tesoro in una posizione casuale nel labirinto.

Ogni volta che il tesoro viene spostato, alcune delle pareti del labirinto possono essere rimosse casualmente. Quindi i labirinti riutilizzati possono contenere cicli.

Nota che i cicli nel labirinto lo rendono molto più difficile perché significa che puoi arrivare di nuovo alla stessa posizione senza tornare indietro.
Riutilizzare un labirinto non ti dà più oro che semplicemente raccogliere e creare un nuovo labirinto.
Questa è al 100% una sfida extra che puoi semplicemente saltare.
Vale la pena solo se le informazioni extra e le scorciatoie ti aiutano a risolvere il labirinto più velocemente.

Il tesoro può essere spostato fino a 300 volte. Dopodiché, usare la Sostanza Strana su di esso non ti darà più oro né sposterà il tesoro.

<spoiler=mostra suggerimento 1>
Ecco un approccio generale per risolvere il problema:

Crea un labirinto e immagina di essere il drone.

Pensa a come cercheresti di trovare il tesoro se fossi nel labirinto.

Scrivi la tua strategia passo dopo passo in modo che qualcun altro possa seguirla senza pensare.

Ora prova a tradurre i tuoi passi in codice.
</spoiler>
<spoiler=mostra suggerimento 2>
Finché non ci sono anelli, tutte le pareti formano un unico grande muro connesso. Se appoggi la mano sinistra al muro e lo segui, attraverserai l'intero labirinto.
Questo approccio richiede pochissimo codice e non devi tenere traccia dei luoghi già visitati. Bastano circa 10 righe di codice.
{{codeexample 
{
    "camera_position": {"x": -1, "y": 2.4, "z": 5},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": false,
    "show_inventory": true,
    "show_output": true,
    "collapsing": false,
    "autoplay": true,
    "items": [{"item": "weird_substance", "n": 10}],
    "world_size": {"x": 4, "y": 4},
    "execution_speed": 2,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 1,
    "seed": -1,
    "exclude_unlocks": ["watering"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
plant(Entities.Bush)
size = get_world_size()
substance = size * 2**(num_unlocked(Unlocks.Mazes) - 1)
use_item(Items.Weird_Substance, substance)
#CODE
directions = [North, East, South, West]
index = 0
while get_entity_type() != Entities.Treasure:
    index = (index - 1) % 4
    for _ in range(4):
        if move(directions[index]):
            break
        index = (index + 1) % 4
do_a_flip()
harvest()
}}
</spoiler>
<spoiler=mostra suggerimento 3>
Invece di muovere il drone in direzioni assolute come est o ovest, può essere utile usare direzioni relative come "gira a destra" o "gira a sinistra". Per farlo devi tenere traccia della direzione in cui il drone si sta muovendo. Il drone non ruota realmente, ma puoi comunque mantenere nel codice una rotazione "virtuale".
Il seguente trucco con l'indice è utile per questo:

{{codeexample 
{
    "camera_position": {"x": -1, "y": 1.8, "z": 5},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "items": [{"item": "weird_substance", "n": 10}],
    "world_size": {"x": 3, "y": 3},
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 1,
    "exclude_unlocks": ["watering"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
directions = [North, East, South, West]
index = 0
move(directions[index])

# gira a destra
index = (index + 1) % 4
move(directions[index])

# gira a sinistra
index = (index - 1) % 4
move(directions[index])
}}


`% 4` permette di ruotare "intorno al cerchio", così `3 (West) + 1` torna a essere `0 (North)`, perché `4 % 4 == 0` e `-1 % 4 == 3`.</spoiler>
<spoiler=mostra suggerimento 4>
Se non riesci a risolverlo, puoi sempre semplificare il problema usando un approccio meno efficiente.
Risolvere un labirinto `1`x`1` è banale.</spoiler>

---

[Statistiche](docs/stats.md)      [Liste](docs/scripting/lists.md)      [Dizionari](docs/scripting/dicts.md)      [Tuple](docs/scripting/tuples.md)

[harvest()](functions/harvest)      [plant()](functions/plant)      [can_move()](functions/can_move)      [move()](functions/move)      [use_item()](functions/use_item)

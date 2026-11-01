[<- Ferro](docs/unlocks/iron.md) <right>[Funghi ->](docs/unlocks/mushroom.md)
---
# Quarzo
Dopo le vene di ferro in `Grounds.Rock`, trovi quarzo nella parte inferiore dello strato di roccia e nella `Grounds.Dirt` dura sottostante (controlla la durezza con `get_hardness()` dei [Sensi Sotterranei](docs/unlocks/underground_senses.md)).

Il codice seguente scava oltre la terra, fino allo strato di roccia. Lì continua a cercare quarzo mentre scava, finché la distanza non è inferiore a 2. Infine stampa la distanza raggiunta.
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
    "items": [{"item": "block", "n": 1}, {"item": "iron", "n": 100}],
    "world_size": {"x": 3, "y": 3},
    "execution_speed": 8,
    "digging_speed": 16,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 9,
    "exclude_unlocks": ["watering", "fertilizer", "mushrooms", "dynamite"]
}
#SETUP
move(East)
move(North)
#CODE
# Scava fino allo strato di roccia
while get_ground_type() != Grounds.Rock:
    dig()

# Continua a scavare finché una vena di quarzo è vicina
while prospect_quartz() == None or prospect_quartz() >= 2:
    for i in range(10):
        dig()

# Stampa la distanza finale dalla vena
print(prospect_quartz())
}}

## Struttura delle Vene
Il quarzo cresce in vene a forma di ago che formano colonne verticali, rendendole difficili da trovare per tentativi.

## Cercare il Quarzo
Per fortuna possiamo prendere il ferro e deformarlo fino a ottenere qualcosa di simile a una bacchetta da rabdomante, così da individuare più facilmente le vene di quarzo. Il comando apposito è `prospect_quartz()`.

`prospect_quartz()` funziona diversamente da `prospect_iron()`. Invece di restituire la direzione verso il ferro più vicino, restituisce la distanza 3D esatta tra il blocco di quarzo più vicino e il drone (distanza euclidea).

Eseguire `prospect_quartz()` costa 1 ferro, quindi conviene usare il comando con parsimonia.

Se `prospect_quartz()` non trova quarzo nelle vicinanze oppure non hai abbastanza ferro per eseguire la ricerca, restituisce `None`.

## Strategia
<spoiler=mostra suggerimento>Puoi ripetere la prospezione e muoverti per vedere come cambia la distanza. Su una superficie piana, minimizzare la distanza può portarti sopra una vena di quarzo. Una strategia simile alla ricerca binaria può ridurre al minimo le chiamate a `prospect_quartz()` e il ferro che consumano.

Strategie più elaborate possono usare la geometria 2D per trovare l'intersezione di due o più cerchi. Oppure puoi scegliere la via difficile: una trilaterazione completa, intersecando tre sfere per trovare la posizione 3D esatta della vena.

Per una radice quadrata puoi usare l'operatore di potenza: ad esempio, `16**0.5` calcola la radice quadrata di 16. Non ci sono funzioni matematiche integrate per trigonometria o vettori: dovrai implementarle.

Ricorda che nelle vicinanze possono esserci più vene: misurazioni vicine potrebbero quindi non indicare la stessa vena.</spoiler>

---

[Statistiche](docs/stats.md)      [Estrazione](docs/unlocks/mining.md)      [Sensi Sotterranei](docs/unlocks/underground_senses.md)      [Variabili](docs/scripting/variables.md)      [Operatori](docs/scripting/operators.md)

[move()](functions/move)      [dig()](functions/dig)      [get_ground_type()](functions/get_ground_type)      [prospect_quartz()](functions/prospect_quartz)

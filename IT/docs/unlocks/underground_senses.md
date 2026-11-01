[<- Estrazione](docs/unlocks/mining.md)
---
# Sensi Sotterranei
Aggiungiamo qualche sensore, così il drone potrà orientarsi nel sottosuolo.

## Posizione Z
Ora puoi usare `get_pos_z()` per ottenere l'altezza del drone (parte da 0 e diventa negativa mentre il drone scende).

{{codeexample 
{
    "camera_position": {"x": -1.5, "y": 0, "z": 10},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "exclude_unlocks": ["watering", "fertilizer"],
    "items": [],
    "world_size": {"x": 5, "y": 5},
    "execution_speed": 2,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 1
}
#SETUP
move(North)
move(North)
move(East)
move(East)
#CODE
print(get_pos_z())
dig()
dig()
dig()
print(get_pos_z())
}}

## Tipo di Terreno
`get_ground_type()` restituisce il tipo di terreno sotto il drone. Puoi passargli una direzione come argomento, per esempio `get_ground_type(North)`, per ottenere il tipo di terreno di una casella vicina.

Ecco come controllare se il blocco sotto il drone è di terra:

{{codeexample 
{
    "camera_position": {"x": -1.5, "y": 0, "z": 8},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "exclude_unlocks": ["watering", "fertilizer"],
    "world_size": {"x": 4, "y": 4},
    "execution_speed": 2,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 1
}
#CODE
dig()
if get_ground_type() == Grounds.Dirt:
    do_a_flip()
}}

## Durezza e Stabilità
`get_hardness()` restituisce la durezza della casella di terreno sotto il drone. Puoi passargli una direzione come argomento, per esempio `get_hardness(North)`. Più alta è la durezza della casella, più tempo serve per scavarla.

`get_stability()` restituisce la stabilità della casella di terreno sotto il drone. Puoi passargli una direzione come argomento, per esempio `get_stability(North)`. Una stabilità pari a 1 significa che il blocco può sopportare una differenza di altezza pari a 1 prima di crollare.

{{codeexample 
{
    "camera_position": {"x": -1, "y": 0, "z": 10},
    "show_image": true,
    "image_size": {"x": 800, "y": 250},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "exclude_unlocks": ["watering", "fertilizer"],
    "world_size": {"x": 5, "y": 5},
    "execution_speed": 2,
    "action_ticks": 200,
    "operation_ticks": 20,
    "seed": 0
}
#SETUP
jump(Unlocks.Rice)
#CODE
print(get_hardness(), "|", get_stability())
while get_hardness() == 1:
    dig()

print(get_hardness(), "|", get_stability())
while get_hardness() == 2 and get_stability() == 3:
    dig()
}}

Nota che i quattro blocchi direttamente adiacenti al drone vengono rimossi a prescindere dalla loro stabilità mentre il drone scava verso il basso, a meno che il blocco non abbia una funzione speciale. Argilla, ferro e quarzo, per esempio, non vengono rimossi da questa regola. Possono comunque crollare per mancanza di stabilità.
---

[Estrazione](docs/unlocks/mining.md)      [Sensori](docs/unlocks/senses.md)

[get_pos_z()](functions/get_pos_z)      [get_ground_type()](functions/get_ground_type)      [get_hardness()](functions/get_hardness)      [get_stability()](functions/get_stability)

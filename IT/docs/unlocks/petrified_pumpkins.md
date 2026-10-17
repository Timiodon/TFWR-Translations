[<- Riso](docs/unlocks/rice.md)
---
# Zucche Pietrificate

A quanto pare si possono trovare zucche nel sottosuolo. Si sono indurite e pietrificate, ma vanno ancora bene per i nostri scopi.

Le zucche pietrificate si trovano nel sottosuolo in blocchi di 3x3x3 o 5x5x5. Non esiste un modo sicuro per trovarle: devi sperare che il drone ne incontri una scavando. Si trovano però nella terra dura sotto lo strato di roccia e ferro, più o meno all'altezza del quarzo (se lo hai sbloccato).

Questo offre un modo alternativo per ottenere zucche senza coltivarle in superficie. Se preferisci coltivarle, puoi tranquillamente ignorare le zucche pietrificate.

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
    "items": [{"item": "hay", "n": 100}],
    "exclude_unlocks": ["mushrooms", "watering", "fertilizer", "pyramid", "dynamite"],
    "world_size": {"x": 6, "y": 6},
    "execution_speed": 8,
    "digging_speed": 16,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 3
}
#SETUP
jump(Unlocks.Petrified_Pumpkins)
move(East)
move(North)
move(North)
move(North)
#CODE
while get_ground_type() != Grounds.Petrified_Pumpkin:
    dig()
z = get_pos_z()
for i in range(get_world_size()):
    for j in range(get_world_size()):
        while get_pos_z() > z:
            dig()
        move(North)
    move(East)
}}

---

[Statistiche](docs/stats.md)      [Estrazione](docs/unlocks/mining.md)      [Sensi Sotterranei](docs/unlocks/underground_senses.md)

[move()](functions/move)      [dig()](functions/dig)      [get_ground_type()](functions/get_ground_type)

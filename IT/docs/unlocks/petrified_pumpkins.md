[<- Riso](docs/unlocks/rice.md)
---
# Zucche Pietrificate
A quanto pare si possono trovare zucche nel sottosuolo. Si sono indurite e pietrificate, ma vanno ancora bene per i nostri scopi. Puoi scavarle con `dig()` per ottenere zucche.

Questo offre un modo alternativo per ottenere zucche senza coltivarle in superficie. Se preferisci coltivarle, puoi tranquillamente ignorare le zucche pietrificate.

{{codeexample 
{
    "camera_position": {"x": -2, "y": 1, "z": 8},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": false,
    "show_inventory": true,
    "show_output": false,
    "collapsing": false,
    "autoplay": true,
    "items": [],
    "exclude_unlocks": ["mushrooms", "watering", "fertilizer", "pyramid", "dynamite", "quartz"],
    "world_size": {"x": 6, "y": 6},
    "execution_speed": 8,
    "digging_speed": 16,
    "action_ticks": 200,
    "operation_ticks": 1,
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
        while get_pos_z() > z - 2 and get_ground_type() != Grounds.Petrified_Pumpkin:
            dig()
        move(North)
    move(East)
for _ in range(3):
    dig()
    move(East)
    dig()
    move(South)
    dig()
    move(West)
    dig()
    move(West)
    dig()
    move(North)
    dig()
    move(North)
    dig()
    move(East)
    dig()
    move(East)
    dig()
    move(South)
    move(West)
}}

Le zucche pietrificate si trovano nel sottosuolo in blocchi di 3x3x3 o 5x5x5. Non esiste un modo sicuro per trovarle: devi sperare che il drone ne incontri una scavando. Si trovano però nella terra dura sotto lo strato di roccia e ferro, più o meno all'altezza del quarzo (se lo hai sbloccato).

---

[Statistiche](docs/stats.md)      [Estrazione](docs/unlocks/mining.md)      [Sensi Sotterranei](docs/unlocks/underground_senses.md)

[move()](functions/move)      [dig()](functions/dig)      [get_ground_type()](functions/get_ground_type)

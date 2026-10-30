[<- Bambù](docs/unlocks/bamboo.md)
---
# Piramidi

Il sottosuolo ora contiene antiche strutture piramidali da cui puoi raccogliere energia!

Le piramidi sono fatte di blocchi di sabbia (`Grounds.Sand`). Sotto la piramide si trova uno strato di fondamenta in calcare (`Grounds.Limestone`). Essendo antiche ed erose, le troverai sempre parzialmente distrutte. Lo strato di fondamenta è sempre presente, ma nella sabbia ci saranno dei buchi. Ecco che aspetto ha una piramide quando la dissotterri:

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
    "items": [{"item": "hay", "n": 100}, {"item": "block", "n": 100}],
    "world_size": {"x": 6, "y": 6},
    "execution_speed": 32,
    "digging_speed": 16,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 7,
    "exclude_unlocks": ["watering", "fertilizer", "mushrooms", "dynamite", "quartz"]
}
#SETUP
jump(Unlocks.Pyramid)
move(North)
#CODE
while get_ground_type() != Grounds.Limestone:
    dig()
do_a_flip()
z = get_pos_z()
for i in range(6):
    for j in range(6):
        while (get_ground_type() != Grounds.Limestone
                and get_ground_type() != Grounds.Sand
                and get_pos_z() > z):
            dig()
        move(North)
    move(East)
}}

I blocchi sopra la piramide sono sempre di terra. Se vuoi dissotterrare una piramide in modo più efficiente rispetto al codice precedente, puoi sfruttare questo fatto.

Come puoi vedere, nella sabbia ci sono diversi buchi da riempire. Quando li riempi e riporti la piramide al suo stato originale, questa si distrugge e ricevi energia come ricompensa.

Puoi restaurare una piramide posizionando blocchi con il comando `place(Grounds.Sand)`. La sabbia è un blocco speciale che crolla immediatamente se non è sostenuto correttamente. Ogni blocco di sabbia deve essere posizionato direttamente sul calcare oppure sopra una base 3x3 di blocchi di sabbia. Ecco una piccola piramide costruita a mano come dimostrazione. Naturalmente, costruirla da solo non ti darà energia:

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
    "items": [{"item": "hay", "n": 100}, {"item": "block", "n": 100}],
    "world_size": {"x": 3, "y": 3},
    "execution_speed": 4,
    "digging_speed": 4,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 9,
    "exclude_unlocks": ["watering", "fertilizer", "mushrooms", "coal", "quartz"]
}
#CODE
for i in range(3):
    for j in range(3):
        place(Grounds.Limestone)
        move(North)
    move(East)

for i in range(3):
    for j in range(3):
        place(Grounds.Sand)
        move(North)
    move(East)

move(North)
move(East)
place(Grounds.Sand)
}}

Una piramide restaurata correttamente è composta da fondamenta quadrate di calcare con lati di lunghezza dispari, per esempio 5x5. Sopra si trova uno strato di blocchi di sabbia delle stesse dimensioni (5x5), seguito da strati progressivamente più piccoli: 3x3 e poi 1x1.

Quando una piramide viene completata, si sgretola e al centro compare un grande girasole. Puoi raccoglierlo per ricevere energia. Più grande è la piramide completata, maggiore è l'energia ottenuta.

---

[Statistiche](docs/stats.md)      [Sensi Sotterranei](docs/unlocks/underground_senses.md)

[move()](functions/move)      [dig()](functions/dig)      [use_item()](functions/use_item)      [place()](functions/place)

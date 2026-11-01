[<- Bambù](docs/unlocks/bamboo.md)
---
# Piramidi
Il sottosuolo ora contiene antiche strutture piramidali da cui puoi raccogliere energia per accelerare il drone!

Le piramidi sono fatte di blocchi di sabbia (`Grounds.Sand`). Sotto la piramide si trova uno strato di fondamenta in calcare (`Grounds.Limestone`). Essendo antiche ed erose, le troverai sempre parzialmente distrutte. Lo strato di fondamenta è sempre presente, ma nella sabbia ci saranno dei buchi.

Ecco come appare una piramide in rovina quando la dissotterri:
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
# Scava per trovare la base di una piramide
while get_ground_type() != Grounds.Limestone:
    dig()

z = get_pos_z() # Ricorda la profondità della base

# Scava tutto ciò che non fa parte della piramide
for i in range(6):
    for j in range(6):
        while (get_ground_type() != Grounds.Limestone
                and get_ground_type() != Grounds.Sand
                and get_pos_z() > z):
            dig()
        move(North)
    move(East)
}}

## Ripristinare la Piramide
Come puoi vedere, nella sabbia ci sono diversi buchi da riempire. Quando riempi i buchi e ripristini la piramide, questa si distrugge e al centro della base di calcare compare un grande girasole. Raccoglilo per ottenere `Items.Power`. Più grande è la piramide completata, maggiore è l'energia ottenuta.

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
# Serve una base di calcare su cui mettere la sabbia
for i in range(3):
    for j in range(3):
        place(Grounds.Limestone)
        move(North)
    move(East)

# Metti uno strato di sabbia di 3x3 sul calcare
for i in range(3):
    for j in range(3):
        place(Grounds.Sand)
        move(North)
    move(East)

# Prova ad aggiungere un altro strato di 3x3
# Solo il blocco centrale è sostenuto e rimane
for i in range(3):
    for j in range(3):
        place(Grounds.Sand)
        move(North)
    move(East)
}}

Una piramide restaurata correttamente è composta da fondamenta quadrate di calcare con lati di lunghezza dispari, per esempio 5x5. Sopra si trova uno strato di blocchi di sabbia delle stesse dimensioni (5x5), seguito da strati progressivamente più piccoli: 3x3 e poi 1x1.

I blocchi sopra la piramide sono sempre di terra. Puoi sfruttare questo fatto per dissotterrare una piramide in modo efficiente.

## Energia
Finché hai energia, il drone la usa per funzionare al doppio della velocità.
Consuma 1 unità di energia ogni 30 azioni, come movimenti, raccolti o semine.
Anche l'esecuzione di altre istruzioni di codice può consumare energia, ma molto meno delle azioni del drone.

In generale, tutto ciò che è accelerato dai potenziamenti di velocità è anche accelerato dall'energia.
Qualsiasi cosa accelerata dall'energia consuma anche energia in proporzione al tempo necessario per eseguirla, ignorando i potenziamenti di velocità.

L'energia non influisce su `dig()`.

---

[Statistiche](docs/stats.md)      [Sensi Sotterranei](docs/unlocks/underground_senses.md)

[move()](functions/move)      [dig()](functions/dig)      [use_item()](functions/use_item)      [place()](functions/place)

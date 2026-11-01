[<- Carbone](docs/unlocks/coal.md) <right>[Quarzo ->](docs/unlocks/quartz.md)
<right>[Prospezione del Ferro ->](docs/unlocks/prospecting.md)
<right>[Mappa del Tesoro ->](docs/unlocks/treasure_map.md)
---
# Ferro
Dopo aver trovato carbone in `Grounds.Dirt`, puoi scavare oltre lo strato di `Grounds.Clay` fino a `Grounds.Rock` per trovare ferro.

A differenza delle vene di carbone, quelle di ferro si estendono anche in verticale. Tutti i blocchi di una vena di ferro sono sempre direttamente adiacenti; non sono mai collegati solo in diagonale.

All'inizio le vene di ferro sono piccole e avrai bisogno di un po' di fortuna per trovarle. Potenziare il ferro aumenta la dimensione massima delle vene e rende più facile trovarle per caso. Per trovarle in modo affidabile, sblocca la [prospezione](docs/unlocks/prospecting.md).

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
    "items": [{"item": "hay", "n": 100}, {"item": "wood", "n": 100}],
    "world_size": {"x": 5, "y": 5},
    "execution_speed": 1,
    "digging_speed": 10,
    "action_ticks": 200,
    "operation_ticks": 50,
    "seed": 5,
    "exclude_unlocks": ["watering", "fertilizer", "mushrooms", "quartz"]
}
#SETUP
#CODE
# Scava finché non appare un blocco di ferro
while get_ground_type() != Grounds.Iron:
    dig()

# Estrai il ferro
dig()
}}

---

[Statistiche](docs/stats.md)      [Estrazione](docs/unlocks/mining.md)      [Prospezione del Ferro](docs/unlocks/prospecting.md)      [Sensi Sotterranei](docs/unlocks/underground_senses.md)

[move()](functions/move)      [dig()](functions/dig)

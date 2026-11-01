[<- Estrazione](docs/unlocks/mining.md) <right>[Bambù ->](docs/unlocks/bamboo.md)
<right>[Zucche Pietrificate ->](docs/unlocks/petrified_pumpkins.md)
<right>[Perlite e Terriccio ->](docs/unlocks/special_soils.md)
---
# Riso
Sotto la superficie e lo strato di `Grounds.Dirt` trovi un sottile strato di `Grounds.Clay`. Questo terreno fertile e intriso d'acqua è perfetto per piantare riso.

Il codice seguente può aiutarti a scavare fino all'argilla e piantare riso:
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
    "items": [],
    "exclude_unlocks": ["watering", "fertilizer"],
    "world_size": {"x": 4, "y": 4},
    "execution_speed": 8,
    "digging_speed": 4,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 1
}
#SETUP
move(East)
#CODE
while get_ground_type() != Grounds.Clay:
    dig()
plant(Entities.Rice)
}}

Quando il drone è sopra un blocco di `Grounds.Clay`, puoi usare `plant(Entities.Rice)` per piantare riso, `can_harvest()` per verificare se è maturo e infine `harvest()` per raccoglierlo.

## Terrazze
Quando pianti riso, il terreno diventa `Grounds.Rice_Terrace` per offrirgli l'ambiente ideale per maturare. Quando il riso è maturo, il terreno si asciuga e diventa `Grounds.Dry_Rice_Terrace`, dove non puoi piantare altro riso. Per fortuna, lo strato è spesso alcuni blocchi: puoi rimuovere il blocco con `dig()` e piantare altro riso sulla `Grounds.Clay` sottostante. Se lo strato si esaurisce, puoi sempre usare `clear()` per ripristinare il mondo e scavare fino a uno nuovo.

---

[Statistiche](docs/stats.md)      [Estrazione](docs/unlocks/mining.md)      [Sensi Sotterranei](docs/unlocks/underground_senses.md)      [If](docs/scripting/if.md)      [Ciclo For](docs/scripting/for.md)

[harvest()](functions/harvest)      [plant()](functions/plant)      [move()](functions/move)      [dig()](functions/dig)      [get_ground_type()](functions/get_ground_type)

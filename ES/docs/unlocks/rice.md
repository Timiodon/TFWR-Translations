[<- Minería](docs/unlocks/mining.md) <right>[Bambú ->](docs/unlocks/bamboo.md)
<right>[Calabazas petrificadas ->](docs/unlocks/petrified_pumpkins.md)
<right>[Perlita y suelo franco ->](docs/unlocks/special_soils.md)
---
# Arroz
Bajo la superficie y la capa de `Grounds.Dirt` encontrarás una fina capa de `Grounds.Clay`. Resulta que este terreno fértil y empapado es perfecto para plantar brotes de arroz.

El siguiente código puede resultarte útil para excavar hacia abajo hasta encontrar arcilla y plantar arroz:
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

Mientras el dron esté sobre un bloque de `Grounds.Clay`, puedes usar `plant(Entities.Rice)` para plantar arroz, `can_harvest()` para comprobar si ha terminado de crecer y, por último, `harvest()` para cosecharlo.

## Terrazas
Al plantar arroz, el terreno se convierte en `Grounds.Rice_Terrace` para ofrecerle el entorno ideal para madurar. Cuando el arroz termina de crecer, el terreno se seca y se convierte en `Grounds.Dry_Rice_Terrace`, donde no se puede plantar más arroz. Por suerte, la capa tiene varios bloques de grosor: puedes retirar el bloque con `dig()` y plantar arroz en la `Grounds.Clay` inferior. Si se agota la capa, siempre puedes usar `clear()` para reiniciar el mundo y excavar hasta otra nueva.

---

[Estadísticas](docs/stats.md)      [Minería](docs/unlocks/mining.md)      [Sentidos subterráneos](docs/unlocks/underground_senses.md)      [If](docs/scripting/if.md)      [Bucle for](docs/scripting/for.md)

[harvest()](functions/harvest)      [plant()](functions/plant)      [move()](functions/move)      [dig()](functions/dig)      [get_ground_type()](functions/get_ground_type)

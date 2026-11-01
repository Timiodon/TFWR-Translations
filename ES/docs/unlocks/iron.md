[<- Carbón](docs/unlocks/coal.md) <right>[Cuarzo ->](docs/unlocks/quartz.md)
<right>[Prospección de hierro ->](docs/unlocks/prospecting.md)
<right>[Mapa del tesoro ->](docs/unlocks/treasure_map.md)
---
# Hierro
Tras encontrar carbón en `Grounds.Dirt`, puedes seguir excavando, atravesar la capa de `Grounds.Clay` y entrar en `Grounds.Rock` para hallar hierro.

A diferencia de las vetas de carbón, las de hierro también se extienden en vertical. Todos los bloques de una veta de hierro están siempre pegados unos a otros; nunca se conectan solo en diagonal.

Las vetas de hierro empiezan siendo pequeñas y necesitarás algo de suerte para encontrarlas. Mejorar el hierro aumenta el tamaño máximo de las vetas y facilita encontrarlas por casualidad. Para encontrarlas de forma fiable, debes desbloquear la [prospección](docs/unlocks/prospecting.md).

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
# Excava hasta que aparezca un bloque de hierro
while get_ground_type() != Grounds.Iron:
    dig()

# Extrae el hierro
dig()
}}

---

[Estadísticas](docs/stats.md)      [Minería](docs/unlocks/mining.md)      [Prospección de hierro](docs/unlocks/prospecting.md)      [Sentidos subterráneos](docs/unlocks/underground_senses.md)

[move()](functions/move)      [dig()](functions/dig)

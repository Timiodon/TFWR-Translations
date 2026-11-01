[<- Exploitation minière](docs/unlocks/mining.md) <right>[Bambou ->](docs/unlocks/bamboo.md)
<right>[Citrouilles pétrifiées ->](docs/unlocks/petrified_pumpkins.md)
<right>[Perlite et terreau ->](docs/unlocks/special_soils.md)
---
# Riz
Sous la surface et la couche de `Grounds.Dirt`, tu trouveras une fine couche de `Grounds.Clay`. Ce sol fertile et détrempé est idéal pour planter du riz.

Le code suivant peut t’aider à creuser jusqu’à l’argile et à planter du riz :
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

Tant que le drone est au-dessus d’un bloc de `Grounds.Clay`, tu peux utiliser `plant(Entities.Rice)` pour y planter du riz, `can_harvest()` pour vérifier s’il est mûr et enfin `harvest()` pour le récolter.

## Terrasses
Lorsque tu plantes du riz, le sol devient `Grounds.Rice_Terrace` pour lui offrir les conditions idéales pour mûrir. Quand le riz est mûr, le sol sèche et devient `Grounds.Dry_Rice_Terrace`, où tu ne peux plus planter de riz. Heureusement, la couche fait plusieurs blocs d’épaisseur : tu peux retirer le bloc avec `dig()` et replanter sur la `Grounds.Clay` située dessous. Si la couche est épuisée, utilise `clear()` pour réinitialiser le monde et creuse jusqu’à une nouvelle couche.

---

[Statistiques](docs/stats.md)      [Exploitation minière](docs/unlocks/mining.md)      [Sens souterrains](docs/unlocks/underground_senses.md)      [If](docs/scripting/if.md)      [Boucle for](docs/scripting/for.md)

[harvest()](functions/harvest)      [plant()](functions/plant)      [move()](functions/move)      [dig()](functions/dig)      [get_ground_type()](functions/get_ground_type)

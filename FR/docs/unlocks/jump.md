[<- Charbon](docs/unlocks/coal.md)
---
# Saut
Ton drone a débloqué la commande `jump()`. Pour l’utiliser, passe-lui un déblocage en argument, par exemple `Unlocks.Iron`.

Cette commande permet de cibler certaines ressources cachées dans le sol et de sauter instantanément jusqu’à elles. Elle est particulièrement utile pour le débogage ou pour rejoindre un filon que tu viens de manquer.

Après le saut, la ressource ciblée devrait se trouver à 3 blocs au maximum de la surface supérieure. `jump()` ne peut être utilisée qu’une seule fois par exécution du programme ; toute tentative supplémentaire provoquera une erreur.

L’exemple suivant saute vers le [riz](docs/unlocks/rice.md), trouve l’argile et plante une rangée de rizières en terrasses :
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
    "items": [{"item": "hay", "n": 10}],
    "world_size": {"x": 4, "y": 4},
    "execution_speed": 1,
    "digging_speed": 4,
    "action_ticks": 200,
    "operation_ticks": 20,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer", "mushrooms"],
    "starting_chunk": 0
}
#CODE
# Sauter près du riz
jump(Unlocks.Rice)

# Planter une rangée de rizières en terrasses
for i in range(get_world_size()):
    # Le saut est imprécis, creuser les derniers blocs
    while get_ground_type() != Grounds.Clay:
        dig()

    plant(Entities.Rice)

    move(East)
}}

## Déblocages compatibles
`jump()` fonctionne uniquement avec les déblocages miniers suivants :
- Charbon
- Fer
- Quartz
- Riz
- Citrouilles pétrifiées
- Sols spéciaux
- Pyramide
- Carte au trésor
- Champignons
- Dynamite

---

[jump()](functions/jump)

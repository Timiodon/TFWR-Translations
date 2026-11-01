[<- Exploitation minière](docs/unlocks/mining.md)
---
# Sens souterrains
Ajoutons quelques capteurs pour que ton drone puisse s’orienter sous terre.

## Position Z
Tu peux maintenant utiliser `get_pos_z()` pour connaître la hauteur du drone (elle commence à 0 et devient négative à mesure que le drone descend).

{{codeexample 
{
    "camera_position": {"x": -1.5, "y": 0, "z": 10},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "exclude_unlocks": ["watering", "fertilizer"],
    "items": [],
    "world_size": {"x": 5, "y": 5},
    "execution_speed": 2,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 1
}
#SETUP
move(North)
move(North)
move(East)
move(East)
#CODE
print(get_pos_z())
dig()
dig()
dig()
print(get_pos_z())
}}

## Type de sol
`get_ground_type()` renvoie le type de sol sous le drone. Tu peux lui passer une direction en argument — par exemple `get_ground_type(North)` — pour obtenir le type de sol d’une case voisine.

Voici comment vérifier si le bloc sous le drone est de la terre :

{{codeexample 
{
    "camera_position": {"x": -1.5, "y": 0, "z": 8},
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
    "execution_speed": 2,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 1
}
#CODE
dig()
if get_ground_type() == Grounds.Dirt:
    do_a_flip()
}}

## Dureté et stabilité
`get_hardness()` renvoie la dureté de la case de sol sous le drone. Tu peux lui passer une direction en argument, comme `get_hardness(North)`. Plus la dureté d’une case est élevée, plus elle est longue à forer.

`get_stability()` renvoie la stabilité de la case de sol sous le drone. Tu peux lui passer une direction en argument, comme `get_stability(North)`. Une stabilité de 1 signifie que le bloc peut supporter une différence de hauteur de 1 avant de s’effondrer.

{{codeexample 
{
    "camera_position": {"x": -1, "y": 0, "z": 10},
    "show_image": true,
    "image_size": {"x": 800, "y": 250},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "exclude_unlocks": ["watering", "fertilizer"],
    "world_size": {"x": 5, "y": 5},
    "execution_speed": 2,
    "action_ticks": 200,
    "operation_ticks": 20,
    "seed": 0
}
#SETUP
jump(Unlocks.Rice)
#CODE
print(get_hardness(), "|", get_stability())
while get_hardness() == 1:
    dig()

print(get_hardness(), "|", get_stability())
while get_hardness() == 2 and get_stability() == 3:
    dig()
}}

Lorsque le drone creuse vers le bas, les quatre blocs directement adjacents sont supprimés quelle que soit leur stabilité, sauf si le bloc possède une fonction spéciale. L’argile, le fer et le quartz, par exemple, ne sont pas supprimés par cette règle. Ils peuvent néanmoins toujours s’effondrer si leur stabilité est insuffisante.
---

[Exploitation minière](docs/unlocks/mining.md)      [Sens](docs/unlocks/senses.md)

[get_pos_z()](functions/get_pos_z)      [get_ground_type()](functions/get_ground_type)      [get_hardness()](functions/get_hardness)      [get_stability()](functions/get_stability)

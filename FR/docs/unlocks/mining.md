[<- Expansion 1](docs/unlocks/expand_1.md) <right>[Sens souterrains ->](docs/unlocks/underground_senses.md)
<right>[Riz ->](docs/unlocks/rice.md)
<right>[Charbon ->](docs/unlocks/coal.md)
---
# Exploitation minière

Ton drone a désormais accès à une foreuse rudimentaire qui lui permet de chercher des trésors sous terre.

Tu peux utiliser la commande `dig()` pour forer le bloc situé sous toi.

Pour commencer, récoltons quelques blocs :

{{codeexample 
{
    "camera_position": {"x": -1, "y": 0, "z": 8},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": false,
    "autoplay": true,
    "items": [{"item": "hay", "n": 100}, {"item": "wood", "n": 100}],
    "world_size": {"x": 4, "y": 4},
    "execution_speed": 2,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer", "mushrooms", "coal", "special_soils"]
}
#SETUP
move(North)
move(East)
#CODE
dig()
do_a_flip()
dig()
do_a_flip()
dig()
do_a_flip()
clear()
}}

Si tu veux retourner à la surface, tu peux utiliser `clear()` à tout moment. Cela restaure également ta ferme.

Survoler un bloc affiche son nom, sa stabilité et sa dureté.

# Foreuse

À mesure que tu creuses, tu remarqueras que les blocs deviennent plus durs et que leur forage prend donc plus de temps. Heureusement, nous pouvons améliorer notre foreuse !

Tu peux utiliser `get_hardness()` pour connaître la dureté du bloc situé sous toi. Si tu rencontres une zone de blocs particulièrement durs, il peut être judicieux de les contourner afin de progresser plus vite :

`while True:
    if get_hardness() < 5:
        dig()
    else:
        move(East)`

Bien sûr, plus tu descends, plus les blocs deviennent résistants. Cette stratégie est utile, mais elle a ses limites.

## Effondrements

Forer vers le bas provoque l’effondrement des blocs alentour. Les quatre blocs adjacents au drone sont toujours détruits. Ensuite, l’effondrement se propage selon la stabilité du sol. Un bloc de stabilité 1, comme une prairie, supporte une différence de hauteur de 1. Autrement dit, si une prairie a un voisin vertical ou horizontal dont la coordonnée z est inférieure d’au moins 2 blocs, elle est détruite.

La stabilité d’un bloc figure dans son infobulle au survol.

Lorsqu’un bloc s’effondre, tous les blocs situés au-dessus de lui sont également supprimés. Tu ne reçois des ressources que pour les blocs directement forés par le drone : ceux perdus dans un effondrement sont détruits sans rien rapporter.

---

[Sens souterrains](docs/unlocks/underground_senses.md)      [Boucle while](docs/scripting/while.md)

[move()](functions/move)      [dig()](functions/dig)

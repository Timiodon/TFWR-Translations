[<- Exploitation minière](docs/unlocks/mining.md) <right>[Fer ->](docs/unlocks/iron.md)
<right>[Saut ->](docs/unlocks/jump.md)
---
# Charbon
Différents minerais se cachent sous terre, attendant que tu les trouves et les extraies. En traversant la surface pour creuser dans `Grounds.Dirt`, le premier minerai que tu trouveras sera le charbon.

Extraire du charbon ne demande rien de spécial : exécute simplement `dig()` lorsque le drone est juste au-dessus d’un bloc de `Grounds.Coal`. Utilise `get_ground_type()` pour examiner le sol sous le drone et `get_ground_type(direction)` pour examiner les quatre blocs voisins.

Le programme suivant est un bon point de départ pour chercher du charbon. Il creuse vers le bas à la recherche d’une couche de charbon.
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
    "world_size": {"x": 4, "y": 4},
    "execution_speed": 4,
    "digging_speed": 2,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 2,
    "exclude_unlocks": ["watering", "fertilizer"]
}
#SETUP
move(North)
move(East)
move(East)
#CODE
# Creuser jusqu’à l’apparition d’un bloc de charbon
while get_ground_type() != Grounds.Coal:
    dig()

# Extraire le charbon
dig()
}}

## À propos des effondrements
Tu ne reçois du charbon que pour les blocs que tu creuses directement, pas pour ceux qui s’effondrent autour du drone. Garde cela à l’esprit pour extraire un maximum de charbon et en perdre le moins possible dans les effondrements.

## Structure des filons
Les filons forment des couches horizontales d’un bloc d’épaisseur, que tu dois découvrir par hasard en creusant la terre. La plupart des blocs de charbon d’une couche se touchent directement, mais certains ne sont reliés qu’en diagonale.

Les gisements de charbon grandissent avec la ferme : améliore encore [Agrandir](unlocks/expand) pour pouvoir extraire davantage de charbon.

## Stratégie
<spoiler=afficher un indice>
Une stratégie simple, surtout pour les petites fermes, consiste à creuser tous les blocs à la profondeur où tu as trouvé du charbon. Pour gagner en efficacité, repère les blocs de charbon avec `get_ground_type(direction)` et évite de perdre du temps à passer sur la terre. Fais attention aux connexions diagonales, que tu manqueras si tu ne te déplaces que sur les blocs de charbon.
</spoiler>

---

[Statistiques](docs/stats.md)      [Exploitation minière](docs/unlocks/mining.md)      [Sens souterrains](docs/unlocks/underground_senses.md)

[move()](functions/move)      [get_ground_type()](functions/get_ground_type)      [dig()](functions/dig)

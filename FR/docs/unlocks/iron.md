[<- Charbon](docs/unlocks/coal.md) <right>[Quartz ->](docs/unlocks/quartz.md)
<right>[Prospection du fer ->](docs/unlocks/prospecting.md)
<right>[Carte au trésor ->](docs/unlocks/treasure_map.md)
---
# Fer
Après avoir trouvé du charbon dans `Grounds.Dirt`, creuse plus bas, au-delà de la couche de `Grounds.Clay`, jusque dans `Grounds.Rock` pour trouver du fer.

Contrairement aux filons de charbon, ceux de fer s’étendent aussi verticalement. Tous les blocs d’un filon de fer se touchent directement ; ils ne sont jamais reliés uniquement en diagonale.

Les filons de fer sont petits au début et il te faudra un peu de chance pour les trouver. Améliorer le fer augmente la taille maximale des filons et facilite leur découverte par hasard. Pour les trouver à coup sûr, débloque la [prospection](docs/unlocks/prospecting.md).

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
# Creuser jusqu’à l’apparition d’un bloc de fer
while get_ground_type() != Grounds.Iron:
    dig()

# Extraire le fer
dig()
}}

---

[Statistiques](docs/stats.md)      [Exploitation minière](docs/unlocks/mining.md)      [Prospection du fer](docs/unlocks/prospecting.md)      [Sens souterrains](docs/unlocks/underground_senses.md)

[move()](functions/move)      [dig()](functions/dig)

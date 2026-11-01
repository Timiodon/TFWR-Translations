[<- Fer](docs/unlocks/iron.md) <right>[Champignon ->](docs/unlocks/mushroom.md)
---
# Quartz
Après les filons de fer dans `Grounds.Rock`, tu trouveras du quartz au fond de la couche de roche et dans la `Grounds.Dirt` dure située dessous (vérifie la dureté avec `get_hardness()` grâce aux [sens souterrains](docs/unlocks/underground_senses.md)).

Le code suivant traverse la terre pour atteindre la couche de roche. Il prospecte alors continuellement le quartz en creusant, jusqu’à ce que la distance soit inférieure à 2. Enfin, il affiche la distance atteinte.
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
    "items": [{"item": "block", "n": 1}, {"item": "iron", "n": 100}],
    "world_size": {"x": 3, "y": 3},
    "execution_speed": 8,
    "digging_speed": 16,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 9,
    "exclude_unlocks": ["watering", "fertilizer", "mushrooms", "dynamite"]
}
#SETUP
move(East)
move(North)
#CODE
# Creuser jusqu’à la couche de roche
while get_ground_type() != Grounds.Rock:
    dig()

# Continuer à creuser jusqu’à approcher un filon de quartz
while prospect_quartz() == None or prospect_quartz() >= 2:
    for i in range(10):
        dig()

# Afficher la distance finale au filon
print(prospect_quartz())
}}

## Structure des filons
Le quartz pousse en filons en forme d’aiguilles qui forment des colonnes verticales, ce qui les rend difficiles à trouver par tâtonnement.

## Prospecter le quartz
Heureusement, nous pouvons utiliser notre fer et le tordre pour fabriquer une sorte de baguette de sourcier qui facilite la localisation de ces filons de quartz. La commande correspondante est `prospect_quartz()`.

`prospect_quartz()` fonctionne différemment de `prospect_iron()`. Au lieu de renvoyer la direction à suivre vers le fer le plus proche, elle renvoie la distance 3D exacte entre le bloc de quartz le plus proche et le drone (distance euclidienne).

Exécuter `prospect_quartz()` coûte 1 fer : mieux vaut donc utiliser cette commande avec parcimonie.

Si `prospect_quartz()` ne trouve aucun quartz à proximité, ou si tu n’as pas assez de fer pour effectuer la recherche, elle renvoie `None`.

## Stratégie
<spoiler=afficher un indice>Tu peux prospecter et te déplacer plusieurs fois pour observer les variations de distance. Sur une surface plane, minimiser la distance peut te placer au-dessus d’un filon de quartz. Une stratégie semblable à la recherche binaire permet de limiter les appels à `prospect_quartz()` et leur consommation de fer.

Des stratégies plus élaborées peuvent utiliser la géométrie 2D pour trouver l’intersection de plusieurs cercles. Tu peux aussi choisir la méthode difficile : une trilatération complète, en intersectant trois sphères pour trouver la position 3D exacte du filon.

Pour calculer une racine carrée, utilise l’opérateur de puissance : par exemple, `16**0.5` donne la racine carrée de 16. Il n’y a pas de fonctions mathématiques intégrées pour la trigonométrie ou les vecteurs ; tu devras les programmer.

Plusieurs filons peuvent se trouver à proximité : des mesures voisines ne désignent donc pas forcément le même filon.</spoiler>

---

[Statistiques](docs/stats.md)      [Exploitation minière](docs/unlocks/mining.md)      [Sens souterrains](docs/unlocks/underground_senses.md)      [Variables](docs/scripting/variables.md)      [Opérateurs](docs/scripting/operators.md)

[move()](functions/move)      [dig()](functions/dig)      [get_ground_type()](functions/get_ground_type)      [prospect_quartz()](functions/prospect_quartz)

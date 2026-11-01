[<- Fer](docs/unlocks/iron.md)
---
# Carte au trésor
Les légendes parlent d’un trésor insaisissable caché par un pirate distrait mort depuis longtemps — ou quelque chose comme ça. Et s’il avait tracé le chemin vers son trésor sur une carte avant de la perdre ? Peut-être l’a-t-il laissée tomber au bord d’une rivière de lave, et la carte a-t-elle été préservée sous une couche de basalte.

Mesurer les blocs de basalte pourrait révéler quelque chose !

<spoiler=dis-m’en plus>
Cherche une couche de `Grounds.Basalt`. Essaie de mesurer le basalte pour voir ce qu’il t’indique. L’indice pourrait te mener à la carte au trésor, et mesurer la carte te donnera certainement le chemin du trésor lui-même — mais sauras-tu déchiffrer ses instructions ?
</spoiler>

<spoiler=dis-moi simplement comment faire>
D’accord, voici le principe : trouve la strate de `Grounds.Basalt` et le bloc de `Grounds.Treasure_Map` situé directement dessous. Tu peux appeler `measure()` sur le basalte pour obtenir la position `(x, y)` du bloc de carte en dessous.

Appelle `measure()` sur le bloc de carte pour obtenir le chemin du trésor sous forme d’une chaîne de lettres indiquant des directions. N, E, S et W correspondent respectivement à `North`, `East`, `South` et `West`, tandis que D signifie « Down » ou « Dig ». Ces lettres décrivent un chemin de blocs `Grounds.Treasure_Path` menant au trésor.

{{codeexample 
{
    "camera_position": {"x": -1.5, "y": 0, "z": 6},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 4, "y": 4},
    "execution_speed": 2,
    "digging_speed": 10,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 3,
    "exclude_unlocks": ["watering", "fertilizer", "dynamite", "iron"]
}

#SETUP
jump(Unlocks.Treasure_Map)
#CODE
# Trouver la couche de basalte
while get_ground_type() != Grounds.Basalt:
    dig()

# Mesurer le basalte renvoie la position de la carte
map_pos = measure()

while get_pos_x() < map_pos[0]:
    move(East)
while get_pos_y() < map_pos[1]:
    move(North)

while get_ground_type() != Grounds.Treasure_Map:
    dig()

# Carte trouvée, la mesurer pour obtenir le chemin
do_a_flip()
instructions = measure()
print("instructions : ", instructions)

# Creuser la carte pour commencer la chasse au trésor
dig()
}}

Tu peux parcourir la chaîne avec une boucle `for` pour la traiter lettre par lettre :
{{codeexample 
{
    "camera_position": {"x": -1.5, "y": 0, "z": 6},
    "show_image": false,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 4, "y": 4},
    "execution_speed": 2,
    "digging_speed": 10,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 3,
    "exclude_unlocks": ["watering", "fertilizer", "dynamite", "iron"]
}
#SETUP
jump(Unlocks.Treasure_Map)
while get_ground_type() != Grounds.Basalt:
    dig()

map_pos = measure()

while get_pos_x() < map_pos[0]:
    move(East)
while get_pos_y() < map_pos[1]:
    move(North)

while get_ground_type() != Grounds.Treasure_Map:
    dig()
#CODE
# Les instructions de la carte sont renvoyées en une seule chaîne
instructions = measure()
# Utiliser for-in pour séparer la chaîne en lettres
for letter in instructions:
    print(letter)
}}

Le drone doit rester au-dessus de blocs de `Grounds.Treasure_Path` en permanence. S’il passe sur un autre type de sol, le chemin se brise et le trésor est perdu.

## Objectif
Au bout du chemin se trouve un bloc `Grounds.Treasure_Goal`. Si le drone ne s’est pas écarté du chemin, une entité `Entities.Underground_Treasure` apparaîtra dessus. Le drone peut appeler `harvest()` sur le coffre pour récupérer son or.

## Récompense
La quantité d’or est proportionnelle à la longueur du chemin du trésor. Améliorer le déblocage Carte au trésor augmente la profondeur du chemin, tandis qu’améliorer Agrandir lui donne plus d’espace pour se déplacer latéralement. Ces deux améliorations augmentent la longueur du chemin et la quantité d’or que tu trouveras.

## Plusieurs drones
Le drone qui creuse le bloc de la carte au trésor doit trouver le trésor sans quitter les blocs du chemin.
</spoiler>

---

[Statistiques](docs/stats.md)      [Boucle for](docs/scripting/for.md)      [Tuples](docs/scripting/tuples.md)      [Sens souterrains](docs/unlocks/underground_senses.md)

[harvest()](functions/harvest)      [move()](functions/move)      [dig()](functions/dig)      [measure()](functions/measure)

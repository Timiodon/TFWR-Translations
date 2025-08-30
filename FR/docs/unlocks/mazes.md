# Labyrinthes
`Items.Weird_Substance`, obtenu en [fertilisant](docs/unlocks/fertilizer.md) les plantes, a un effet étrange sur les buissons. Si le drone est sur un buisson et que tu appelles `use_item(Items.Weird_Substance, amount)`, le buisson se transformera en un labyrinthe de haies.
La taille du labyrinthe dépend de la quantité de `Items.Weird_Substance` utilisée (le deuxième argument de l'appel `use_item()`).
Sans améliorations de labyrinthe, utiliser `n` `Items.Weird_Substance` créera un labyrinthe de `n`x`n`. Chaque niveau d'amélioration du labyrinthe double le trésor, mais il double aussi la quantité de `Items.Weird_Substance` nécessaire.
Donc pour créer un labyrinthe de la taille du champ :

`plant(Entities.Bush)
substance = get_world_size() * 2**(num_unlocked(Unlocks.Mazes) - 1)
use_item(Items.Weird_Substance, substance)`


Pour une raison inconnue, le drone ne peut pas voler au-dessus des haies, même si elles n'ont pas l'air si hautes.

Un trésor est caché quelque part dans la haie. Utilise `harvest()` sur le trésor pour recevoir une quantité d'or égale à la surface du labyrinthe. (Par exemple, un labyrinthe de 5x5 rapportera 25 d'or.)

Si tu utilises `harvest()` ailleurs, le labyrinthe disparaîtra simplement.

`get_entity_type()` est égal à `Entities.Treasure` si le drone est sur le trésor et `Entities.Hedge` partout ailleurs dans le labyrinthe.

Les labyrinthes ne contiennent pas de boucles, à moins de les réutiliser (voir ci-dessous comment faire). Il n'y a donc aucun moyen pour le drone de revenir à la même position sans faire demi-tour.

Tu peux vérifier s'il y a un mur en essayant de le traverser.
`move()` retourne `True` en cas de succès et `False` sinon.

Si tu n'as aucune idée de comment atteindre le trésor, jette un œil à l'indice 1. Il te montrera comment aborder ce genre de problème.


Pour un défi supplémentaire, tu peux aussi réutiliser le labyrinthe en utilisant à nouveau la même quantité de `Items.Weird_Substance` sur le trésor.
Cela augmentera la quantité d'or dans le trésor de la valeur d'un labyrinthe complet et le déplacera à une position aléatoire dans le labyrinthe.

Utiliser `measure()` sur un trésor retourne sa future position sous forme de tuple.
`next_x, next_y = measure()`

Chaque fois que le trésor est déplacé, un mur aléatoire peut être retiré du labyrinthe. Les labyrinthes réutilisés peuvent donc contenir des boucles.

Note que les boucles dans le labyrinthe rendent les choses beaucoup plus difficiles, car cela signifie que tu peux revenir au même endroit sans faire demi-tour.
Réutiliser un labyrinthe ne rapporte pas plus d'or que d'en récolter un et d'en faire apparaître un nouveau.
C'est un défi 100% optionnel que tu peux tout à fait ignorer.
Cela n'en vaut la peine que si les informations supplémentaires et les raccourcis t'aident à résoudre le labyrinthe plus rapidement.

Le même labyrinthe peut être résolu un maximum de 300 fois. Cela correspond à 299 déplacements. Après cela, utiliser de la substance étrange sur le trésor n'augmentera plus l'or qu'il contient et `measure()` retournera `None`.

<spoiler=montrer l'indice 1>Voici une approche générale pour résoudre le problème :

Crée un labyrinthe et imagine que tu es le drone.

Pense à la façon dont tu essaierais de trouver le trésor si tu étais dans le labyrinthe.

Écris ta stratégie étape par étape pour que quelqu'un d'autre puisse la suivre sans réfléchir.

Maintenant, essaie de traduire tes étapes en code.
</spoiler>
<spoiler=montrer l'indice 2>Tant qu'il n'y a pas de boucles : tous les murs ne forment en réalité qu'un seul grand mur connecté. Si tu suis le mur, il te guidera à travers tout le labyrinthe.
Cette approche nécessite très peu de code et tu n'as pas besoin de savoir où tu es déjà allé. Une dizaine de lignes de code suffisent.</spoiler>
<spoiler=montrer l'indice 3>Au lieu de déplacer le drone dans des directions absolues comme est ou ouest, il peut être très utile de le déplacer dans des directions relatives comme "tourner à droite" ou "tourner à gauche". Pour ce faire, tu dois garder en mémoire la direction actuelle du drone. Le drone ne tourne jamais vraiment, mais tu peux maintenir une rotation "virtuelle" dans le code.
L'astuce d'index suivante est utile pour cela :

`directions = [North, East, South, West]
index = 0`

Utilise `% 4` pour lui permettre de tourner "en cercle", de sorte qu'après `West`, il revienne à `North`.
`# tourner à droite
index = (index + 1) % 4`

`# tourner à gauche
index = (index - 1) % 4

move(directions[index])`</spoiler>
<spoiler=montrer l'indice 4>Si tu n'arrives pas à le résoudre, tu peux toujours te faciliter la vie et le faire de manière moins efficace.
Résoudre un labyrinthe de `1`x`1` est trivial.</spoiler>
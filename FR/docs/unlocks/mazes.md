# Labyrinthes
`Items.Weird_Substance`, qui est obtenu en [fertilisant](docs/unlocks/fertilizer.md) les plantes, a un effet étrange sur les buissons. Si le drone est sur un buisson et que vous appelez `use_item(Items.Weird_Substance, amount)`, le buisson se transformera en un labyrinthe de haies.
La taille du labyrinthe dépend de la quantité d'`Items.Weird_Substance` utilisée (le deuxième argument de l'appel `use_item()`).
Sans améliorations de labyrinthe, l'utilisation de `n` `Items.Weird_Substance` donnera un labyrinthe de `n`x`n`. Chaque niveau d'amélioration de labyrinthe double le trésor, mais il double également la quantité d'`Items.Weird_Substance` nécessaire.
Donc pour faire un labyrinthe de champ complet :

`plant(Entities.Bush)
n_substance = get_world_size() * 2**(num_unlocked(Unlocks.Mazes) - 1)
use_item(Items.Weird_Substance, n_substance)`


Pour une raison quelconque, le drone ne peut pas voler au-dessus des haies, même si elles n'ont pas l'air si hautes.

Il y a un trésor caché quelque part dans la haie. Utilisez `harvest()` sur le trésor pour recevoir de l'or égal à la superficie du labyrinthe. (Par exemple, un labyrinthe de 5x5 rapportera 25 or.)

Si vous utilisez `harvest()` ailleurs, le labyrinthe disparaîtra simplement.

`get_entity_type()` est égal à `Entities.Treasure` si le drone est sur le trésor et `Entities.Hedge` partout ailleurs dans le labyrinthe.

Les labyrinthes ne contiennent aucune boucle à moins que vous ne réutilisiez le labyrinthe (voir ci-dessous comment réutiliser un labyrinthe). Il n'y a donc aucun moyen pour le drone de se retrouver à la même position sans revenir en arrière.

Vous pouvez vérifier s'il y a un mur en essayant de le traverser.
`move()` retourne `True` s'il a réussi et `False` sinon.

Si vous n'avez aucune idée de comment atteindre le trésor, jetez un œil à l'Indice 1. Il vous montre comment aborder un problème comme celui-ci.


Pour un défi supplémentaire, vous pouvez également réutiliser le labyrinthe en utilisant la même quantité d'`Items.Weird_Substance` sur le trésor à nouveau.
Cela augmentera la quantité d'or dans le trésor d'un labyrinthe complet et le déplacera à une position aléatoire dans le labyrinthe.

Utiliser `measure()` sur un trésor retourne la position vers laquelle il se déplacera, sous forme de tuple.
`next_x, next_y = measure()`

Chaque fois que le trésor est déplacé, un mur aléatoire peut être retiré du labyrinthe. Les labyrinthes réutilisés peuvent donc contenir des boucles.

Notez que les boucles dans le labyrinthe le rendent beaucoup plus difficile car cela signifie que vous pouvez vous retrouver au même endroit sans revenir en arrière.
Réutiliser un labyrinthe ne vous donne pas plus d'or que de simplement récolter et faire apparaître un nouveau labyrinthe.
C'est un défi 100% supplémentaire que vous pouvez simplement ignorer.
Cela ne vaut le coup que si les informations supplémentaires et les raccourcis vous aident à résoudre le labyrinthe plus rapidement.

Le même labyrinthe peut être résolu un maximum de 300 fois. Cela correspond à 299 relocalisations. Après cela, utiliser de la substance étrange sur le trésor n'augmentera plus l'or qu'il contient et `measure()` retournera `None`.

<spoiler=montrer l'indice 1>Voici une approche générale pour résoudre le problème :

Créez un labyrinthe et imaginez que vous êtes le drone.

Pensez à la façon dont vous essaieriez de trouver le trésor si vous étiez dans le labyrinthe.

Écrivez votre stratégie étape par étape pour que quelqu'un d'autre puisse la suivre sans réfléchir.

Maintenant, essayez de traduire vos étapes en code.
</spoiler>
<spoiler=montrer l'indice 2>Tant qu'il n'y a pas de boucles : Tous les murs ne sont en réalité qu'un seul grand mur connecté. Si vous suivez le mur, il vous mènera à travers tout le labyrinthe.
Cette approche nécessite très peu de code et vous n'avez pas besoin de garder une trace de là où vous êtes déjà allé. Environ 10 lignes de code suffisent.</spoiler>
<spoiler=montrer l'indice 3>Au lieu de déplacer le drone dans des directions absolues comme est ou ouest, il peut être très utile de le déplacer dans des directions relatives comme "tourner à droite" ou "tourner à gauche". Pour ce faire, vous devez garder une trace de la direction dans laquelle le drone se déplace actuellement. Le drone ne tourne jamais réellement, mais vous pouvez toujours garder une rotation "virtuelle" dans le code.
L'astuce d'index suivante est utile pour cela :

`directions = [North, East, South, West]
index = 0`

Utilisez `% 4` pour lui permettre de tourner "autour du cercle", de sorte qu'après `West`, il revienne à `North`.
`# tourner à droite
index = (index + 1) % 4`

`# tourner à gauche
index = (index - 1) % 4

move(directions[index])`</spoiler>
<spoiler=montrer l'indice 4>Si vous ne pouvez pas le résoudre, vous pouvez toujours vous simplifier la vie et le faire de manière moins efficace.
Résoudre un labyrinthe de `1`x`1` est trivial.</spoiler>
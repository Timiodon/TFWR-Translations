# La 1.0 est enfin là !
Après plus de trois ans et demi de développement constant, plus de 20 mises à jour et vos incroyables retours, l'accès anticipé est enfin terminé.

## Quoi de neuf dans la 1.0 ?
- Plusieurs drones pour maximiser votre agriculture
- Un arbre de déverrouillage retravaillé avec une progression plus exponentielle
- 60 succès pour tester vos compétences
- Déverrouiller certains succès donnera des chapeaux spéciaux à votre drone
- Une refonte complète du son
- Une nouvelle piste musicale
- Des améliorations de confort et divers correctifs
- Changements majeurs : les améliorations seront partiellement réinitialisées. La réutilisation des labyrinthes fonctionne un peu différemment.

Merci beaucoup à vous tous d'avoir soutenu The Farmer Was Replaced de l'accès anticipé jusqu'à sa sortie complète. 
J'ai hâte de voir comment vous utiliserez les multiples drones de manière créative et astucieuse !
-Timon

N'hésitez pas non plus à nous rejoindre sur Discord : 
[Discord](https://discord.com/invite/kj33cJkeJn)

## Notes de mise à jour complètes
Changements majeurs :
-En raison de la refonte de l'arbre technologique, les numéros d'amélioration des anciennes sauvegardes ne seront plus valides. Le jeu réinitialisera toutes les améliorations à un niveau raisonnable lorsque vous ouvrirez une ancienne sauvegarde.
-Si vous réutilisez des labyrinthes, vous devez maintenant d'abord repositionner le trésor, puis mesurer la position, au lieu de mesurer d'abord et de repositionner ensuite.

Gameplay :
-Ajout d'infobulles avec des informations utiles en survolant les cases de la ferme.
-Utiliser `measure()` n'importe où dans le labyrinthe renvoie maintenant toujours la position du trésor actuel. Vous n'avez plus besoin de mesurer le trésor spécifiquement.
-Il y a maintenant une fonction `can_move()` pour le labyrinthe.
-Les citrouilles grandissent maintenant jusqu'à 6x6 au lieu de 5x5.
-Le comportement de séchage du sol a légèrement changé. Au lieu de sécher de 1 % toutes les 0,8 à 1,2 secondes, chaque case de sol a maintenant 10 % de chance de sécher toutes les 0,1 secondes.
-Le temps de croissance des cactus est maintenant toujours d'exactement 1 seconde.
-Les citrouilles laissent maintenant derrière elles une citrouille morte pour indiquer qu'elles sont mortes.
-Ajout de `pet_the_piggy()`.
-`num_unlocked()` se déverrouille maintenant déjà avec les Sens.

Audio :
-L'audio a été complètement refait.
-Il y a maintenant de la musique quand vous lancez le jeu !

Visuels :
-Les visuels de l'arbre technologique ont été complètement retravaillés.
-Le panneau d'inventaire en haut à gauche de l'écran a maintenant un bel effet visuel de ramassage d'objet.
-Les cactus sont maintenant marron quand ils ne sont pas correctement triés pour que ce soit plus visible.
-Les plantes sont maintenant visibles immédiatement après avoir été plantées, même si elles n'ont pas encore poussé.

Éditeur de code :
-Double-cliquer sur des identifiants avec des underscores sélectionne maintenant l'identifiant entier.
-Si l'option « tabulations en espaces » est désactivée, les espaces d'indentation sont maintenant convertis en tabulations.
-Le zoom est maintenant beaucoup plus fluide.
-Le compléteur de code est maintenant bien conscient des imports et peut donner des suggestions depuis d'autres fichiers.
-Ajout de différents curseurs pour l'édition de texte et le redimensionnement des fenêtres.
-Les pas du débogueur sont maintenant basés sur la ligne de code au lieu des ticks de simulation.

Autres :
-Vous pouvez maintenant enchaîner les opérateurs de comparaison comme en Python.
-`get_cost(Entities.Hedge)` et `get_cost(Entities.Treasure)` retournent maintenant le coût d'un labyrinthe de 1x1.
-Ajout d'un paramètre de résolution.
-Ajout d'un paramètre pour désactiver les surlignages clignotants quand le code s'exécute.
-L'exécution du code a été encore optimisée, permettant au jeu de tourner plus fluidement pendant que le code s'exécute.
-Ajout d'une touche « Afficher/Cacher l'ATH ».

Correctifs :
-Certains des cas les plus courants où le surlignage du code était visible à travers d'autres fenêtres ont été corrigés.
-Les actions comme le labourage ne peuvent plus affecter le comportement de séchage de l'eau.
-Correction des problèmes de raccourcis clavier sur les claviers non américains.
-Correction de la tirelire qui s'éloignait parfois très loin de la ferme.
-Correction de l'engrais qui n'infectait pas les plantes entièrement développées.
-Correction de `set_world_size(get_world_size())` qui réinitialisait la position du drone.
-Correction d'une interaction entre la simulation et le dinosaure qui laissait beaucoup de pommes derrière.
-Correction du bug qui faisait bouger les messages d'erreur quand on cliquait sur minimiser puis qu'on ouvrait le menu.
-Correction des messages d'erreur qui apparaissaient pendant que vous tapiez encore.

Changements majeurs des anciennes mises à jour que vous auriez pu manquer :
-Les fonctions définies dans d'autres fichiers (fenêtres dans le jeu) ne sont plus importées implicitement. Vous devez maintenant déverrouiller et utiliser des instructions d'importation explicites comme en Python (voir le déverrouillage de l'importation).
-`Items.Bones` a été renommé en `Items.Bone` pour que tous les objets soient au singulier.
-`Entities.Carrots` a été renommé en `Entities.Carrot` pour que toutes les entités soient au singulier.
-`Grounds.Turf` a été renommé en `Grounds.Grassland` pour que ce soit plus facile à comprendre.
-`Items.Water_Tank` a été renommé en `Items.Water` car la fonctionnalité de remplissage du réservoir a été supprimée.
-`Unlocks.Benchmark` a été remplacé par `Unlocks.Timing`.
-`get_op_count()` a été renommé en `get_tick_count()`.
-`set_farm_size()` a été renommé en `set_world_size()` pour être cohérent avec `get_world_size()`.
-`get_companion()` retourne maintenant un tuple de la forme (entité, (x, y)) au lieu d'une liste.
-`trade()` a été retiré du jeu.
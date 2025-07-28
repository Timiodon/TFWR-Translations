# Dinosaures
Les dinosaures sont des créatures anciennes et majestueuses qui peuvent être cultivées pour leurs os anciens.

Malheureusement, les dinosaures ont disparu il y a longtemps, donc le mieux que nous puissions faire maintenant est de nous déguiser en un.
À cette fin, vous avez reçu le nouveau chapeau de dinosaure.

Le chapeau peut être équipé avec
`change_hat(Hats.Dinosaur_Hat)`

Malheureusement, il ne ressemble pas tout à fait à la publicité...

Si vous équipez le chapeau de dinosaure et avez assez de citrouilles, une [pomme](objects/apple) sera automatiquement achetée et placée sous le drone.
Lorsque le drone est sur une pomme et se déplace à nouveau, il mangera la pomme et sa queue grandira d'une unité. Si vous pouvez vous le permettre, une nouvelle pomme sera achetée et placée à un endroit aléatoire.
La pomme ne peut pas apparaître si quelque chose d'autre est planté là où elle veut être.

La queue du dinosaure sera traînée derrière le drone, remplissant les cases précédentes sur lesquelles le drone s'est déplacé. Si un drone essaie de se déplacer sur la queue, `move()` échouera et retournera `False`. 
Le dernier segment de la queue se déplacera pendant le mouvement, vous pouvez donc vous déplacer dessus. Cependant, si le serpent remplit toute la ferme, vous ne pourrez plus bouger. Vous pouvez donc vérifier si le serpent est entièrement développé en vérifiant si vous ne pouvez plus bouger.

Utiliser `measure()` sur une pomme retournera la position de la prochaine pomme sous forme de tuple.

`next_x, next_y = measure()`

Lorsque le chapeau est de nouveau déséquipé en équipant un chapeau différent, la queue sera récoltée.
Vous recevrez un nombre d'os égal au carré de la longueur de la queue. Donc pour une queue de longueur `n`, vous recevrez `n**2` `Items.Bone`.
Par exemple :
longueur 1 => 1 os
longueur 2 => 4 os
longueur 3 => 9 os
longueur 4 => 16 os
longueur 16 => 256 os
longueur 100 => 10000 os

Le Chapeau de Dinosaure est très lourd, donc si vous l'équipez, `move()` prendra 800 ticks au lieu de 200. Cependant, chaque fois que vous ramassez une pomme, le nombre de ticks utilisés par `move()` est réduit de 3% (arrondi à l'inférieur), car une queue plus longue peut vous aider à vous déplacer.

La boucle suivante affiche le nombre de ticks utilisés par `move()` après n'importe quel nombre de pommes :

`ticks = 800
for i in range(100):
    print("ticks after ", i, " apples: ", ticks)
    ticks -= ticks * 0.03 // 1`

<spoiler=montrer l'indice 1>Si vous continuez à vous déplacer le long du même chemin qui couvre tout le champ, vous pouvez facilement obtenir un serpent qui couvre tout le champ à chaque fois, car vous couvrirez chaque emplacement libre avant de revenir là où se trouve votre queue. Ce n'est pas très efficace, mais ça fonctionne.
Les champs de taille impaire peuvent être plus difficiles. Si vous avez débloqué `Unlocks.Debug2`, vous pouvez changer la taille du champ pour quelque chose de plus pratique.</spoiler>
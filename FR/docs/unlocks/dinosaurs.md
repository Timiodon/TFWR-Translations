# Dinosaures
Les dinosaures sont d'anciennes créatures majestueuses que l'on peut cultiver pour obtenir des os anciens.

Malheureusement, les dinosaures ont disparu il y a longtemps, alors le mieux que l'on puisse faire maintenant, c'est se déguiser en dinosaure.
Pour cela, vous avez reçu le nouveau chapeau dinosaure.

Le chapeau peut être équipé avec
`change_hat(Hats.Dinosaur_Hat)`

Malheureusement, il ne ressemble pas vraiment à la publicité...

Si vous équipez le chapeau dinosaure et que vous avez suffisamment de citrouilles, une [apple](objects/apple) sera automatiquement achetée et placée sous le drone.
Lorsque le drone est au-dessus d'une pomme et se déplace à nouveau, il mangera la pomme et fera pousser sa queue d'un cran. Si vous pouvez vous le permettre, une nouvelle pomme sera achetée et placée à un endroit aléatoire.
La pomme ne peut pas apparaître si quelque chose d'autre est planté là où elle veut être.

La queue du dinosaure sera traînée derrière le drone, remplissant les cases précédentes sur lesquelles le drone s'est déplacé. Si un drone essaie de se déplacer sur la queue, `move()` échouera et renverra `False`.
Le dernier segment de la queue se dégagera pendant le mouvement, ce qui vous permet de vous déplacer dessus. Cependant, si le serpent remplit toute la ferme, vous ne pourrez plus vous déplacer. Vous pouvez donc vérifier si le serpent est entièrement développé en vérifiant si vous ne pouvez plus vous déplacer.

Utiliser `measure()` sur une pomme renverra la position de la prochaine pomme sous forme de tuple.

`next_x, next_y = measure()`

Lorsque le chapeau est retiré en mettant un autre chapeau, la queue sera récoltée.
Vous recevrez des os égaux au carré de la longueur de la queue. Donc pour une queue de longueur `n` vous recevrez `n**2` `Items.Bone`.
Par exemple :
longueur 1 => 1 os
longueur 2 => 4 os
longueur 3 => 9 os
longueur 4 => 16 os
longueur 16 => 256 os
longueur 100 => 10 000 os

Le chapeau dinosaure est très lourd, donc si vous l'équipez, cela fera en sorte que `move()` prenne 800 ticks au lieu de 200. Cependant, chaque fois que vous ramassez une pomme, le nombre de ticks utilisé par `move()` est réduit de 3% (arrondi à l'entier inférieur), parce qu'une queue plus longue peut vous aider à vous déplacer.

La boucle suivante imprime le nombre de ticks utilisés par `move()` après n'importe quel nombre de pommes :

`ticks = 800
for i in range(100):
    print("ticks après ", i, " pommes : ", ticks)
    ticks -= ticks * 0.03 // 1`

<spoiler=montrer l'indice 1>Si vous continuez à vous déplacer le long du même chemin qui couvre tout le champ, vous pouvez facilement obtenir un serpent qui couvre tout le champ à chaque fois, parce que vous couvrirez chaque emplacement libre avant de revenir là où votre queue est. Ce n'est pas très efficace, mais ça marche.
Les champs de taille impaire peuvent être plus difficiles. Si vous avez `Unlocks.Debug2` débloqué, vous pouvez changer la taille du champ pour quelque chose de plus pratique.</spoiler>
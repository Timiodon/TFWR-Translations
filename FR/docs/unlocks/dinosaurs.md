# Dinosaures
Les dinosaures sont d'anciennes créatures majestueuses qui peuvent être élevées pour leurs os anciens.

Malheureusement, les dinosaures ont disparu il y a très longtemps, alors le mieux que nous puissions faire est de nous déguiser.
À cet effet, tu as reçu le nouveau chapeau de dinosaure.

Le chapeau peut être équipé avec
`change_hat(Hats.Dinosaur_Hat)`

Malheureusement, il n'est pas tout à fait comme sur la publicité...

Si tu équipes le chapeau de dinosaure et que tu as assez de citrouilles, une [pomme](objects/apple) sera automatiquement achetée et placée sous le drone.
Quand le drone est sur une pomme et se déplace à nouveau, il mange la pomme et sa queue s'allonge d'une case. Si tu en as les moyens, une nouvelle pomme sera achetée et placée à un endroit aléatoire.
La pomme ne peut pas apparaître si quelque chose d'autre est planté à l'endroit prévu.

La queue du dinosaure est traînée derrière le drone, remplissant les cases sur lesquelles il est passé. Si un drone essaie de se déplacer sur la queue, `move()` échouera et retournera `False`.
Le dernier segment de la queue s'écartera pendant le déplacement, tu pourras donc te déplacer dessus. Cependant, si le serpent remplit toute la ferme, tu ne pourras plus bouger. Tu peux donc vérifier si le serpent est à sa taille maximale en vérifiant si tu ne peux plus te déplacer.

Utiliser `measure()` sur une pomme retournera la position de la prochaine pomme sous forme de tuple.

`next_x, next_y = measure()`

Lorsque le chapeau est retiré en en équipant un autre, la queue est récoltée.
Tu recevras un nombre d'os égal au carré de la longueur de la queue. Ainsi, pour une queue de longueur `n`, tu recevras `n**2` `Items.Bone`.
Par exemple :
longueur 1 => 1 os
longueur 2 => 4 os
longueur 3 => 9 os
longueur 4 => 16 os
longueur 16 => 256 os
longueur 100 => 10000 os

Le chapeau de dinosaure est très lourd, donc si tu l'équipes, `move()` prendra 400 ticks au lieu de 200. Cependant, chaque fois que tu ramasses une pomme, le nombre de ticks utilisés par `move()` est réduit de 3% (arrondi à l'inférieur), car une queue plus longue peut t'aider à te déplacer.

La boucle suivante affiche le nombre de ticks utilisés par `move()` après un certain nombre de pommes :

`ticks = 400
for i in range(100):
    print("ticks après ", i, " pommes : ", ticks)
    ticks -= ticks * 0.03 // 1`

Tu n'as qu'un seul chapeau de dinosaure, donc un seul drone peut le porter.

<spoiler=montrer l'indice 1>Si tu suis toujours le même chemin qui couvre tout le champ, tu peux facilement obtenir un serpent qui couvre tout le champ à chaque fois. Ce n'est pas très efficace, mais ça marche.
Traverser entièrement une très grande ferme peut prendre beaucoup de temps et tu n'auras peut-être pas besoin d'autant d'os. N'hésite pas à utiliser `set_farm_size()` pour ramener la taille de la ferme à quelque chose de plus pratique.</spoiler>
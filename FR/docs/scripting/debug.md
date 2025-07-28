# Débogage
Parfois, votre code ne fonctionne tout simplement pas et vous devez découvrir pourquoi. Il existe quelques outils pour vous aider à le faire.

Le premier est d'exécuter le programme pas à pas.
Vous pouvez passer en mode pas à pas avec le bouton à côté du bouton Exécuter ou en définissant un breakpoint.

Les breakpoints peuvent être ajoutés en cliquant sur le panneau des breakpoints à gauche du code.
![](Breakpoints227)
Lorsque l'exécution atteint la ligne où se trouve le breakpoint, elle passera automatiquement en mode pas à pas.

Lorsque vous déplacez votre souris sur une variable, sa valeur actuelle est affichée.

La fonction `print()` peut également être très utile. Elle écrira toute valeur qui lui est passée directement dans les airs.

Exemples :

Afficher "0.24".
`print(0.24)`

Afficher "True" ou "False".
`print(can_harvest())`

Afficher la position actuelle.
`print(get_pos_x(), get_pos_y())`

La fonction print affiche la valeur directement dans les airs et sur la page [Sortie](docs/output.md).

Écrire dans les airs peut parfois être un peu lent si vous voulez afficher beaucoup de valeurs.
Dans ce cas, vous pouvez utiliser la fonction `quick_print()` qui n'affiche que dans la fenêtre de sortie.

La fenêtre de sortie enregistre également les avertissements et les erreurs, donc si quelque chose ne fonctionne pas comme prévu, il peut être utile de la vérifier.

Lorsque l'exécution s'arrête, la sortie est également écrite dans le fichier output.txt dans le dossier du jeu. [output.txt](persistent_data_path/output.txt).
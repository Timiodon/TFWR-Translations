# Débogage
Parfois, ton code ne fonctionne tout simplement pas et tu dois trouver pourquoi. Il existe quelques outils pour t'aider à le faire.

Le premier est d'exécuter le programme pas à pas.
Tu peux passer en mode pas à pas avec le bouton à côté du bouton Exécuter ou en définissant un point d'arrêt.

Les points d'arrêt peuvent être ajoutés en cliquant sur le panneau des points d'arrêt à gauche du code.
![](Breakpoints227)
Lorsque l'exécution atteint la ligne où se trouve le point d'arrêt, elle passera automatiquement en mode pas à pas.

Lorsque tu passes la souris sur une variable, sa valeur actuelle s'affiche.

La fonction `print()` peut aussi être très utile. Elle écrira toute valeur qui lui est passée directement dans les airs.

Exemples :

Affiche "0.24".
`print(0.24)`

Affiche "True" ou "False".
`print(can_harvest())`

Affiche la position actuelle.
`print(get_pos_x(), get_pos_y())`

La fonction print affiche la valeur directement dans les airs et sur la page [Sortie](docs/output.md).

Écrire dans les airs peut parfois être un peu lent si tu veux afficher beaucoup de valeurs.
Dans ce cas, tu peux utiliser la fonction `quick_print()` qui n'affiche que dans la fenêtre de sortie.

La fenêtre de sortie enregistre également les avertissements et les erreurs, donc si quelque chose ne fonctionne pas comme prévu, il peut être utile de la vérifier.

Lorsque l'exécution s'arrête, la sortie est également écrite dans le fichier output.txt dans le dossier du jeu. [output.txt](persistent_data_path/output.txt).
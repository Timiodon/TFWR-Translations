# Débogage
Parfois, ton code ne fonctionne tout simplement pas et tu dois comprendre pourquoi. Il y a quelques outils pour t'aider à faire ça.

Le premier est d'exécuter le programme étape par étape.
Tu peux entrer en mode pas-à-pas avec le bouton à côté du bouton Exécuter ou en plaçant un breakpoint.

Les breakpoints peuvent être ajoutés en cliquant sur le panneau de breakpoint à gauche du code.
![](Breakpoints227)
Quand l'exécution atteint la ligne où se trouve le breakpoint, elle basculera automatiquement en mode pas-à-pas.

Lorsque tu passes ta souris sur une variable, sa valeur actuelle s'affiche.

La fonction `print()` peut aussi être très utile. Elle écrira toute valeur qui lui est passée directement dans l'air.

Exemples :

Imprime "0.24".
`print(0.24)`

Imprime "True" ou "False".
`print(can_harvest())`

Imprime la position actuelle.
`print(get_pos_x(), get_pos_y())`

La fonction print affiche la valeur directement dans l'air et sur la page [Output](docs/output.md).

Écrire dans l'air peut parfois être un peu lent si tu veux imprimer beaucoup de valeurs.
Dans ce cas, tu peux utiliser la fonction `quick_print()` qui affiche uniquement dans la fenêtre de sortie.

La fenêtre de sortie enregistre également les avertissements et erreurs, donc si quelque chose ne fonctionne pas comme prévu, ça peut être utile de vérifier ça.

Quand l'exécution s'arrête, la sortie est également écrite dans le fichier output.txt dans le dossier du jeu. [output.txt](persistent_data_path/output.txt).
# Chargement des Sauvegardes
Malheureusement, il arrive parfois qu'un fichier de sauvegarde soit corrompu ou que tu perdes des fichiers de code. Si cela t'arrive, tu peux essayer de charger une sauvegarde. Si cela arrive régulièrement, essaie de désactiver le Steam Cloud.

Une sauvegarde est faite à chaque fois que le jeu est sauvegardé, et un petit nombre de sauvegardes sont conservées au cas où tu aurais besoin de restaurer quelque chose.
Ces sauvegardes se trouvent dans le [répertoire de sauvegarde](persistent_data_path/Backup). Ce sont des copies des sauvegardes du [répertoire des sauvegardes](persistent_data_path/Saves).
La manière la plus simple de charger une sauvegarde est de copier le dossier de la sauvegarde spécifique que tu veux charger dans le répertoire des sauvegardes.

Une sauvegarde est un dossier contenant un fichier `save.json` et un tas de fichiers `.py`.
Si tu n'as perdu que quelques fichiers de code, ou si les fichiers de code sont toujours là mais que le fichier `save.json` est corrompu, tu peux aussi remplacer uniquement les parties corrompues par les fichiers correspondants de la sauvegarde.
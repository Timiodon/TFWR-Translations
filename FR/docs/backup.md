# Chargement des sauvegardes
Malheureusement, il arrive parfois qu'un fichier de sauvegarde soit corrompu ou que vous perdiez des fichiers de code. Si cela vous arrive, vous pouvez essayer de charger une sauvegarde. Si cela se produit régulièrement, essayez de désactiver le Steam Cloud.

Une sauvegarde est effectuée à chaque fois que le jeu est sauvegardé, et un petit nombre de sauvegardes sont conservées au cas où vous auriez besoin de restaurer quelque chose.
Ces sauvegardes se trouvent dans le [répertoire de sauvegarde](persistent_data_path/Backup). Ce sont des copies des sauvegardes dans le [répertoire de sauvegarde](persistent_data_path/Saves).
La manière la plus simple de charger une sauvegarde est de copier le dossier de la sauvegarde spécifique que vous souhaitez charger dans le répertoire de sauvegarde.

Une sauvegarde est un dossier avec un fichier `save.json` et un tas de fichiers `.py`.
Si vous n'avez perdu que quelques fichiers de code, ou si les fichiers de code sont toujours là mais que le fichier `save.json` est corrompu, vous pouvez également remplacer uniquement les parties corrompues par les fichiers correspondants de la sauvegarde.
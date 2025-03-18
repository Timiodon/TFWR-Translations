# Charger des sauvegardes
Malheureusement, parfois un fichier de sauvegarde se corrompt ou vous perdez certains fichiers de code. Si cela vous arrive, vous pouvez essayer de charger une sauvegarde. Si cela se produit régulièrement, essayez de désactiver le Steam Cloud.

Une sauvegarde est créée chaque fois que le jeu est sauvegardé, et un petit nombre de sauvegardes est conservé au cas où vous auriez besoin de restaurer quelque chose.
Ces sauvegardes peuvent être trouvées dans le [répertoire de sauvegarde](persistent_data_path/Backup). Ce sont des copies des sauvegardes dans le [répertoire des sauvegardes](persistent_data_path/Saves).
Le moyen le plus simple de charger une sauvegarde est de copier le dossier de la sauvegarde spécifique que vous souhaitez charger dans le répertoire des sauvegardes.

Une sauvegarde est un dossier avec un fichier `save.json` et un ensemble de fichiers `.py`.
Si vous n'avez perdu que quelques fichiers de code, ou si les fichiers de code sont toujours là mais que le fichier `save.json` est corrompu, vous pouvez également remplacer uniquement les parties corrompues par les fichiers correspondants de la sauvegarde.
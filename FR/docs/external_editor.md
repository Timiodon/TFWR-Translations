# Éditeur externe
L'éditeur de texte en jeu est généralement suffisant pour jouer à ce jeu, mais bien sûr, il ne peut pas rivaliser avec des éditeurs de texte plus sophistiqués comme Visual Studio Code.

Le jeu sauvegarde tous les fichiers de code en tant que fichiers .py, vous pouvez donc les éditer avec des éditeurs Python.
Notez que c'est uniquement pour des raisons de commodité. Le langage en jeu n'est pas réellement Python, mais il est suffisamment proche pour que Python IntelliSense fonctionne décemment.
Vous pouvez trouver les fichiers dans le [dossier de sauvegarde](persistent_data_path/Saves).

Chaque sauvegarde contient également un fichier `__builtins__.py`, qui contient des définitions Python intégrées qui correspondent aux intégrations du jeu pour activer IntelliSense.
VS Code est capable de détecter `__builtins__.py` automatiquement, mais certains éditeurs peuvent ne fonctionner que si vous faites `from __builtins__ import *`.

Pour voir les changements externes en jeu sans avoir à recharger la sauvegarde, vous devez activer l'option "File Watcher". Si vous créez ou supprimez des fichiers en externe, vous devrez toujours recharger la sauvegarde pour les voir.

## Utilisation de VS Code
Visual Studio Code est l'éditeur de code recommandé à utiliser avec The Farmer Was Replaced.

Vous pouvez l'installer [ici](https://code.visualstudio.com/download).

Après l'avoir téléchargé, installez l'extension Python dans VS Code.

Une fois que vous l'avez, ouvrez le [dossier](persistent_data_path/Saves) qui contient vos fichiers `.py` dans VS Code. Assurez-vous d'ouvrir le dossier entier, pas seulement les fichiers individuels, sinon le fichier `__builtins__.py` ne fonctionnera pas.

Dans le jeu, assurez-vous d'avoir activé l'option "File Watcher". Maintenant, chaque fois que vous sauvegardez dans VS Code, les changements apparaîtront automatiquement dans le jeu.

C'est tout ! Vous pouvez maintenant écrire votre code dans un éditeur de code professionnel !
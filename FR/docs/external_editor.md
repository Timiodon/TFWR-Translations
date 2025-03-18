# Éditeur Externe
L'éditeur de texte intégré est généralement suffisant pour jouer à ce jeu, mais bien sûr, il ne peut pas rivaliser avec des éditeurs de texte plus sophistiqués comme Visual Studio Code.

Le jeu enregistre tous les fichiers de code sous forme de fichiers .py, donc vous pouvez les éditer avec des éditeurs Python. Notez que c'est uniquement pour votre confort. Le langage du jeu n'est pas réellement Python, mais il est suffisamment proche pour que Python IntelliSense fonctionne correctement dessus.
Vous pouvez trouver les fichiers dans le [dossier de sauvegarde](persistent_data_path/Saves).

Chaque sauvegarde contient également un fichier `__builtins__.py`, qui contient des définitions Python intégrées correspondant aux intégrations du jeu pour activer IntelliSense. VS Code est capable de détecter automatiquement `__builtins__.py`, mais certains éditeurs peuvent ne fonctionner que si vous faites `from __builtins__ import *`.

Pour voir les changements externes dans le jeu sans avoir à recharger la sauvegarde, vous devez activer l'option "File Watcher". Si vous créez ou supprimez des fichiers de manière externe, vous devrez quand même recharger la sauvegarde pour les voir.

## Utiliser VS Code
Visual Studio Code est l'éditeur de code recommandé pour utiliser avec The Farmer Was Replaced.

Vous pouvez l'installer [ici](https://code.visualstudio.com/download).

Après l'avoir téléchargé, installez l'extension Python dans VS Code.

Une fois que vous avez cela, ouvrez le [dossier](persistent_data_path/Saves) qui contient vos fichiers `.py` dans VS Code. Assurez-vous d'ouvrir tout le dossier, pas seulement les fichiers individuels, sinon le fichier `__builtins__.py` ne fonctionnera pas.

Dans le jeu, assurez-vous que l'option "File Watcher" est activée. Maintenant, chaque fois que vous sauvegardez dans VS Code, les changements apparaîtront automatiquement dans le jeu.

Voilà ! Maintenant, vous pouvez écrire votre code dans un éditeur de code professionnel !
# Éditeur Externe
L'éditeur de texte en jeu est généralement suffisant pour jouer à ce jeu, mais bien sûr, il ne peut pas rivaliser avec des éditeurs de texte plus sophistiqués comme Visual Studio Code.

Le jeu sauvegarde tous les fichiers de code en tant que fichiers .py, tu peux donc les modifier avec des éditeurs Python.
Note que c'est uniquement pour la commodité. Le langage en jeu n'est pas réellement Python, mais il est suffisamment proche pour que l'IntelliSense de Python fonctionne décemment dessus.
Tu peux trouver les fichiers dans le [dossier de sauvegarde](persistent_data_path/Saves).

Chaque sauvegarde contient également un fichier `__builtins__.py`, qui contient des définitions Python intégrées qui correspondent aux intégrations du jeu pour activer l'IntelliSense.
VS Code est capable de détecter `__builtins__.py` automatiquement, mais certains éditeurs peuvent ne fonctionner que si tu fais `from __builtins__ import *`.

Pour voir les changements externes en jeu sans avoir à recharger la sauvegarde, tu dois activer l'option "File Watcher". Si tu crées ou supprimes des fichiers en externe, tu devras toujours recharger la sauvegarde pour les voir.

## Utiliser VS Code
Visual Studio Code est l'éditeur de code recommandé à utiliser avec The Farmer Was Replaced.

Tu peux l'installer [ici](https://code.visualstudio.com/download).

Après l'avoir téléchargé, installe l'extension Python dans VS Code.

Une fois que tu as cela, ouvre le [dossier](persistent_data_path/Saves) qui contient tes fichiers `.py` dans VS Code. Assure-toi d'ouvrir le dossier entier, pas seulement les fichiers individuels, sinon le fichier `__builtins__.py` ne fonctionnera pas.

Dans le jeu, assure-toi que l'option "File Watcher" est activée. Maintenant, chaque fois que tu sauvegardes dans VS Code, les changements apparaîtront automatiquement dans le jeu.

C'est tout ! Maintenant, tu peux écrire ton code dans un éditeur de code professionnel !
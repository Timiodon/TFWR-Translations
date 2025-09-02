# Externer Editor
Der im Spiel eingebaute Texteditor ist in der Regel ausreichend, um dieses Spiel zu spielen, aber natürlich kann er nicht mit anspruchsvolleren Texteditoren wie Visual Studio Code mithalten.

Das Spiel speichert alle Codedateien als .py-Dateien, sodass du sie mit Python-Editoren bearbeiten kannst.
Beachte, dass dies nur der Bequemlichkeit dient. Die Sprache im Spiel ist nicht wirklich Python, aber sie ist nah genug dran, dass Python IntelliSense recht gut damit funktioniert.
Du findest die Dateien im [Speicherordner](persistent_data_path/Saves).

Jeder Spielstand enthält auch eine `__builtins__.py`-Datei, die eingebaute Python-Definitionen enthält, die den im Spiel eingebauten Funktionen entsprechen, um IntelliSense zu ermöglichen.
VS Code kann `__builtins__.py` automatisch erkennen, aber einige Editoren funktionieren möglicherweise nur, wenn du `from __builtins__ import *` hinzufügst.

Um externe Änderungen im Spiel zu sehen, ohne den Spielstand neu laden zu müssen, musst du die Option "File Watcher" aktivieren. Wenn du Dateien extern erstellst oder löschst, musst du den Spielstand trotzdem neu laden, um sie zu sehen.

## Verwendung von VS Code
Visual Studio Code ist der empfohlene Code-Editor zur Verwendung mit The Farmer Was Replaced.

Du kannst es [hier](https://code.visualstudio.com/download) installieren.

Nach dem Herunterladen installiere die Python-Erweiterung in VS Code.

Sobald du das hast, öffne den [Ordner](persistent_data_path/Saves), der deine `.py`-Dateien enthält, in VS Code. Stelle sicher, dass du den ganzen Ordner öffnest, nicht nur die einzelnen Dateien, sonst funktioniert die `__builtins__.py`-Datei nicht.

Stelle im Spiel sicher, dass die Option "File Watcher" aktiviert ist. Jetzt werden jedes Mal, wenn du in VS Code speicherst, die Änderungen automatisch im Spiel angezeigt.

Das ist alles! Jetzt kannst du deinen Code in einem professionellen Code-Editor schreiben!
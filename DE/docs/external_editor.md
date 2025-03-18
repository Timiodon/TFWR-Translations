# Externer Editor
Der im Spiel integrierte Texteditor ist normalerweise ausreichend, um dieses Spiel zu spielen, aber natürlich kann er nicht mit ausgefeilteren Texteditoren wie Visual Studio Code mithalten.

Das Spiel speichert alle Code-Dateien als .py-Dateien ab, sodass du sie mit Python-Editoren bearbeiten kannst. Beachte, dass dies nur der Bequemlichkeit dient. Die im Spiel verwendete Sprache ist eigentlich kein Python, aber sie ist nah genug, dass Python IntelliSense damit gut funktioniert. Du findest die Dateien im [Speicherordner](persistent_data_path/Saves).

Jeder Speicherstand enthält auch eine `__builtins__.py`-Datei, die integrierte Python-Definitionen enthält, die den im Spiel genutzten Built-ins entsprechen, um IntelliSense zu ermöglichen. VS Code kann `__builtins__.py` automatisch erkennen, aber einige Editoren funktionieren möglicherweise nur, wenn du `from __builtins__ import *` machst.

Um externe Änderungen im Spiel zu sehen, ohne den Speicherstand neu laden zu müssen, musst du die Option "File Watcher" aktivieren. Wenn du Dateien extern erstellst oder löschst, musst du den Speicherstand trotzdem neu laden, um sie zu sehen.

## Nutzung von VS Code
Visual Studio Code ist der empfohlene Code-Editor für die Nutzung mit The Farmer Was Replaced.

Du kannst es [hier](https://code.visualstudio.com/download) installieren.

Nachdem du es heruntergeladen hast, installiere die Python-Erweiterung in VS Code.

Sobald du dies getan hast, öffne den [Ordner](persistent_data_path/Saves), der deine `.py`-Dateien in VS Code enthält. Achte darauf, den gesamten Ordner zu öffnen und nicht nur die einzelnen Dateien, sonst funktioniert die `__builtins__.py`-Datei nicht.

Stelle im Spiel sicher, dass du die Option "File Watcher" aktiviert hast. Jetzt werden jedes Mal, wenn du in VS Code speicherst, die Änderungen automatisch im Spiel angezeigt.

Das war's! Jetzt kannst du deinen Code in einem professionellen Code-Editor schreiben!
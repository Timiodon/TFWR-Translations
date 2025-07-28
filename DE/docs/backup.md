# Laden von Backups
Leider wird manchmal eine Speicherdatei beschädigt oder du verlierst einige Codedateien. Wenn dir das passiert, kannst du versuchen, ein Backup zu laden. Wenn es regelmäßig passiert, versuche, die Steam Cloud auszuschalten.

Ein Backup wird jedes Mal erstellt, wenn das Spiel gespeichert wird, und eine kleine Anzahl von Backups wird aufbewahrt, falls du etwas wiederherstellen musst.
Diese Backups findest du im [Backup-Verzeichnis](persistent_data_path/Backup). Es sind Kopien der Spielstände im [Speicher-Verzeichnis](persistent_data_path/Saves).
Der einfachste Weg, ein Backup zu laden, besteht darin, den Ordner des spezifischen Backups, das du laden möchtest, in das Speicherverzeichnis zu kopieren.

Ein Spielstand ist ein Ordner mit einer `save.json`-Datei und einer Reihe von `.py`-Dateien.
Wenn du nur ein paar Codedateien verloren hast oder die Codedateien noch vorhanden sind, aber die `save.json`-Datei beschädigt ist, kannst du auch nur die beschädigten Teile durch die entsprechenden Dateien aus dem Backup ersetzen.
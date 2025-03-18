# Loading Backups
Unfortunately, sometimes a save file gets corrupted or you lose some code files. If this happens to you, you can try loading a backup. If it happens regularly, try turning off the Steam Cloud.

A backup is made every time the game is saved, and a small number of backups are kept in case you need to restore something.
These backups can be found in the [backup directory](persistent_data_path/Backup). They are copies of the saves in the [save directory](persistent_data_path/Saves).
The easiest way to load a backup is to copy the folder of the specific backup you want to load to the save directory.

A save is a folder with a `save.json` file and a bunch of `.py` files.
If you only lost a few code files, or the code files are still there but the `save.json` file is corrupted, you can also replace only the corrupted parts with the corresponding files from the backup.
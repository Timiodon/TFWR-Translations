# Caricamento dei Backup
Purtroppo, a volte un file di salvataggio si corrompe o perdi alcuni file di codice. Se ti succede, puoi provare a caricare un backup. Se succede regolarmente, prova a disattivare il Steam Cloud.

Viene creato un backup ogni volta che il gioco viene salvato, e un piccolo numero di backup viene conservato nel caso tu debba ripristinare qualcosa.
Questi backup si trovano nella [cartella backup](persistent_data_path/Backup). Sono copie dei salvataggi nella [cartella salvataggi](persistent_data_path/Saves).
Il modo più semplice per caricare un backup è copiare la cartella del backup specifico che vuoi caricare nella cartella salvataggi.

Un salvataggio è una cartella con un file `save.json` e un po' di file `.py`.
Se hai perso solo alcuni file di codice, o i file di codice sono ancora lì ma il file `save.json` è corrotto, puoi anche sostituire solo le parti corrotte con i file corrispondenti del backup.
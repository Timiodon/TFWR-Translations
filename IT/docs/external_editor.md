# External Editor
L'editor di testo in-game è solitamente sufficiente per giocare a questo gioco, ma ovviamente non può competere con editor di testo più sofisticati come Visual Studio Code.

Il gioco salva tutti i file di codice come file .py, quindi puoi modificarli con editor Python. 
Nota che questo è solo per comodità. La lingua in-game non è effettivamente Python, ma è abbastanza simile da permettere a Python IntelliSense di funzionare decentemente.
Puoi trovare i file nella [cartella di salvataggio](persistent_data_path/Saves).

Ogni salvataggio contiene anche un file `__builtins__.py`, che contiene definizioni Python integrate che corrispondono ai built-in del gioco per abilitare IntelliSense. 
VS Code è in grado di rilevare `__builtins__.py` automaticamente, ma alcuni editor potrebbero funzionare solo se fai `from __builtins__ import *`.

Per vedere le modifiche esterne in-game senza dover ricaricare il salvataggio, devi abilitare l'opzione "File Watcher". Se crei o elimini file esternamente, dovrai comunque ricaricare il salvataggio per vederli.

## Usare VS Code
Visual Studio Code è l'editor di codice raccomandato da usare con The Farmer Was Replaced.

Puoi installarlo [qui](https://code.visualstudio.com/download).

Dopo averlo scaricato, installa l'estensione Python in VS Code.

Una volta fatto ciò, apri la [cartella](persistent_data_path/Saves) che contiene i tuoi file `.py` in VS Code. Assicurati di aprire l'intera cartella, non solo i singoli file, altrimenti il file `__builtins__.py` non funzionerà.

Nel gioco, assicurati di avere attivato l'opzione "File Watcher". Ora, ogni volta che salvi in VS Code, le modifiche appariranno automaticamente nel gioco.

Ecco fatto! Ora puoi scrivere il tuo codice in un editor di codice professionale!
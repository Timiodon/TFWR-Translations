# Cargando Copias de Seguridad
Desafortunadamente, a veces un archivo de guardado se corrompe o pierdes algunos archivos de código. Si esto te sucede, puedes intentar cargar una copia de seguridad. Si sucede regularmente, intenta desactivar la Nube de Steam.

Se hace una copia de seguridad cada vez que se guarda el juego, y se guardan un pequeño número de copias de seguridad en caso de que necesites restaurar algo.
Estas copias de seguridad se pueden encontrar en el [directorio de copias de seguridad](persistent_data_path/Backup). Son copias de los guardados en el [directorio de guardado](persistent_data_path/Saves).
La forma más fácil de cargar una copia de seguridad es copiar la carpeta de la copia de seguridad específica que quieres cargar al directorio de guardado.

Un guardado es una carpeta con un archivo `save.json` y un montón de archivos `.py`.
Si solo perdiste algunos archivos de código, o los archivos de código todavía están allí pero el archivo `save.json` está dañado, también puedes reemplazar solo las partes dañadas con los archivos correspondientes de la copia de seguridad.
# Cargando Copias de Seguridad
Desafortunadamente, a veces un archivo de guardado se corrompe o pierdes algunos archivos de código. Si esto te pasa, puedes intentar cargar una copia de seguridad. Si ocurre regularmente, intenta desactivar la Nube de Steam.

Se hace una copia de seguridad cada vez que se guarda el juego, y se mantienen un pequeño número de copias de seguridad por si necesitas restaurar algo.
Estas copias de seguridad se encuentran en el [directorio de copias de seguridad](persistent_data_path/Backup). Son copias de los guardados en el [directorio de guardados](persistent_data_path/Saves).
La forma más fácil de cargar una copia de seguridad es copiar la carpeta de la copia específica que deseas cargar en el directorio de guardados.

Un guardado es una carpeta con un archivo `save.json` y un montón de archivos `.py`.
Si solo perdiste unos pocos archivos de código, o los archivos de código todavía están allí pero el archivo `save.json` está corrupto, también puedes reemplazar solo las partes corruptas con los archivos correspondientes de la copia de seguridad.
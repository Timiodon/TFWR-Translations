# Editor Externo
El editor de texto en el juego suele ser suficiente para jugar, pero, por supuesto, no puede competir con editores de texto más sofisticados como Visual Studio Code.

El juego guarda todos los archivos de código como archivos .py, por lo que puedes editarlos con editores de Python. Ten en cuenta que esto es solo por comodidad. El idioma en el juego no es realmente Python, pero es lo suficientemente parecido como para que Python IntelliSense funcione decentemente en él. Puedes encontrar los archivos en la [carpeta de guardado](persistent_data_path/Saves).

Cada guardado también contiene un archivo `__builtins__.py`, que incluye definiciones de Python integradas que coinciden con las integradas en el juego para habilitar IntelliSense. VS Code es capaz de detectar `__builtins__.py` automáticamente, pero algunos editores pueden funcionar solo si haces `from __builtins__ import *`.

Para ver los cambios externos en el juego sin tener que recargar la partida, debes habilitar la opción "File Watcher". Si creas o eliminas archivos externamente, aún necesitarás recargar la partida para verlos.

## Usando VS Code
Visual Studio Code es el editor de código recomendado para usar con The Farmer Was Replaced.

Puedes instalarlo [aquí](https://code.visualstudio.com/download).

Después de descargarlo, instala la extensión de Python en VS Code.

Una vez que tengas eso, abre la [carpeta](persistent_data_path/Saves) que contiene tus archivos `.py` en VS Code. Asegúrate de abrir toda la carpeta, no solo los archivos individuales, de lo contrario, el archivo `__builtins__.py` no funcionará.

En el juego, asegúrate de tener activada la opción "File Watcher". Ahora, cada vez que guardes en VS Code, los cambios aparecerán automáticamente en el juego.

¡Eso es todo! ¡Ahora puedes escribir tu código en un editor de código profesional!
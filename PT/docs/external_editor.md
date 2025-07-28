# Editor Externo
O editor de texto do jogo é geralmente suficiente para jogar este jogo, mas claro que não pode competir com editores de texto mais sofisticados como o Visual Studio Code.

O jogo guarda todos os ficheiros de código como ficheiros .py, para que os possas editar com editores de Python.
Nota que isto é apenas por conveniência. A linguagem do jogo não é realmente Python, mas é suficientemente próxima para que o IntelliSense do Python funcione decentemente.
Podes encontrar os ficheiros na [pasta de saves](persistent_data_path/Saves).

Cada save também contém um ficheiro `__builtins__.py`, que contém definições Python incorporadas que correspondem às do jogo para permitir o IntelliSense.
O VS Code consegue detetar `__builtins__.py` automaticamente, mas alguns editores podem só funcionar se fizeres `from __builtins__ import *`.

Para ver as alterações externas no jogo sem ter de recarregar o save, deves ativar a opção "File Watcher". Se criares ou apagares ficheiros externamente, ainda precisarás de recarregar o save para os ver.

## Usar o VS Code
O Visual Studio Code é o editor de código recomendado para usar com The Farmer Was Replaced.

Podes instalá-lo [aqui](https://code.visualstudio.com/download).

Depois de o descarregares, instala a extensão Python no VS Code.

Quando tiveres isso, abre a [pasta](persistent_data_path/Saves) que contém os teus ficheiros `.py` no VS Code. Certifica-te de que abres a pasta inteira, não apenas os ficheiros individuais, caso contrário o ficheiro `__builtins__.py` não funcionará.

No jogo, certifica-te de que tens a opção "File Watcher" ativada. Agora, sempre que guardares no VS Code, as alterações aparecerão automaticamente no jogo.

É isso! Agora podes escrever o teu código num editor de código profissional!
# Editor Externo
O editor de texto do jogo geralmente é suficiente para jogar, mas, claro, não pode competir com editores de texto mais sofisticados como o Visual Studio Code.

O jogo salva todos os arquivos de código como arquivos .py, então você pode editá-los com editores de Python. 
Note que isso é apenas por conveniência. A linguagem dentro do jogo não é exatamente Python, mas é suficientemente próxima para que o IntelliSense do Python funcione bem com ela.
Você pode encontrar os arquivos na [pasta de salvamento](persistent_data_path/Saves).

Cada salvamento também contém um arquivo `__builtins__.py`, que contém definições baseadas em Python que correspondem aos built-ins do jogo para habilitar o IntelliSense. 
O VS Code consegue detectar o `__builtins__.py` automaticamente, mas alguns editores podem funcionar apenas se você fizer `from __builtins__ import *`.

Para ver alterações externas no jogo sem precisar recarregar o salvamento, você deve habilitar a opção "File Watcher". Se você criar ou deletar arquivos externamente, ainda precisará recarregar o salvamento para vê-los.

## Usando VS Code
O Visual Studio Code é o editor de código recomendado para usar com The Farmer Was Replaced.

Você pode instalá-lo [aqui](https://code.visualstudio.com/download).

Depois de baixá-lo, instale a extensão Python no VS Code.

Uma vez feito isso, abra a [pasta](persistent_data_path/Saves) que contém seus arquivos `.py` no VS Code. Certifique-se de abrir a pasta inteira, e não apenas arquivos individuais, caso contrário o arquivo `__builtins__.py` não funcionará.

No jogo, certifique-se de que a opção "File Watcher" está ativada. Agora, toda vez que você salvar no VS Code, as mudanças aparecerão automaticamente no jogo.

É isso! Agora você pode escrever seu código em um editor de código profissional!
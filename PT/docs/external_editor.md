# Editor Externo
O editor de texto do jogo geralmente é suficiente para jogar, mas é claro que não pode competir com editores de texto mais sofisticados como o Visual Studio Code.

O jogo salva todos os arquivos de código como arquivos .py, então você pode editá-los com editores de Python. 
Note que isso é apenas por conveniência. A linguagem do jogo não é realmente Python, mas é próxima o suficiente para que o IntelliSense do Python funcione decentemente.
Você pode encontrar os arquivos na [pasta de salvamento](persistent_data_path/Saves).

Cada jogo salvo também contém um arquivo `__builtins__.py`, que contém definições embutidas do Python que correspondem às do jogo para habilitar o IntelliSense. 
O VS Code consegue detectar `__builtins__.py` automaticamente, mas alguns editores podem funcionar apenas se você fizer `from __builtins__ import *`.

Para ver as alterações externas no jogo sem ter que recarregar o salvamento, você deve habilitar a opção "File Watcher". Se você criar ou deletar arquivos externamente, ainda precisará recarregar o salvamento para vê-los.

## Usando o VS Code
O Visual Studio Code é o editor de código recomendado para usar com The Farmer Was Replaced.

Você pode instalá-lo [aqui](https://code.visualstudio.com/download).

Após baixá-lo, instale a extensão Python no VS Code.

Depois de fazer isso, abra a [pasta](persistent_data_path/Saves) que contém seus arquivos `.py` no VS Code. Certifique-se de abrir a pasta inteira, não apenas os arquivos individuais, caso contrário, o arquivo `__builtins__.py` não vai funcionar.

No jogo, certifique-se de que a opção "File Watcher" está ativada. Agora, toda vez que você salvar no VS Code, as alterações aparecerão automaticamente no jogo.

É isso! Agora você pode escrever seu código em um editor de código profissional!
# Carregando Backups
Infelizmente, às vezes um arquivo de salvamento fica corrompido ou você perde alguns arquivos de código. Se isso acontecer com você, pode tentar carregar um backup. Se acontecer regularmente, tente desativar o Steam Cloud.

Um backup é feito toda vez que o jogo é salvo, e um pequeno número de backups é mantido caso você precise restaurar algo.
Esses backups podem ser encontrados no [diretório de backup](persistent_data_path/Backup). Eles são cópias dos salvamentos no [diretório de salvamento](persistent_data_path/Saves).
A maneira mais fácil de carregar um backup é copiar a pasta do backup específico que você deseja carregar para o diretório de salvamento.

Um salvamento é uma pasta com um arquivo `save.json` e vários arquivos `.py`.
Se você perdeu apenas alguns arquivos de código, ou os arquivos de código ainda estão lá, mas o arquivo `save.json` está corrompido, você também pode substituir apenas as partes corrompidas com os arquivos correspondentes do backup.
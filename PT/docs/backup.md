# Carregar Backups
Infelizmente, por vezes um ficheiro de save fica corrompido ou perdes alguns ficheiros de código. Se isto te acontecer, podes tentar carregar um backup. Se acontecer regularmente, tenta desativar a Steam Cloud.

É feito um backup sempre que o jogo é guardado, e um pequeno número de backups é mantido caso precises de restaurar algo.
Estes backups podem ser encontrados no [diretório de backup](persistent_data_path/Backup). São cópias dos saves no [diretório de saves](persistent_data_path/Saves).
A maneira mais fácil de carregar um backup é copiar a pasta do backup específico que queres carregar para o diretório de saves.

Um save é uma pasta com um ficheiro `save.json` e um monte de ficheiros `.py`.
Se perdeste apenas alguns ficheiros de código, ou os ficheiros de código ainda estão lá, mas o ficheiro `save.json` está corrompido, também podes substituir apenas as partes corrompidas pelos ficheiros correspondentes do backup.
# A versão 1.0 finalmente chegou!
Após mais de três anos e meio de desenvolvimento constante, mais de 20 atualizações e seu feedback incrível, o Acesso Antecipado finalmente chegou ao fim.

## O que há de novo na versão 1.0?
- Múltiplos drones para maximizar sua fazenda
- Uma árvore de desbloqueio reformulada com uma progressão mais exponencial
- 60 conquistas para testar suas habilidades
- Desbloquear certas conquistas dará chapéus especiais ao seu drone
- Uma reformulação completa do som
- Uma nova faixa de música
- Melhorias de qualidade de vida e várias correções
- Mudanças Drásticas: As melhorias serão parcialmente redefinidas. A reutilização de labirintos funciona de maneira um pouco diferente.

Muito obrigado a todos por apoiarem The Farmer Was Replaced desde o Acesso Antecipado até o lançamento completo. 
Mal posso esperar para ver como vocês usarão os múltiplos drones de maneiras criativas e inteligentes!
-Timon

Não se esqueça também de se juntar a nós no Discord: 
[Discord](https://discord.com/invite/kj33cJkeJn)

## Notas Completas da Atualização
Mudanças Drásticas:
-Devido à reformulação da árvore de tecnologia, os números de melhorias dos jogos salvos antigos não serão mais válidos. O jogo redefinirá todas as melhorias para um nível razoável quando você abrir um jogo salvo antigo.
-Se você estiver reutilizando labirintos, agora precisa primeiro reposicionar o tesouro e depois medir a posição, em vez de primeiro medir e depois reposicionar.

Jogabilidade:
-Adicionadas dicas de ferramentas com informações úteis ao passar o mouse sobre as casas da fazenda.
-Usar `measure()` em qualquer lugar do labirinto agora sempre retorna a posição do tesouro atual. Você não precisa mais medir o tesouro especificamente.
-Agora existe uma função `can_move()` para o labirinto.
-Abóboras agora escalam até 6x6 em vez de 5x5.
-O comportamento de secagem do solo mudou um pouco. Em vez de secar 1% a cada 0.8 a 1.2 segundos, cada casa de solo agora tem 10% de chance de secar a cada 0.1 segundos.
-O tempo de crescimento do cacto agora é sempre exatamente 1 segundo.
-Abóboras agora deixam para trás uma abóbora morta para indicar que morreram.
-Adicionado `pet_the_piggy()`.
-`num_unlocked()` agora é desbloqueado junto com os Sentidos.

Áudio:
-O áudio foi completamente refeito.
-Agora há música quando você inicia o jogo!

Visuais:
-Os visuais da árvore de tecnologia foram completamente reformulados.
-O painel de inventário no canto superior esquerdo da tela agora tem um belo efeito visual de coleta de item.
-Cactos agora são marrons quando não estão corretamente ordenados para torná-los mais visíveis.
-As plantas agora são visíveis imediatamente após o plantio, mesmo que ainda não tenham crescido.

Editor de Código:
-Clicar duas vezes em identificadores com sublinhados agora seleciona o identificador inteiro.
-Se a opção "tabs para espaços" estiver desativada, os espaços de indentação agora são convertidos em tabulações.
-O zoom agora é muito mais suave.
-O autocompletar de código agora está ciente de importações e pode dar sugestões de outros arquivos.
-Adicionados cursores diferentes para editar texto e redimensionar janelas.
-Os passos do depurador agora são baseados na linha de código em vez de nos ticks de simulação.

Outros:
-Agora você pode encadear operadores de comparação como em Python.
-`get_cost(Entities.Hedge)` e `get_cost(Entities.Treasure)` agora retornam o custo de um labirinto 1x1.
-Adicionada uma configuração de resolução.
-Adicionada uma configuração para desligar os destaques piscantes quando o código está em execução.
-A execução do código foi otimizada ainda mais, permitindo que o jogo rode mais suavemente enquanto o código está em execução.
-Adicionado um atalho de teclado "Alternar HUD".

Correções:
-Alguns dos casos mais comuns de destaques de código visíveis através de outras janelas foram corrigidos.
-Ações como arar não podem mais afetar o comportamento de secagem da água.
-Corrigidos problemas de atalhos de teclado em teclados não americanos.
-Corrigido o porquinho-cofre se movendo para muito longe da fazenda às vezes.
-Corrigido fertilizante não infectando plantas totalmente crescidas.
-Corrigido `set_world_size(get_world_size())` redefinindo a posição do drone.
-Corrigida uma interação entre simulação e dinossauro que fazia com que muitas maçãs fossem deixadas para trás.
-Corrigido o bug que fazia com que as mensagens de erro se movessem ao clicar em minimizar e depois abrir o menu.
-Corrigidas mensagens de erro que apareciam enquanto você ainda estava digitando.

Mudanças Drásticas de Atualizações Anteriores que você pode ter perdido:
-Funções definidas em outros arquivos (janelas no jogo) não são mais importadas implicitamente. Agora você precisa desbloquear e usar instruções de importação explícitas como em Python (Veja o desbloqueio de importação).
-`Items.Bones` foi renomeado para `Items.Bone` para que todos os itens fiquem no singular.
-`Entities.Carrots` foi renomeado para `Entities.Carrot` para que todas as entidades fiquem no singular.
-`Grounds.Turf` foi renomeado para `Grounds.Grassland` para facilitar o entendimento.
-`Items.Water_Tank` foi renomeado para `Items.Water` porque o recurso de reabastecimento do tanque foi removido.
-`Unlocks.Benchmark` foi substituído por `Unlocks.Timing`.
-`get_op_count()` foi renomeado para `get_tick_count()`.
-`set_farm_size()` foi renomeado para `set_world_size()` para ser consistente com `get_world_size()`.
-`get_companion()` agora retorna uma tupla no formato (entidade, (x, y)) em vez de uma lista.
-`trade()` foi removido do jogo.
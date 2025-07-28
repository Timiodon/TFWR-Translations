# Unlocks Automáticos
Para automatizar completamente o jogo, podes usar a função `unlock()` para desbloquear funcionalidades automaticamente.
Por exemplo, podes usar `unlock(Unlocks.Speed)` e `unlock(Unlocks.Expand)` para desbloquear as funcionalidades de velocidade e expansão.

Para determinar o custo de um unlock, basta usar a função `get_cost()` como farias para uma planta ou item.
Exemplo:
`get_cost(Unlocks.Loops)`
retorna `{Items.Hay:5}`

Se quiseres saber quantos de um determinado unlock tens, usa a função `num_unlocked(unlock)`.

Por exemplo, `num_unlocked(Unlocks.Speed)` retornará o número de melhorias de velocidade que tens.

`num_unlocked(Unlocks.Senses)` retornará `1` se os sentidos estiverem desbloqueados e `0` se não estiverem.

Também podes usar `num_unlocked()` em Itens, Entities ou Grounds. Isto retornará `1` se estiver desbloqueado, caso contrário `0`.

Tem cuidado, `num_unlocked(Unlocks.Carrots)` retornará o número de vezes que foi desbloqueado/melhorado.
`num_unlocked(Items.Carrot)` retornará apenas `0` ou `1`. (O mesmo para outras plantas)

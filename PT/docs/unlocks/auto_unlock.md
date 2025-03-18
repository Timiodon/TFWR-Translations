# Desbloqueios Automáticos
Para automatizar completamente o jogo, você pode usar a função `unlock()` para desbloquear recursos automaticamente.
Por exemplo, você pode usar `unlock(Unlocks.Speed)` e `unlock(Unlocks.Expand)` para desbloquear as funcionalidades de velocidade e expansão.

Para determinar o custo de um desbloqueio, basta usar a função `get_cost()` como faria para uma planta ou item.
Exemplo:
`get_cost(Unlocks.Loops)`
retorna `{Items.Hay:5}`

Se você quiser descobrir quantos de um desbloqueio específico possui, use a função `num_unlocked(unlock)`.

Por exemplo, `num_unlocked(Unlocks.Speed)` retornará o número de melhorias de velocidade que você tem.

`num_unlocked(Unlocks.Senses)` retornará `1` se os sentidos estiverem desbloqueados e `0` se não estiverem.

Você também pode usar `num_unlocked()` em Items, Entities ou Grounds. Isso retornará `1` se estiver desbloqueado, caso contrário `0`.

Tenha cuidado `num_unlocked(Unlocks.Carrots)` retornará o número de vezes que foi desbloqueado/melhorado. 
`num_unlocked(Items.Carrot)` só retornará `0` ou `1`. (O mesmo para outras plantas)
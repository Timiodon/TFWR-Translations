# Desbloqueios Automáticos
Para automatizar completamente o jogo, você pode usar a função `unlock()` para desbloquear recursos automaticamente.
Por exemplo, você pode usar `unlock(Unlocks.Speed)` e `unlock(Unlocks.Expand)` para desbloquear os recursos de velocidade e expansão.

Para determinar o custo de um unlock, simplesmente use a função `get_cost()` como faria para uma planta ou item.
Exemplo:
`get_cost(Unlocks.Loops)`
retorna `{Items.Hay:5}`

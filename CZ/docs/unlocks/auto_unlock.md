# Automatické odemykání
Pro plnou automatizaci hry můžete použít funkci `unlock()` k automatickému odemykání funkcí.
Například můžete použít `unlock(Unlocks.Speed)` a `unlock(Unlocks.Expand)` k odemčení rychlosti a rozšíření.

K určení ceny odemčení jednoduše použijte funkci `get_cost()`, stejně jako byste to udělali pro rostlinu nebo předmět.
Příklad:
`get_cost(Unlocks.Loops)`
vrátí `{Items.Hay:5}`

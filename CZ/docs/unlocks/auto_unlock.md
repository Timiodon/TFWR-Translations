# Auto Unlocks
Pro plnou automatizaci hry můžeš použít funkci `unlock()` k automatickému odemykání funkcí.  
Například můžeš použít `unlock(Unlocks.Speed)` a `unlock(Unlocks.Expand)` pro odemknutí vylepšení rychlosti a rozšíření farmy.

Pro zjištění ceny odemknutí použij funkci `get_cost()` stejně jako u rostlin nebo předmětů.  
Příklad:  
`get_cost(Unlocks.Loops)`  
vrátí `{Items.Hay:5}`

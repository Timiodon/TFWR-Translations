# Množiny (Sets)
Množiny jsou jako [slovníky](docs/scripting/dicts.md), ale bez hodnot. Jsou to jen neuspořádané sady klíčů. 

Vytvářejí se jako slovníky, ale bez hodnot.
`set = {North, East, West}`

Použijte `set()` k vytvoření prázdné množiny. Všimněte si, že `{}` vytvoří prázdný slovník.

Použijte `set.add(elem)` k přidání nového prvku do množiny.

Použijte `set.remove(elem)` k odstranění prvku z množiny.

Použijte `if elem in set:` ke kontrole, zda množina obsahuje prvek.

Použijte `for elem in set:` k iteraci všech prvků v množině.
U větších množin funguje operátor `in` mnohem rychleji než u seznamu.

Stejně jako slovníky jsou množiny neuspořádané, takže neexistují žádné záruky ohledně pořadí, v jakém jsou prvky iterovány.

Prvky v množinách jsou také jedinečné, takže přidání prvku, který již v množině je, množinu nezmění.
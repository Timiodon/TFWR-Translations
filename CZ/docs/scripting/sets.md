# Sets
Množiny (sets) jsou podobné jako [slovníky](docs/scripting/dicts.md), ale bez hodnot. Jsou to jen neuspořádané soubory klíčů.

Vytvářejí se stejně jako slovníky, ale bez hodnot.
`set = {North, East, West}`

Pro vytvoření prázdné množiny použij `set()`.  
Pozor – zápis `{}` vytvoří prázdný slovník.

Pomocí `set.add(elem)` přidáš nový prvek do množiny.

Pomocí `set.remove(elem)` odstraníš prvek z množiny.

Pomocí `if elem in set:` zkontroluješ, zda množina obsahuje daný prvek.

Pomocí `for elem in set:` můžeš projít všechny prvky množiny. U větších množin je operátor `in` výrazně rychlejší než u seznamu.

Stejně jako u slovníků nejsou prvky v množině uspořádané, takže pořadí jejich průchodu není zaručeno.

Navíc prvky v množině jsou jedinečné – přidání prvku, který už v množině existuje, množinu nijak nezmění.
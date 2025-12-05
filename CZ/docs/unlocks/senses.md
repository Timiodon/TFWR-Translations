# Senses
Dron teď umí vidět! 👀  

Funkce `get_pos_x()` a `get_pos_y()` vracejí aktuální souřadnice X a Y dronu. Na počáteční pozici mají obě hodnotu `0`. Souřadnice X se zvyšuje o `1` s každou dlaždicí směrem na `East` a souřadnice Y se zvyšuje o `1` s každou dlaždicí směrem na `North`.

`num_items(item)` vrací, kolik dané položky máš.  
Například `num_items(Items.Hay)` vrátí množství sena, které máš.

`get_entity_type()` a `get_ground_type()` vracejí typ objektu nebo typu půdy, který je právě pod dronem.

Udělá otočku, pokud je nad keřem:
`if get_entity_type() == Entities.Bush:
	do_a_flip()`

Klíčové slovo `None` je teď také odemčeno! `None` je hodnota, která představuje „žádnou hodnotu“.  
Například funkce bez příkazu `return` ve skutečnosti vrátí `None`.

`get_entity_type()` vrátí `None`, pokud pod dronem není žádný objekt.

Pokud chceš zjistit, kolik máš odemčených vylepšení určitého typu, použij funkci `num_unlocked(unlock)`.

Například `num_unlocked(Unlocks.Speed)` vrátí počet vylepšení rychlosti, které máš.

`num_unlocked(Unlocks.Senses)` vrátí `1`, pokud jsou smysly odemknuté, a `0`, pokud ještě nejsou.

`num_unlocked()` můžeš použít také pro Items, Entities nebo Grounds. Vrátí `1`, pokud je položka odemknutá, jinak `0`.

Pozor — `num_unlocked(Unlocks.Carrots)` vrátí, kolikrát bylo toto odemknutí/upgrady provedeno.  
`num_unlocked(Items.Carrot)` ale vrátí pouze `0` nebo `1` (stejně jako u ostatních rostlin).

# Smysly
Dron už vidí!

Funkce `get_pos_x()` a `get_pos_y()` vracejí aktuální x a y pozici drona. Na startovní pozici jsou obě `0`. Pozice x se zvyšuje o `1` každé políčko směrem na `East` (východ) a pozice y se zvyšuje o `1` každé políčko směrem na `North` (sever).

`num_items(item)` vrací, kolik máte daného předmětu.
Například `num_items(Items.Hay)` vrací, kolik máte sena.

`get_entity_type()` a `get_ground_type()` vracejí typ entity nebo podkladu, který je pod dronem.

Udělejte salto, pokud jste nad keřem:
`if get_entity_type() == Entities.Bush:
	do_a_flip()`

Klíčové slovo `None` je nyní také odemčeno! `None` je hodnota, která představuje, že neexistuje žádná hodnota.
Například funkce, která nemá žádný příkaz `return`, ve skutečnosti vrátí `None`.

`get_entity_type()` vrátí `None`, pokud pod dronem není žádná entita.


Pokud chcete zjistit, kolik máte konkrétního odemčení, použijte funkci `num_unlocked(unlock)`.

Například `num_unlocked(Unlocks.Speed)` vrátí počet vylepšení rychlosti, které máte.

`num_unlocked(Unlocks.Senses)` vrátí `1`, pokud jsou smysly odemčeny, a `0`, pokud nejsou.

Můžete také použít `num_unlocked()` na předměty, entity nebo podklady. To vrátí `1`, pokud je to odemčeno, jinak `0`.

Buďte opatrní, `num_unlocked(Unlocks.Carrots)` vrátí počet, kolikrát to bylo odemčeno/vylepšeno.
`num_unlocked(Items.Carrot)` vrátí pouze `0` nebo `1`. (Totéž platí pro ostatní rostliny)
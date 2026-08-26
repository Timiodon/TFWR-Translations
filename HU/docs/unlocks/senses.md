# Érzékek
A drón már lát!
A `get_pos_x()` és `get_pos_y()` függvények a drón aktuális x és y pozícióját adják vissza. A kezdő pozícióban mindkettő `0`. Az x pozíció `1`-el nő minden csempével `East` irányba és az y pozíció `1`-el nő minden csempével `North` irányba.

A `num_items(item)` visszaadja, mennyi itemed van.
Például `num_items(Items.Hay)` visszaadja, mennyi szénád van.

A `get_entity_type()` és `get_ground_type()` a drón alatti entitás vagy talaj típusát adják vissza.

Szaltót csinál, ha bokor felett vagy:
`if get_entity_type() == Entities.Bush:
	do_a_flip()`

A `None` kulcsszó is feloldásra került most! A `None` egy érték, ami azt jelenti, hogy nincs érték.
Például egy függvény, aminek nincs `return` utasítása, valójában `None`-t ad vissza.

A `get_entity_type()` `None`-t ad vissza, ha nincs entitás a drón alatt.

Ha ki akarod deríteni, hányszor van feloldva egy particular feloldás, használd a `num_unlocked(unlock)` függvényt.

Például `num_unlocked(Unlocks.Speed)` visszaadja a sebességfejlesztések számát.

`num_unlocked(Unlocks.Senses)` `1`-et ad vissza, ha az érzékek fel vannak oldva és `0`, ha nem.

Használhatod a `num_unlocked()`-ot Items, Entities vagy Grounds on is. Ez `1`-et ad vissza, ha fel van oldva, különben `0`-t.

Vigyázz, `num_unlocked(Unlocks.Carrots)` a feloldások/fejlesztések számát adja vissza.
`num_unlocked(Items.Carrot)` csak `0`-t vagy `1`-et ad vissza. (Ugyanúgy más növényekre is)
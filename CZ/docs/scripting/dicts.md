# Slovníky
Slovníky jsou datová struktura, která umožňuje přiřazovat klíčům hodnoty — podobně jako skutečný slovník přiřazuje slovům jejich význam. Vyhledávání v nich je velmi rychlé.

Slovník lze vytvořit takto:
`right_of = {North:East, East:South, South:West, West:North}`

Výraz před dvojtečkou je klíč a výraz za dvojtečkou je hodnota, ke které klíč směřuje.  
Výše uvedený slovník přiřazuje každému směru směr, který je vpravo od něj.

Další příklad mapuje pozici dronu na entitu, nad kterou se nachází:
`x, y = get_pos_x(), get_pos_y()
entity_dict = {(x,y):get_entity_type()}`

Přístup k hodnotě podle klíče je podobný přístupu k prvku seznamu:
`value = dict[key]`

Příklad:
`orientation = right_of[South]`
Tímto se nastaví `orientation` na `West`.

Nový pár klíč–hodnota lze přidat takto:
`dict[key] = value`

Příklad:
`entity_dict[(get_pos_x(), get_pos_y())] = get_entity_type()`
Tímto se aktualizuje entita uložená pro aktuální pozici.

Klíče jsou jedinečné, takže přidání klíče, který už ve slovníku existuje, přepíše předchozí hodnotu.

Pomocí `dict.pop(key)` odstraníš pár klíč–hodnota ze slovníku `dict`.

Výraz `key in dict` vrátí `True`, pokud se `key` ve slovníku nachází, jinak `False`.  
Můžeš tedy použít `if key in dict:` pro kontrolu, zda slovník daný klíč obsahuje.

Použitím slovníku v cyklu `for` můžeš procházet všechny klíče:
`for key in dict:
	value = dict[key]`

Pořadí, ve kterém se klíče procházejí, není zaručeno.

Viz také [Sets](docs/scripting/sets.md)
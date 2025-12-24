# Slovníky
Slovník (dictionary) je datová struktura, která mapuje klíče na hodnoty — podobně jako slovník mapuje slova na jejich definice.

Slovník lze vytvořit takto:
`right_of = {North:East, East:South, South:West, West:North}`

Výraz před dvojtečkou je klíč a výraz za dvojtečkou je hodnota, na kterou klíč ukazuje.
Výše uvedený slovník mapuje každý směr na směr napravo.

Jiný příklad mapuje pozici dronu na entitu pod ním:
`x, y = get_pos_x(), get_pos_y()
entity_dict = {(x,y):get_entity_type()}`

Přístup k hodnotě přes klíč je podobný přístupu k prvku seznamu:
`value = dict[key]`

Příklad:
`orientation = right_of[South]`
Tím se nastaví `orientation` na `West`.

Novou dvojici klíč–hodnota přidáte:
`dict[key] = value`

Příklad:
`entity_dict[(get_pos_x(), get_pos_y())] = get_entity_type()`
Tím aktualizujete entitu uloženou pro aktuální pozici.

Klíče jsou unikátní; přidání existujícího klíče přepíše předchozí hodnotu.

K odstranění použijte `dict.pop(key)`.

Výraz `key in dict` vrátí `True`, pokud `key` v `dict` existuje, jinak `False`. Můžete tedy použít `if key in dict:`.

Zařazením slovníku do `for` smyčky projdete všechny jeho klíče:
`for key in dict:
    value = dict[key]`

Pořadí iterace klíčů není garantováno.

Viz také [Množiny](docs/scripting/sets.md)
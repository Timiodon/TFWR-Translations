# Szótárak
A szótárak olyan adatszerkezetek, amelyek lehetővé teszik kulcsok értékekre képezését, ahogyan egy valódi szótár a szavakat a definícióikra képezi le, és nagyon gyorsan ki lehet őket keresni.

Szótárat így lehet létrehozni:
`right_of = {North:East, East:South, South:West, West:North}`

A kettőspont előtti kifejezés a kulcs, és a kettőspont utáni kifejezés az az érték, amelyre a kulcs képez.
A fenti szótár minden irányt a tőle jobbra lévő irányra képez.

Itt egy újabb, ami a drón pozícióját ahhoz az entitáshoz rendeli, amely fölött éppen van.
`x, y = get_pos_x(), get_pos_y()
entity_dict = {(x,y):get_entity_type()}`

A kulcshoz rendelt érték elérése hasonló a lista elemének eléréséhez:
`value = dict[key]`

Példa:
`orientation = right_of[South]`
Ez az `orientation`-t `West`-re állítja.

Új kulcs-érték párost így adhatsz hozzá a szótárhoz:
`dict[key] = value`

Példa:
`entity_dict[(get_pos_x(), get_pos_y())] = get_entity_type()`
Ez frissíti az aktuális pozícióhoz tárolt entitást.

A kulcsok egyediek, így egy már létező kulcs hozzáadása felülírja az előző értéket.

Használd a `dict.pop(key)`-t kulcs-érték pár eltávolításához a `dict`-ből.

`key in dict` `True`-ra értékelődik, ha a `key` kulcs a `dict`-ben, és `False` egyébként.
Tehát használhatod az `if key in dict:`-t annak ellenőrzésére, hogy a `dict` tartalmazza-e a kulcsot.

Szótárat for ciklusban használva végigiterálhatsz az összes kulcson:
`for key in dict:
	value = dict[key]`

Nincs garancia arra, hogy milyen sorrendben iterálódnak a kulcsok.

Lásd még: [Sets](docs/scripting/sets.md)
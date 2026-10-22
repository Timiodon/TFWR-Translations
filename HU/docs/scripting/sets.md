# Set/Halmazok
A halmazok olyanok, mint a [szótárak](docs/scripting/dicts.md), de értékek nélkül. Egyszerűen rendezetlen kulcsok halmaza.

Létrehozása úgy történik, mint a szótáraké, de értékek nélkül.
`set = {North, East, West}`

Üres halmaz létrehozásához használd a `set()`-t. Figyelj arra, hogy `{}` üres szótárat hoz létre.

Új elem hozzáadásához a halmazhoz használd a `set.add(elem)`-t.

Elem eltávolításához a halmazból használd a `set.remove(elem)`-t.

Ellenőrzéshez, hogy a halmaz tartalmaz-e egy elemet, használd az `if elem in set:`-t.

Az összes elem iterálásához a halmazban használd a `for elem in set:`-t.
Nagyobb halmazoknál a `in` operátor sokkal gyorsabban működik, mint egy listán.

Csakúgy, mint a szótárak, a halmazok is rendezetlenek, így nincs garancia arra, hogy milyen sorrendben iterálódnak az elemek.

Továbbá a halmaz elemei egyediek, így egy már meglévő elem hozzáadása nem változtatja meg a halmazt.
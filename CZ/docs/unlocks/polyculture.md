# Polyculture
Možná sis už všiml, že rostliny někdy dávají vyšší výnos, když jsou zasazeny vedle sebe.  
Tráva, keře, stromy a mrkve mají vyšší výnos, pokud mají správného rostlinného „společníka“. Preferovaný společník je pro každou rostlinu jiný a nelze ho předem odhadnout. Naštěstí můžeš zjistit preferenci rostliny, která je právě pod dronem, pomocí `get_companion()`. Tato funkce vrátí dvojici (tuple), kde první prvek určuje typ rostliny, kterou si přeje mít jako společníka, a druhý prvek určuje pozici, na které ho chce mít.

`plant_type, (x, y) = get_companion()`

Například pokud zasadíš keř a poté zavoláš `get_companion()`, může vrátit něco jako `(Entities.Carrot, (3, 5))`. To znamená, že tento keř by chtěl mít mrkev na pozici `(3,5)`. Pokud tedy zasadíš mrkev na `(3,5)` a následně keř sklidíš, získáš více dřeva. Na růstové fázi mrkve přitom nezáleží.

Rostlinný společník může být `Entities.Grass`, `Entities.Bush`, `Entities.Tree` nebo `Entities.Carrot`. Každá rostlina si svého společníka vybírá náhodně, ale nikdy si nevybere sama sebe. Pozice společníka může být libovolné místo do 3 kroků od rostliny, kromě její vlastní pozice.

Pokud pod dronem není žádná rostlina, která by měla společníka, funkce `get_companion()` vrátí `None`.

Než je polykultura odemčena, multiplikátor výnosu je `5`. S každým vylepšením se tento násobitel zdvojnásobí.
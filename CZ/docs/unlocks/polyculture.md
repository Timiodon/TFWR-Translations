# Polykultura
Možná jste si již všimli, že někdy rostliny vynášejí více, když jsou vysazeny společně.
Tráva, keře, stromy a mrkve vynášejí více, když mají správného rostlinného společníka. Preference společníka je pro každou jednotlivou rostlinu jiná a nelze ji předvídat. Naštěstí lze preferenci společníka rostliny pod dronem změřit pomocí `get_companion()`. Vrací n-tici, kde prvním prvkem je typ rostliny, kterou chce jako společníka, a druhým prvkem je pozice, kde chce svého společníka.

`plant_type, (x, y) = get_companion()`

Například pokud zasadíte keř a poté zavoláte `get_companion()`, vrátí něco jako `(Entities.Carrot, (3, 5))`. To znamená, že tento keř by chtěl mít mrkve na pozici `(3,5)`. Takže pokud zasadíte mrkve na `(3,5)` a poté sklidíte keř, vynese více dřeva. Na fázi růstu mrkve nezáleží.

Preference společníka rostliny může být buď `Entities.Grass`, `Entities.Bush`, `Entities.Tree` nebo `Entities.Carrot`. Každá rostlina si to vybírá náhodně, ale vždy si vybere jinou rostlinu než sebe. Pozice může být také jakákoli pozice do 3 tahů od rostliny kromě pozice samotné rostliny.

Pokud pod dronem není žádná rostlina, která má preferenci společníka, `get_companion()` vrátí `None`.

Před odemčením polykultury je násobitel výnosu `5`. Zdvojnásobuje se pokaždé, když ji vylepšíte.
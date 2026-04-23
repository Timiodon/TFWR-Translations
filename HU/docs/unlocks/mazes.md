# Labirintusok
Az `Items.Weird_Substance`, amit [trágyázással](docs/unlocks/fertilizer.md) növényekből kapsz, furcsa hatással van a bokrokra. Ha a drón egy bokor felett van és hívod a `use_item(Items.Weird_Substance, amount)`-t, a bokor labirintussá nő sövényből.
A labirintus mérete az `Items.Weird_Substance` mennyiségétől függ (a `use_item()` hívás második argumentuma).
Labirintus fejlesztések nélkül `n` `Items.Weird_Substance` használata `n`x`n` labirintust eredményez. Minden labirintus fejlesztési szint megduplázza a kincset, de megduplázza a szükséges `Items.Weird_Substance` mennyiségét is.
Tehát teljes mező labirintus készítéséhez:

`plant(Entities.Bush)
substance = get_world_size() * 2**(num_unlocked(Unlocks.Mazes) - 1)
use_item(Items.Weird_Substance, substance)`

Valamiért a drón nem tud a sövények felett repülni, annak ellenére, hogy nem néznek ki olyan magasanak.

Van egy kincs elrejtve valahol a sövényben. Használd a `harvest()`-t a kincsen, hogy a labirintus területével egyenlő aranyat kapj. (Például egy 5x5 labirintus 25 aranyat hoz.)

Ha bárhol máshol használod a `harvest()`-t, a labirintus egyszerűen eltűnik.

A `get_entity_type()` `Entities.Treasure`-t ad vissza, ha a drón a kincs felett van és `Entities.Hedge` minden máshol a labirintusban.

A labirintusok nem tartalmaznak hurkokat, kivéve ha újrafelhasználod a labirintust (lásd lejjebb, hogyan újrafelhasználni a labirintust). Tehát nincs módja a drónnak ugyanabba a pozícióba kerülni visszafelé menés nélkül.

Ellenőrizheted, hogy van-e fal azáltal, hogy megpróbálsz áthaladni rajta.
`move()` `True`-t ad vissza, ha sikeres és `False` egyébként.

A `can_move()` használható annak ellenőrzésére, hogy van-e fal anélkül, hogy mozognál.

Ha fogalmad sincs, hogyan juts el a kincsig, nézd meg az 1. tippet. Megmutatja, hogyan közelíts meg egy ilyen problémát.

A `measure()` használata a labirintus bárhol visszaadja a kincs pozícióját.
`x, y = measure()`

Extra kihívásként újrafelhasználhatod a labirintust azonos mennyiségű `Items.Weird_Substance` használatával a kincsen.
Ez összegyűjti a kincset és új kincset spawnol véletlenszerű pozícióba a labirintusban.

Minden alkalommal, amikor a kincs mozog, a labirintus falainak néhány véletlenszerűen eltávolításra kerülhet. Tehát az újrafelhasznált labirintusok hurkokat tartalmazhatnak.

Figyelj arra, hogy a hurkok a labirintusban sokkal nehezebbé teszik, mert azt jelenti, hogy ugyanabba a helyzetbe juthatsz mozgás nélkül.
Labirintus újrafelhasználása nem ad több aranyat, mint egyszerűen betakarítani és új labirintust spawnolni.
Ez 100%-ban extra kihívás, amit egyszerűen kihagyhatsz.
Csak akkor éri meg, ha az extra információ és a shortcutok segítenek a labirintus gyorsabb megoldásában.

A kincs legfeljebb 300-szor relokálható. Ezután a kincsen weird substance használata nem növeli többé az aranyat benne és nem mozog többé.

<spoiler=show hint 1>Íme egy általános megközelítés a probléma megoldásához:

Hozz létre egy labirintust és képzeld el, hogy te vagy a drón.

Gondolkodj azon, hogyan próbálnád megtalálni a kincset, ha a labirintusban lennél.

Írd le a stratégiádat lépésről lépésre, hogy valaki más követhesse gondolkodás nélkül.

Most próbáld lefordítani a lépéseidet kódra.
</spoiler>
<spoiler=show hint 2>Amíg nincsenek hurkok: Az összes fal igazából egy nagy összefüggő fal. Ha követed a falat, az végigvezet az egész labirintuson.
Ez a megközelítés nagyon kevés kódot igényel és nem kell nyomon követned, hol jártál már. Körülbelül 10 sornyi kódra van szükséged.</spoiler>
<spoiler=show hint 3>Ahelyett, hogy abszolút irányokban mozgatnád a drónt mint kelet vagy nyugat, nagyon hasznos lehet a drónt relatív irányokban mozgatni mint "fordulj jobbra" vagy "fordulj balra". Ehhez nyomon kell követned, melyik irányba mozog a drón jelenleg. A drón soha nem forog valójában, de tarthatsz egy "virtuális" rotációt a kódban.
A következő index trükk hasznos ehhez:

`directions = [North, East, South, West]
index = 0`

Használd a `% 4`-et, hogy lehetővé tedd a "körbe forgást", így `West` után vissza wrapel `North`-ra.
`# fordulj jobbra
index = (index + 1) % 4`

`# fordulj balra
index = (index - 1) % 4

move(directions[index])`</spoiler>
<spoiler=show hint 4>Ha nem tudod megoldani, mindig megkönnyítheted az életed és kevésbé hatékonyan csinálhatod.
Egy `1`x`1` labirintus megoldása triviális.</spoiler>
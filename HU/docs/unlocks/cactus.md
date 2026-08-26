# Kaktusz
Mint más növények, a [kaktuszok](objects/cactus) termeszthetők talajon és betakaríthatók szokásosan.

Azonban különböző méretekben jönnek és furcsa rendezési érzékkel rendelkeznek.

Ha betakarítasz egy teljesen megnőtt kaktuszt és az összes szomszédos kaktusz rendezett sorrendben van, az is betakarítja az összes szomszédos kaktuszt rekurzívan.

Egy kaktusz rendezett sorrendben lévőnek számít, ha az összes `North` és `East` irányú szomszédos kaktusz teljesen megnőtt és nagyobb vagy egyenlő méretű, és az összes `South` és `West` irányú szomszédos kaktusz teljesen megnőtt és kisebb vagy egyenlő méretű.

A betakarítás csak akkor terjed tovább, ha az összes szomszédos kaktusz teljesen megnőtt és rendezett sorrendben van.
Ez azt jelenti, hogy ha egy megnőtt kaktuszokból álló négyzet méret szerint rendezett és te betakarítasz egy kaktuszt, az egész négyzetet betakarítja.

Egy teljesen megnőtt kaktusz barnának fog látszani, ha nem rendezett. Rendezés után újra zöldre vált.

Olyan kaktuszt kapsz, amennyi a betakarított kaktuszok számának négyzete. Tehát ha `n` kaktuszt betakarítasz egyszerre, `n**2` `Items.Cactus`-t kapsz.

A kaktusz mérete a `measure()`-el mérhető.
Mindig ezekből a számokból egy: `0,1,2,3,4,5,6,7,8,9`.

Átadhatod az irányt is a `measure(direction)`-nak a drón melletti szomszédos csempe méréséhez abban az irányban.

Felemelhetsz egy kaktuszt a szomszédjával bármely irányban a `swap()` paranccsal.
`swap(direction)` felcseréli a drón alatti objektumot a drón `direction` irányában lévő egy csempével lévő objektummal.

## Példák
Mindegyik rácsban az összes kaktusz rendezett sorrendben van és a betakarítás az egész mezőre terjed:
`3 4 5    3 3 3    1 2 3    1 5 9
2 3 4    2 2 2    1 2 3    1 3 8
1 2 3    1 1 1    1 2 3    1 3 4`

Ebben a rácsban csak a bal alsó kaktusz van rendezett sorrendben, ami nem elég a terjedéshez:
`1 5 3
4 9 7
3 3 2`

<spoiler=show hint 1>
Ha a sorok már rendezettek, az oszlopok rendezése nem rendezi szét a sorokat.
</spoiler>
<spoiler=show hint 2>
Ha nem vagy ismerős a rendezési algoritmusokban, érdemes lehet online utánuk nézni és elgondolkodni, melyikeket lehetne adaptálni ehhez a problémához. Tartsd észben, hogy nem mindegyik működik, mert csak szomszédos kaktuszokat cserélhetsz.
</spoiler>
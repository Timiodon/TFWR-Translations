# Cactus
Stejně jako ostatní rostliny mohou být [kaktusy](objects/cactus) pěstovány na půdě a sklizeny obvyklým způsobem.

Mají však různé velikosti a zvláštní smysl pro pořádek.

Pokud sklidíš plně vyrostlý kaktus a všichni sousední kaktusy jsou ve správném pořadí, dojde ke sklizni všech sousedních kaktusů rekurzivně.

Kaktus je považován za seřazený, pokud všichni sousedé na `North` a `East` jsou plně vyrostlí a stejně velcí nebo větší a všichni sousedé na `South` a `West` jsou plně vyrostlí a stejně velcí nebo menší.

Sklizeň se šíří pouze tehdy, když jsou všechny sousední kaktusy plně vyrostlé a seřazené.  
To znamená, že pokud je čtverec vyrostlých kaktusů seřazen podle velikosti a sklidíš jeden z nich, sklidí se celý čtverec.

Plně vyrostlý kaktus bude hnědý, pokud není seřazen. Jakmile se seřadí, znovu zezelená.

Za sklizeň obdržíš počet kaktusů rovný druhé mocnině počtu sklizených kaktusů. Takže pokud sklidíš `n` kaktusů současně, dostaneš `n**2` `Items.Cactus`.

Velikost kaktusu lze změřit pomocí `measure()`.  
Hodnota je vždy jedno z těchto čísel: `0,1,2,3,4,5,6,7,8,9`.

Do `measure(direction)` můžeš také předat směr a změřit sousední dlaždici v daném směru od dronu.

Kaktus můžeš vyměnit se sousedem v libovolném směru pomocí příkazu `swap()`.  
`swap(direction)` vymění objekt pod dronem s objektem o jedno pole v daném směru dronu.

## Příklady
V každé z těchto mřížek jsou všechny kaktusy seřazeny a sklizeň se rozšíří po celém poli:
`3 4 5    3 3 3    1 2 3    1 5 9
2 3 4    2 2 2    1 2 3    1 3 8
1 2 3    1 1 1    1 2 3    1 3 4`

V této mřížce je seřazen pouze kaktus vlevo dole, což nestačí k rozšíření sklizně:
`1 5 3
4 9 7
3 3 2`

<spoiler=show hint 1>
Pokud jsou řádky již seřazené, seřazení sloupců je nerozhodí.
</spoiler>
<spoiler=show hint 2>
Pokud neznáš třídicí algoritmy, můžeš si je vyhledat a zamyslet se, které z nich by se daly přizpůsobit tomuto problému. Měj na paměti, že ne všechny budou fungovat, protože můžeš prohazovat pouze sousední kaktusy.
</spoiler>

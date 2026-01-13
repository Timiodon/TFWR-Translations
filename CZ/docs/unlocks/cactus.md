# Kaktus
Stejně jako ostatní rostliny, [kaktusy](objects/cactus) lze pěstovat na půdě a sklízet jako obvykle.

Přicházejí však v různých velikostech a mají zvláštní smysl pro pořádek.

Pokud sklidíte plně vzrostlý kaktus a všechny sousední kaktusy jsou seřazeny, sklidí se také všechny sousední kaktusy rekurzivně.

Kaktus je považován za seřazený, pokud jsou všechny sousední kaktusy na `North` (sever) a `East` (východ) plně vzrostlé a větší nebo stejné velikosti a všechny sousední kaktusy na `South` (jih) a `West` (západ) jsou plně vzrostlé a menší nebo stejné velikosti.

Sklizeň se rozšíří pouze tehdy, pokud jsou všechny sousední kaktusy plně vzrostlé a seřazené.
To znamená, že pokud je čtverec vzrostlých kaktusů seřazen podle velikosti a sklidíte jeden kaktus, sklidí se celý čtverec.

Plně vzrostlý kaktus bude vypadat hnědě, pokud není seřazen. Jakmile je seřazen, znovu zezelená.

Získáte kaktusy rovné počtu sklizených kaktusů na druhou. Takže pokud sklidíte `n` kaktusů současně, získáte `n**2` `Items.Cactus`.

Velikost kaktusu lze změřit pomocí `measure()`.
Je to vždy jedno z těchto čísel: `0,1,2,3,4,5,6,7,8,9`.

Můžete také předat směr do `measure(direction)` pro změření sousedního políčka v daném směru od drona.

Kaktus můžete prohodit s jeho sousedem v libovolném směru pomocí příkazu `swap()`.
`swap(direction)` prohodí objekt pod dronem s objektem o jedno políčko ve směru `direction` od drona.

## Příklady
V každé z těchto mřížek jsou všechny kaktusy seřazeny a sklizeň se rozšíří po celém poli:
`3 4 5    3 3 3    1 2 3    1 5 9
2 3 4    2 2 2    1 2 3    1 3 8
1 2 3    1 1 1    1 2 3    1 3 4`

V této mřížce je seřazen pouze levý dolní kaktus, což nestačí k tomu, aby se sklizeň rozšířila:
`1 5 3
4 9 7
3 3 2`

<spoiler=zobrazit nápovědu 1>
Pokud jsou řádky již seřazeny, seřazení sloupců řádky nerozhází.
</spoiler>
<spoiler=zobrazit nápovědu 2>
Pokud nejste obeznámeni s řadicími algoritmy, možná si je budete chtít vyhledat online a zamyslet se nad tím, které z nich by se daly přizpůsobit tomuto problému. Mějte na paměti, že ne všechny fungují, protože můžete prohazovat pouze sousední kaktusy.
</spoiler>
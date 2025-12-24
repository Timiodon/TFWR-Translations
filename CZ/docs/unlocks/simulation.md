# Simulace

Simulace vám umožňují rychle testovat kód bez změny stavu skutečné farmy.
Počáteční stav simulace lze libovolně zvolit a po skončení simulace bude skutečná farma v přesně stejném stavu, v jakém byla před zahájením simulace.

Funkce `simulate()` se používá ke spuštění simulace.

soubor, ve kterém by mělo provádění začít
`filename = "f1"`

začít se vším odemčeným a plně vylepšeným
`sim_unlocks = Unlocks`

začít s 10000 mrkvemi a 50 senem
`sim_items = {Items.Carrot : 10000, Items.Hay : 50}`

začít s globální proměnnou "a" s hodnotou 13
`sim_globals = {"a" : 13}`

použít pevný náhodný seed (semínko)
`seed = 0`

zrychlit simulaci faktorem 64
`speedup = 64`

spustit simulaci
`run_time = simulate(filename, sim_unlocks, sim_items, sim_globals, seed, speedup)`

Funkce `simulate()` vrací čas v sekundách, který trvalo simulovat daný startovní soubor.

### Název souboru
Prvním argumentem funkce simulate je název souboru. Toto je název, který se zobrazuje v horní části okna s kódem. Simulace spustí zadaný soubor, jako byste na něj klikli tlačítkem Spustit (Execute).

### Počáteční odemčení
Všechny programovací funkce, jako jsou smyčky, příkazy if, seznamy, slovníky,... zůstanou vždy odemčeny.

Druhý argument vám umožňuje specifikovat, se kterými odemčeními/vylepšeními by měla simulace začít navíc k programovacím funkcím. Měla by to být sekvence odemčení. Simulace začne se všemi odemčeními v sekvenci vylepšenými na jejich maximální úroveň.

Pokud chcete specifikovat jinou úroveň vylepšení než maximální, můžete předat slovník, který mapuje odemčení na úrovně odemčení. V tomto případě záporné hodnoty odpovídají maximální úrovni odemčení.

### Počáteční předměty
Třetí argument vám umožňuje předat slovník, který mapuje předměty na čísla. Určuje předměty, se kterými se má simulace začít.

### Počáteční globální proměnné
Protože simulace spouští zcela nové provádění programu, nemůžete přistupovat k proměnným z programu, který simulaci spouští.
Je však možné předat hodnoty do simulace pomocí čtvrtého argumentu. Toto je slovník, který mapuje názvy proměnných ve formě řetězců na hodnoty. Tyto proměnné jsou poté přidány do globálního rozsahu provádění uvnitř simulace.

Všimněte si, že toto kopíruje všechny hodnoty, takže jejich změna uvnitř simulace neovlivní původní hodnoty mimo simulaci. Není možné vrátit hodnoty ze simulace jiné než čas, který trval běh.

### Náhodný seed
Pátý argument vám umožňuje specifikovat náhodný seed použitý v simulaci. Musí to být kladné celé číslo. Záporné hodnoty způsobí použití náhodného seedu.

Náhodný seed ovlivňuje vše od doby růstu rostlin přes rozložení bludiště až po dobu rozpadu vody. Pokud spustíte stejnou simulaci vícekrát se stejným náhodným seedem a stejnými počátečními podmínkami, výsledek by měl být vždy stejný.

### Zrychlení
Šestým argumentem je počáteční zrychlení simulace. To vám umožní rychle testovat věci. Pokud hra nestíhá nastavenou rychlost, automaticky se zpomalí.

Zrychlení nijak neovlivňuje výsledek simulace. Existuje pouze pro zkrácení doby čekání.
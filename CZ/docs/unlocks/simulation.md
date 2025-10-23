# Simulation

Simulace ti umožní rychle testovat kód, aniž by se změnil stav skutečné farmy.  
Počáteční stav simulace lze zvolit libovolně a po skončení simulace bude reálná farma ve stejném stavu jako před jejím spuštěním.

K zahájení simulace slouží funkce `simulate()`.

soubor, ve kterém má provádění začít
`filename = "f1"`

začni se vším odemčeným a plně vylepšeným
`sim_unlocks = Unlocks`

začni s 10000 mrkvemi a 50 seny
`sim_items = {Items.Carrot : 10000, Items.Hay : 50}`

začni s globální proměnnou „a“ s hodnotou 13
`sim_globals = {"a" : 13}`

použij pevné náhodné semínko
`seed = 0`

zrychli simulaci 64×
`speedup = 64`

spusť simulaci
`run_time = simulate(filename, sim_unlocks, sim_items, sim_globals, seed, speedup)`

Funkce `simulate()` vrací čas v sekundách, který trvalo odsimulovat zadaný startovní soubor.

### File Name
První argument funkce simulate je název souboru. To je jméno zobrazené nahoře v okně s kódem. Simulace spustí zadaný soubor, jako bys na něm klikl na tlačítko Execute.

### Starting Unlocks
Všechny programátorské funkce (smyčky, if, lists, dicts, …) zůstávají vždy odemčené.

Druhý argument umožňuje určit, se kterými odemknutími/upgrady má simulace začít navíc k programátorským funkcím. Měla by to být posloupnost odemknutí. Simulace začne se všemi odemknutími z této posloupnosti v jejich maximální úrovni.

Pokud chceš určit jinou než maximální úroveň vylepšení, můžeš předat slovník, který mapuje odemknutí na úrovně. V tomto případě záporné hodnoty odpovídají maximální úrovni.

### Starting Items
Třetí argument umožňuje předat slovník, který mapuje předměty na čísla. Tím určíš, s jakými předměty simulace začne.

### Starting Globals
Protože simulace spouští zcela nové provádění programu, nelze přistupovat k proměnným z programu, který simulaci startuje.  
Je ale možné předat hodnoty do simulace pomocí čtvrtého argumentu. Jde o slovník mapující názvy proměnných (řetězce) na hodnoty. Tyto proměnné se pak přidají do globálního scope uvnitř simulace.

Pamatuj, že se všechny hodnoty kopírují, takže jejich změny uvnitř simulace neovlivní původní hodnoty mimo simulaci. Z simulace není možné vracet hodnoty jinak než čas běhu.

### Random Seed
Pátý argument umožňuje určit náhodné semínko použité v simulaci. Musí to být kladné celé číslo. Záporné hodnoty způsobí použití náhodného semínka.

Náhodné semínko ovlivňuje vše od dob růstu rostlin přes rozložení bludišť až po dobu vysychání vody. Pokud spustíš tutéž simulaci vícekrát se stejným semínkem a se stejnými počátečními podmínkami, výsledek by měl být vždy stejný.

### Speedup
Šestý argument je počáteční zrychlení simulace. To ti umožní testovat věci rychleji. Pokud hra nestíhá nastavenou rychlost, automaticky ji zpomalí.

Zrychlení žádným způsobem neovlivňuje výsledek simulace. Slouží pouze ke zkrácení čekání.

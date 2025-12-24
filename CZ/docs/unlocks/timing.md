# Časování
Pokud opravdu chcete optimalizovat své metody, musíte pochopit, jak se v této hře měří čas. Toto odemčení je celé o tom.

## Nové funkce
Existují dvě užitečné funkce pro měření, jak dlouho věci trvají:

`get_time()` vrací čas v sekundách od začátku hry.

`get_tick_count()` vrací počet tiků provedených od začátku provádění.

Tyto dvě funkce, stejně jako `quick_print()`, jsou zcela zdarma. Dokonce i operace volání je pro ně zdarma.

## Podrobnosti o běhu (Runtime)

### Upozornění
Takhle výkon v reálném světě nefunguje. Jsou to jen pravidla vymyšlená pro tuto hru, aby měla konzistentní a srozumitelný model časování.
Pravděpodobně vás to bude zajímat pouze tehdy, pokud chcete hyper-optimalizovat svůj kód.


Základní jednotka času pro provádění kódu se nazývá "tik". Bez vylepšení rychlosti a energie probíhá provádění rychlostí `400` tiků za sekundu.

Obecně platí, že operace, které kombinují dvě hodnoty, jako jsou `+, -, *, /, //, %, and, or, ...`, trvají jeden tik.
Jednohodnotové `-` a `not` jsou zdarma.
Větev `if` také trvá jeden tik (navíc k času, který trvá vyhodnocení podmínkového výrazu).
Volání funkcí a čtení a zápisy proměnných jsou zdarma, ale definice funkcí trvají 1 tik.
Příkazy `import` jsou zdarma.
Přístup k importovanému modulu pomocí operátoru `.` je zdarma.
Pokud byla funkce nebo modul předán prostřednictvím argumentů nebo přiřazení proměnných, jeho použití bude stát 1 tik místo 0.
Cykly `for` a `while` trvají jeden tik na spuštění, ale iterace jsou zdarma (nepočítaje čas na vyhodnocení výrazů podmínky/sekvence).
`return`, `break` a `continue` jsou všechny zdarma.
`pass` trvá jeden tik, takže jej lze použít k vytvoření přesných zpoždění.
Indexování do datové struktury trvá jeden tik pro operátor indexu a v případě slovníku nebo množiny další tiky v závislosti na velikosti klíče.

Počet tiků, které vestavěné funkce potřebují k provedení, je zdokumentován v dokumentaci každé funkce individuálně.
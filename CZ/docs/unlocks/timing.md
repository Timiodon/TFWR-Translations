# Timing
Pokud chceš své postupy opravdu optimalizovat, musíš pochopit, jak se ve hře měří čas.  Tento odemykatelný prvek se celý točí právě kolem toho.

## Nové funkce
Existují dvě užitečné funkce pro měření doby trvání:

`get_time()` vrací čas v sekundách od začátku hry.

`get_tick_count()` vrací počet „ticků“ (časových kroků) provedených od začátku vykonávání.

Tyto dvě funkce, stejně jako `quick_print()`, jsou zcela zdarma — ani jejich volání nestojí žádné ticky.

## Detaily běhu

### Upozornění
Takhle výkon ve skutečnosti ve světě programování nefunguje. Toto jsou jen pravidla vytvořená pro účely hry, aby měření času bylo konzistentní a srozumitelné.  
Bude tě to zajímat hlavně tehdy, pokud chceš svůj kód extrémně optimalizovat.

Základní jednotkou času pro vykonávání kódu je „tick“. Bez vylepšení rychlosti a bez energie běží vykonávání rychlostí `400` ticků za sekundu.

Obecně platí, že operace, které kombinují dvě hodnoty jako `+, -, *, /, //, %, and, or, ...` trvají 1 tick.  
Jednohodnotové `-` a `not` jsou zdarma.  
Větev `if` trvá 1 tick (navíc k času potřebnému na vyhodnocení podmínky).  
Volání funkcí a čtení či zápis do proměnných jsou zdarma, ale definice funkcí trvá 1 tick.  
Příkazy `import` jsou zdarma.  
Přístup k importovanému modulu pomocí `.` operátoru je také zdarma.  
Pokud je funkce nebo modul předán přes argument nebo přiřazen do proměnné, jejich použití stojí 1 tick místo 0.  
Smyčky `for` a `while` trvají 1 tick při spuštění, ale jednotlivé iterace jsou zdarma (nepočítaje čas na vyhodnocení podmínek nebo sekvencí).  
`return`, `break` a `continue` jsou zdarma.  
`pass` trvá 1 tick, takže můžeš vytvářet přesné časové prodlevy.  
Indexování do datové struktury trvá 1 tick pro přístupový operátor a v případě slovníků či množin navíc další ticky podle velikosti klíče.

Počet ticků, které zabírají vestavěné funkce, je uveden v dokumentaci každé funkce zvlášť.

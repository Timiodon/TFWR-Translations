# Debug
Někdy kód prostě nefunguje a je potřeba zjistit proč. K tomu existuje několik užitečných nástrojů.

Prvním z nich je krokové provádění programu.  
Do režimu krokování se přepneš tlačítkem vedle tlačítka Spustit nebo nastavením breakpointu.

Breakpointy lze přidat kliknutím do panelu vlevo od kódu.  
![](Breakpoints227)  
Když běh programu dosáhne řádku s breakpointem, automaticky se přepne do režimu krokování.

Když najedeš myší na proměnnou, zobrazí se její aktuální hodnota.

Funkce `print()` je také velmi užitečná – vypíše jakoukoli hodnotu, kterou jí předáš, přímo do vzduchu.

Příklady:

Vypíše „0.24“  
`print(0.24)`

Vypíše „True“ nebo „False“.  
`print(can_harvest())`

Vypíše aktuální pozici.  
`print(get_pos_x(), get_pos_y())`

Funkce `print()` vypisuje hodnoty přímo do vzduchu i na stránku [Output](docs/output.md).

Zápis do vzduchu může být někdy pomalejší, pokud chceš vypisovat hodně hodnot.  
V takovém případě můžeš použít funkci `quick_print()`, která vypisuje pouze do výstupního okna.

Výstupní okno také zaznamenává varování a chyby, takže pokud něco nefunguje podle očekávání, je užitečné ho zkontrolovat.

Když se běh programu zastaví, výstup se také uloží do souboru output.txt ve složce hry. [output.txt](persistent_data_path/output.txt)
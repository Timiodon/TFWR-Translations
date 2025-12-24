# Ladění
Někdy kód nefunguje a je potřeba najít proč. K dispozici je několik nástrojů, které s tím pomůžou.

Prvním je krokové (step-by-step) provádění programu.
Do krokového režimu se dostanete tlačítkem vedle tlačítka Execute nebo nastavením breakpointu.

Breakpointy lze přidat kliknutím do panelu vlevo od kódu.
![](Breakpoints227)
Když se provádění dostane na řádek s breakpointem, přepne se automaticky do krokového režimu.

Po najetí myší na proměnnou se zobrazí její aktuální hodnota.

Funkce `print()` je také velmi užitečná — vypíše libovolnou předanou hodnotu přímo do vzduchu.

Příklady:

Vytiskne "0.24".
`print(0.24)`

Vytiskne "True" nebo "False".
`print(can_harvest())`

Vytiskne aktuální pozici.
`print(get_pos_x(), get_pos_y())`

Funkce `print` zapisuje hodnotu do vzduchu i na stránku [Výstup](docs/output.md).

Pokud chcete tisknout hodně hodnot a je to pomalé, použijte `quick_print()`, která tiskne pouze do výstupního okna.

Výstupní okno také loguje varování a chyby, takže pokud něco nefunguje, je užitečné ho zkontrolovat.

Po zastavení provádění se vypisují data i do souboru `output.txt` ve složce hry. [output.txt](persistent_data_path/output.txt).
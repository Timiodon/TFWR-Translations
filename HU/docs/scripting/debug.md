# Debug
Néha a kód egyszerűen nem működik, és ki kell derítened, miért. Van néhány eszköz, ami segít ebben.

Az első a program lépésenkénti végrehajtása.
Beléphetsz lépésenkénti módba a Végrehajtás gomb melletti gombbal vagy breakpoint beállításával.

Breakpointok hozzáadhatók a kód melletti breakpoint panelre kattintva.
![](Breakpoints227)
Amikor a végrehajtás eléri a breakpoint sorát, automatikusan lépésenkénti módba kapcsol.

Amikor a változó fölé viszed az egeret, megjelenik az aktuális értéke.

A `print()` függvény is nagyon hasznos lehet. Bármely átadott értéket közvetlenül a levegőbe ír.

Példák:

Írja ki a "0.24"-et.
`print(0.24)`

Írja ki a "True" vagy "False"-t.
`print(can_harvest())`

Írja ki az aktuális pozíciót.
`print(get_pos_x(), get_pos_y())`

A print függvény az értéket közvetlenül a levegőbe és a [Kimenet](docs/output.md) oldalra írja.

A levegőbe írás néha egy kicsit lassú lehet, ha sok értéket akarsz kiírni.
Ebben az esetben használhatod a `quick_print()` függvényt, ami csak a kimeneti ablakba ír.

A kimeneti ablak a figyelmeztetéseket és hibákat is naplózza, szóval ha valami nem a várt módon működik, hasznos lehet ellenőrizni.

Amikor a végrehajtás leáll, a kimenet a game folderben lévő output.txt fájlba is íródik. [output.txt](persistent_data_path/output.txt).
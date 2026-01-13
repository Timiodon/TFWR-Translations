# Nahrát Zálohu
Bohužel se někdy může stát, že se uložená hra poškodí nebo dojde ke ztrátě některých souborů s kódem. Pokud se ti to stane, můžeš zkusit načíst zálohu. Pokud se to děje často, zkus vypnout Steam Cloud.

Záloha se vytvoří pokaždé, když se hra uloží, a několik posledních záloh se uchovává pro případ, že bude potřeba něco obnovit.
Tyto zálohy najdeš ve složce [backup directory](persistent_data_path/Backup). Jedná se o kopie uložených her ze složky [save directory](persistent_data_path/Saves).
Nejjednodušší způsob, jak načíst zálohu, je zkopírovat složku konkrétní zálohy, kterou chceš načíst, do složky s uloženými hrami.

Uložená hra je složka, která obsahuje soubor `save.json` a několik `.py` souborů.
Pokud jsi přišel pouze o několik souborů s kódem, nebo pokud soubory s kódem zůstaly, ale soubor `save.json` je poškozený, můžeš nahradit pouze poškozené části odpovídajícími soubory ze zálohy.
# Načítání záloh
Bohužel se občas stane, že je soubor se save poškozený nebo přijdete o některé soubory s kódem. Když se to stane, můžete zkusit načíst zálohu. Pokud se to děje opakovaně, zkuste vypnout Steam Cloud.

Záloha se vytvoří při každém uložení hry a uchovává se několik posledních záloh pro případ, že budete něco potřebovat obnovit.
Zálohy najdete ve [složce záloh](persistent_data_path/Backup). Jsou to kopie uložených her ze [složky se savy](persistent_data_path/Saves).
Nejjednodušší způsob, jak načíst zálohu, je zkopírovat složku konkrétní zálohy, kterou chcete obnovit, do složky se savy.

Save je složka obsahující soubor `save.json` a řadu `.py` souborů.
Pokud jste přišli jen o pár souborů s kódem, nebo jsou soubory s kódem stále přítomné, ale `save.json` je poškozený, můžete ze zálohy zkopírovat pouze chybějící nebo poškozené soubory.
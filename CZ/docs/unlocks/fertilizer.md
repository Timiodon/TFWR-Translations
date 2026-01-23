# Fertilizer
V určitém bodě už čekání na růst rostlin není dostatečně efektivní.  
Podobně jako u vody budeš automaticky dostávat 1 hnojivo každých 10 sekund, přičemž s každým vylepšením se toto množství zdvojnásobí.

Hnojivo dokáže nechat rostliny okamžitě vyrůst. `use_item(Items.Fertilizer)` zkrátí zbývající dobu růstu rostliny pod dronem o 2 sekundy.

To však má i vedlejší účinky.  
Rostliny vypěstované pomocí hnojiva budou nakažené.

Když je rostlina nakažená, polovina jejího výnosu se při sklizni změní na `Items.Weird_Substance`.  
Podivná látka (`Weird Substance`) může být použita i na rostliny — přepíná stav nákazy rostliny a všech sousedních rostlin.

Takže pokud zavoláš `use_item(Items.Weird_Substance)` na nakažené rostlině, vyléčí ji; pokud ji použiješ na zdravé rostlině, nakazí ji.

Pokud ji použiješ na nakažené rostlině, která má zdravé sousedy, rostlina se vyléčí, ale sousedé se nakazí — a naopak.

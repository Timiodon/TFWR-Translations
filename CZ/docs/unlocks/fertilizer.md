# Hnojivo
V určitém okamžiku čekání na růst rostlin prostě už není dostatečně efektivní.
Podobně jako u vody automaticky obdržíte 1 hnojivo každých 10 sekund, což se s každým vylepšením zdvojnásobuje.

Hnojivo může způsobit, že rostliny vyrostou okamžitě. `use_item(Items.Fertilizer)` zkrátí zbývající dobu růstu rostliny pod dronem o 2 sekundy.

To má určité vedlejší účinky.
Rostliny vypěstované s hnojivem budou infikovány.

Když je rostlina infikována, polovina jejího výnosu se při sklizni změní na `Items.Weird_Substance` (podivná látka).
Podivnou látku lze také použít na rostliny, což má za následek přepnutí stavu infikování rostliny a všech sousedních rostlin.

Takže pokud zavoláte `use_item(Items.Weird_Substance)` na infikovanou rostlinu, vyléčí ji to, ale pokud ji použijete na zdravou rostlinu, infikuje ji to.

Pokud ji použijete na infikovanou rostlinu, která má zdravé sousedy, rostlinu vyléčí, ale infikuje sousedy a naopak.
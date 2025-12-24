# Zalévání
Rostliny rostou rychleji, když jsou zalévány. Půda má hladinu vody v rozmezí od `0` do `1`.
Funkce `get_water()` vrací hladinu vody v půdě, nad kterou se nachází.

Rychlost růstu rostliny se lineárně škáluje od 1x rychlosti při hladině vody 0 do 5x rychlosti při hladině vody 1.

Půda časem vysychá: V průměru ztratí 1 % své aktuální vody za sekundu, ale existuje v tom určitá náhodná odchylka. Udržování vysoké hladiny vody spotřebuje mnohem více vody než udržování nízké hladiny vody.

Na své rostliny můžete použít vodu. Jedna nádrž vody se automaticky přidá do vašeho inventáře každých 10 sekund.
Vylepšení `Unlocks.Watering` zdvojnásobí množství vody, které získáte každých 10 sekund.

Nádrž pojme `0.25` vody.

Zavolejte `use_item(Items.Water)` nad jakoukoli půdou, abyste ji zalili.

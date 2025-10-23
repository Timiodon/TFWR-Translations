# Watering
Rostliny rostou rychleji, když jsou zalévané. Půda má úroveň vlhkosti od `0` do `1`.  
Funkce `get_water()` vrací aktuální úroveň vody v půdě pod dronem.

Rychlost růstu rostliny se zvyšuje lineárně — od 1× rychlosti při hladině vody 0 až po 5× rychlost při hladině vody 1.

Půda časem vysychá: průměrně ztrácí 1 % své aktuální vody za sekundu, ale existuje určitá náhodná odchylka. Udržování vysoké úrovně vody spotřebuje mnohem více vody než udržování nízké.

Na rostliny můžeš použít vodu. Jeden zásobník vody se automaticky přidá do inventáře každých 10 sekund.  
Vylepšení `Unlocks.Watering` zdvojnásobí množství vody, které dostaneš každých 10 sekund.

Jeden zásobník obsahuje `0.25` jednotky vody.

Zavolej `use_item(Items.Water)` nad jakoukoli půdou, abys ji zalil.

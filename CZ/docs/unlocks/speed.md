# Vylepšení rychlosti
Rychlost provádění byla zdvojnásobena. Problém je v tom, že dron nyní sklízí rychleji, než tráva stihne dorůst, což má za následek žádnou sklizeň. K vyřešení tohoto problému jsou nyní odemčeny větve [if](docs/scripting/if.md) a funkce [can_harvest](functions/can_harvest).

## Kontrola před sklizní
Doposud jsme měli jako podmínky pouze `True` a `False`, což samozřejmě není s `if` příliš užitečné.

Nová funkce can_harvest() poskytuje lepší podmínku. `can_harvest()` vrací `True`, pokud lze rostlinu pod dronem sklidit, a `False` v opačném případě.

`if can_harvest():
	#udělej něco`

Důvod, proč můžete tuto funkci použít jako podmínku takto, je ten, že vrací booleovskou hodnotu.

Návratová hodnota v podstatě znamená, že po provedení funkčnosti se výraz volání funkce vyhodnotí na vrácenou hodnotu.

Co se stane, když běží výše uvedený kód:
	- spustí se if
	- zavolá se `can_harvest()`
	- `can_harvest()` udělá svou věc
	- `can_harvest()` vrátí `True` nebo `False`
	- příkaz je nyní `if True:` nebo `if False:`
	- blok kódu se provede pouze tehdy, pokud lze sklízet

Nyní můžeme použít `if`, abychom zabránili dronu sklízet příliš brzy.
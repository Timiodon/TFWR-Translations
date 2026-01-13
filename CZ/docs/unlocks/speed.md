# Zvýšení rychlosti
Rychlost vykonávání byla zdvojnásobena. Problém je v tom, že dron nyní sklízí rychleji, než tráva stíhá růst, což vede k tomu, že nakonec nesklidí vůbec nic. Aby bylo možné tuto situaci řešit, byly nyní odemknuty větve [if](docs/scripting/if.md) a funkce [can_harvest](functions/can_harvest).

## Kontrola před sklizní
Doposud jsme měli jako podmínky pouze `True` a `False`, což samozřejmě není pro `if` příliš užitečné.

Nová funkce `can_harvest()` poskytuje lepší podmínku. `can_harvest()` vrací `True`, pokud rostlina pod dronem může být sklizena, a `False` v opačném případě.

`if can_harvest():
	#do something`

Důvod, proč můžeš tuto funkci použít jako podmínku, je ten, že vrací **návratová boolean hodnota**.

**návratová boolean hodnota** v podstatě znamená, že po provedení funkce se výraz volající funkci vyhodnotí na hodnotu, kterou funkce vrátila.

Co se stane, když se spustí výše uvedený kód:
	- spustí se `if`
	- zavolá se `can_harvest()`
	- `can_harvest()` provede svou činnost
	- `can_harvest()` vrátí `True` nebo `False`
	- výraz se nyní změní na `if True:` nebo `if False:`
	- blok kódu se provede pouze tehdy, pokud je možné sklízet

Nyní můžeme použít `if`, abychom zabránili dronovi sklízet příliš brzy.

# Rozšíření 2
Vaše farma se opět rozrostla! Nyní již dlaždice nejsou v pěkné řadě, takže musíte najít způsob, jak procházet čtvercovou mřížku.

S cyklem `while` to není možné, dokud neodemknete smysly a operátory.
Je čas představit cyklus `for`.

Vše o cyklu `for` si můžete přečíst na stránce [Cyklus For](docs/scripting/for.md), ale prozatím jej budete potřebovat pouze k opakování kódu pevně stanovený počet krát.

`#udělej n salt
for i in range(5):
	do_a_flip()`

`range(n)` vytvoří rozsah čísel od `0` do `n-1`, který má `n` prvků. Cyklus `for` spustí své tělo jednou pro každý prvek v sekvenci. V tomto příkladu bude `do_a_flip()` zavoláno `5` krát.

Nyní je také k dispozici funkce `get_world_size()`. Vrací délku strany vaší farmy. Tímto způsobem můžete psát kód, který se nerozbije s dalším vylepšením rozšíření.

`for i in range(get_world_size()):
	harvest()
	move(North)`

Tento příklad sklidí jeden sloupec farmy pro jakoukoli velikost farmy.

Pokud jste uvízli ve snaze přijít na to, jak pohybovat dronem po farmě, podívejte se na nápovědu níže.
<spoiler=zobrazit nápovědu>Existuje samozřejmě několik způsobů, jak se pohybovat po farmě.
To, co hledáme, je způsob, jak ji projít systematickým způsobem, který se nerozbije, když se farma znovu rozroste.
Systematický způsob, jak se dostat na každé místo na farmě, by bylo opakovat následující 2 kroky donekonečna:

1. Pohybujte se na `North` (sever), dokud se nevrátíte na začátek.
2. Pohněte se na `East` (východ).

`for i in range(get_world_size()):` může být užitečné pro převedení této myšlenky do kódu.
</spoiler>
<spoiler=zobrazit možné řešení> Základní průchod by mohl vypadat takto:

`for i in range(get_world_size()):
	for j in range(get_world_size()):
		#udělej salto na každém políčku
		do_a_flip()
		move(North)
	move(East)`
</spoiler>
# Rozšíření 2
Tvoje farma se znovu rozšířila! Dlaždice už teď nejsou v jedné řadě, takže musíš najít způsob, jak projít čtvercovou mřížku.

Pomocí smyčky `while` to zatím není možné, dokud neodemkneš smysly (senses) a operátory.  
Nastal čas představit smyčku `for`.

O smyčce `for` si můžeš přečíst vše na stránce [For Loop](docs/scripting/for.md), ale pro začátek ji budeš potřebovat jen k opakování kódu pevně daný početkrát.

`#udělej n otoček
for i in range(5):
	do_a_flip()`

`range(n)` vytvoří rozsah čísel od `0` do `n-1`, který má `n` prvků. Smyčka `for` provede své tělo jednou pro každý prvek v této posloupnosti. V tomto příkladu bude `do_a_flip()` zavoláno `5`×.

Nyní je dostupná i funkce `get_world_size()`. Ta vrací délku strany tvé farmy, takže můžeš psát kód, který se nerozbije při dalším rozšíření farmy.

`for i in range(get_world_size()):
	harvest()
	move(North)`

Tento příklad sklidí jeden sloupec farmy bez ohledu na její velikost.

Pokud nevíš, jak přesně dronem pohybovat po celé farmě, podívej se na nápovědu níže.
<spoiler=show hint>Existuje samozřejmě několik způsobů, jak se po farmě pohybovat.  
Cílem je ale najít systematický způsob, který se nerozbije při dalším rozšíření farmy.  
Systematické pokrytí celé farmy lze udělat opakováním těchto dvou kroků donekonečna:

1. Pohybuj se na `North`, dokud se nevrátíš zpět.
2. Pohni se na `East`

`for i in range(get_world_size()):` se ti může hodit při převodu této myšlenky do kódu.
</spoiler>
<spoiler=show possible solution>Základní průchod farmou může vypadat takto:

`for i in range(get_world_size()):
	for j in range(get_world_size()):
		#udělej otočku na každé dlaždici
		do_a_flip()
		move(North)
	move(East)`
</spoiler>

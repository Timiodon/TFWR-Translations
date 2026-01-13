# Trees
[Stromy](objects/tree) jsou lepší způsob, jak získat dřevo než keře — dávají totiž 5 kusů dřeva. Stejně jako keře je můžeš sázet na trávu nebo ornou půdu.

Stromy mají rády prostor, a pokud je zasadíš těsně vedle sebe, jejich růst se zpomalí. Doba růstu se zdvojnásobí za každý strom, který roste přímo na dlaždici na sever, východ, západ nebo jih od něj. Takže pokud zasadíš stromy na každé políčko, porostou `2*2*2*2 = 16`× pomaleji.

<spoiler=show> Operátor `%` se tu může hodit. Pamatuj, že `%` vrací zbytek po dělení. Sudá čísla dělená `2` mají zbytek `0`, zatímco lichá mají zbytek `1`.  
Můžeš tedy zjistit, zda je číslo sudé, například takto:

`def is_even(n):
	return n % 2 == 0`

Tato funkce vrátí `True`, pokud je `n` sudé, a `False`, pokud není.
</spoiler>

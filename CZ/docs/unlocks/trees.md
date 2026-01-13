# Stromy
[Stromy](objects/tree) jsou lepší způsob, jak získat dřevo, než keře. Každý dává 5 dřeva. Stejně jako keře je lze sázet na trávu nebo půdu.

Stromy mají rády prostor a jejich sázení hned vedle sebe zpomalí jejich růst. Doba růstu se zdvojnásobí za každý strom, který je na políčku přímo na sever, východ, západ nebo jih od něj. Takže pokud zasadíte stromy na každé políčko, budou růst `2*2*2*2 = 16`krát déle.

<spoiler=zobrazit> Operátor `%` zde může být užitečný. Pamatujte, že operátor `%` vrací zbytek po dělení. Sudá čísla dělená `2` mají zbytek `0` a lichá čísla dělená `2` mají zbytek `1`.
Takže můžete zkontrolovat, zda je číslo sudé, takto:

`def is_even(n):
	return n % 2 == 0`

To vrátí `True`, pokud je n sudé, a `False`, pokud není.
</spoiler>
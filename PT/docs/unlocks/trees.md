# Árvores
[Árvores](objects/tree) são uma maneira melhor de obter madeira do que arbustos. Elas dão 5 de madeira cada. Como os arbustos, podem ser plantadas na grama ou no solo.

As árvores gostam de ter algum espaço e plantá-las bem próximas umas das outras diminuirá seu crescimento. O tempo de crescimento é dobrado para cada árvore que está em uma casa diretamente a North, East, West ou South dela. Então, se você plantar árvores em todas as casas, elas levarão `2*2*2*2 = 16` vezes mais tempo para crescer.

<spoiler=show> O operador `%` pode ser útil aqui. Lembre-se que o operador `%` retorna o resto da divisão. Números pares divididos por `2` têm resto `0` e números ímpares divididos por `2` têm resto `1`.
Então você pode verificar se um número é par assim:

`def is_even(n):
	return n % 2 == 0`

Isso retorna `True` se n for par e `False` se não for.
</spoiler>
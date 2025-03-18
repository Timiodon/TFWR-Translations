# Árvores
[Trees](objects/tree) são uma maneira melhor de conseguir madeira do que arbustos. Elas dão 5 madeiras cada. Assim como os arbustos, podem ser plantadas na grama ou no solo.

As árvores gostam de ter espaço e plantá-las bem próximas umas das outras vai atrasar seu crescimento. O tempo de crescimento é dobrado para cada árvore que estiver em um quadrado diretamente ao norte, leste, oeste ou sul dela. Então, se você plantar árvores em todos os quadrados, elas levarão `2*2*2*2 = 16` vezes mais tempo para crescer.

<spoiler=show> O operador `%` pode ser útil aqui. Lembre-se de que o operador `%` retorna o restante da divisão. Números pares divididos por `2` têm resto `0` e números ímpares divididos por `2` têm resto `1`. Então você pode verificar se um número é par assim:

`def is_even(n):
	return n % 2 == 0`

Isso retorna `True` se n for par e `False` se não for.
</spoiler>
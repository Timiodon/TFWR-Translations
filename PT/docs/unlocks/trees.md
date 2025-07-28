# Árvores
As [árvores](objects/tree) são uma forma melhor de obter madeira do que os arbustos. Dão 5 de madeira cada uma. Tal como os arbustos, podem ser plantadas em relva ou solo.

As árvores gostam de ter algum espaço e plantá-las umas ao lado das outras irá abrandar o seu crescimento. O tempo de crescimento é duplicado por cada árvore que está num quadrado diretamente a norte, este, oeste ou sul dela. Portanto, se plantares árvores em todos os quadrados, elas demorarão `2*2*2*2 = 16` vezes mais tempo a crescer.

<spoiler=mostrar> O operador `%` pode ser útil aqui. Lembra-te que o operador `%` retorna o resto da divisão. Os números pares divididos por `2` têm um resto de `0` e os números ímpares divididos por `2` têm um resto de `1`.
Então, podes verificar se um número é par desta forma:

`def is_even(n):
	return n % 2 == 0`

Isto retorna `True` se n for par e `False` se não for.
</spoiler>
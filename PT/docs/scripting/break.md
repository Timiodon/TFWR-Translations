# Break
`break` permite parar um loop mais cedo. Quando a instrução `break` é alcançada, ela sairá imediatamente do loop mais interno e começará a executar o código após o loop.

`for i in range(10):
	break
print(i)`
Isso imprime `0` porque `i` é `0` na primeira iteração do loop e então a instrução break encerra o loop.

Também funciona em loops `while`.

`while True:
	if can_harvest():
		break`

Este código executa o loop `while` até que `can_harvest()` seja `True`. 
Tem o mesmo efeito que

`while not can_harvest():
	pass`

Em loops aninhados, `break` sempre sai do loop mais interno.

`for i in range(10):
	for j in range(10):
		break
		print("isso nunca é impresso")
	print("isso é impresso 10 vezes")`
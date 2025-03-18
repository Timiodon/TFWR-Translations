# Break
`break` permite parar um loop antes do fim. Quando a instrução `break` é alcançada, ela sai imediatamente do loop mais interno e começa a executar o código após o loop.

`for i in range(10):
	break
print(i)`
Isso imprime `0` porque `i` é `0` na primeira iteração do loop e então a instrução break termina o loop.

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
		print("this is never printed")
	print("this is printed 10 times")`
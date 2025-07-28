# Break
`break` permite parar um loop mais cedo. Quando a instrução `break` é alcançada, ela sairá imediatamente do loop mais interno e começará a executar o código após o loop.

`for i in range(10):
	break
print(i)`
Isto imprime `0` porque `i` é `0` na primeira iteração do loop e depois a instrução break termina o loop.

Também funciona em loops `while`.

`while True:
	if can_harvest():
		break`

Este código executa o loop `while` até `can_harvest()` ser `True`.
Tem o mesmo efeito que

`while not can_harvest():
	pass`

Em loops aninhados, `break` sai sempre do loop mais interno.

`for i in range(10):
	for j in range(10):
		break
		print("isto nunca é impresso")
	print("isto é impresso 10 vezes")`
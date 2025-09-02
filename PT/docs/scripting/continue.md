# Continue
`continue` permite parar a iteração atual de um loop e pular para a próxima iteração do loop mais interno.

`for i in range(10):
	continue
    print("isso nunca é impresso")`

Isso executa todas as `10` iterações do loop, mas a instrução `print` após o `continue` é sempre pulada.

Também funciona em loops `while`.

`while True:
	if not can_harvest():
		continue
    
    harvest()`

Este código só chama `harvest()` quando `can_harvest()` é `True`. 
Tem o mesmo efeito que

`while True:
	if can_harvest():
		harvest()`

Em loops aninhados, `continue` sempre afeta o loop mais interno.

`for i in range(10):
	for j in range(10):
	    print("isso é impresso 100 vezes")
		continue
		print("isso nunca é impresso")
	print("isso é impresso 10 vezes")`
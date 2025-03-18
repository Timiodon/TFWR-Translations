# Continue
continue permite parar a iteração atual de um loop e pular para a próxima iteração do loop mais interno.

`for i in range(10):
    continue
    print("this is never printed")`

Isso executa todas as `10` iterações do loop, mas o comando `print` após o `continue` é sempre pulado.

Também funciona em loops `while`.

`while True:
    if not can_harvest():
        continue
    
    harvest()`

Esse código só chama `harvest()` quando `can_harvest()` é `True`.
Tem o mesmo efeito que

`while True:
    if can_harvest():
        harvest()`

Em loops aninhados, `continue` sempre afeta o loop mais interno.

`for i in range(10):
    for j in range(10):
        print("this is printed 100 times")
        continue
        print("this is never printed")
    print("this is printed 10 times")`
# Melhoria de Velocidade
A velocidade de execução foi duplicada. O problema é que o drone agora colhe mais rápido do que a relva consegue crescer, resultando em nenhuma colheita. Para lidar com isto, as ramificações [if](docs/scripting/if.md) e a função [can_harvest](functions/can_harvest) estão agora desbloqueadas.

## Verificar Antes de Colher
Até agora só tínhamos `True` e `False` como condições, o que, claro, não é muito útil com `if`.

A nova função can_harvest() fornece uma condição melhor. `can_harvest()` retorna `True` se a planta debaixo do drone puder ser colhida e `False` caso contrário.

`if can_harvest():
	#fazer algo`

A razão pela qual podes usar esta função como condição desta forma é porque ela retorna um valor booleano.

Um valor de retorno significa essencialmente que, após a funcionalidade ser executada, a expressão da chamada da função avalia para o valor retornado.

O que acontece quando o código acima é executado:
	-o if é executado
	-`can_harvest()` é chamada
	-`can_harvest()` faz o que tem a fazer
	-`can_harvest()` retorna `True` ou `False`
	-a declaração é agora `if True:` ou `if False:`
	-o bloco de código só é executado se for possível colher

Agora podemos usar `if` para impedir que o drone colha demasiado cedo.
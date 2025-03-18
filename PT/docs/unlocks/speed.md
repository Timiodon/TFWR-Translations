# Upgrade de Velocidade
A velocidade de execução foi dobrada. O problema é que o drone agora colhe mais rápido do que a grama pode crescer, resultando em nenhuma colheita. Para lidar com isso, os ramos [if](docs/scripting/if.md) e a função [can_harvest](functions/can_harvest) agora estão desbloqueados.

## Verificando Antes de Colher
Até agora só tínhamos `True` e `False` como condições, o que, é claro, não é muito útil com `if`.

A nova função can_harvest() oferece uma condição melhor. `can_harvest()` retorna `True` se a planta sob o drone pode ser colhida e `False` caso contrário.

`if can_harvest():
	#do something`

A razão pela qual você pode usar essa função como condição é porque ela retorna um valor booleano.

Um valor de retorno essencialmente significa que, após a execução da funcionalidade, a expressão de chamada da função é avaliada para o valor retornado.

O que acontece quando o código acima é executado:
	-o if é executado
	-`can_harvest()` é chamado
	-`can_harvest()` faz sua função
	-`can_harvest()` retorna `True` ou `False`
	-a declaração agora é `if True:` ou `if False:`
	-o bloco de código só é executado se puder colher

Agora podemos usar `if` para impedir que o drone colha cedo demais.
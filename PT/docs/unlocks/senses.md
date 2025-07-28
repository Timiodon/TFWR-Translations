# Sentidos
O drone agora consegue ver!

As funções `get_pos_x()` e `get_pos_y()` retornam a posição x e y atual do drone. Na posição inicial, ambas são `0`. A posição x aumenta em `1` a cada quadrado em direção a `East` e a posição y aumenta em `1` a cada quadrado em direção a `North`.

`num_items(item)` retorna quantos de um item tens.
Por exemplo, `num_items(Items.Hay)` retorna quanto feno tens.

`get_entity_type()` e `get_ground_type()` retornam o tipo de entity ou solo que está debaixo do drone.

Faz um pino se estiveres sobre um arbusto:
`if get_entity_type() == Entities.Bush:
	do_a_flip()`

A palavra-chave `None` também está desbloqueada agora! `None` é um valor que representa que não há valor.
Por exemplo, uma função que não tem uma instrução `return` na verdade retornará `None`.

`get_entity_type()` retorna `None` se não houver nenhuma entity debaixo do drone.

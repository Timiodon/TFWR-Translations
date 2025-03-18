# Sentidos
O drone pode ver agora!

As funções `get_pos_x()` e `get_pos_y()` retornam a posição atual x e y do drone. Na posição inicial, ambas são `0`. A posição x aumenta em `1` para cada azulejo em direção ao `East` e a posição y aumenta em `1` para cada azulejo em direção ao `North`.

`num_items(item)` retorna quantos itens você possui.
Por exemplo, `num_items(Items.Hay)` retorna quanto feno você tem.

`get_entity_type()` e `get_ground_type()` retornam o tipo de entidade ou terreno que está sob o drone.

Faça um flip se estiver sobre um arbusto:
`if get_entity_type() == Entities.Bush:
	do_a_flip()`

A palavra-chave `None` também foi desbloqueada agora! `None` é um valor que representa que não há valor.
Por exemplo, uma função que não tem uma declaração `return` na verdade retornará `None`.

`get_entity_type()` retorna `None` se não houver nenhuma entidade sob o drone.
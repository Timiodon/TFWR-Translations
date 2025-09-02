# Sentidos
O drone pode ver agora! 

As funções `get_pos_x()` e `get_pos_y()` retornam a posição x e y atual do drone. Na posição inicial, ambas são `0`. A posição x aumenta em `1` a cada casa em direção a `East` e a posição y aumenta em `1` a cada casa em direção a `North`.

`num_items(item)` retorna quantos itens de um tipo você tem.
Por exemplo, `num_items(Items.Hay)` retorna quanto feno você tem.

`get_entity_type()` e `get_ground_type()` retornam o tipo de entidade ou solo que está sob o drone.

Dê uma pirueta se estiver sobre um arbusto:
`if get_entity_type() == Entities.Bush:
	do_a_flip()`

A palavra-chave `None` também está desbloqueada agora! `None` é um valor que representa a ausência de valor.
Por exemplo, uma função que não tem uma declaração `return` na verdade retornará `None`.

`get_entity_type()` retorna `None` se не houver entidade sob o drone.


Se você quiser descobrir quantos de um determinado desbloqueio você tem, use a função `num_unlocked(unlock)`.

Por exemplo, `num_unlocked(Unlocks.Speed)` retornará o número de melhorias de velocidade que você tem.

`num_unlocked(Unlocks.Senses)` retornará `1` se os sentidos estiverem desbloqueados e `0` se не estiverem.

Você também pode usar `num_unlocked()` em Itens, Entidades ou Solos. Isso retornará `1` se estiver desbloqueado, caso contrário `0`.

Tenha cuidado, `num_unlocked(Unlocks.Carrots)` retornará o número de vezes que foi desbloqueado/melhorado.
`num_unlocked(Items.Carrot)` retornará apenas `0` ou `1`. (O mesmo para outras plantas)
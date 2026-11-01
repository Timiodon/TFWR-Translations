[<- Arroz](docs/unlocks/rice.md) <right>[Blocos Coloridos ->](docs/unlocks/debug_place.md)
<right>[Pirâmides ->](docs/unlocks/pyramid.md)
---
# Bambu
O bambu é uma planta que cresce para cima. Seu drone precisa retirar regularmente os frutos marrons para que ele continue crescendo. Podemos fazer isso com o comando `hover` recém-desbloqueado.

O bambu deve ser plantado em solo arado (`Grounds.Soil`) e custa arroz.

O código abaixo planta bambu e espera que cresça até o primeiro fruto.
{{codeexample
{
"camera_position": {"x": -1, "y": 0, "z": 10},
"show_image": true,
"image_size": {"x": 800, "y": 500},
"show_code": true,
"show_inventory": true,
"show_output": false,
"collapsing": true,
"autoplay": false,
"items": [{"item": "rice", "n": 100}],
"world_size": {"x": 4, "y": 4},
"execution_speed": 2,
"action_ticks": 200,
"operation_ticks": 200,
"seed": 1,
"exclude_unlocks": ["watering", "fertilizer", "mushrooms", "coal"]
}
#SETUP
move(North)
move(East)
#CODE
till()
plant(Entities.Bamboo)
move(East) # afaste-se para o bambu crescer
}}

## Frutos
O bambu cresce exatamente 1 bloco por segundo.

O bambu produz frutos a cada poucos blocos. Quando isso acontece, ele para de crescer e você precisa entrar nele com o drone para destruir o fruto. O bambu pode crescer até o terceiro fruto. Depois disso, não crescerá mais em altura, mesmo que você retire o fruto.

Para retirar frutos, primeiro use `hover` para alcançar a altura correta. Depois use `move` para entrar no fruto e retirá-lo, e novamente `move` para se afastar e deixar o bambu crescer.

Use `measure()` no bambu para verificar a altura do próximo fruto. `measure()` conta a partir de `0`, então `hover(measure())` leva o drone até a altura do fruto.

{{codeexample
{
"camera_position": {"x": -1, "y": 0, "z": 10},
"show_image": true,
"image_size": {"x": 800, "y": 500},
"show_code": true,
"show_inventory": true,
"show_output": false,
"collapsing": true,
"autoplay": false,
"items": [{"item": "rice", "n": 100}],
"world_size": {"x": 4, "y": 4},
"execution_speed": 2,
"action_ticks": 200,
"operation_ticks": 200,
"seed": 1,
"exclude_unlocks": ["watering", "fertilizer", "mushrooms", "coal"]
}
#SETUP
move(North)
move(East)
#CODE
till()
plant(Entities.Bamboo)
hover(measure()) # paire na altura do fruto

move(East) # afaste-se e espere crescer
for i in range(3):
    do_a_flip()

move(West) # retire o fruto
move(East) # afaste-se novamente
}}

## Pairando
O comando `hover` recebe um argumento: a altura em que pairar, um número de `0` a `18`. A altura padrão do drone é `1`. `hover` não permite descer para dentro de entidades sólidas. Se o drone já estiver sobre o bambu, não poderá entrar nele executando `hover(0)`.

`hover` retorna `True` se o drone alcançou a altura especificada, ou `False` caso contrário.

Também existe o comando `get_hover`, que retorna a altura atual em que o drone paira.

Se usar `dig`, `harvest` ou `plant` enquanto paira, o drone volta à altura padrão (`1`).

Por fim, a altura de voo não afeta `get_pos_z()`. Ele sempre retorna a posição z do bloco sob o drone.

## Colhendo Bambu
Você pode usar `harvest()`, mas a forma recomendada de colher bambu é entrar nele com o drone na altura `0` (`hover(0)`). Isso colhe a planta inteira de uma vez.

Para colher sem destruir o bambu, entre nele com `move` em qualquer altura, por exemplo usando `hover(3)`. Isso colhe todos os segmentos dessa altura para cima, mas mantém o bambu vivo. Um bambu parcialmente colhido dessa forma volta a produzir frutos, que você terá que retirar novamente.

Nos dois casos, a produção equivale ao quadrado do número de segmentos de bambu destruídos. Quanto mais alto o bambu, maior a produção.

---

[Estatísticas](docs/stats.md)      [Loop For](docs/scripting/for.md)      [Variáveis](docs/scripting/variables.md)      [If](docs/scripting/if.md)      [Funções](docs/scripting/functions.md)      [Arroz](docs/unlocks/rice.md)

[harvest()](functions/harvest)      [plant()](functions/plant)      [move()](functions/move)      [till()](functions/till)      [measure()](functions/measure)

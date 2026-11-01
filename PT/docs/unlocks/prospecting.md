[<- Ferro](docs/unlocks/iron.md)
---
# Prospecção de Ferro
Talvez você tenha percebido que às vezes é difícil encontrar veios de ferro. Você poderia escavar ao acaso, mas existe uma forma melhor: como o ferro é magnético, podemos detectá-lo à distância.

O comando `prospect_iron()` faz exatamente isso. `prospect_iron()` retorna a direção (`North`, `East`, `South` ou `West`) em que o drone deve se mover para dar um passo em direção ao minério de ferro mais próximo.

O comando custa 1 carvão.

`prospect_iron()` retorna `None` se o drone já estiver diretamente sobre o minério de ferro mais próximo, se você não tiver carvão suficiente ou se não houver ferro ao alcance.

Você pode usar o código a seguir para se aproximar um passo do próximo minério de ferro:

{{codeexample 
{
    "camera_position": {"x": -1, "y": 0, "z": 8},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [{"item": "coal", "n": 100}],
    "world_size": {"x": 5, "y": 5},
    "execution_speed": 1,
    "digging_speed": 10,
    "action_ticks": 200,
    "operation_ticks": 50,
    "seed": 8,
    "exclude_unlocks": ["watering", "fertilizer", "mushrooms", "quartz"]
}
#SETUP
jump(Unlocks.Iron)
#CODE
# Verifique se a prospecção retorna uma direção
if prospect_iron() != None:
    move(prospect_iron()) # Aproxime-se do veio de ferro
}}

Talvez você queira otimizar este código com uma variável, pois ele chama `prospect_iron()` duas vezes e custa 2 carvões.

## Cálculo de Distância
O minério de ferro mais próximo é calculado pelo número de passos que o drone precisa dar. Se houver minério 2 blocos a leste e 3 ao norte, a distância será 5, pois o drone levaria cinco passos para chegar lá.

Escavar também conta como um passo. Assim, se o ferro estiver enterrado 7 blocos abaixo, a distância será 12: cinco passos para se posicionar sobre o ferro e sete escavações para alcançá-lo.

---

[Ferro](docs/unlocks/iron.md)      [Sentidos Subterrâneos](docs/unlocks/underground_senses.md)

[move()](functions/move)      [dig()](functions/dig)      [prospect_iron()](functions/prospect_iron)

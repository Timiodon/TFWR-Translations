[<- Expansão 1](docs/unlocks/expand_1.md) <right>[Sentidos Subterrâneos ->](docs/unlocks/underground_senses.md)
<right>[Arroz ->](docs/unlocks/rice.md)
<right>[Carvão ->](docs/unlocks/coal.md)
---
# Mineração

Seu drone ganhou acesso a uma broca primitiva, que permite procurar tesouros no subsolo.

Você pode usar o comando `dig()` para escavar o bloco abaixo.

Por enquanto, vamos coletar alguns blocos:

{{codeexample 
{
    "camera_position": {"x": -1, "y": 0, "z": 8},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": false,
    "autoplay": true,
    "items": [{"item": "hay", "n": 100}, {"item": "wood", "n": 100}],
    "world_size": {"x": 4, "y": 4},
    "execution_speed": 2,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer", "mushrooms", "coal", "special_soils"]
}
#SETUP
move(North)
move(East)
#CODE
dig()
do_a_flip()
dig()
do_a_flip()
dig()
do_a_flip()
clear()
}}

Se quiser voltar à superfície, você pode usar `clear()` a qualquer momento. Isso também restaura sua fazenda.

Passe o mouse sobre um bloco para ver seu nome, estabilidade e dureza.

# Broca

À medida que escava mais fundo, você perceberá que os blocos ficam mais duros, fazendo a escavação levar mais tempo. Ainda bem que podemos melhorar a broca!

Você pode usar `get_hardness()` para verificar a dureza do bloco abaixo. Se encontrar uma área de blocos especialmente duros, pode ser melhor contorná-los para avançar mais rápido:

`while True:
    if get_hardness() < 5:
        dig()
    else:
        move(East)`

É claro que os blocos ficam cada vez mais resistentes conforme você desce. Essa estratégia ajuda, mas tem seus limites.

## Desmoronamentos

Escavar para baixo faz os blocos ao redor desmoronarem. Os quatro blocos ao lado do drone são sempre destruídos. Depois disso, o desmoronamento se propaga conforme a estabilidade do solo. Um bloco com estabilidade 1, como a pastagem, suporta uma diferença de altura de 1. Em outras palavras, se a pastagem tiver um vizinho vertical ou horizontal cuja coordenada z esteja 2 ou mais blocos abaixo, ela será destruída.

A estabilidade de um bloco aparece na dica exibida ao passar o mouse.

Quando um bloco desmorona, todos os blocos acima dele também são removidos. Você só recebe recursos dos blocos que o drone escava diretamente; blocos perdidos em um desmoronamento são destruídos sem render recursos.

---

[Sentidos Subterrâneos](docs/unlocks/underground_senses.md)      [Loop While](docs/scripting/while.md)

[move()](functions/move)      [dig()](functions/dig)

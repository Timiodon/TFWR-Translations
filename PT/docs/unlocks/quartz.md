[<- Ferro](docs/unlocks/iron.md) <right>[Cogumelo ->](docs/unlocks/mushroom.md)
---
# Quartzo
Depois dos veios de ferro em `Grounds.Rock`, você encontra quartzo no fundo da camada de rocha e na `Grounds.Dirt` dura abaixo (verifique a dureza com `get_hardness()` dos [Sentidos Subterrâneos](docs/unlocks/underground_senses.md)).

O código abaixo atravessa a terra e entra na camada de rocha. Lá, prospecta quartzo continuamente enquanto escava, até a distância ser menor que 2. Por fim, imprime a distância alcançada.
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
    "items": [{"item": "block", "n": 1}, {"item": "iron", "n": 100}],
    "world_size": {"x": 3, "y": 3},
    "execution_speed": 8,
    "digging_speed": 16,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 9,
    "exclude_unlocks": ["watering", "fertilizer", "mushrooms", "dynamite"]
}
#SETUP
move(East)
move(North)
#CODE
# Escave até a camada de rocha
while get_ground_type() != Grounds.Rock:
    dig()

# Continue até um veio de quartzo estar perto
while prospect_quartz() == None or prospect_quartz() >= 2:
    for i in range(10):
        dig()

# Imprima a distância final até o veio
print(prospect_quartz())
}}

## Estrutura dos Veios
O quartzo cresce em veios semelhantes a agulhas. Os veios formam colunas verticais, tornando-os difíceis de encontrar por tentativa e erro.

## Prospectando Quartzo
Felizmente, podemos transformar nosso ferro em algo parecido com uma vara de radiestesia para localizar esses veios com mais facilidade. O comando é `prospect_quartz()`.

`prospect_quartz()` funciona de forma diferente de `prospect_iron()`. Em vez da direção para o ferro mais próximo, retorna a distância 3D exata entre o bloco de quartzo mais próximo e o drone (distância euclidiana).

Executar `prospect_quartz()` custa 1 ferro, então use-o com moderação.

Se `prospect_quartz()` não encontrar quartzo por perto ou você não tiver ferro suficiente, ele retorna `None`.

## Estratégia
<spoiler=mostrar dica>Você pode prospectar e se mover repetidamente para observar como a distância muda. Em uma superfície plana, minimizar a distância pode levar você para cima de um veio de quartzo. Uma estratégia semelhante à busca binária pode minimizar as chamadas a `prospect_quartz()` e o ferro consumido.

Estratégias mais elaboradas podem usar geometria 2D para encontrar a interseção de dois ou mais círculos. Você também pode escolher o caminho difícil: uma trilateração completa, cruzando três esferas para encontrar a posição 3D exata do veio.

Para calcular uma raiz quadrada, use o operador de potência: por exemplo, `16**0.5` dá a raiz quadrada de 16. Não existem funções matemáticas integradas para trigonometria ou vetores; você terá que implementá-las.

Pode haver vários veios por perto, então medições próximas nem sempre apontam para o mesmo veio.</spoiler>

---

[Estatísticas](docs/stats.md)      [Mineração](docs/unlocks/mining.md)      [Sentidos Subterrâneos](docs/unlocks/underground_senses.md)      [Variáveis](docs/scripting/variables.md)      [Operadores](docs/scripting/operators.md)

[move()](functions/move)      [dig()](functions/dig)      [get_ground_type()](functions/get_ground_type)      [prospect_quartz()](functions/prospect_quartz)

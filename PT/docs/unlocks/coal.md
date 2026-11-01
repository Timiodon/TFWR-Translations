[<- Mineração](docs/unlocks/mining.md) <right>[Ferro ->](docs/unlocks/iron.md)
<right>[Salto ->](docs/unlocks/jump.md)
---
# Carvão
Vários minérios se escondem no subsolo, esperando que você os encontre e extraia. Ao atravessar a superfície e escavar em `Grounds.Dirt`, o primeiro minério que você encontra é carvão.

Não é preciso nada especial para extrair carvão: execute `dig()` quando o drone estiver diretamente sobre um bloco de `Grounds.Coal`. Use `get_ground_type()` para verificar o que está sob o drone e `get_ground_type(direction)` para verificar os quatro blocos adjacentes.

O programa a seguir é um bom ponto de partida para encontrar carvão. Ele escava para baixo em busca de uma camada de carvão.
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
    "items": [],
    "world_size": {"x": 4, "y": 4},
    "execution_speed": 4,
    "digging_speed": 2,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 2,
    "exclude_unlocks": ["watering", "fertilizer"]
}
#SETUP
move(North)
move(East)
move(East)
#CODE
# Escave até aparecer um bloco de carvão
while get_ground_type() != Grounds.Coal:
    dig()

# Extraia o carvão
dig()
}}

## Nota sobre Desmoronamentos
Você só recebe carvão dos blocos que escava diretamente, não dos que desmoronam ao redor do drone. Leve isso em conta para extrair o máximo de carvão e perder o mínimo em desmoronamentos.

## Estrutura dos Veios
Os veios formam camadas horizontais com 1 bloco de espessura, que você deve encontrar por acaso ao escavar a terra. A maioria dos blocos de carvão de uma camada fica diretamente adjacente, mas alguns só se conectam na diagonal.

As jazidas de carvão crescem proporcionalmente à fazenda. Continue melhorando [Expandir](unlocks/expand) para extrair mais carvão.

## Estratégia
<spoiler=mostrar dica>
Uma estratégia simples, sobretudo em fazendas pequenas, é escavar todos os blocos na profundidade em que você encontrou carvão. Para aumentar a eficiência, registre onde viu carvão usando `get_ground_type(direction)` e evite perder tempo passando sobre terra. Tome cuidado com as conexões diagonais, que você perderá se andar apenas sobre carvão.
</spoiler>

---

[Estatísticas](docs/stats.md)      [Mineração](docs/unlocks/mining.md)      [Sentidos Subterrâneos](docs/unlocks/underground_senses.md)

[move()](functions/move)      [get_ground_type()](functions/get_ground_type)      [dig()](functions/dig)

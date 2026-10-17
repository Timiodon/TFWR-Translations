[<- Cogumelo](docs/unlocks/mushroom.md) <right>[Broca Explosiva ->](docs/unlocks/explosive_drill.md)
---
# Dinamite

O explosivo revolucionário, deixado por expedições de mineração anteriores. (In)felizmente, sua broca é perfeita para detonar dinamite e destruir todos os blocos ao redor.

Para minerar dinamite com segurança, encontre o estrato duplo de `Grounds.Dynamite` e `Grounds.Soot`. O solo de dinamite acima envelheceu, e alguns blocos são seguros para escavar. Outros ainda estão ativos e explodem ao serem escavados.

{{codeexample 
{
    "camera_position": {"x": -3, "y": -3, "z": 12},
    "show_image": true,
    "image_size": {"x": 900, "y": 500},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": false,
    "autoplay": true,
    "items": [{"item": "hay", "n": 100}],
    "world_size": {"x": 5, "y": 5},
    "execution_speed": 8,
    "digging_speed": 8,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 4,
    "exclude_unlocks": ["watering", "fertilizer", "mushrooms", "coal", "quartz", "petrified_pumpkins"]
}
#SETUP
jump(Unlocks.Dynamite)
#CODE
while get_ground_type() != Grounds.Soot:
    dig()
dig()
dig()
}}

Você consegue encontrar e escavar todos os blocos inertes, deixando apenas os ativos? Cada bloco ativo cercado apenas por outros blocos ativos ou por fuligem renderá dinamite extra quando o estrato desaparecer.

Felizmente, os blocos de fuligem abaixo ajudam: eles detectam quantos blocos de dinamite vizinhos estão ativos. Não informam quais, apenas o total, então você precisa combinar leituras de vários blocos de fuligem.

Chamar `measure()` em um bloco de fuligem retorna o número de minas nos oito blocos vizinhos do estrato de dinamite acima. O valor varia de `0` (nenhuma mina ativa) a `8` (todos os vizinhos contêm uma mina ativa).

A primeira escavação no estrato de dinamite é sempre inerte. Cada bloco minerado rende um pouco de dinamite. Quando o estrato é destruído, seja removendo todos os blocos inertes ou atingindo dinamite ativa, você também recebe uma quantidade de dinamite igual ao quadrado do número de blocos ativos totalmente expostos.

Se você escavar dinamite ativa, os dois estratos explodem. É possível verificar isso usando `get_ground_type()` depois de escavar `Grounds.Dynamite`. Se o solo não for `Grounds.Soot`, você não resolveu o quebra-cabeça. Por outro lado, se o último bloco de dinamite inerte for escavado, todos os blocos de dinamite desaparecem e você recebe o rendimento máximo do quebra-cabeça. O estrato de fuligem permanece, mas `measure()` retorna `None`, indicando que o quebra-cabeça foi resolvido com sucesso.

`# Escave um bloco de dinamite e verifique o estado do quebra-cabeça
def dig_dynamite():
    dig()
    if get_ground_type() != Grounds.Soot:
        # Dinamite ativa escavada, quebra-cabeça fracassou
        return False
    elif measure() == None:
        # Último bloco inerte escavado, quebra-cabeça resolvido
        return True
    else:
        # A medição retornou um número, quebra-cabeça ainda em andamento
        return None
`

O número de minas ativas e a dificuldade de encontrá-las aumentam com a profundidade.

A dinamite coletada pode ser usada com `use_item(Items.Dynamite)` e explode imediatamente abaixo do drone.

Melhore a dinamite para aumentar a produção ao escavar blocos de dinamite e expor totalmente blocos ativos. A melhoria também aumenta em 30% a energia das explosões.

---

[Estatísticas](docs/stats.md)      [Sentidos Subterrâneos](docs/unlocks/underground_senses.md)      [Dicionários](docs/scripting/dicts.md)      [Conjuntos](docs/scripting/sets.md)

[move()](functions/move)      [dig()](functions/dig)      [measure()](functions/measure)      [use_item()](functions/use_item)

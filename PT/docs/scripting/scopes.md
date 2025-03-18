# Escopos de Nomes

Escopos determinam quais variáveis podem ser acessadas de onde. Um escopo é basicamente um mapeamento de nomes para valores. Eles funcionam basicamente da mesma forma que em Python.

Há um escopo global, e cada função tem um escopo local. Quando você define uma variável, ela é adicionada ao escopo atual. Qualquer coisa fora de uma definição de função é considerada parte do escopo global.

`x = 1` Atribui o valor `1` ao nome `x` no escopo global.

Essa declaração `def` atribui uma função ao nome `f` no escopo global.
`def f():
    `Atribui o valor `1` ao nome `y` no escopo local de `f`.`
    y = 1

    `Atribui uma função ao nome `g` no escopo local de `f`.`
    def g():
        pass`

`f()` Recupera a função armazenada em `f` do escopo global e a chama.

`print(y)` Esta instrução de impressão no escopo global lança um erro porque `y` nunca foi declarado no escopo global, então não podemos lê-lo aqui. Ele existiu apenas no escopo local de `f`.

## A palavra-chave global

Por padrão, todas as variáveis em funções se associam ao escopo local, mesmo se uma variável com o mesmo nome existir no escopo global.

`x == 0

def f():
    x = 1
f()
print(x)`

Este código imprime `0` porque o `x` local dentro de `f` não é a mesma variável que o `x` global, então o `x` global permanece inalterado. Isso é importante porque, do contrário, uma chamada de função poderia acidentalmente sobrescrever uma variável global que por acaso tem o mesmo nome que uma variável local daquela função.

Se você quiser escrever em uma variável global, é preciso fazer isso explicitamente usando a palavra-chave `global`.

`x == 0

def f():
    global x
    x = 1
f()
print(x)`

Neste exemplo, `global x` associa `x` à variável global `x` definida acima dela. Isso agora irá imprimir `1`. Note que mudar variáveis globais geralmente é o primeiro passo para criar um código espaguete, onde cada parte do programa afeta todas as outras partes do programa, então não exagere.

## Loops e bifurcações

Loops e bifurcações não criam seus próprios escopos, então qualquer coisa declarada dentro deles ainda pode ser usada fora.

`for i in range(3):
    pass
print(i)`

Isso irá imprimir `2` porque a última iteração do loop `for` atribuiu `2` a `i`.
# Scopes de Nomes
Os scopes determinam que variáveis podem ser acedidas e de onde. Um scope é basicamente um mapeamento de nomes para valores.
Funcionam basicamente da mesma forma que em Python.

Existe um scope global, e cada função tem um scope local.
Quando defines uma variável, ela é adicionada ao scope atual.
Qualquer coisa fora de uma definição de função é considerada parte do scope global.

`x = 1`
Atribui um valor de `1` ao nome `x` no scope global.

Esta declaração `def` atribui uma função ao nome `f` no scope global.
`def f():
    `Atribui um valor de `1` ao nome `y` no scope local de `f`.`
    y = 1

    `Atribui uma função ao nome `g` no scope local de `f`.`
    def g():
        pass`

`f()`
Recupera a função guardada em `f` do scope global e chama-a.

`print(y)`
Esta instrução print no scope global lança um erro porque `y` nunca foi declarado no scope global, então não podemos lê-lo aqui.
Só existia no scope local de `f`.

## A palavra-chave global
Por defeito, todas as variáveis em funções associam-se ao scope local, mesmo que exista uma variável com o mesmo nome no scope global.

`x = 0

def f():
    x = 1
f()
print(x)`

Este código imprime `0` porque o `x` local dentro de `f` não é a mesma variável que o `x` global, então o `x` global permanece inalterado. Isto é importante porque, caso contrário, uma chamada de função poderia acidentalmente substituir uma variável global que por acaso tem o mesmo nome de uma variável local dessa função.

Se quiseres escrever numa variável global, deves fazê-lo explicitamente usando a palavra-chave `global`.

`x = 0

def f():
    global x
    x = 1
f()
print(x)`

Neste exemplo, `global x` associa `x` à variável global `x` definida acima. Isto agora imprimirá `1`.
Nota que alterar variáveis globais é geralmente o primeiro passo para o código esparguete, onde cada parte do programa afeta todas as outras partes do programa, por isso não abuses.

## Loops e ramificações
Loops e ramificações não criam os seus próprios scopes, então qualquer coisa declarada dentro deles ainda pode ser usada fora.

`for i in range(3):
    pass
print(i)`

Isto imprimirá `2` porque a última iteração do loop `for` atribuiu `2` a `i`.
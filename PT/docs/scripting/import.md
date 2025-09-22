# Import
Colocar todo o seu código em um único arquivo rapidamente se torna incontrolável. 
Instruções `import` permitem que você importe funções e variáveis globais de outro arquivo.
Como funciona em uma captura de tela:
![](ImportsInOnePicture400)

Aqui, `import module2` executa o arquivo chamado `module2` e te dá acesso a todas as suas variáveis globais.
Você pode então acessar variáveis e funções dentro do módulo importado usando o operador `.`.
Então, neste exemplo, `module2.print_x()` chama `print_x()` em `module2`.

### Não precisa ler mais

Você também pode mover as variáveis globais do módulo importado para o escopo atual onde a instrução de importação é executada, usando a sintaxe `from`.

`from module2 import print_x
print_x()`
Importa apenas as variáveis globais especificadas de `module2`.

ou

`from module2 import *
print_x()`
Importa todas as variáveis globais de `module2`.

Isso também importa o arquivo `module2`, mas em vez de acessá-lo através de uma variável chamada `module2`, ele desempacota as variáveis globais de `module2` e as atribui diretamente no escopo local.

Esta forma de importação geralmente não é recomendada porque não funciona bem quando dois arquivos importam um ao outro, e você pode acidentalmente sobrescrever variáveis no arquivo que está importando devido a colisões de nomes. É mais seguro evitar a sintaxe `from` se você não sabe o que está fazendo.

# Como realmente funciona

## TLDR
Importações podem ser pouco intuitivas, mas a maioria dos problemas pode ser evitada usando a sintaxe `import file` em vez de `from file import`, e envolvendo tudo que não é uma definição global em
`if __name__ == "__main__":`

## Efeitos Colaterais da Importação
A primeira vez que você importa um arquivo, ele executará o arquivo inteiro e então te dará acesso a todas as variáveis que foram definidas durante a execução.
Se você importar o mesmo arquivo novamente, ele apenas retornará o módulo em cache da primeira vez.

Isso significa que as instruções de importação podem ter efeitos colaterais. Se você importar um arquivo que chama `harvest()`, ele realmente vai colher durante a importação. Mas quando você o importar novamente, ele não colherá de novo porque o arquivo é executado apenas uma vez.

Existe uma maneira de evitar tais efeitos colaterais usando a variável `__name__`. Esta é uma variável que é definida automaticamente como `"__main__"` quando um arquivo é executado diretamente, e como o nome do arquivo quando um arquivo é executado através de `import`.
É considerado uma boa prática colocar qualquer código que você não queira que seja executado quando o arquivo é importado dentro de um bloco `if __name__ == "__main__":`.

Uma estrutura de arquivo comum em Python é colocar o código que deve ser executado quando o arquivo é iniciado em uma função `main()`. Desta forma, você tem uma distinção clara entre variáveis locais (definidas dentro de `main()`) e variáveis globais que podem ser importadas (definidas fora de `main()`).

`a_global_variable = "global"

def main():
    a_local_variable = "local"
    # do things

if __name__ == "__main__":
    main()`

## Ciclos de Importação
O que acontece se o arquivo `a` importa o arquivo `b` e o arquivo `b` importa o arquivo `a`?

file `a`:
`import b
x = 0`

file `b`:
`import a
def f():
    print(a.x)`

Isso funcionará bem. Digamos que nenhum dos dois arquivos esteja carregado ainda, e alguém execute `import a`.

-`a` executa até a linha `import b`.
-`b` executa até a linha `import a`.
-O módulo `a` já existe, mas não contém `x` porque só chegou até a linha `import b`.
-`b` armazena uma referência ao módulo `a` parcialmente carregado em uma variável chamada `a`.
-`b` executa a instrução `def` e armazena a função `f()`.
-`a` continua a executar e inicializa `x`.

Quando alguém chama `b.f()`, ele imprimirá corretamente `0` porque o módulo `a` ao qual `b` tem uma referência agora está totalmente carregado.

Agora, considere o mesmo código usando a sintaxe `from`.

file `a`:
`from b import *
x = 0`

file `b`:
`from a import *
def f():
    print(x)`

-`a` executa até a linha `from b import *`.
-`b` executa até a linha `from a import *`.
-O módulo `a` já existe, mas ainda não foi totalmente executado.
-`b` desempacota tudo o que está atualmente em `a` para seu próprio escopo global. Neste ponto, `a` não contém nada porque ainda não chegou à linha `x = 0`, então nada é importado.
-`b` executa a instrução `def` e armazena a função `f()`.
-`a` continua a executar e inicializa `x`.

Se alguém chamar `b.f()` agora, receberá um erro de que `x` não existe no escopo atual. Isso acontece porque desta vez `b` não tem uma referência ao `a` que ainda está carregando e não vê as definições que foram adicionadas após a importação.
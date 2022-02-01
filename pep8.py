"""
PEP8 - Python Enhancement Proposal

São propostas de melhorias para a linguagem Python

The Zen of Python

import this

A ideia = da PEP8 é que possamos escrever código Python de forma Pythonica

[1] - Utilize Camel Case para nomes de classes

class Calculadora:
    pass


class CalculadoraCientifica:
    pass


[2] - Utilize nomes em minúsculo, serapados por underline para funções ou variáveis

def soma():
    pass


def soma_dois():
    pass


numero = 4

numero_impar = 5

[3] - Utilize quatro espaços oara identação! (NÃO use tab)

if 'a' in 'banana':
    print('tem')

[4] - Linhas em branco
 - Separar funções e definições de classe com duas linhas em branco:
 - Métodos dentro de uma classe devem ser separados com uma única inha em branco;

[5] - Imports
 - Imports devem ser sempre feitos em linhas separadas;

#Import Errado

 import sys, os

 #Import Certo

 import sys
 import os

 # Não há problemas em utilizar:

 from types Strings, ListType

 # Caso tenha muitos imports de um mesmo pacote, recomenda-se fazer:

 from types import (
    StringType,
    ListType,
    SetType,
    OutroType
)

# Imports devem ser colocados no topo do arquivo, logo depois de quaiquer comentários ou docstring e
# antes de constantes ou variáreis globais

[6] - Espaços em expressões e instruções

# Não faça

funcao ( algo[ 1 ], { outro: 2 } )

# Faça

funcao(algo[1], {outro: 2})

# Não faça

algo (1)

# Faça

algo(1)

# Não faça

dict ['chave'] = lista [indice]

# Faça

dict['chave'] = lista[indice]

# Não faça

x               = 1
y               = 2
varialvel_longa = 5

# Faça

x = 1
y = 2
variavel_longa = 5

[7] - Termine sempre uma instrução com uma nova lingua

"""

import this

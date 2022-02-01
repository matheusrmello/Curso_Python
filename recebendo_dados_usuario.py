"""
Recebendo dados do usuario

input() -> Todo dado recebido via input é do tipo String

Em Python string é tudo que estiver entre:
 - Aspas simples;
 - Aspas duplas;
 - Aspas simples triplas;
 - Aspas duplas triplas;

Exemplos:
 - Aspas simples -> 'Matheus'
 - Aspas duplas -> "Matheus"
 - Asplas simples triplas -> '''Matheus'''
"""
# - Aspas duplas triplas -> """Matheus"""

# Entrada de dados

# print("Qual seu nome?")
# nome = input()
nome = input('QUal o seu nome? ')

# Exemplo de print 'antigo' 2.x
# print('Seja bem-vindo %s' % nome)

# Exemplo de print 'moderno' 3.x
# print("Seja bem-vindo {0}".format(nome))

# Exemplo de print 'mais atual' 3.7
print(f'Seja bem vindo {nome}')
# print("Qual a sua idade?")
# idade = input()
idade = input('Qual a sua idade? ')

# Processamento

# Saida
# Exemplo de print 'antigo' 2.x
# print("A %s tem %s anos" % (nome, idade))

# Exemplo de print 'moderno' 3.x
# print('A {0} tem {1} anos' .format(nome, idade))

# Exemplo de print 'mais atual' 3.7
print(f'O {nome} tem {idade} anos')

"""
# int(idade) => cast

Cast é a 'conversão' de um tipo de dado 
"""
print(f'O {nome} nasceu em {2022 - int(idade)}')

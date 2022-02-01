"""
Tipo string

Já vimos que em Python um dado é considerado do tipo string sempre que:
 - Estiver entre àspas simples -> 'uma string', '234', 'a', 'True', '42.3'
 - Estiver entre àspas duplas -> "uma string", "234", "a", "True", "42.3"
 - Estiver entre àspas simples  triplas -> '''uma string''', '''234''', '''a''', '''True''', '''42.3'''

nome = 'Matheus'
print(nome)
print(type(nome))

nome = 'Matheus \nMello'
print(nome)
print(type(nome))

nome = "Matheus' bar"
print(nome)
print(type(nome))

nome = 'Matheus \"Mello'
print(nome)

print(type(nome))

print(nome.upper())

print(nome.lower())

print(nome.split()) # Transforma em uma lista de strings

print(nome[0:4] # Slice de string

print(nome[0:4] # Slice de string

# [ 0,         1]
#['Matheus', 'Mello' ]
print(nome.split()[0])

print(nome.split()[1])
 """
# - Estiver entre àspas duplas triplas -> """uma string""", """234""", """a""", """True""", """42.3"""

# [0,    1,   2,   3,   4,   5,   6,   7,   8,   9,   10,  11, 12]
# ['M', 'a', 't', 'h', 'e', 'u', 's', '', 'M', 'e', 'l', 'l', 'o']
nome = 'Matheus Mello'

"""
[:: -1] -> Comece do primeiro elemento, vá até o ultimo elemento e inverta
"""
print(nome[::-1]) #Inversão da String `Pythônico

print(nome.replace('o', 'e'))

print(type(nome))

texto = 'socorram me subino onibus em marrocos' # Palíndromo
print(texto)

print(texto[::-1])

nome = 'arara'
print(nome)

print(nome[::-1])
